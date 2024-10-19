import numpy as np
import open3d as o3d
def gen_grid(pitch: float, length: int) -> o3d.geometry.LineSet:
    line_set = o3d.geometry.LineSet()
    max_value = length * pitch
    x = np.arange(-max_value, max_value+pitch, pitch)
    x = np.repeat(x, 2)
    y = np.full_like(x, -max_value)
    y[::2] = max_value
    z = np.zeros_like(x)
    points_Y = np.vstack((x, y, z)).T

    y = np.arange(-max_value, max_value+pitch, pitch)
    y = np.repeat(y, 2)
    x = np.full_like(y, -max_value)
    x[::2] = max_value
    z = np.zeros_like(y)
    points_X = np.vstack((x, y, z)).T

    points = np.vstack((points_X, points_Y))
    line_set.points = o3d.utility.Vector3dVector(points)
    lines = np.arange(points.shape[0]).reshape(-1, 2)
    line_set.lines = o3d.utility.Vector2iVector(lines)

    line_set.paint_uniform_color((0.5, 0.5, 0.5))

    return line_set

def gen_circle(r: float, points: int = 100) -> o3d.geometry.LineSet:
    theta = np.linspace(0, 2*np.pi, points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(x)

    points = np.vstack((x, y, z)).T
    line_set = o3d.geometry.LineSet()
    line_set.points = o3d.utility.Vector3dVector(points)
    lines = np.zeros((points.shape[0]-1, 2), dtype=int)
    lines[:, 0] = np.arange(points.shape[0]-1)
    lines[:, 1] = np.arange(points.shape[0]-1) + 1
    line_set.lines = o3d.utility.Vector2iVector(lines)

    line_set.paint_uniform_color((0.5, 0.5, 0.5))

    return line_set