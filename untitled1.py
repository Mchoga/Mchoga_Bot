import requests
import youtube_dl

import os
#from pydub import AudioSegment
from moviepy.editor import *
from mutagen.easyid3 import EasyID3

from  mutagen.mp3 import  MPEGInfo
from  mutagen.mp3 import  MP3
from pytube import YouTube


from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK, APIC
from mutagen.easyid3 import EasyID3

yt_link = 'https://music.youtube.com/watch?v=MS8nzdQkNXk&list=RDAMPLOLAK5uy_lq1nVIPf-IP_CgZtt4Mjx_lJ1kzgcbRTU'
def download_yt(yt_link):
    """download the video in mp3 format from youtube"""
    yt = YouTube(yt_link)
    # remove chars that can't be in a windows file name
    yt.title = "".join([c for c in yt.title if c not in ['/', '\\', '|', '?', '*', ':', '>', '<', '"']])
    # don't download existing files if the user wants to skip them
    exists = os.path.exists(f"../music/{yt.title}.mp3")


    # download the music
    video = yt.streams.filter(only_audio=True).first()
    vid_file = video.download(output_path="../music/tmp")
    # convert the downloaded video to mp3
    base = os.path.splitext(vid_file)[0]
    audio_file = base + ".mp3"
    mp4_no_frame = AudioFileClip(vid_file)
    mp4_no_frame.write_audiofile(audio_file, logger=None)
    mp4_no_frame.close()
    os.remove(vid_file)
    os.replace(audio_file, f"../music/tmp/{yt.title}.mp3")
    audio_file = f"../music/tmp/{yt.title}.mp3"
    print(audio_file)
    mp3file = EasyID3(audio_file)
    mp3file["albumartist"] = "artist_name"
    mp3file["artist"] = "artists"
    mp3file["album"] = "album_name"
    mp3file["title"] = "track_title"
    mp3file.save()
    return audio_file

download_yt(yt_link)