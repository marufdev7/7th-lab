import matplotlib.pyplot as plt

rectangle = [(1, 1), (5, 1), (5, 3), (1, 3), (1, 1)]

sx, sy = 1.8, 1.5

tx, ty = 4, 2

scaled = [(x * sx, y * sy) for x, y in rectangle]

translated = [(x + tx, y + ty) for x, y in scaled]


def draw(poly, label):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    plt.plot(xs, ys, marker="o", label=label)


plt.figure(figsize=(16, 9))

draw(rectangle, "Original")
draw(scaled, "After Scaling")
draw(translated, "After Scaling and Translation")

plt.title("2D Transformation: Scaling and Translation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()

# Save and show the plot
plt.savefig("08_scaling_translation_output.png", dpi=120)
plt.show()
