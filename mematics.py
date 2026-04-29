import math, time, sys
max_reps = 125 # Search depth

# For testing ;)))
def main():
    print("Test")
    Generate_Mematics()

def Generate_Mematics():
    sys.stdout.write("\033[2J")

    # Width needs to be roughly double the height
    width, height = 60, 30

    # 1. Personality vectors
    vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ]

    # 2. Personality limits
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    angle_x, angle_y, angle_z = 0, 0, 0

    try:
        reps = 0
        while reps < max_reps:
            reps += 1
            # Initialize empty screen buffer
            screen = [[' ' for _ in range(width)] for _ in range(height)]
            projected = []

            # 3. I'm not explaining this
            for v in vertices:
                x, y, z = v[0], v[1], v[2]

                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y, z = new_y, new_z

                new_x = x * math.cos(angle_y) + z * math.sin(angle_y)
                new_z = -x * math.sin(angle_y) + z * math.cos(angle_y)
                x, z = new_x, new_z

                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x, y = new_x, new_y

                distance = 3
                z += distance
                fov = 15
                
                p_x = int(width / 2 + (x * fov / z) * 2) 
                p_y = int(height / 2 + (y * fov / z))
                projected.append((p_x, p_y))

            # 4. Render
            for edge in edges:
                x0, y0 = projected[edge[0]]
                x1, y1 = projected[edge[1]]
                
                # DDA (Digital Differential Analyzer) Line Algorithm
                dx = x1 - x0
                dy = y1 - y0
                steps = max(abs(dx), abs(dy))
                
                if steps > 0:
                    x_inc = dx / steps
                    y_inc = dy / steps
                    cx, cy = float(x0), float(y0)
                    
                    for _ in range(int(steps) + 1):
                        ix, iy = int(cx), int(cy)
                        # Only draw if within terminal bounds
                        if 0 <= ix < width and 0 <= iy < height:
                            screen[iy][ix] = '@' # The character that makes up the cube
                        cx += x_inc
                        cy += y_inc

            # Render the frame
            # Move cursor to top-left (\033[H) instead of clearing screen to prevent flickering
            sys.stdout.write("\033[H")
            
            output = ""
            for row in screen:
                output += "".join(row) + "\n"
            
            sys.stdout.write(output)
            sys.stdout.flush()

            # Increment rotation for next frame
            angle_x += 0.04
            angle_y += 0.03
            angle_z += 0.02

            time.sleep(0.04) # Render rate

    except KeyboardInterrupt:
        time.sleep(1)