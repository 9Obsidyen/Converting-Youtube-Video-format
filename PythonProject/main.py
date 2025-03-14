import yt_dlp
import subprocess
import os


def check_ffmpeg_installed():
    """
    Checks if FFmpeg is installed on the system and accessible through the PATH environment variable.
    If FFmpeg is not found, raise an error.
    """
    try:
        # Try to get FFmpeg's version to confirm it's installed
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg is installed and accessible.")
    except FileNotFoundError:
        raise Exception("FFmpeg is not installed or not found in the system's PATH. Please install FFmpeg and ensure it's in the PATH.")
    except subprocess.CalledProcessError:
        raise Exception("FFmpeg installation is incorrect or FFmpeg could not be executed.")


def download_and_convert_video(url, resolution='720p', output_format='avi'):
    """
    Downloads a YouTube video and converts it into the desired format using FFmpeg.
    
    - Downloads the video in the specified resolution (e.g., 720p, 1080p, etc.).
    - Converts the downloaded video to the specified format using FFmpeg.
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

    # Function to convert the downloaded video to the desired format using FFmpeg
    def convert_to_format(input_file, output_file, output_format):
        try:
            # Check if FFmpeg is installed and accessible in the system's PATH
            check_ffmpeg_installed()

            # Construct the FFmpeg command for video conversion
            cmd = [
                "ffmpeg",  # FFmpeg is assumed to be available globally via PATH
                "-i", input_file,  # Input file path
            ]
            
            # Set the output format and codecs based on the desired format
            if output_format == "avi":
                cmd += ["-c:v", "libxvid", "-c:a", "libmp3lame"]  # Use libmp3lame for MP3 audio codec in AVI
            elif output_format == "mp4":
                cmd += ["-c:v", "libx264", "-c:a", "aac"]  # Use libx264 for video and AAC for audio in MP4
            elif output_format == "mov":
                cmd += ["-c:v", "prores_ks", "-c:a", "pcm_s16le"]  # Use ProRes for MOV video and PCM audio
            elif output_format == "mkv":
                cmd += ["-c:v", "libx264", "-c:a", "aac"]  # MKV with libx264 and AAC
            elif output_format == "flv":
                cmd += ["-c:v", "flv", "-c:a", "aac"]  # FLV format with H.264 video and AAC audio
            else:
                raise Exception(f"Unsupported format: {output_format}")

            cmd.append(output_file)  # Output file path

            # Run the FFmpeg command
            subprocess.run(cmd, check=True)
            print(f"Video successfully converted to {output_format.upper()} format. Output saved as: {output_file}")

        except subprocess.CalledProcessError as e:
            # Handle errors during the conversion process
            print(f"An error occurred during the conversion: {e}")
        except FileNotFoundError:
            # If FFmpeg is not installed or not in PATH, raise an exception
            raise Exception("FFmpeg is not installed. Please install FFmpeg to proceed!")

    # Download the video and convert it to the selected format
    download_video(url, resolution)
    convert_to_format("downloaded_video.mp4", f"converted_video.{output_format}", output_format)


# Prompt the user to input the YouTube video URL, desired resolution, and output format
url = input("Enter the YouTube video URL: ")
resolution = input("Enter the desired resolution (e.g., 720p, 1080p, 2k, 4k): ")
output_format = input("Enter the desired output format (avi, mp4, mov, mkv, flv): ").lower()

# Ensure the user enters a valid format
valid_formats = ['avi', 'mp4', 'mov', 'mkv', 'flv']
if output_format not in valid_formats:
    print(f"Invalid format '{output_format}' entered. Defaulting to 'avi'.")
    output_format = 'avi'

download_and_convert_video(url, resolution, output_format)
