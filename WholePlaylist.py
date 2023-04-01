from pytube import YouTube
from pytube import Playlist
import os
path = input("Path to stored: ")
os.chdir(path)
my_playlist = input("Playlist URL: ")
playlist = Playlist(my_playlist)
print(f'Playlist name: {playlist.title}')
print(f'Number of musics: {playlist.length}')
Suc = 0
faillist = []
print("---------- Start Downloading ----------")
for url in playlist:
	music = YouTube(url)
	name = music.title
	try:
		music.streams.filter().get_audio_only().download(filename= name + ".mp3")
		print("{} --> Successed.".format(name))
		Suc += 1
	except:
		print("{} --> Failed.".format(name))
		faillist.append(name)
print("---------------------------------------")
print("Finished. {} successed, {} failed.".format(Suc,len(faillist)))
if len(faillist) > 0:
	print("Failed downloading:")
	for f in faillist:
		print(f)
