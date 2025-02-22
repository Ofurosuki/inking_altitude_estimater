import numpy as np
import crosspoint

# 4点のサンプル点群データの生成（それぞれ対応する点が分かっているとき / 同じ順序が対応点）
# source_points = np.array([[0.295351,0.189433,-0.003291],
#                      [0.666709,-0.014655,-0.004194],
#                      [0.698039,0.887681,-0.009014],
#                      [0.002438,0.895326,-0.010552]])  # ソース点群

# target_points = np.array([[0.3, 0.2, 0.0],
#                      [0.677, 0.0, 0.0],
#                      [0.7, 0.9, 0.0],
#                      [0.0, 0.9, 0.0]])  # ターゲット点群
def least_square():
    source_points = np.array([crosspoint.crosspoint(0),
                            crosspoint.crosspoint(1),
                            crosspoint.crosspoint(2),
                            crosspoint.crosspoint(3)])  # ソース点群

    target_points = np.array([[0.1, 0.2, 0.0],
                            [0.5,0.2,0.0],
                            [0.4,0.8,0.0],
                            [0.1,0.8,0.0]])  # ターゲット点群

    # 重心を計算
    source_center = np.mean(source_points, axis=0)
    target_center = np.mean(target_points, axis=0)

    # 中心化
    source_centered = source_points - source_center
    target_centered = target_points - target_center

    # 行列の計算
    H = source_centered.T @ target_centered

    # SVDを実行
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T  # 回転行列

    # 平行移動の計算
    t = target_center - R @ source_center

    # 変換行列を構築
    transformation_matrix = np.eye(4)
    transformation_matrix[:3, :3] = R
    transformation_matrix[:3, 3] = t

    # ソース点群を変換
    source_transformed = (R @ source_points.T).T + t
    print("Source transformed:")
    print(source_transformed)

    print("Target points:")
    print(target_points)

    # 変換行列を出力
    print("Transformation matrix:")
    print(transformation_matrix)

    import open3d as o3d

    #PointCloudオブジェクトの作成
    source_pc = o3d.geometry.PointCloud()
    source_pc.points = o3d.utility.Vector3dVector(source_points)
    source_pc.paint_uniform_color([1, 0, 0])  # 赤色

    target_pc = o3d.geometry.PointCloud()
    target_pc.points = o3d.utility.Vector3dVector(target_points)
    target_pc.paint_uniform_color([0, 1, 0])  # 緑色

    # ソース点群を変換して表示
    source_pc_transformed = o3d.geometry.PointCloud()
    source_pc_transformed.points = o3d.utility.Vector3dVector(source_transformed)
    source_pc_transformed.paint_uniform_color([0, 0, 1])  # 青色

    print("R=")
    print(R)
    print("t=")
    print(t)

    # 点群を重ねて表示
    o3d.visualization.draw_geometries([source_pc,source_pc_transformed, target_pc])

    return R, t

#least_square()