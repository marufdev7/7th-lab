import math
import matplotlib.pyplot as plt

triangle = [(1, 1), (5, 1), (3, 4), (1, 1)]

tx, ty = 4, 2

angle = 45
rad = math.radians(angle)

translated = [(x + tx, y + ty) for x, y in triangle]

# Apply rotation
rotated = [
    (x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad))
    for x, y in translated
]


def draw(poly, label):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    plt.plot(xs, ys, marker="o", label=label)


plt.figure(figsize=(16, 9))

draw(triangle, "Original")
draw(translated, "After Translation")
draw(rotated, "After Translation and Rotation")

plt.title("2D Transformation: Translation and Rotation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()

plt.savefig("07_translation_rotation_output.png", dpi=120)
plt.show()
