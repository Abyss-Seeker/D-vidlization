import moviepy.audio.fx.audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.editor import *
import moviepy.audio.fx.all as afx
import os

# -----audio edition-----
def audio_volume(audio, n1, n2):  # n就是音量几倍,n1左声道,n2右声道
    audio = audio.volumex([n1, n2])
    return audio

def audio_volume2(audio, n):  # n就是音量几倍,n1左声道,n2右声道
    audio = audio.volumex([n, n])
    return audio

def audio_speed(audio,n): #倍速播放
    dur = audio.duration
    audio = audio.fl_time(lambda t: n * t, apply_to=['mask', 'audio'])
    audio = audio.set_duration(dur / n)
    return audio

def audio_edit(audio, n1, n2):  # n1,n2为开始时间和结束时间in seconds
    if n2 == -1:
        n2 = audio.duration
    audio = audio.subclip(n1, n2)
    return audio

def audio_loop(audio, n):  # n为循环次数
    audio =audio_fade(audio,0.5,0.5) #默认增加了每个音频片段前后各0.5秒的渐入渐出以更好衔接
    audio = afx.audio_loop(audio, nloops=n)
    return audio

def audio_fade(audio, n1, n2): #n1为渐入时间，n2为渐出时间，都是以秒为单位
    audio = moviepy.audio.fx.audio_fadein.audio_fadein(audio, duration=n1)
    audio = audio_fadeout(audio, duration=n2)
    return audio

def audio_3D(audio,x):  #将音频转成3D环绕，x可以为0.1，0.5，1，2，3，5
    x=-x
    n = int(audio.duration)
    audioList = []
    a, b= 0, 30  # 左声道，右声道，Δx
    for i in range(n):
        for ii in range(10):
            # print('a2',i,ii)
            clip = audio_edit(audio, i + ii / 10, i + ii / 10 + 0.1) #把每一个小片段是0.1秒
            if a * b == 0:
                x *= -1
            a, b = a + x, b - x
            #print(a, b)
            clip = audio_volume(clip, a / 10, b / 10)
            audioList.append(clip)
    audio = concatenate_audioclips(audioList)
    return audio

def audio_compress(path,name,name2,compress_num):
    os.chdir(path)
    os.system("ffmpeg -y -i "+str(name)+" -ar "+str(compress_num)+" "+name2)