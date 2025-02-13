import open3d as o3d
# pcd = o3d.io.read_point_cloud("pcd/ref0_0.pcd")
# # 引数を設定して、平面を推定
# plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
#                                          ransac_n=3,
#                                          num_iterations=1000)
# # 平面モデルの係数を出力
# [a, b, c, d] = plane_model
# print(f"Plane equation: {a:.4f}x + {b:.4f}y + {c:.4f}z + {d:.4f} = 0")


def plane_fitting(pcd_path):
    pcd = o3d.io.read_point_cloud(pcd_path)
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)
    [a, b, c, d] = plane_model
    #print(f"Plane equation: {a:.4f}x + {b:.4f}y + {c:.4f}z + {d:.4f} = 0")
    return plane_model

# # インライアの点を抽出して色を付ける
# inlier_cloud = pcd.select_by_index(inliers)
# inlier_cloud.paint_uniform_color([1.0, 0, 0])

# # 平面以外の点を抽出
# outlier_cloud = pcd.select_by_index(inliers, invert=True)

# # 可視化
# o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])