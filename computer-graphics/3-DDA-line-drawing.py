import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 18, 13

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

points = []

for i in range(steps + 1):
    points.append((round(x), round(y)))
    x += x_inc
    y += y_inc

xs, ys = zip(*points)

plt.figure(figsize=(16, 9))
plt.scatter(xs, ys, s=90)
plt.plot(xs, ys)
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.savefig("01_dda_line_output.png", dpi=120)
plt.show()
