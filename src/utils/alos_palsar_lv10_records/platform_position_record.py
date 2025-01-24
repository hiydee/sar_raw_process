record_structure = [
    # P3-37 (1/2)
    ["1-4", "B4", "record_number"],  # レコード番号
    ["5-5", "B1", "first_record_subtype_code"],  # 第1レコードサブタイプコード
    ["6-6", "B1", "record_type_code"],  # レコードタイプコード
    ["7-7", "B1", "second_record_subtype_code"],  # 第2レコードサブタイプコード
    ["8-8", "B1", "third_record_subtype_code"],  # 第3レコードサブタイプコード
    ["9-12", "B4", "platform_data_record_length"],  # プラットフォームデータレコード長
    ["13-44", "A32", "orbit_information"],  # プラットフォーム情報（予測値や定値など）
    ["45-60", "F16.7", "scene_center_geocentric_vector_x"],  # シーンセンタの地球中心ベクトル（X）
    ["61-76", "F16.7", "scene_center_geocentric_vector_y"],  # シーンセンタの地球中心ベクトル（Y）
    ["77-92", "F16.7", "scene_center_geocentric_vector_z"],  # シーンセンタの地球中心ベクトル（Z）
    ["93-108", "F16.7", "scene_center_geocentric_vector_x_prime"],  # シーンセンタの地球中心ベクトル（X’）
    ["109-124", "F16.7", "scene_center_geocentric_vector_y_prime"],  # シーンセンタの地球中心ベクトル（Y’）
    ["125-140", "F16.7", "scene_center_geocentric_vector_z_prime"],  # シーンセンタの地球中心ベクトル（Z’）
    ["141-144", "I4", "data_point_count"],  # データポイント数
    ["145-148", "I4", "first_point_year"],  # 第1ポイントの年（YYYY）
    ["149-152", "I4", "first_point_month"],  # 第1ポイントの月（MM）
    ["153-156", "I4", "first_point_day"],  # 第1ポイントの日（DD）
    ["157-160", "I4", "first_point_day_of_year"],  # 第1ポイントの年内日（DOY）
    ["161-182", "E22.15", "first_point_seconds"],  # 第1ポイントの秒（小数部含む）
    # P3-38 (2/2)
    ["183-204", "E22.15", "time_interval_between_points"],  # ポイント間のインターバル時間（秒）
    ["205-268", "A64", "eci_ecr_coordinates"],  # ECI/ECR座標情報
    ["269-290", "E22.15", "greenwich_mean_time"],  # グリッニチ平均時角
    ["291-306", "F16.7", "scene_direction_along_track"],  # シーン方向ベクトル（X）
    ["307-322", "F16.7", "scene_direction_cross_track"],  # シーン方向ベクトル（Y）
    ["323-338", "F16.7", "scene_direction_radius_track"],  # シーン方向ベクトル（Z）
    ["339-354", "F16.7", "scene_velocity_along_track"],  # シーン速度ベクトル（X）
    ["355-370", "F16.7", "scene_velocity_cross_track"],  # シーン速度ベクトル（Y）
    ["371-386", "F16.7", "scene_velocity_radius_track"],  # シーン速度ベクトル（Z）
    ]

# 動的に追加データポイントを定義
start_byte = 387  # 第1データポイントの開始バイト
point_size = 132  # 1データポイントのバイト数
num_points = 28   # データポイント数

for i in range(1, num_points + 1):  # 第1データポイントから第28データポイントまで
    offset = start_byte + (i - 1) * point_size
    record_structure.extend([
        [f"{offset}-{offset + 21}", "E22.15", f"point_{i}_geocentric_vector_x"],  # 地心ベクトルX
        [f"{offset + 22}-{offset + 43}", "E22.15", f"point_{i}_geocentric_vector_y"],  # 地心ベクトルY
        [f"{offset + 44}-{offset + 65}", "E22.15", f"point_{i}_geocentric_vector_z"],  # 地心ベクトルZ
        [f"{offset + 66}-{offset + 87}", "E22.15", f"point_{i}_velocity_vector_x"],  # 速度ベクトルX
        [f"{offset + 88}-{offset + 109}", "E22.15", f"point_{i}_velocity_vector_y"],  # 速度ベクトルY
        [f"{offset + 110}-{offset + 131}", "E22.15", f"point_{i}_velocity_vector_z"],  # 速度ベクトルZ
    ])

# フィールド No.35-37
record_structure.extend(
    [
        ["4083-4100", "A18", "blank"],  # 空白 (フィールド No.35)
        ["4101-4101", "I1", "leap_second_flag"],  # うるう秒フラグ (フィールド No.36)
        ["4102-4680", "A579", "blank"],  # 空白 (フィールド No.37)
    ]
)

