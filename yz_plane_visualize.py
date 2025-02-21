import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

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
    pcd_file = 'C:\\Users\\smcon\\Desktop\\MTL_control_dev\\mtl_motor_control\\output_0221_2.pcd'
else:
    pcd_file = '/home/nextryo/Downloads/output_crop.pcd'
x_value = 0.1  # User-specified x-value
tolerance = 0.05  # Margin around the x-value
visualize_yz_plane(pcd_file, x_value, tolerance)
#plt.legend(['calibrated'])
pcd_file_uncalibrated='/home/nextryo/Downloads/output_uncalibrated_crop.pcd'
visualize_yz_plane(pcd_file_uncalibrated, x_value, tolerance)
#plt.legend(['uncalibrated'])

plt.show()