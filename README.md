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

1. Download the FFmpeg Windows build from the [FFmpeg official website](https://ffmpeg.org/download.html).
   - Select **Windows** and then choose **Windows builds by BtbN** or **Gyan** for a precompiled version.
   
2. Extract the contents of the downloaded zip file.
   - You will see a folder named `ffmpeg`.

3. Add the `bin` folder to your system's PATH environment variable:
   - **Right-click on 'This PC' (or 'My Computer') > Properties**.
   - Click on **Advanced system settings** on the left.
   - Click **Environment Variables**.
   - Under **System Variables**, scroll to find the **Path** variable and select it.
   - Click **Edit**.
   - Add the full path of the `bin` directory inside the extracted FFmpeg folder (e.g., `C:\ffmpeg\bin`).
   - Click **OK** to save the changes.

4. Verify FFmpeg installation:
   - Open a Command Prompt and type:
     ```
     ffmpeg -version
     ```
   - If FFmpeg is correctly installed, it should display version information.

#### For macOS:

1. You can install `ffmpeg` using [Homebrew](https://brew.sh/):
   - First, ensure you have Homebrew installed. If not, run:
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Then, install FFmpeg using:
     ```
     brew install ffmpeg
     ```
   
2. Verify FFmpeg installation:
   - Open the Terminal and type:
     ```
     ffmpeg -version
     ```
   - If installed correctly, you should see version information.

#### For Linux (Ubuntu/Debian):

1. To install `ffmpeg`, run the following commands:

```
sudo apt update sudo apt install ffmpeg
```


2. Verify FFmpeg installation:
- Open a terminal and type:
  ```
  ffmpeg -version
  ```
- If FFmpeg is correctly installed, it will display version details.

### 4. Dependencies:
The script uses the `subprocess` library, which is built into Python, so no additional installation is needed for it.

## Usage

1. Clone this repository to your local machine:

```
git clone https://github.com/9Fahrenheit Converting-Youtube-video-to-avi-format.git
```

2. Navigate to the script directory:

```
cd Converting-Youtube-video-to-avi-format
```

3. Run the script:

```
python main.py
```

4. When prompted, paste the YouTube video URL that you wish to download and convert.

## Notes

- **Ensure that `ffmpeg` is correctly installed and accessible via your system’s PATH.**
- The script will download the video, select the best available format (preferably 720p), and save it as `downloaded_video.mp4`.
- After the download, it will convert the video to `converted_video.avi` using `ffmpeg`.

## Troubleshooting

- **FFmpeg Not Found**: If you encounter an error stating that `ffmpeg` is not found, ensure that FFmpeg is installed and added to your system’s PATH. You can verify it by running `ffmpeg -version` in the terminal.
- **Download Failures**: If the download fails, check if the URL is correct or if there are issues with the YouTube video (e.g., region restrictions or private video settings).

