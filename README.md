# YouTube Video Downloader & Converter

## Description

This Python script allows you to download videos from YouTube and convert them into various formats. Supported formats include `avi`, `mp4`, `mov`, `mkv`, and `flv`. After the video is downloaded, it will be converted into the selected format and resolution using FFmpeg.

## Requirements

### 1. Python
This script requires Python 3.x. You can download Python from [here](https://www.python.org/downloads/).

### 2. yt-dlp
`yt-dlp` is a Python library that allows you to download videos from YouTube. To install `yt-dlp`, run the following command in your terminal or command prompt:

pip install yt-dlp

### 3. FFmpeg
FFmpeg is a powerful multimedia framework that is required for video conversion. You need to install FFmpeg on your system for the script to work.

#### Windows:
1. Download the FFmpeg Windows build from the [FFmpeg official website](https://ffmpeg.org/download.html).
2. Extract the files and add the `bin` folder to your system's `PATH` environment variable. This allows you to run `ffmpeg` from anywhere in the command line.
3. To check if FFmpeg is installed correctly, run the following command in the command prompt:

```
ffmpeg -version
```

#### macOS:
You can install FFmpeg using Homebrew on macOS:

```
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
To install FFmpeg on Ubuntu/Debian systems, run the following commands:

```
sudo apt update sudo apt install ffmpeg
```

To verify the installation, run:

```
ffmpeg -version
```

Make sure FFmpeg is added to your system's `PATH` environment variable.

### 4. Other Requirements:
The script also uses the built-in Python `subprocess` library, so no additional installation is required for that.

## Usage

1. Clone this repository to your local machine:

```
git clone https://github.com/9Fahrenheit/Converting-Youtube-video-to-avi-format.git
```

2. Navigate to the script directory:

```
cd Converting-Youtube-video-to-avi-format
```

3. Run the script:

```
python main.py
```

4. When the script is run, you will be prompted to enter the YouTube video URL, the resolution (e.g., `720p`, `1080p`), and the desired video format (e.g., `avi`, `mp4`, `mov`, `mkv`, `flv`).

### Example Usage:

```
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ 
Enter the desired resolution (e.g., 720p, 1080p, 2k, 4k): 720p 
Enter the desired output format (avi, mp4, mov, mkv, flv): mp4
```

## How It Works

1. The script takes the YouTube video URL and uses `yt-dlp` to download the video in the specified resolution.
2. After downloading, the video file is converted to the selected format using `ffmpeg`.
3. The converted video is saved in the chosen format.

## Supported Video Formats

The script supports converting videos to the following formats:
- **AVI**: Converted using `libxvid` video codec and `libmp3lame` audio codec.
- **MP4**: Converted using `libx264` video codec and `aac` audio codec.
- **MOV**: Converted using `prores_ks` video codec and `pcm_s16le` audio codec.
- **MKV**: Converted using `libx264` video codec and `aac` audio codec.
- **FLV**: Converted using `flv` video codec and `aac` audio codec.

## Troubleshooting

- **FFmpeg not found error**: If you encounter an error indicating that FFmpeg is not found, make sure it is installed correctly. You can verify its installation by running `ffmpeg -version` in your terminal.
  
- **Video download failure**: Ensure the YouTube URL is correct and the video is accessible. There may also be issues related to video quality or format compatibility.

## Contribution

This project is open-source and contributions are welcome. Feel free to submit pull requests!
