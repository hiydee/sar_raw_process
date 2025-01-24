record_structure = [
    ["1-4", "B4", "record_number"],  # レコード番号
    ["5-5", "B1", "first_record_subtype_code"],  # 第1レコードサブタイプコード
    ["6-6", "B1", "record_type_code"],  # レコードタイプコード
    ["7-7", "B1", "second_subtype_code"],  # 第2サブタイプコード
    ["8-8", "B1", "third_subtype_code"],  # 第3サブタイプコード
    ["9-12", "B4", "record_length"],  # レコード長
    ["13-16", "I4", "calibration_record_sequence_number"],  # キャリブレーションデータレコード順序番号
    ["17-20", "I4", "sample_count"],  # 有効サンプル数
    ["21-37", "A17", "data_start_time"],  # 校正データ開始時刻 (YYYYMMDDHHMMSS)
    ["38-54", "A17", "data_end_time"],  # 校正データ終了時刻 (YYYYMMDDHHMMSS)
    ["55-58", "I4", "att_setting_value"],  # 校正器ATT設定値 (0～63)
    ["59-59", "I1", "alc_status"],  # 校正器    ALC (0=ON, 1=OFF)
    ["60-60", "I1", "agc_mgc"],  # 校正器    AGC/MGC (0=AGC, 1=MGC)
    ["61-64", "I4", "pulse_width_microsec"],  # 送信パルス幅 (14～40 microsec)
    ["65-68", "I4", "chirp_bandwidth_Mhz"],  # チャープ帯域 (28MHz, 14MHz)
    ["69-72", "I4", "sampling_frequency_Mhz"],  # サンプリング周波数 (32MHz, 16MHz)
    ["73-76", "I4", "bit_count"],  # 量子化ビット数 (5ビット, 3ビット)
    ["77-80", "I4", "chirp_replica_data_count"],  # チャープレプリカデータ数 (1, 2)
    ["81-84", "I4", "chirp_replica_line_count"],  # チャープレプリカ積算データライン数
]


