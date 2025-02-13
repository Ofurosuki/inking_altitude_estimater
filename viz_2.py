import numpy as np
import plotly.graph_objects as go

# 水平角 (azimuth) と仰角 (elevation) のグリッド
azimuth = np.linspace(0, np.pi, 20)  # 0° から 180°
elevation = np.linspace(0, np.pi / 2, 10)  # 0° から 90°
azimuth, elevation = np.meshgrid(azimuth, elevation)

# 半球のデカルト座標
r = 1  # 半径
x = r * np.sin(elevation) * np.cos(azimuth)
y = r * np.sin(elevation) * np.sin(azimuth)
z = r * np.cos(elevation)

# 3D メッシュプロット
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

# 表示
fig.show()
