record_structure = [
    # P3-49 (1/3)
    ["1-4", "B4", "record_sequence_number"],  # レコード順序番号
    ["5-5", "B1", "first_record_subtype_code"],  # 第1レコードサブタイプコード
    ["6-6", "B1", "record_type_code"],  # レコードタイプコード
    ["7-7", "B1", "second_record_subtype_code"],  # 第2レコードサブタイプコード
    ["8-8", "B1", "third_record_subtype_code"],  # 第3レコードサブタイプコード
    ["9-12", "B4", "record_length"],  # レコード長
    # PREFIX DATA-GENERAL INFORMATION
    ["13-16", "B4", "sar_data_line_number"],  # SARデータライン番号
    ["17-20", "B4", "sar_data_record_index"],  # SARデータレコードインデックス
    ["21-24", "B4", "num_left_justified_pixels"],  # 実際の左詰めピクセルの数
    ["25-28", "B4", "num_data_pixels"],  # 実際のデータピクセル数
    ["29-32", "B4", "num_right_justified_pixels"],  # 右詰めピクセルの数
    # PREFIX DATA-SENSOR PARAMETERS
    ["33-36", "B4", "sensor_parameter_update_flag"],  # センサーパラメータ更新フラグ
    ["37-40", "B4", "sensor_aquisition_year"],  # センサー取得年
    ["41-44", "B4", "sensor_aquisition_day_of_year"],  # センサー取得日 (年内通算)
    ["45-48", "B4", "sensor_aquisition_msec_of_day"],  # センサー取得ミリ秒 (日内通算)
    ["49-50", "B2", "sar_channel_id"],  # SARチャンネルID
    ["51-52", "B2", "sar_channel_code"],  # SARチャンネルコード
    ["53-54", "B2", "transmit_pulse_polarization"],  # 送信パルス偏波

    # P3-50 (2/3)
    ["55-56", "B2", "pulse_polarization_continuation"],  # パルス偏波の続き
    ["57-60", "B4", "prf_mhz"],  # パルス繰り返し周波数 (PRF値)
    ["61-64", "B4", "scan_number"],  # スキャン番号
    ["65-66", "B2", "onboard_range_compression_flag"],  # オンボードレンジ圧縮フラグ
    ["67-68", "B2", "chirp_modulation_type"],  # チャープ変調タイプ
    ["69-72", "B4", "chirp_length_pulse_width_nsec"],  # チャープ長 (パルス幅)
    ["73-76", "B4", "chirp_constant_coefficient"],  # チャープ定数係数
    ["77-80", "B4", "chirp_linear_coefficient"],  # チャープ一次係数
    ["81-84", "B4", "chirp_quadratic_coefficient"],  # チャープ二次係数
    ["85-88", "B4", "reserved"],  # 予備
    ["89-92", "B4", "reserved"],  # 予備
    ["93-96", "B4", "receiver_gain_db"],  # 受信機ゲイン (dB)
    ["97-100", "B4", "invalid_line_flag"],  # 無効ラインフラグ
    ["101-104", "B4", "electrical_elevation_angle_from_nadir"],  # アンテナ直下からの電気的エレベーション角
    ["105-108", "B4", "mechanical_elevation_angle_from_nadir"],  # アンテナ直下からの電気的エレベーション角
    ["109-112", "B4", "electrical_antenna_squint_angle"],  # 電気的アンテナ斜視角
    ["113-116", "B4", "mechanical_antenna_squint_angle"],  # 機械的アンテナ斜視角    
    ["117-120", "B4", "slant_range_to_first_data"],  # 最初のデータまでのスラントレンジ
    ["121-124", "B4", "data_record_window_position"],  # データレコード窓位置
    ["125-128", "B4", "reserved"],  # 予備

    # P3-51 (3/3)
    # PREFIX DATA-PLATFORM REFERENCE INFORMATION
    ["129-132", "B4", "satellite_position_update_flag"],  # 衛星位置パラメータ更新フラグ
    ["133-136", "B4", "satellite_latitude"],  # 衛星緯度 [1/1,000,000 度]
    ["137-140", "B4", "satellite_longitude"],  # 衛星経度 [1/1,000,000 度]
    ["141-144", "B4", "satellite_altitude"],  # 衛星高度 [m]
    ["145-148", "B4", "satellite_ground_track_velocity"],  # 対地衛星速度 [cm/sec]
    ["149-160", "3B4", "satellite_velocity_components"],  # 衛星速度成分 X', Y', Z' [cm/sec]
    ["161-172", "3B4", "satellite_acceleration_components"],  # 衛星加速度成分 X'', Y'', Z'' [cm/sec²]
    ["173-176", "B4", "track_angle"],  # トラック角 [1/1,000,000 度]
    ["177-180", "B4", "true_course_angle"],  # 真の進行方向 [1/1,000,000 度]
    ["181-184", "B4", "pitch_angle"],  # ピッチ角 [1/1,000,000 度]
    ["185-188", "B4", "roll_angle"],  # ロール角 [1/1,000,000 度]
    ["189-192", "B4", "yaw_angle"],  # ヨー角 [1/1,000,000 度]
    # PREFIX DATA-SENSOR/FACILITY SPECIFIC AUXILIARY DATA
    ["193-284", "B92", "reserved"],  # 空白 (NULL)
    ["285-288", "B4", "palsar_frame_number"],  # PALSARフレーム番号
    ["289-388", "B100", "auxiliary_observation_data"],  # 観測補助データ（生データ）
    ["389-412", "B24", "null_data"],  # オール0 (空白)
]



