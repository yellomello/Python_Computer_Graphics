import turtle
import colorsys
import cv2
import numpy as np
from PIL import ImageGrab

# Setup Turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

# Video Settings
frame_width = s.window_width()
frame_height = s.window_height()
video_out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height))

n = 70
h = 0

# Set the position of the turtle graphics window
s.setup(width=frame_width, height=frame_height)

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.6)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)

    # Capture the screen area occupied by the Turtle graphics window
    bbox = s._root.bbox("all")
    if bbox:  # Check if bbox is not None
        img = ImageGrab.grab(bbox)
        if img:  # Check if img is captured correctly
            # Convert PIL Image to a format OpenCV can handle
            frame = np.array(img)
            if frame.size > 0:  # Ensure frame is not empty
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                # Write frame to video
                video_out.write(frame)
            else:
                print("Captured frame is empty")
        else:
            print("Failed to capture image")
    else:
        print("Failed to get bounding box")

# Release video writer and close window
video_out.release()
cv2.destroyAllWindows()
turtle.done()
