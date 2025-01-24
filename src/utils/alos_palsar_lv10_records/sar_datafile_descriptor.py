record_structure = [
    # P3-45 (1/4)
    ["1-4", "B4", "record_number"],  # レコード番号
    ["5-5", "B1", "first_record_subtype_code"],  # 第1レコードサブタイプコード
    ["6-6", "B1", "record_type_code"],  # レコードタイプコード
    ["7-7", "B1", "second_record_subtype_code"],  # 第2レコードサブタイプコード
    ["8-8", "B1", "third_record_subtype_code"],  # 第3レコードサブタイプコード
    ["9-12", "B4", "record_length"],  # レコード長
    ["13-14", "A2", "ascii_ebcdic_flag"],  # ASCII/EBCDICフラグ
    ["15-16", "A2", "blank"],  # 空白
    ["17-28", "A12", "format_descriptor"],  # フォーマット説明書
    ["29-30", "A2", "format_revision_level"],  # フォーマットリビジョンレベル
    ["31-32", "A2", "file_designation"],  # ファイル設計コード
    ["33-44", "A12", "software_release_revision"],  # ソフトウェアリリース＆リビジョン番号
    ["45-64", "A20", "file_id"],  # ファイルID
    ["65-68", "A4", "record_sequence_flag"],  # レコード順序フラグ
    ["69-76", "I8", "record_sequence_number"],  # 順序番号
    ["77-80", "I4", "continuation_field_length"],  # 連続番号フィールド長
    
    # P3-46 (2/4)
    ["81-84", "A4", "record_code_position_format_flag"],  # レコードコードと位置形式フラグ
    ["85-92", "I8", "record_code_position"],  # レコードコード位置
    ["93-96", "I4", "record_code_field_length"],  # レコードコードフィールド長
    ["97-100", "A4", "record_length_position_format_flag"],  # レコード長と位置形式フラグ
    ["101-108", "I8", "record_length_position"],  # レコード長位置
    ["109-112", "I4", "record_length_field_length"],  # レコード長フィールド長
    ["113-113", "A1", "reserved"],  # 予備
    ["114-114", "A1", "reserved"],  # 予備
    ["115-115", "A1", "reserved"],  # 予備
    ["116-116", "A1", "reserved"],  # 予備
    ["117-180", "A64", "reserved"],  # 予備
    ["181-186", "I6", "sar_data_record_count"],  # SARデータレコード数
    ["187-192", "I6", "sar_data_record_length"],  # SARデータレコード長
    ["193-216", "A24", "reserved"],  # 予備
    ["217-220", "I4", "sample_bit_length"],  # サンプルビット長
    ["221-224", "I4", "samples_per_data_group"],  # データグループあたりのサンプル数
    ["225-228", "I4", "bytes_per_data_group"],  # データグループあたりのバイト数
   
   # P3-47 (3/4)
    ["229-232", "A4", "data_group_justification"],  # データグループ内部のジャスティフィケーションと要求
    ["233-236", "I4", "sar_channel_count"],  # SARのチャンネル数
    ["237-244", "I8", "lines_per_dataset"],  # データセット内のライン数
    ["245-248", "I4", "leftside_border_pixel_count_per_line"],  # ラインあたりの左側のボーダーピクセル数
    ["249-256", "I8", "data_groups_per_line"],  # 1ラインあたりのデータグループ数
    ["257-260", "I4", "rightside_border_pixel_count_per_line"],  # ラインあたりの右側のボーダーピクセル数
    ["261-264", "I4", "border_lines_start"],  # 先頭のボーダーライン数
    ["265-268", "I4", "border_lines_end"],  # 末尾のボーダーライン数
    ["269-272", "A4", "interleaving_id"],  # インターリービングID
    ["273-274", "I2", "physical_records_per_line"],  # ラインあたりの物理レコード数
    ["275-276", "I2", "physical_records_per_multichannel"],  # マルチチャンネルあたりの物理コード数
    ["277-280", "I4", "prefix_data_length_per_record"],  # レコードあたりのPREFIX_DATAのバイト数
    ["281-288", "I8", "sar_data_length_per_record"],  # レコードあたりのSARデータのバイト数
    ["289-292", "I4", "suffix_data_length_per_record"],  # レコードあたりのサフィックスデータのバイト数
    ["293-296", "A4", "prefix_suffix_repetition_flag"],  # プレフィックス/サフィックス繰り返しフラグ
    ["297-304", "A8", "sample_line_locator"],  # サンプルデータライン番号ロケータ
    ["305-312", "A8", "sar_channel_locator"],  # SARチャンネルロケータ
    ["313-320", "A8", "line_time_locator"],  # SARデータのライン時間ロケータ
    ["321-328", "A8", "left_justified_count_locator"],  # 左詰め計測ロケータ
    ["329-336", "A8", "right_justified_count_locator"],  # 右詰め計測ロケータ

    # P3-48 (4/4)
    ["337-340", "A4", "pixel_packing_indicator"],  # 詰め込みピクセルの存在指標
    ["341-368", "A28", "blank"],  # 空白
    ["369-376", "A8", "sar_data_line_quality_locator"],  # SARデータのライン品質コードロケータ
    ["377-384", "A8", "calibration_info_locator"],  # 較正情報フィールドロケータ
    ["385-392", "A8", "gain_locator"],  # ゲイン量フィールドロケータ
    ["393-400", "A8", "bias_locator"],  # バイアス量フィールドロケータ
    ["401-428", "A28", "sar_data_format_indicator"],  # SARデータフォーマット形式指標
    ["429-432", "A4", "sar_data_format_code"],  # SARデータフォーマット形式コード
    ["433-436", "I4", "left_justified_pixel_bit_count"],  # 左詰めピクセルのビット数
    ["437-440", "I4", "right_justified_pixel_bit_count"],  # 右詰めピクセルのビット数
    ["441-448", "I8", "maximum_pixel_value"],  # ピクセルの最大値
    ["449-720", "A272", "blank"],  # 空白

]



