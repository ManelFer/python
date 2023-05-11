from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os

def download_video():
    link = input('Digite o Link do Vídeo')
    path = input('Caminho de download')
    yt = YouTube(link)
    #Fazer o dowload
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download Completo")