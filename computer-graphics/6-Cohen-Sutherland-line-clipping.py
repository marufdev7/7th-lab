import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

x_min, y_min = 2, 2
x_max, y_max = 12, 8

x1, y1 = 0, 4
x2, y2 = 15, 10

original = (x1, y1, x2, y2)


def compute_code(x, y):
    code = INSIDE

    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT

    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP

    return code


code1 = compute_code(x1, y1)
code2 = compute_code(x2, y2)

accept = False

while True:
    if code1 == 0 and code2 == 0:
        accept = True
        break

    elif code1 & code2:
        break

    else:
        code_out = code1 if code1 != 0 else code2

        if code_out & TOP:
            x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            y = y_max

        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            y = y_min

        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            x = x_max

        else:
            y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            x = x_min

        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = compute_code(x2, y2)

plt.figure(figsize=(16, 9))

plt.gca().add_patch(
    Rectangle(
        (x_min, y_min),
        x_max - x_min,
        y_max - y_min,
        fill=False,
        linewidth=3,
    )
)

plt.plot(
    [original[0], original[2]],
    [original[1], original[3]],
    linestyle="--",
    marker="o",
    label="Original Line",
)

if accept:
    plt.plot(
        [x1, x2],
        [y1, y2],
        marker="o",
        linewidth=4,
        label="Clipped Line",
    )

plt.title("Cohen-Sutherland Line Clipping Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.savefig("10_cohen_sutherland_output.png", dpi=120)
plt.show()
