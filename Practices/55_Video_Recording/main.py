import cv2
import numpy as np
import mss
import time

# Output file
OUTPUT = "Practices/Video_Recording/recording.mp4"

# Screen size
with mss.mss() as sct:
    monitor = sct.monitors[1]
    width = monitor["width"]
    height = monitor["height"]

    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(OUTPUT, fourcc, 20.0, (width, height))

    print("Recording for 10 seconds...")

    start = time.time()

    while time.time() - start < 10:
        screenshot = sct.grab(monitor)

        frame = np.array(screenshot)

        # BGRA -> BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        out.write(frame)

    out.release()

print("Saved:", OUTPUT)