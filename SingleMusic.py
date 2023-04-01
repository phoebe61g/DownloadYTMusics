from pytube import YouTube
import os
path = input("Path to stored: ")
os.chdir(path)
url = input("Music's URL: ")
music = YouTube(url)
name = music.title
print("Downloading: {name}")
try:
    music.streams.filter().get_audio_only().download(filename= name + ".mp3")
    print("Successed.")
except:
    print("Failed.")
