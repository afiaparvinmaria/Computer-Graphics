 
#exercise 01 ( fixed values version - no user input)
""" import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx
    dS = 2 * dy
    dT = 2 * (dy - dx)

    x_points = [x]
    y_points = [y]

    print(f"Initial values: dx = {dx}, dy = {dy}, d = {d}")

    while x < x2:
        if d < 0:
            d += dS
        else:
            d += dT
            y += 1
        x += 1

        x_points.append(x)
        y_points.append(y)

        print(f"x = {x}, y = {y}, d = {d}")

    
    plt.plot(x_points, y_points, marker='o', color='blue')
    plt.title("Bresenham's Line Drawing (0,0) to (8,5)")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


bresenham_line(0, 0, 8, 5) """



#exercise 02 (user input version)
""" 
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

    print(f"Initial values: dx = {dx}, dy = {dy}, d = {d}")

    while x < x2:
        if d < 0:
            d += dS
        else:
            d += dT
            y += 1
        x += 1

        x_points.append(x)
        y_points.append(y)

        print(f"x = {x}, y = {y}, d = {d}")

    
    plt.plot(x_points, y_points, marker='o', color='blue')
    plt.title(f"Bresenham's Line from ({x1}, {y1}) to ({x2}, {y2})")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

bresenham_line(x1, y1, x2, y2) """


#exercise 03 (Modify the y-increment direction based on slope.)
 
""" #To handle lines with negative slope (e.g., top-right to bottom-left or vice versa), we need to adjust how y is updated. Specifically:
If the slope is negative, we decrease y when d ≥ 0 instead of increasing it. """


""" import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1  
    sy = 1 if y2 > y1 else -1  

    x_points = [x]
    y_points = [y]

    # Decide whether to iterate over x or y
    if dx > dy:
        d = 2 * dy - dx
        while x != x2:
            if d < 0:
                d += 2 * dy
            else:
                y += sy
                d += 2 * (dy - dx)
            x += sx
            x_points.append(x)
            y_points.append(y)
    else:
        d = 2 * dx - dy
        while y != y2:
            if d < 0:
                d += 2 * dx
            else:
                x += sx
                d += 2 * (dx - dy)
            y += sy
            x_points.append(x)
            y_points.append(y)

   
    plt.plot(x_points, y_points, marker='o', color='purple')
    plt.title(f"Bresenham's Line from ({x1}, {y1}) to ({x2}, {y2})")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# Example with negative slope
bresenham_line(0, 5, 8, 0)
 """



#exercise 04 (Add print statements to show the values of d, x, and y in each iteration.)
""" import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx
    dS = 2 * dy
    dT = 2 * (dy - dx)

    x_points = [x]
    y_points = [y]

    print(f"Initial values: dx = {dx}, dy = {dy}, d = {d}")

    while x < x2:
        if d < 0:
            d += dS
        else:
            d += dT
            y += 1
        x += 1

        x_points.append(x)
        y_points.append(y)

        print(f"d = {d}, x = {x}, y = {y}")

    plt.plot(x_points, y_points, marker='o', color='purple')
    plt.title(f"Bresenham's Line Drawing ({x1},{y1}) to ({x2},{y2})")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

bresenham_line(1, 1, 6, 4)
 """
 
""" import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
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

    # Plot the line
    plt.plot(x_points, y_points, marker='o', linestyle='-', color='blue')
    plt.title(f"Bresenham's Line Drawing from ({x1},{y1}) to ({x2},{y2})")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


# Octant examples in order:

# Octant 1: x+, y+, slope between 0 and 1
bresenham_line(2, 3, 10, 7)

# Octant 2: x+, y+, slope > 1
bresenham_line(2, 3, 5, 10)

# Octant 3: x-, y+, slope > 1
bresenham_line(10, 3, 5, 10)

# Octant 4: x-, y+, slope between 0 and 1
bresenham_line(10, 3, 2, 7)

# Octant 5: x-, y-, slope between 0 and 1
bresenham_line(10, 7, 2, 3)

# Octant 6: x-, y-, slope > 1
bresenham_line(5, 10, 2, 3)

# Octant 7: x+, y-, slope > 1
bresenham_line(2, 10, 7, 3)

# Octant 8: x+, y-, slope between 0 and 1
bresenham_line(5, 7, 10, 3)
 """


#exercise 05 (Compare Bresenham's and DDA algorithms by plotting both lines on the same graph.)
""" import matplotlib.pyplot as plt

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

def dda_line_points(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points

def compare_bresenham_dda(x1, y1, x2, y2):
    x_bres, y_bres = bresenham_line_points(x1, y1, x2, y2)
    x_dda, y_dda = dda_line_points(x1, y1, x2, y2)

    plt.plot(x_dda, y_dda, 'go--', label='DDA')
    plt.plot(x_bres, y_bres, 'bo-', label='Bresenham')
    plt.title(f"Compare DDA vs Bresenham from ({x1},{y1}) to ({x2},{y2})")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


compare_bresenham_dda(2, 3, 10, 7) """

#exercise 06 (Count the number of pixels drawn for a diagonal line.)
""" import matplotlib.pyplot as plt

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

# Diagonal line coordinates
x_start, y_start = 0, 0
x_end, y_end = 10, 10

# Get the pixels from Bresenham's algorithm
pixels_x, pixels_y = bresenham_line_points(x_start, y_start, x_end, y_end)

# Print the number of pixels drawn
print("Number of pixels drawn for diagonal line:", len(pixels_x))

# Plot the pixels
plt.plot(pixels_x, pixels_y, 'bo-', label='Bresenham Pixels')
plt.title("Bresenham Line Drawing - Diagonal")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()
 """
 
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




 