import matplotlib.pyplot as plt

x1, y1 = 2, 2
x2, y2 = 17, 10

points = []

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

err = dx - dy

x, y = x1, y1

while True:
    points.append((x, y))

    if x == x2 and y == y2:
        break

    e2 = 2 * err

    if e2 > -dy:
        err -= dy
        x += sx

    if e2 < dx:
        err += dx
        y += sy

xs, ys = zip(*points)

plt.figure(figsize=(16, 9))
plt.scatter(xs, ys, s=90)
plt.plot(xs, ys)
plt.title("Bresenham Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("02_bresenham_line_output.png", dpi=120)
plt.show()
