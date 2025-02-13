import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# メッシュの分割数
num_theta = 30  # 水平角の分割数
num_phi = 30    # 仰角の分割数
r = 1           # 半球の半径

# 角度をラジアンで生成
theta = np.linspace(0, np.pi, num_theta)  # 0°〜180°
phi = np.linspace(-np.pi/4, np.pi/4, num_phi)  # -90°〜90°
theta, phi = np.meshgrid(theta, phi)  # メッシュグリッド作成

# 極座標からデカルト座標へ変換
x = r * np.cos(phi) * np.cos(theta)
y = r * np.cos(phi) * np.sin(theta)
z = r * np.sin(phi)

# 3Dプロット
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# メッシュ描画
ax.plot_wireframe(x, y, z, color='b', linewidth=0.5)

# 軸のラベルと枠線を削除
ax.set_xticks([])  # X軸目盛りを非表示
ax.set_yticks([])  # Y軸目盛りを非表示
ax.set_zticks([])  # Z軸目盛りを非表示
ax.set_frame_on(False)  # 枠を削除

# タイトル（不要なら削除）
ax.set_title("Hemispherical Mesh (-90 to 90 elevation)")

plt.show()
