# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:03:39 2023

@author: EMINEM
"""
import urllib

import requests
#import youtube_dl
from pytube import YouTube
from moviepy.editor import *

import os
#from pydub import AudioSegment




from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK, APIC
from mutagen.easyid3 import EasyID3



class conversion:

    searched_song_results  = {}
    searched_song_location = ""

    def getsong(self,searched_song_resultsx,searched_song_locationy,index):
        global searched_song_results
        global searched_song_location
        searched_song_results = searched_song_resultsx
        searched_song_location = searched_song_locationy
        print(searched_song_results)

        return (conversion().song_download(index))




    def song_download(self,index):


        link = 'https://music.youtube.com/watch?v='+searched_song_results[index][4]
        print(link)
        #song_info = youtube_dl.YoutubeDL().extract_info(url=link, download=False)
        #filename = f"{song_info['title']}.mp3"
        filename = searched_song_results[index][0]+".mp3"

        yt = YouTube(link)
        yt.title = "".join([c for c in yt.title if c not in ['/', '\\', '|', '?', '*', ':', '>', '<', '"']])
        video = yt.streams.filter(only_audio=True).first()
        vid_file = video.download(output_path = searched_song_location)
        base = os.path.splitext(vid_file)[0]
        audio_file = base + ".mp3"
        mp4_no_frame = AudioFileClip(vid_file)
        mp4_no_frame.write_audiofile(audio_file, logger=None)
        mp4_no_frame.close()
        os.remove(vid_file)
        #os.replace(audio_file, searched_song_location+"\\"+yt.title+".mp3")
        os.replace(audio_file, searched_song_location+"/"+yt.title+".mp3")
        print(audio_file)
        #audio_file = searched_song_location+"\\"+yt.title+".mp3"
        audio_file = searched_song_location+"/"+yt.title+".mp3"

        #
        # ydl_opts = {
        #
        #     'format': 'best' , "outtmpl": filename,
        #     # 'postprocessors': [{
        #     #     'key': 'FFmpegExtractAudio',
        #     #     'preferredcodec': 'mp3',
        #     #     'preferredquality': '192',
        #     # }],
        # }
        #
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     ydl.extract_info(link, download=True)

        conversion().song_tagging(audio_file,index)
        return filename



    def getalbum(self):
        #getsong()
        pass


    def song_tagging(self,filename,index):

            artwork_url = searched_song_results[index][5]
            artwork_data = requests.get(artwork_url).content









            # #Read the ID3 tag or create one if not present
            # try:
            #     tags = ID3(searched_song_location+'\\'+filename)
            # except ID3NoHeaderError:
            #     print("Adding ID3 header")
            #     tags = ID3()
            #     # tags = EasyID3()
            #
            # tags["TIT2"] = TIT2(encoding=3, text=searched_song_results[index][0])
            # tags["TALB"] = TALB(encoding=3, text=searched_song_results[index][1])
            # tags["TPE2"] = TPE2(encoding=3, text=u'Band')
            # tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'My comment')
            # tags["TPE1"] = TPE1(encoding=3, text=searched_song_results[0][2])
            # tags["TCOM"] = TCOM(encoding=3, text=u'Composer')
            # tags["TCON"] = TCON(encoding=3, text=u'Genre')
            # tags["TDRC"] = TDRC(encoding=3, text=u'None')
            # tags["TRCK"] = TRCK(encoding=3, text=u'N/A')
            #
            # try:
            #     with open("C:\\Users\\mchog\\Desktop\\EMINEM\\IMG_6096.JPEG", 'rb') as albumart:
            #         tags['APIC'] = APIC(
            #             encoding=3,
            #             mime='image/jpeg',
            #
            #             type=3, desc=u'Cover'
            #             ,data=artwork_data
            #         )
            #
            #
            #
            #
            # except IOError:
            #
            #     pass
            # # tags.save(filename=song,v2_version=3)
            # # tags.save(filename=song,v1=1)
            #
            # tags.save(searched_song_location+'\\'+filename)
            location = filename
            mp3file = EasyID3(location)
            mp3file["albumartist"] = searched_song_results[0][2]
            mp3file["artist"] = searched_song_results[0][2]
            mp3file["album"] = searched_song_results[index][1]
            mp3file["title"] = searched_song_results[index][0]
            mp3file.save()

            audio = ID3(filename)



            audio.save(v2_version=3)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)
            print(searched_song_location)

            print('adding album art')

            audio = ID3(filename)
            with urllib.request.urlopen(artwork_url) as albumart:
                audio["APIC"] = APIC(
                    encoding=3, mime="image/jpeg", type=3, desc="Cover", data=albumart.read()
                )
            audio.save(v2_version=3)








