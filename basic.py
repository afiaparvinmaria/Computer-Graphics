import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    x_points, y_points = [], []
    for _ in range(int(steps) + 1):
        x_points.append(int(x + 0.5))  # Integer-only rounding
        y_points.append(int(y + 0.5))
        x += x_inc
        y += y_inc
    return x_points, y_points

# Line endpoints
x1, y1 = 2, 3
x2, y2 = 12, 9

# Get line points
x_points, y_points = dda_line(x1, y1, x2, y2)

# Draw the grid
plt.figure(figsize=(8, 6))
plt.xticks(range(0, 16))
plt.yticks(range(0, 16))
plt.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal')

# Draw the line over the grid
plt.plot(x_points, y_points, 'ro-', label='Line Path')
plt.title("DDA Line Over a Grid")
plt.legend()
plt.show()
