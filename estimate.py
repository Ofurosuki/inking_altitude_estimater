import open3d as o3d
import pandas as pd
import numpy as np
import grid as grd
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
point_cloud.colors = o3d.utility.Vector3dVector(colors)

# Remove points with z value under 0.3
mask = points[:, 2] >= 0.3
filtered_points = points[mask]
filtered_colors = colors[mask]

pcd_tree = o3d.geometry.KDTreeFlann(point_cloud)

# Update the point cloud with filtered points and colors
point_cloud.points = o3d.utility.Vector3dVector(filtered_points)
point_cloud.colors = o3d.utility.Vector3dVector(filtered_colors)

#load waypoints file
csv_waypoints = 'waypoints.csv'
waypoints = pd.read_csv(csv_waypoints)
assert set(waypoints.columns) == {'x', 'y', 'z'}, "CSV must contain x, y, z columns"
waypoints_array = waypoints.values


print("Find its neighbors with distance less than 0.2, and paint them green.")
# [k, idx, _] = pcd_tree.search_radius_vector_3d([1,1,0], 0.2)
# np.asarray(point_cloud.colors)[idx[1:], :] = [0, 1, 0]
# # average neighbors z value 
# average_z = np.mean(filtered_points[idx[0:], 2])
# print("Average z value of neighbors:", average_z)


unevenness = []
def estimate_unevenness(pcd, k, radius):
    pcd_tree = o3d.geometry.KDTreeFlann(pcd)
    for i in range(len(pcd.points)):
        [k, idx, _] = pcd_tree.search_radius_vector_3d(pcd.points[i], radius)
        average_z = np.mean(np.asarray(pcd.points)[idx[1:], 2])
        unevenness.append(pcd.points[i][2] - average_z)
    return unevenness

def write_to_csv(filename):
    data = pd.DataFrame(unevenness, columns=['unevenness'])
    data.to_csv(filename, index=False)



# Step 4: Visualize the point cloud
grid=grd.gen_grid(1, 10)
coordinates_frame=o3d.geometry.TriangleMesh.create_coordinate_frame(size=1, origin=[0,0,0])
o3d.visualization.draw_geometries([point_cloud, grid, coordinates_frame])





