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

print(os.path.dirname(os.path.abspath(__file__)))