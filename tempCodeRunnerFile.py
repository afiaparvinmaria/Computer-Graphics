import matplotlib.pyplot as plt

def bresenham_line_points(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x, y = x1, y1

    if dx > dy:
        err = dx // 2
        while x != x2:
            x_points.append(x)
            y_points.append(y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy // 2
        while y != y2:
            x_points.append(x)
            y_points.append(y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    x_points.append(x2)
    y_points.append(y2)
    return x_points, y_points

plt.figure(figsize=(8, 6))
colors = ['b', 'g', 'r', 'm']


for i, n in enumerate(range(5, 9)):  # 5,6,7,8
    px, py = bresenham_line_points(2, 4, n, n)
    print(f"Line from (2,4) to ({n},{n}) pixels: {len(px)}")
    plt.plot(px, py, marker='o', color=colors[i], label=f'Line to ({n},{n})')

plt.title("Multiple Diagonal Lines Using Loop")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()