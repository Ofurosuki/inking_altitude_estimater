import open3d as o3d
import pandas as pd
import numpy as np
import grid as grd
import pickle as pkl
import open3d as o3d
import pandas as pd

use_pickle = True
if use_pickle:
    with open('point_cloud_light.pkl', 'rb') as f:
        points = pkl.load(f)
else:
    csv_file = 'random_data.csv'  # use world frame data because the value fro waypoint is in world frame
    data = pd.read_csv(csv_file)
    # Ensure the CSV file has the correct columns
    assert set(data.columns) == {'x', 'y', 'z', 'R', 'G', 'B'}, "CSV must contain x, y, z, R, G, B columns"

    # Step 2: Extract point coordinates and color information
    points = data[['x', 'y', 'z']].values
    colors = data[['R', 'G', 'B']].values   # Normalize color values to [0, 1]

# Step 3: Create an Open3D PointCloud object
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
point_cloud.colors = o3d.utility.Vector3dVector([0.5, 0.5, 0.5] for _ in range(len(points)))
# Load waypoints file
csv_waypoints = 'waypoints.csv'
waypoints = pd.read_csv(csv_waypoints)
waypoints_points = waypoints[['x', 'y', 'z']].values
print(waypoints_points)

# Create a point cloud of waypoints
waypoints_cloud = o3d.geometry.PointCloud()
waypoints_cloud.points = o3d.utility.Vector3dVector(waypoints_points)
waypoints_cloud.colors = o3d.utility.Vector3dVector([1, 0, 0] for _ in range(len(waypoints_points)))


# Step 4: Visualize the point cloud of waypoints
assert set(waypoints.columns) == {'x', 'y', 'z'}, "CSV must contain x, y, z columns"
waypoints_array = waypoints.values


print("Find its neighbors with distance less than 0.2, and paint them green.")
# [k, idx, _] = pcd_tree.search_radius_vector_3d([1,1,0], 0.2)
# np.asarray(point_cloud.colors)[idx[1:], :] = [0, 1, 0]
# # average neighbors z value 
# average_z = np.mean(filtered_points[idx[0:], 2])
# print("Average z value of neighbors:", average_z)


unevenness = []
def estimate_unevenness(pcd, radius,target):
    pcd_tree = o3d.geometry.KDTreeFlann(pcd)
    for i in range(len(target.points)):
        if target.points[i][1] < -1.0:
            radius = 0.1
        [k, idx, _] = pcd_tree.search_radius_vector_3d(target.points[i], radius)
        print("num:", len(idx))
        np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]
        average_z = np.mean(np.asarray(pcd.points)[idx[1:], 2])
        unevenness.append(average_z)
    return unevenness

def write_to_csv(filename):
    data = pd.DataFrame(unevenness, columns=['unevenness'])
    data.to_csv(filename, index=False)


print(estimate_unevenness(point_cloud, 0.03, waypoints_cloud))

# Step 4: Visualize the point cloud
grid=grd.gen_grid(0.1, 10)
coordinates_frame=o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1, origin=[0,0,0])
o3d.visualization.draw_geometries([point_cloud, grid, coordinates_frame,waypoints_cloud])





