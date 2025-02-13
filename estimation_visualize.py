import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
csv_file = "estimated_xyz.csv"  # Change this to your actual CSV file
csv_file_nearest= "nearest_xyz.csv"
df = pd.read_csv(csv_file)
df_nearest = pd.read_csv(csv_file_nearest)

# Plot x vs z
plt.figure(figsize=(8, 6))
plt.scatter(df["x"], df["z_estimate"], label="Z-average", color="b", alpha=0.7)
#plt.scatter(df_nearest["x"], df_nearest["z_estimate"], label="Nearest Neighbour", color="r", alpha=0.7)
plt.xlabel("X-axis")
plt.ylabel("Z-axis")
plt.title("X-Z Scatter Plot")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
