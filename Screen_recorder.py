import numpy as np
import cv2
import pyautogui
import time

# Set screen resolution
resolution = (1920, 1080)

# Define the codec and create a VideoWriter object
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Set the duration for the recording (in seconds)
recording_duration = 30  # Record for 10 seconds(time = n/15*5)
start_time = time.time()

while True:
    # Take screenshot using pyautogui
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert the frame color from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    # Check if the recording duration has been exceeded
    if time.time() - start_time > recording_duration:
        break

# Release the VideoWriter object
out.release()
