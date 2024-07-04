"""
Module Name: Extract image frames and metadata from GoPro video files
Author: Rifat Sabbir Mansur
Date: May 28, 2023
Description: This script extracts image frames from GoPro video files and writes it to a folder.
    It also extracts GPS data from a GoPro MP4 video file and writes it to a CSV file.
    [√] Works for both GoPro original files, i.e. MP4 and 360 files.
Dependencies:
    * gopro_extract_frames_moviepy.py | function: extract_frames
    * gopro_extract_using_gpmf_csv.py | function: extract_metadata
"""

import logging
from datetime import datetime
from gopro_extract_frames_moviepy import extract_frames
from gopro_extract_using_gpmf_csv import extract_metadata

# i.e if video of duration 30 seconds, saves 1 frame per second = 30 frames saved in total
SAVING_FRAMES_PER_SECOND = 1

# i.e if video of duration 30 seconds, saves 1 frame per second = 30 frames saved in total
# if set to 2 then 15 frames saved in total
FRAMES_AFTER_NUMBER_OF_SECONDS = 1

# Name of the video file(s)
# VIDEO_FILE = "toy_vid.mp4"
VIDEO_FILE = "GH010025-001.MP4"
# VIDEO_FILE = "GS010027-003.360"
VIDEO_FILE_LIST = ["GH010025-001.MP4", "GS010027-003.360"]

# Having the current datetime in the filename and the log file
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

# Create the file
# and output every level since 'DEBUG' is used
# and remove all headers in the output
# using empty format=''
log_filename = 'gopro_main_' + timestamp_str + '.log'
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='')

def extract_frames_and_metadata(video_file=VIDEO_FILE, 
                                output_dir=None, 
                                saving_frames_per_second=SAVING_FRAMES_PER_SECOND, 
                                frames_after_number_of_seconds=FRAMES_AFTER_NUMBER_OF_SECONDS):
    """
    This function extracts image frames and metadata from GoPro video files.
    :param str video_file: Name of the video file
    :param str output_dir: Name of the output directory
    :param int saving_frames_per_second: Number of frames to save per second
    :param int frames_after_number_of_seconds: Number of frames to save after every number of seconds
    :return: None
    :rtype: None
    :raises ValueError: from "format_timedelta" function while formatting timedelta objects
    :raises FileNotFoundError: from "extract_frames" function while reading the video file
    :raises ValueError: from "extract_frames" function while converting string to datetime object
    """
    # Extract metadata from the video file and store metadata list in a variable
    metadata_list = extract_metadata(video_file, output_dir, frames_after_number_of_seconds)
    
    # Extract image frames from the video file
    extract_frames(video_file, output_dir, saving_frames_per_second, metadata_list)

def multi_vids_extraction(vid_list=[], 
                          output_dir=None,
                          saving_frames_per_second=SAVING_FRAMES_PER_SECOND,
                          frames_after_number_of_seconds=FRAMES_AFTER_NUMBER_OF_SECONDS):
    """
    This function extracts image frames and metadata from multiple GoPro video files.
    :param list vid_list: List of video files
    :param str output_dir: Name of the output directory
    :param int saving_frames_per_second: Number of frames to save per second
    :param int frames_after_number_of_seconds: one frame to save after every number of seconds
    :return: None
    :rtype: None
    :raises ValueError: from "extract_frames_and_metadata" function while extracting image frames and metadata
    """

    file_count = 0

    # Check if the list is empty
    if len(vid_list) == 0:
        logging.error("No video files found. Please provide one or more video files.")
        return False

    # Extract image frames and metadata from each video file
    for vid in vid_list:
        file_count += 1

        # Print time before starting the extraction
        start_time = datetime.now()
        print(f"Started extracting image frames and metadata from {vid} at {start_time}")

        print(f"{file_count}. Video filename: {vid}")
        extract_frames_and_metadata(vid, 
                                    output_dir,
                                    saving_frames_per_second,
                                    frames_after_number_of_seconds)

        # Print time after finishing the extraction
        end_time = datetime.now()
        print(f"Finished extracting image frames and metadata from {vid} at {end_time}")

        # Calculate the total time taken
        total_time = end_time - start_time

        # Extract hours, minutes, and seconds from the timedelta
        hours = total_time.seconds // 3600
        minutes = (total_time.seconds // 60) % 60
        seconds = total_time.seconds % 60

        # Format the total time as a string
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        # Print extration time
        print(f"Total time taken: {formatted_time}")

    # Print success message
    logging.info(f"Successfully extracted image frames and metadata from {len(vid_list)} video files.")
    return True

if __name__ == "__main__":
    """
    This is the main function that is executed when the script is run.
    """

    # Extract image frames and metadata from a single video file
    # extract_frames_and_metadata(VIDEO_FILE)

    # Extract image frames and metadata from multiple video files
    multi_vids_extraction(VIDEO_FILE_LIST)


