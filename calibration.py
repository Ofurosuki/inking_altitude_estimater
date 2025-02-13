import numpy as np

def calculate_plane_equation(p1, p2, p3):
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)

    normal_vector = np.cross(v1, v2)
    a, b, c = normal_vector

    d = -np.dot(normal_vector, p1)

    return a, b, c, d

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

planeA=[(0.442941, 0.395048, 0.011962), (0.539461,0.118925,0.012163), (0.231414,0.150011,0.011163)]
planeB=[(0.697707,0.453330,0.160451),(0.694942,0.142854,0.166290),(0.694342,0.244707,0.069407)]
planeC=[(0.184931,-0.002437,0.185886),(0.517880,-0.008044,0.210572),(0.424602,-0.006983,0.086972)]


a1, b1, c1, d1 = calculate_plane_equation(planeA[0], planeA[1], planeA[2])
a2, b2, c2, d2 = calculate_plane_equation(planeB[0], planeB[1], planeB[2])
a3, b3, c3, d3 = calculate_plane_equation(planeC[0], planeC[1], planeC[2])
A=np.array([[a1, b1, c1],
         [a2, b2, c2],
         [a3, b3, c3]])
# print("A=")
# print(A)
B=np.array([-d1, -d2, -d3])
intersection = np.linalg.solve(A, B)
diff=np.array([0.7,0,0.018])
intersection = intersection-diff
print("intersection=")
print(intersection)

R=np.array([normalize([a2, b2, c2]),
            normalize([a3, b3, c3]),
         normalize([-a1, -b1, -c1])])
R=R.T  
print("R=")
print(R)

# point=np.array([0.5,0.5,0.5])
# point_modified=R*(point+intersection)

# print("point_modified=")
# print(point_modified)

source_points = np.array([[0.295351,0.189433,-0.003291],
                     [0.666709,-0.014655,-0.004194],
                     [0.698039,0.887681,-0.009014],
                     [0.002438,0.895326,-0.010552]])  # ソース点群

target_points = np.array([[0.3, 0.2, 0.0],
                     [0.677, 0.0, 0.0],
                     [0.7, 0.9, 0.0],
                     [0.0, 0.9, 0.0]])  # ターゲット点群

transformed_points = R @ source_points.T +intersection.reshape(3, 1)
print("transformed_points=")
print(transformed_points.T)

import open3d as o3d

source_object = o3d.geometry.PointCloud()
source_object.points = o3d.utility.Vector3dVector(source_points)
source_object.paint_uniform_color([1, 0, 0])  # 赤色

target_object = o3d.geometry.PointCloud()
target_object.points = o3d.utility.Vector3dVector(target_points)
target_object.paint_uniform_color([0, 1, 0])  # 緑色

transformed_object = o3d.geometry.PointCloud()
transformed_object.points = o3d.utility.Vector3dVector(transformed_points.T)
transformed_object.paint_uniform_color([0, 0, 1])  # 青色

o3d.visualization.draw_geometries([source_object, target_object, transformed_object])
#print(normalize([1, 1, 0]))



# 結果を表示
#print(f"平面の方程式: {a1}x + {b1}y + {c1}z + {d1} = 0")