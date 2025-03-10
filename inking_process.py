import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

# Read the CSV file
csv_file = './mitsui.csv'

# import chardet
# with open(csv_file, "rb") as f:
#   result = chardet.detect(f.read())
# print(result)

csv_data = []
with open(csv_file, 'r',encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        csv_data.append(','.join(row))
print(csv_data)
#Example CSV data
# csv_data = [
#     "100,120,100,100,150,100",
#     "200,220,200,200,250,200"
# ]


# Parse the CSV data into a list of line segments
lines = []
for line in csv_data:
    coords = list(map(float, line.split(',')))
    # for i in range(0, len(coords) - 2, 2):  # Iterate over pairs of points
    #   lines.append(((coords[i], coords[i+1]), (coords[i+2], coords[i+3])))
    lines.append(((coords[0], coords[1]), (coords[3], coords[4])))
print(coords)
print(lines)


# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)
#ax.invert_yaxis()  # Invert y-axis for correct visualization
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('inking simulation')

# Create an empty line object
line_segments = []
for _ in range(len(lines)):
    line, = ax.plot([], [], 'bo-', markersize=5)  # Blue circles with line
    #line, = ax.plot([], [], 'r-', lw=2)  # Red line
    line_segments.append(line)

# Animation function
def update(frame):
    if frame < len(lines):
        (x1, y1), (x2, y2) = lines[frame]
        line_segments[frame].set_data([x1, x2], [y1, y2])  # Update line coordinates
    return line_segments

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(lines), interval=1000, repeat=False)

# Show animation
plt.show()
