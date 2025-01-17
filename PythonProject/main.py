import yt_dlp
import subprocess


def download_and_convert_video(url):
    # Video formatlarını listele
    def list_available_formats(url):
        ydl_opts = {
            'quiet': True,  # Çıktıyı sessiz yap
            'force_generic_extractor': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            return formats

    # Video indirme işlemi
    def download_video(url, resolution='720p'):
        formats = list_available_formats(url)

        # Sadece sesli ve görüntülü formatları seç
        valid_formats = [
            f for f in formats if
            f.get('height') is not None and f.get('acodec') != 'none' and f.get('vcodec') != 'none'
        ]

        if not valid_formats:
            raise Exception("Ses ve görüntü içeren uygun bir format bulunamadı. Başka bir video seçin!")

        # 720p çözünürlüğü seçmeye çalış
        selected_format = None
        for f in valid_formats:
            if f.get('height') == 720 and f['ext'] in ['mp4', 'webm']:
                selected_format = f
                break

        # Eğer 720p formatı bulunamazsa en iyi çözünürlük seçilir
        if not selected_format:
            print(f"{resolution} çözünürlük bulunamadı, en uygun formatı seçiyorum...")
            selected_format = max(valid_formats, key=lambda f: f['height'])

        # İndirilen formatı video olarak kaydet
        ydl_opts = {
            'format': selected_format['format_id'],
            'outtmpl': 'downloaded_video.%(ext)s',
            'noplaylist': True,  # Playlist yok
            'quiet': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Video indiriliyor: {url}")
            ydl.download([url])
        print(f"Video indirildi: {selected_format['format_id']} çözünürlük")

    # İndirilen videoyu AVI formatına farklı bir ses codec'i ile dönüştürün
    def convert_to_avi(input_file, output_file):
        try:
            # ffmpeg kullanarak video dönüştürme işlemini yapar
            cmd = [
                "ffmpeg",
                "-i", input_file,  # Girdi dosyası
                "-c:v", "libxvid",  # AVI için video codec
                "-c:a", "mp3",  # MP3 formatında ses codec'i ekle
                output_file
            ]
            subprocess.run(cmd, check=True)
            print(f"Video AVI formatına dönüştürüldü ve şu dosya olarak kaydedildi: {output_file}")

        except subprocess.CalledProcessError as e:
            print(f"Dönüştürme sırasında bir hata oluştu: {e}")
        except FileNotFoundError:
            raise Exception("FFmpeg yüklenmemiş. Lütfen FFmpeg'i kurun!")

    # Videoyu indir ve dönüştür
    download_video(url)
    convert_to_avi("downloaded_video.mp4", "converted_video.avi")


# Kullanıcıdan video linkini al
url = input("YouTube video linkini girin: ")
download_and_convert_video(url)
