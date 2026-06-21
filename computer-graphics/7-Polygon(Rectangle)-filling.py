import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

x_min, y_min = 3, 3
x_max, y_max = 14, 9

filled = []

for y in range(y_min, y_max + 1):
    for x in range(x_min, x_max + 1):
        filled.append((x, y))

xs, ys = zip(*filled)

plt.figure(figsize=(16, 9))
plt.scatter(xs, ys, s=120)

plt.gca().add_patch(
    Rectangle(
        (x_min, y_min),
        x_max - x_min,
        y_max - y_min,
        fill=False,
        linewidth=3,
    )
)

plt.title("Polygon Rectangle Filling Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("06_rectangle_filling_output.png", dpi=120)
plt.show()
