import struct
import pandas as pd
from . import alos_palsar_lv10_records

def read_sar_leader_file(file_path):
    """
    Reads the SAR leader file and extracts structured records based on the specifications.
    """
    records = {}

    # Define the structure of each record based on the SAR Leader specification
    record_definitions = [
        ("file_descriptor", 720),  # レコード 4: ファイルディスクリプタ
        ("dataset_summary", 4096),  # レコード 5: データセットサマリ
        ("platform_position_data", 4680),  # レコード 6: プラットフォーム位置データ
        ("attitude_data", 8192),  # レコード 7: 姿勢データ
        ("calibration_data", 13212),  # レコード 8: キャリブレーションデータ
        # 以下は現状省略
        # ("facility_related_data_1", 1540000),  # レコード 9: 設備関連データ 1
        # ("facility_related_data_2", 4314000),  # レコード 10: 設備関連データ 2
        # ("facility_related_data_3", 345000),  # レコード 11: 設備関連データ 3
        # ("facility_related_data_4", 325000),  # レコード 12: 設備関連データ 4
        # ("facility_related_data_5", 325000),  # レコード 13: 設備関連データ 5
        # ("facility_related_data_6", 3072),  # レコード 14: 設備関連データ 6
        # ("facility_related_data_7", 511000),  # レコード 15: 設備関連データ 7
        # ("facility_related_data_8", 4370000),  # レコード 16: 設備関連データ 8
        # ("facility_related_data_9", 728000),  # レコード 17: 設備関連データ 9
        # ("facility_related_data_10", 15000),  # レコード 18: 設備関連データ 10
    ]

    with open(file_path, "rb") as f:
        current_position = 0
        for record_name, length in record_definitions:
            f.seek(current_position)
            data = f.read(length)
            records[record_name] = data
            current_position += length
    return records

def read_sar_image_metadata(file_path):
    """
    Reads the SAR image file and extracts structured records based on the specifications.
    """
    records = {}

    # Define the structure of each record based on the SAR Leader specification
    record_definitions = [
        # ファイルディスクリプタ
        ("file_descriptor", 720),
        
        # プレフィックスデータ
        # 可変の場合があるので、多めに取っている
        # プレフィックスデータの後には、実際のデータがある
        ("signal_data_metainfo", 412 + 200),  
    ]

    with open(file_path, "rb") as f:
        current_position = 0
        for record_name, length in record_definitions:
            f.seek(current_position)
            data = f.read(length)
            records[record_name] = data
            current_position += length

    return records

def parse_record(data, record_structure):
    """
    Parse binary data according to the record structure.

    Args:
        record_structure (list): List of record field definitions.
        data (bytes): Binary data to parse.

    Returns:
        pd.DataFrame: Parsed data as a DataFrame.
    """
    records = []
    for field in record_structure:
        byte_num, field_type, name = field
        start_byte = int(byte_num.split("-")[0]) - 1
        end_byte = int(byte_num.split("-")[-1])
        field_data = data[start_byte:end_byte]


        if field_type.startswith("B"):  # Binary (unsigned integers)
            byte_count = end_byte - start_byte
            if byte_count == 1:  # 1 バイトの場合
                value = struct.unpack(">B", field_data)[0]
            elif byte_count == 2:  # 2 バイトの場合
                value = struct.unpack(">H", field_data)[0]
            elif byte_count == 4:  # 4 バイトの場合
                value = struct.unpack(">I", field_data)[0]
            else:  # 複数バイト（配列として解釈）
                value = struct.unpack(f">{byte_count}B", field_data)  # 配列として展開

        elif field_type.startswith("I"):  # Integer
            try:
                value = int(field_data.decode("ascii").strip())
            except ValueError:
                value = None
        elif field_type.startswith("F"):  # Floating-point
            try:
                value = float(field_data.decode("ascii").strip())
            except ValueError:
                value = None
        elif (
            field_type.startswith("A")  # ASCII data
            or field_type.startswith("CH")  # Character data
        ):
            value = field_data.decode("ascii").strip()
        elif field_type.startswith("E"):  # Exponential notation
            try:
                value = float(field_data.decode("ascii").strip())
            except ValueError:
                value = None

        elif field_type == "3B4":  # 3つの 4 バイト整数
            if len(field_data) == 12:  # 確認: データが12バイトあること
                value = struct.unpack(">III", field_data)  # 3つの 4 バイト整数を展開
            else:
                raise ValueError(
                    f"Invalid data length for 3B4: {len(field_data)} bytes"
                )

        else:  # Unsupported or unknown type
            value = None
        # print(name, value)
        records.append(
            {
                "byte_num": byte_num,
                "type": field_type,
                "name": name,
                "value": value,
            }
        )

    return pd.DataFrame(records)

def get_led_metadatas(led_file_path):
    sar_reader_records = read_sar_leader_file(led_file_path)
    
    # dataset_summary
    dataset_summary_structure = (
        alos_palsar_lv10_records.dataset_summary_record.record_structure
    )    
    dataset_summary_df = parse_record(
        sar_reader_records["dataset_summary"], dataset_summary_structure
    )


    # platform_position_data
    platform_position_data_structure = (
        alos_palsar_lv10_records.platform_position_record.record_structure
    )
    platform_position_data_df = parse_record(
        sar_reader_records["platform_position_data"], platform_position_data_structure
    )

    # cal_metadata
    cal_metadata_structure = alos_palsar_lv10_records.cal_metadata_record.record_structure
    cal_metadata_df = parse_record(
        sar_reader_records["calibration_data"], cal_metadata_structure
    )

    # cal_data
    cal_data_df = None  # 未実装

    metadatas = {
        "dataset_summary": dataset_summary_df,
        "platform_position_data": platform_position_data_df,
        "cal_metadata": cal_metadata_df,
        "cal_data": cal_data_df,
    }
    return metadatas
    
    
def get_image_metadatas(image_file_path):
    sar_image_records = read_sar_image_metadata(image_file_path)
    # datafile_descriptor
    sar_datafile_descriptor_structure = (
        alos_palsar_lv10_records.sar_datafile_descriptor.record_structure
    )
    sar_datafile_descriptor_df = parse_record(
        sar_image_records["file_descriptor"], sar_datafile_descriptor_structure
    )

    # signal_data_metainfo
    signal_data_metainfo_structure = (
        alos_palsar_lv10_records.signal_data_record.record_structure
    )
    signal_data_prefix_df = parse_record(
        sar_image_records["signal_data_metainfo"], signal_data_metainfo_structure
    )

    metadatas = {
        "datafile_descriptor": sar_datafile_descriptor_df,
        "signal_data_prefix": signal_data_prefix_df,
    }
    return metadatas
