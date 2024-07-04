"""
This script extracts GPS data from a GoPro MP4 video file and writes it to a CSV file.

[Issue] (Unsolved) The GPS data is incorrect. It always returns the same GPS value for all image frames.

"""

import cv2
import pandas as pd
import exiftool
import datetime
import os

VIDEO_PATH = "toy_vid.mp4"

# Initialize the ExifTool
with exiftool.ExifTool() as et:

    # Open the video file
    video = cv2.VideoCapture(VIDEO_PATH)

    # Make sure the video is opened correctly
    if not video.isOpened():
        print("Could not open video")
        exit()

    # Initialize the frame counter
    frame_counter = 0

    # Initialize the time counter
    time_counter = 0

    # Initialize a list to store the data
    data = []

    # Create a new directory with current datetime in its name
    dt_string = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(dt_string, exist_ok=True)

    while True:
        # Read the next frame
        ret, frame = video.read()

        # If the frame was not retrieved, then we have reached the end of the video
        if not ret:
            break

        # If the current frame is at the one-second mark
        if video.get(cv2.CAP_PROP_POS_MSEC) // 1000 == time_counter:
            # Save the frame as an image in the new directory
            cv2.imwrite(os.path.join(dt_string, f"frame_{frame_counter}.jpg"), frame)

            # Get the GPS info of the current frame
            gps_info = et.get_tag("Composite:GPSPosition", VIDEO_PATH)

            # Append the frame id and GPS info to the data list
            data.append([frame_counter, gps_info])

            # Increment the frame and time counters
            frame_counter += 1
            time_counter += 1

    # Release the video file
    video.release()

    # Create a DataFrame from the data list
    df = pd.DataFrame(data, columns=["frame_id", "gps_info"])

    # Save the DataFrame to a CSV file in the new directory
    df.to_csv(os.path.join(dt_string, "frame_gps_info.csv"), index=False)
