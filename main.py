import urllib.request
import random
import argparse
import os
import pyperclip
from pytube import YouTube


def FromTo(start,end):
    for i in range(ord(start),ord(end)):
        yield chr(i)

def GenerateName():
    white_list = []
    result = ''
    for i in FromTo('A','Z'):
        white_list.append(i)
    for i in FromTo('a','z'):
        white_list.append(i)
    for i in FromTo('0','9'):
        white_list.append(i)
    for i in range(10):
        result+=random.choice(white_list)
    return result


def youtube(url:str,name:str) -> None:
    YouTube(url).streams.first().download("./video",filename=name)

parser = argparse.ArgumentParser()
parser.add_argument('-n',action='store',dest='name',help='Name of video')
args = parser.parse_args()
url_link = pyperclip.paste()

if args.name:
    name = args.name
else:
    name = GenerateName()
if not os.path.exists("./video"):
    os.makedirs("./video")
directory = os.walk('./video')
path, dirs, files = next(directory)
if f'{name}.mp4' in files:
    resave = input('Файл с таким именем уже существует.Перезаписать его? Y/N  ')
    if resave == 'N':
        name = input("Введите новое имя файла: ")
try:
    if "https://www.youtube.com/watch" in url_link or "https://vk.com/video" in url_link:
        youtube(url_link,name)
    else:
        urllib.request.urlretrieve(url_link, f'video/{name}.mp4')
    print(f"Файл {name}.mp4 успешно создан!")
except Exception as e:
    print("Я не могу скачать видео по этой ссылке, попробуйте снова...")
    print(e)
