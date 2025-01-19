import yt_dlp
import subprocess
import os


def check_ffmpeg_installed():
    """
    Checks if FFmpeg is installed in the 'ffmpeg/bin' directory relative to the location of 'main.py'.
    Ensures that the FFmpeg executable is found in the correct directory.
    """
    ffmpeg_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ffmpeg", "bin", "ffmpeg.exe")
    
    # If FFmpeg executable is not found in the specified directory, raise an error
    if not os.path.exists(ffmpeg_path):
        raise Exception("FFmpeg.exe not found. Please ensure 'ffmpeg/bin' is in the same directory as 'main.py'.")
    
    return ffmpeg_path


def download_and_convert_video(url, resolution='720p'):
    """
    Downloads a YouTube video and converts it into an AVI file using FFmpeg.
    
    - Downloads the video in the specified resolution (e.g., 720p, 1080p, etc.).
    - Converts the downloaded video to AVI format using the 'libxvid' video codec and 'mp3' audio codec.
    """
    
    # Function to list all available formats for a given YouTube URL
    def list_available_formats(url):
        ydl_opts = {
            'quiet': True,  # Suppress unnecessary output
            'force_generic_extractor': False,  # Use the default extractor
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract metadata (formats) for the video without downloading it
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            return formats

    # Function to download the video in a selected resolution
    def download_video(url, resolution='720p'):
        formats = list_available_formats(url)

        # Filter formats to include only those with both audio and video codecs
        valid_formats = [
            f for f in formats if
            f.get('height') is not None and f.get('acodec') != 'none' and f.get('vcodec') != 'none'
        ]

        if not valid_formats:
            raise Exception("No valid format with both video and audio found. Please choose another video!")

        # Convert the desired resolution (e.g., '720p') to integer (720)
        target_resolution = int(resolution[:-1]) if resolution.endswith('p') else 0

        selected_format = None
        # Attempt to select the format that matches the target resolution
        for f in valid_formats:
            if f.get('height') == target_resolution and f['ext'] in ['mp4', 'webm']:
                selected_format = f
                break

        # If the requested resolution is not found, select the highest available resolution
        if not selected_format:
            print(f"Requested resolution {resolution} not found. Selecting the best available resolution...")
            selected_format = max(valid_formats, key=lambda f: f['height'])

        # Configure download options with the selected format
        ydl_opts = {
            'format': selected_format['format_id'],
            'outtmpl': 'downloaded_video.%(ext)s',  # Output file name template
            'noplaylist': True,  # Download a single video, not a playlist
            'quiet': False,  # Show download progress
        }

        # Download the selected video format
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
        print(f"Video successfully downloaded in {selected_format['format_id']} format.")

    # Function to convert the downloaded video to AVI format using FFmpeg
    def convert_to_avi(input_file, output_file):
        try:
            # Check if FFmpeg is installed in the 'ffmpeg/bin' directory
            ffmpeg_path = check_ffmpeg_installed()

            # Construct the FFmpeg command for video conversion
            cmd = [
                ffmpeg_path,  # Path to FFmpeg executable
                "-i", input_file,  # Input file path
                "-c:v", "libxvid",  # Video codec: libxvid (for AVI format)
                "-c:a", "mp3",  # Audio codec: mp3
                output_file  # Output file path
            ]
            # Run the FFmpeg command
            subprocess.run(cmd, check=True)
            print(f"Video successfully converted to AVI format. Output saved as: {output_file}")

        except subprocess.CalledProcessError as e:
            # Handle errors during the conversion process
            print(f"An error occurred during the conversion: {e}")
        except FileNotFoundError:
            # If FFmpeg is not installed, raise an exception
            raise Exception("FFmpeg is not installed. Please install FFmpeg to proceed!")

    # Download the video and convert it to AVI format
    download_video(url, resolution)
    convert_to_avi("downloaded_video.mp4", "converted_video.avi")


# Prompt the user to input the YouTube video URL and desired resolution
url = input("Enter the YouTube video URL: ")
resolution = input("Enter the desired resolution (e.g., 720p, 1080p, 2k, 4k): ")
download_and_convert_video(url, resolution)
