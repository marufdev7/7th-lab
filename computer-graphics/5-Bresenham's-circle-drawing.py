import matplotlib.pyplot as plt

xc, yc = 0, 0
r = 8

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
d = 3 - 2 * r

while x <= y:
    add_points(x, y)

    if d < 0:
        d = d + 4 * x + 6
    else:
        d = d + 4 * (x - y) + 10
        y -= 1

    x += 1

xs, ys = zip(*points)

plt.figure(figsize=(16, 9))
plt.scatter(xs, ys, s=90)
plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("03_bresenham_circle_output.png", dpi=120)
plt.show()
