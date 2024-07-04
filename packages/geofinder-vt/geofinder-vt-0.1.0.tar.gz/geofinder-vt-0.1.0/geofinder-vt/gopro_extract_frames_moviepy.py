"""
Module Name: Extract image frames from GoPro video files
Author: Rifat Sabbir Mansur
Date: May 27, 2023
Description: This script extracts GPS data from a GoPro MP4 video file and writes it to a CSV file.
    [√] Works for GoPro original files, i.e. MP4 and 360 files.
Reference: 
    Tutorial: https://www.thepythoncode.com/article/extract-frames-from-videos-in-python
    GitHub: https://github.com/x4nth055/pythoncode-tutorials/blob/master/python-for-multimedia/extract-frames-from-video/extract_frames_moviepy.py
Dependencies:
    System must have ffmpeg installed and added to PATH
        brew install ffmpeg

"""

from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import datetime
import logging

# i.e if video of duration 30 seconds, saves 1 frame per second = 30 frames saved in total
SAVING_FRAMES_PER_SECOND = 1

# Name of the video file 
# VIDEO_FILE = "toy_vid.mp4"
# VIDEO_FILE = "GH010025-001.MP4"
VIDEO_FILE = "GS010027-003.360"

# Having the current datetime in the filename and the log file
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create the file
# and output every level since 'DEBUG' is used
# and remove all headers in the output
# using empty format=''
log_filename = 'gopro_extract_frames_moviepy_' + VIDEO_FILE.replace('.','') + timestamp_str + '.log'
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='')

def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def extract_frames(video_file, 
                    filename=None, 
                    saving_frames_per_second=SAVING_FRAMES_PER_SECOND,
                    metadata_list=None):
    # load the video clip
    video_clip = VideoFileClip(video_file)
    # make a folder by the name of the video file
    if filename is None:
        filename, _ = os.path.splitext(video_file)
        filename += "-moviepy"
        filename += "-" + timestamp_str
    
    if not os.path.isdir(filename):
        os.mkdir(filename)

    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    # if SAVING_FRAMES_PER_SECOND is set to 0, step is 1/fps, else 1/SAVING_FRAMES_PER_SECOND
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    
    count = 0
   
    # iterate over each possible frame
    for current_duration in np.arange(0, video_clip.duration, step):
        # format the file name based on the metadata_list and save it
        # frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration))
        if count < len(metadata_list):
            frame_name = metadata_list[count]
        else:
            frame_name = metadata_list[-1]
        frame_filename = os.path.join(filename, f"frame_{frame_name}.jpg")
        # save the frame with the current duration
        video_clip.save_frame(frame_filename, current_duration)
        count += 1


if __name__ == "__main__":
    """
    This is the main function that is executed when the script is run.
    """

    import sys
    video_file = VIDEO_FILE
    extract_frames(video_file, None, SAVING_FRAMES_PER_SECOND)