import matplotlib.pyplot as plt

xc, yc = 0, 0
r = 9
points = []


def add_points(x, y):
    points.extend(
        [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ]
    )


x = 0
y = r
p = 1 - r
while x <= y:
    add_points(x, y)
    if p < 0:
        p = p + 2 * x + 3
    else:
        p = p + 2 * (x - y) + 5
        y -= 1
    x += 1
xs, ys = zip(*points)
plt.figure(figsize=(16, 9))
plt.scatter(xs, ys, s=90)
plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("04_midpoint_circle_output.png", dpi=120)
plt.show()
