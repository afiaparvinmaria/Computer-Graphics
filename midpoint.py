# import matplotlib.pyplot as plt

# def midpoint_line(X1, Y1, X2, Y2):
#     pixels = []

#     dy = Y2 - Y1
#     dx = X2 - X1

#     if abs(dy) <= abs(dx):  # dy <= dx case
#         if X1 > X2: 
#             X1, X2 = X2, X1
#             Y1, Y2 = Y2, Y1

#         d = dy - (dx / 2)
#         x, y = X1, Y1
#         pixels.append((x, y))  # plot initial point

#         while x < X2:
#             x += 1
#             if d < 0:
#                 d = d + dy  
#             else:
#                 d = d + dy - dx  
#                 y += 1 
#             pixels.append((x, y)) 

#     else:  # dx <= dy case
#         if Y1 > Y2: 
#             X1, X2 = X2, X1
#             Y1, Y2 = Y2, Y1

#         d = dx - (dy / 2)
#         x, y = X1, Y1
#         pixels.append((x, y))  # plot initial point

#         while y < Y2:
#             y += 1
#             if d < 0:
#                 d = d + dx  
#             else:
#                 d = d + dx - dy  
#                 x += 1 
#             pixels.append((x, y))  # plot(x, y)

#     return pixels

# # Example
# start = (2, 3)
# end = (15, 10)
# pixels = midpoint_line(start[0], start[1], end[0], end[1])

# # Plot
# x_vals, y_vals = zip(*pixels)
# plt.plot(x_vals, y_vals, 'ro')  # red dots
# plt.title("Midpoint Line Generation Algorithm")
# plt.grid(True)
# plt.gca().set_aspect('equal')
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def midpoint_line(X1, Y1, X2, Y2):
    pixels = []

    dy = Y2 - Y1
    dx = X2 - X1

    if abs(dy) <= abs(dx):  # dy <= dx case
        if X1 > X2: 
            X1, X2 = X2, X1
            Y1, Y2 = Y2, Y1

        d = dy - (dx / 2)
        x, y = X1, Y1
        pixels.append((x, y))  # plot initial point

        while x < X2:
            x += 1
            if d < 0:
                d = d + dy  
            else:
                d = d + dy - dx  
                y += 1 
            pixels.append((x, y)) 

    else:  # dx <= dy case
        if Y1 > Y2: 
            X1, X2 = X2, X1
            Y1, Y2 = Y2, Y1

        d = dx - (dy / 2)
        x, y = X1, Y1
        pixels.append((x, y))  # plot initial point

        while y < Y2:
            y += 1
            if d < 0:
                d = d + dx  
            else:
                d = d + dx - dy  
                x += 1 
            pixels.append((x, y))  # plot(x, y)

    return pixels

# Example
start = (2, 3)
end = (15, 10)
pixels = midpoint_line(start[0], start[1], end[0], end[1])

# Plotting setup
fig, ax = plt.subplots()

# Box size (1x1 grid cells)
box_size = 1

# Draw grid lines
ax.set_xticks(range(start[0], end[0] + 1))
ax.set_yticks(range(start[1], end[1] + 1))
ax.grid(True, which='both')

# Draw the filled boxes for each pixel
for x, y in pixels:
    rect = patches.Rectangle((x, y), box_size, box_size, linewidth=1, facecolor='red', edgecolor='black')
    ax.add_patch(rect)

# Outline the path (the exact pixels along the line)
x_vals, y_vals = zip(*pixels)
plt.plot(x_vals, y_vals, color='blue', linewidth=2, label="Path (Line)")

# Plot the straight line connecting the start and end points (for comparison)
plt.plot([start[0], end[0]], [start[1], end[1]], 'b--', label="Straight Line")  # dashed blue line

# Add labels, title, and grid
plt.title("Midpoint Line Generation with Filled Boxes")
plt.xlabel("X")
plt.ylabel("Y")

# Ensure the aspect ratio is equal for square boxes
plt.gca().set_aspect('equal')

# Show the plot
plt.legend()
plt.show()

