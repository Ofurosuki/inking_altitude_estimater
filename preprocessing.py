import pandas as pd
import open3d as o3d
import pickle as pkl
import grid as grd
import numpy as np


use_pickle = False
if use_pickle:
    with open('point_cloud.pkl', 'rb') as f:
        points = pkl.load(f)
else:
    #csv_file = 'C:\\Users\\smcon\\Desktop\\MTL_control_dev\\mtl_motor_control\\points.csv'  # use world frame data because the value fro waypoint is in world frame
    csv_file = 'C:\\Users\\smcon\\Desktop\\MTL_control_dev\\mtl_motor_control\\points.csv'
    data = pd.read_csv(csv_file,low_memory=False)
    # Ensure the CSV file has the correct columns
    assert set(data.columns) == {'x', 'y', 'z', 'R', 'G', 'B'}, "CSV must contain x, y, z, R, G, B columns"

    # Step 2: Extract point coordinates and color information
    points = data[['x', 'y', 'z']].values
    colors = data[['R', 'G', 'B']].values   # Normalize color values to [0, 1]

    # Remove points with z value more than 0
    #points = points[points[:, 2] <=0.5]
    

    # Remove points with x value less than -500
    #points = points[points[:, 1] >= 500]
    #points = points[ points[:, 2] <= 140]
    #colors = colors[points[:, 0] >= -500]
    # Switch points' x and y
    #points[:, [0, 1]] = points[:, [1, 0]] #lefthanded to rightha
    


    with open('point_cloud.pkl', 'wb') as f:
        pkl.dump(points, f)


# Step 3: Create an Open3D PointCloud object
#points = points[points[:, 2] <= -0.3]
#points += translation
points=points[points[:, 2] <= 0.3]
points = points[points[:, 1] >= 0]
points = points[points[:, 0] >= 0]
points = points[points[:, 0] <= 1.5]
#switch x and y
points[:, [0, 1]] = points[:, [1, 0]]  # lefthanded to righthanded for visualization
#translation = np.array([0, 0.03, 0.0])
#points += translation
with open('point_cloud_light_tokura.pkl', 'wb') as f:
        pkl.dump(points, f)

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
point_cloud.colors = o3d.utility.Vector3dVector([0.5, 0.5, 0.5] for _ in range(len(points)))
# Step 4: Add coordinate axes to the point cloud
grid = grd.gen_grid(0.1, 10)
coordinate_axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
o3d.visualization.draw_geometries([point_cloud, coordinate_axes, grid])  # Visualize the point cloud
