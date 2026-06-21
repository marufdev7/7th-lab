import math
import matplotlib.pyplot as plt

triangle = [(2, 1), (7, 1), (4, 5), (2, 1)]

px, py = 4, 2

angle = 60
rad = math.radians(angle)

rotated = []
for x, y in triangle:
    x_shift = x - px
    y_shift = y - py
    xr = x_shift * math.cos(rad) - y_shift * math.sin(rad) + px
    yr = x_shift * math.sin(rad) + y_shift * math.cos(rad) + py
    rotated.append((xr, yr))


def draw(poly, label):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    plt.plot(xs, ys, marker="o", label=label)


plt.figure(figsize=(16, 9))

draw(triangle, "Original Triangle")
draw(rotated, "Rotated Triangle")

plt.scatter([px], [py], s=160, label="Rotation Point")

plt.title("General Point to Point Rotation of a Triangle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()

plt.savefig("12_point_rotation_triangle_output.png", dpi=120)
plt.show()
