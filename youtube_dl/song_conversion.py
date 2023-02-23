# # -*- coding: utf-8 -*-
# """
# Created on Mon Feb 20 21:03:39 2023
#
# @author: EMINEM
# """
#
# import yt_dlp
#
# from mutagen.id3 import ID3NoHeaderError
# from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK, APIC
# from mutagen.mp3 import MP3
# from mutagen.easyid3 import EasyID3
#
#
#
# def run():
#     video_url = "https://music.youtube.com/watch?v=9_rgBR-IYdM"
#     video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
#
#
#     filename = f"{video_info['title']}.mp3"
#
#     ydl_opts = {
#         'format': 'bestaudio',"outtmpl":filename,
#
#     }
#
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.extract_info(video_url,download=True)
#         song = "C:\\Users\\mchog\\Desktop\\ytmusic\\Twisted.mp3"
#
#
#
#
# # Read the ID3 tag or create one if not present
#         try:
#             tags = ID3(song)
#         except ID3NoHeaderError:
#             print("Adding ID3 header")
#             tags = ID3()
#             #tags = EasyID3()
#
#         tags["TIT2"] = TIT2(encoding= 3, text="Title")
#         tags["TALB"] = TALB(encoding= 3, text=u'Album')
#         tags["TPE2"] = TPE2(encoding= 3, text=u'Band')
#         tags["COMM"] = COMM(encoding= 3, lang=u'eng', desc='desc', text=u'My comment')
#         tags["TPE1"] = TPE1(encoding= 3, text=u'Artist')
#         tags["TCOM"] = TCOM(encoding= 3, text=u'Composer')
#         tags["TCON"] = TCON(encoding= 3, text=u'Genre')
#         tags["TDRC"] = TDRC(encoding= 3, text=u'2010')
#         tags["TRCK"] = TRCK(encoding= 3, text=u'track_number')
#
#         try:
#             with open("C:\\Users\\mchog\\Desktop\\EMINEM\\IMG_6096.JPEG", 'rb') as albumart:
#                 tags['APIC'] = APIC(
#                     encoding=3,
#                     mime='image/jpeg',
#
#                     type=3, desc=u'Cover',
#                     data=albumart.read()
#                 )
#                 print("Called baby")
#
#
#
#         except IOError:
#
#             pass
#         # tags.save(filename=song,v2_version=3)
#         # tags.save(filename=song,v1=1)
#
#
#         tags.save(song)
#
#
#
#
#
#
#
#
#
#
# run()
#
