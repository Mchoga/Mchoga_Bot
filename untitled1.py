from pytube import YouTube
from ytmusicapi.parsers import browsing
from ytmusicapi import YTMusic
import os

header = "C:\\Users\\mchog\\Desktop\\Mchoga_Bot\\ytmusic\\header.json"
yt = YTMusic(header)
results = yt.search("eminem", filter="albums")




x = 77
if x ==5:
    print(5)

if x ==7:
    print(7)
else:
    print("none")