import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx
    dS = 2 * dy
    dT = 2 * (dy - dx)

    x_points = [x]
    y_points = [y]

    while x < x2:
        if d < 0:
            d += dS
        else:
            d += dT
            y += 1
        x += 1
        x_points.append(x)
        y_points.append(y)

    # Plot the line
    plt.plot(x_points, y_points, marker='o', color='blue')
    plt.title("Bresenham's Line Drawing")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# Example run
bresenham_line(2, 3, 10, 7)
