import matplotlib.pyplot as plt

xc, yc = 0, 0
rx, ry = 10, 6
points = []


def add_points(x, y):
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ])


x = 0
y = ry

rx2 = rx * rx
ry2 = ry * ry

dx = 2 * ry2 * x
dy = 2 * rx2 * y

p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

while dx < dy:
    add_points(x, y)

    if p1 < 0:
        x += 1
        dx = dx + 2 * ry2
        p1 = p1 + dx + ry2
    else:
        x += 1
        y -= 1
        dx = dx + 2 * ry2
        dy = dy - 2 * rx2
        p1 = p1 + dx - dy + ry2

p2 = (
    (ry2 * (x + 0.5) * (x + 0.5))
    + (rx2 * (y - 1) * (y - 1))
    - (rx2 * ry2)
)

while y >= 0:
    add_points(x, y)

    if p2 > 0:
        y -= 1
        dy = dy - 2 * rx2
        p2 = p2 + rx2 - dy
    else:
        y -= 1
        x += 1
        dx = dx + 2 * ry2
        dy = dy - 2 * rx2
        p2 = p2 + dx - dy + rx2

xs, ys = zip(*points)

plt.figure(figsize=(16, 9))
plt.scatter(xs, ys, s=90)
plt.title("Midpoint Ellipse Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("05_midpoint_ellipse_output.png", dpi=120)
plt.show()