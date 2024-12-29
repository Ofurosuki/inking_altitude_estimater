import numpy as np

def calculate_plane_equation(p1, p2, p3):
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)

    normal_vector = np.cross(v1, v2)
    a, b, c = normal_vector

    d = -np.dot(normal_vector, p1)

    return a, b, c, d


planeA=[(0.442941, 0.395048, 0.011962), (0.539461,0.118925,0.012163), (0.231414,0.150011,0.011163)]
planeB=[(0.697707,0.453330,0.160451),(0.694942,0.142854,0.166290),(0.694342,0.244707,0.069407)]
planeC=[(0.184931,-0.002437,0.185886),(0.517880,-0.008044,0.210572),(0.424602,-0.006983,0.086972)]


a1, b1, c1, d1 = calculate_plane_equation(planeA[0], planeA[1], planeA[2])
a2, b2, c2, d2 = calculate_plane_equation(planeB[0], planeB[1], planeB[2])
a3, b3, c3, d3 = calculate_plane_equation(planeC[0], planeC[1], planeC[2])
A=np.array([[a1, b1, c1],
         [a2, b2, c2],
         [a3, b3, c3]])
B=np.array([-d1, -d2, -d3])
intersection = np.linalg.solve(A, B)
print(intersection)




# 結果を表示
#print(f"平面の方程式: {a1}x + {b1}y + {c1}z + {d1} = 0")