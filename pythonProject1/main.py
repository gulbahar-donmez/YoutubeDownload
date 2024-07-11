#import pytube

#url=input("indireceğiniz videonun url'sini giriniz:")
#path="C:\\Users\\Gulbahar-NB\\PycharmProjects\\Downloader\\pythonProject1\\İndirilenler"
#try:
#    pytube.YouTube(url).streams.get_highest_resolution().download(path)
#    print("Video başarıyla indirildi.")
#except Exception as e:
 #   print(f"Bir hata oluştu: {e}")
#

import yt_dlp

url = input("indireceğiniz videonun url'sini giriniz:")
path = "C:\\Users\\Gulbahar-NB\\PycharmProjects\\Downloader\\pythonProject1\\İndirilenler"

ydl_opts = {
    'outtmpl': f'{path}/%(title)s.%(ext)s',
    'format': 'best'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Video başarıyla indirildi.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
