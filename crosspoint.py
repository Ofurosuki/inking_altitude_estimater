import plane 
import numpy as np

def crosspoint(index):
    matrix=np.array([plane.plane_fitting("pcd/ref"+str(index)+"_0.pcd"),
            plane.plane_fitting("pcd/ref"+str(index)+"_1.pcd"),
            plane.plane_fitting("pcd/ref"+str(index)+"_2.pcd")])


    # Extract columns 1 to 3
    A = matrix[:, 0:3]
    B = -matrix[:, 3]
    # print(matrix)
    # print("Extracted columns:")
    # print(A)
    # print(B)

    intersection=np.linalg.solve(A, B)
    # print("intersection=")
    # print(intersection)
    return intersection

print(crosspoint(0))
print(crosspoint(1))
print(crosspoint(2))
print(crosspoint(3))