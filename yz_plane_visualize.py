import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import LeastSquare as ls

def visualize_xz_plane(pcd_file, y_value, tolerance=0.05):
    """
    Load a PCD file and visualize the x-z plane of points within a margin of the specified y-value.

    :param pcd_file: Path to the PCD file.
    :param y_value: The y-coordinate where we want to extract the x-z plane.
    :param tolerance: The margin within which y-values will be considered.
    """
    # Load PCD file
    pcd = o3d.io.read_point_cloud(pcd_file)
    points = np.asarray(pcd.points)

    # Select points within the tolerance range of y_value
    mask = (points[:, 1] >= y_value - tolerance) & (points[:, 1] <= y_value + tolerance)
    xz_plane_points = points[mask][:, [0, 2]]  # Extract x and z coordinates

    if xz_plane_points.size == 0:
        print(f"No points found within y = {y_value} ± {tolerance}")
        return

    # Plotting x-z plane
    plt.figure(figsize=(8, 6))
    plt.scatter(xz_plane_points[:, 0], xz_plane_points[:, 1], s=1)  # Plot X (X-axis) vs Z (Y-axis)
    plt.xlabel('X-axis')
    plt.ylabel('Z-axis')
    plt.title(f'X-Z Plane at Y ≈ {y_value} (±{tolerance})')
    #plt.gca().invert_yaxis()  # Optional: Invert Y-axis for typical orientation
    plt.grid(True)

def visualize_yz_plane(pcd_file, x_value, tolerance=0.05):
    """
    Load a PCD file and visualize the y-z plane of points within a margin of the specified x-value.

    :param pcd_file: Path to the PCD file.
    :param x_value: The x-coordinate where we want to extract the y-z plane.
    :param tolerance: The margin within which x-values will be considered.
    """
    # Load PCD file
    pcd = o3d.io.read_point_cloud(pcd_file)
    points = np.asarray(pcd.points)
    # Increase z-values by 0.01
    #points[:, 2] += 0.01
    
    

    # Select points within the tolerance range of x_value
    mask = (points[:, 0] >= x_value - tolerance) & (points[:, 0] <= x_value + tolerance)
    yz_plane_points = points[mask][:, 1:3]  # Extract y and z coordinates

    if yz_plane_points.size == 0:
        print(f"No points found within x = {x_value} ± {tolerance}")
        return

    # Plotting y-z plane
    #plt.figure(figsize=(8, 6))
    y=np.linspace(0.1,0.3,100)
    z=y*0+0.005
    plt.plot(y,z,color='red')
    y2=np.linspace(0.3,0.7,100)
    z2=y2*0+0.01
    plt.plot(y2,z2,color='red')
    plt.scatter(yz_plane_points[:, 0], yz_plane_points[:, 1], s=1)  # Plot Y (X-axis) vs Z (Y-axis)
    plt.xlabel('Y-axis')
    plt.ylabel('Z-axis')
    plt.title(f'Y-Z Plane at X ≈ {x_value} (±{tolerance})')
    #plt.gca().invert_yaxis()  # Optional: Invert Y-axis for typical orientation
    plt.grid(True)
    
import platform
# Example usage:
if platform.system() == 'Windows':
    print('Platform: Windows')
    pcd_file = './output_0221_2.pcd'
else:
    pcd_file = '/home/nextryo/Downloads/output_crop.pcd'
x_value = 0.1  # User-specified x-value
tolerance = 0.05  # Margin around the x-value
visualize_yz_plane(pcd_file, x_value, tolerance)
#plt.legend(['calibrated'])
#pcd_file_uncalibrated='/home/nextryo/Downloads/output_uncalibrated_crop.pcd'
#visualize_yz_plane(pcd_file_uncalibrated, x_value, tolerance)
#plt.legend(['uncalibrated'])
pcd = o3d.io.read_point_cloud(pcd_file)
points = np.asarray(pcd.points)

R,t=ls.least_square()  #load R,t from least_square.py
transformed_points = (R @ points.T).T + t
o3d.io.write_point_cloud('./output_0221_2_transformed.pcd', o3d.geometry.PointCloud(points=o3d.utility.Vector3dVector(transformed_points)))
visualize_yz_plane('./output_0221_2_transformed.pcd', x_value, tolerance)



plt.show()

visualize_xz_plane('./output_0221_2_transformed.pcd', 0.2, 0.05)
plt.show()