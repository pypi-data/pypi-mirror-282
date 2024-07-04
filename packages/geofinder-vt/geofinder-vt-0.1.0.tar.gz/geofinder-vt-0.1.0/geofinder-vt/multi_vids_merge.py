from moviepy.editor import concatenate_videoclips, VideoFileClip

def merge_videos(video_files=None, output_file="merged_vids.MP4"):
    """
    Merges multiple video files into a single video file using MoviePy.

    Args:
        video_files (list): A list of file paths to the video files to be merged.
        output_file (str): The file path to save the merged video file. Default is "merged_vids.MP4".

    Returns:
        bool: True if the video files were successfully merged and saved to the output file, False otherwise.
    """
    
    if video_files is not None:
        # Load video files using MoviePy
        video_clips = [VideoFileClip(video) for video in video_files]

        # Concatenate video clips into a single video
        final_clip = concatenate_videoclips(video_clips)

        # Write the result to a file    
        final_clip.write_videofile(output_file, codec='libx264')

        return True
    else:
        print("No video files to merge")
        return False

