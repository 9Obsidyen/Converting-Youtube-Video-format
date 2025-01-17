# Video Download and Convert Script

## Description

This Python script allows users to download videos from YouTube using `yt-dlp`,  
with the ability to select the best available video format (preferably 720p resolution).  
It also supports converting the downloaded video to AVI format using `ffmpeg`,  
with the audio converted to MP3.  
This tool is ideal for users who need to download YouTube videos and convert them to a specific format for offline use or further editing.

## Installation

Before running the script, ensure you have the following dependencies installed:

### 1. Python
This script requires Python 3.x. You can download Python from [here](https://www.python.org/downloads/).

### 2. yt-dlp
To install `yt-dlp`, run the following command in your terminal or command prompt:

```
  pip install yt-dlp
```

### 3. FFmpeg
`ffmpeg` is a powerful multimedia processing tool used to convert videos between formats. You need to have `ffmpeg` installed on your system to convert videos.

#### For Windows:
1. Download the FFmpeg Windows build from [FFmpeg official website](https://ffmpeg.org/download.html).
2. Extract the contents and add the `bin` folder to your system’s PATH environment variable. This will allow you to use `ffmpeg` from the command line.

#### For macOS:
You can install `ffmpeg` using Homebrew:

```
  brew install ffmpeg
```

#### For Linux (Ubuntu/Debian):
To install `ffmpeg`, run:

```
  sudo apt update
  sudo apt install ffmpeg
```

Make sure that FFmpeg is added to your PATH. You can verify its installation by running:

```
  ffmpeg -version
```


### 4. Dependencies:
The script also uses the `subprocess` library, which is built into Python, so no additional installation is needed for it.

## Usage

1. Clone this repository to your local machine:

```
  git clone https://github.com/yourusername/video-download-and-convert.git
```

2. Navigate to the script directory:

```
  cd video-download-and-convert
```

3. Run the script:

```
  python script_name.py
```


4. When prompted, paste the YouTube video URL that you wish to download and convert.

## Notes

- Ensure that `ffmpeg` is correctly installed and accessible via your system’s PATH.
- The script will download the video, select the best available format (preferably 720p), and save it as `downloaded_video.mp4`.
- After the download, it will convert the video to `converted_video.avi` using `ffmpeg`.

## Troubleshooting

- If you encounter an error stating that `ffmpeg` is not found, make sure it is installed and added to your system’s PATH.
- If the download fails, check if the URL is correct or if there are issues with the YouTube video.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

