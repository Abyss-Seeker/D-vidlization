# 需要并可以开代理/VPN
from time import asctime as t
import os
import re
try:
    from pytube import YouTube, Playlist
    from moviepy.editor import AudioFileClip
except:
    try:
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pytube')
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy')
    except:
        os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pytube')
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy')
finally:
    from pytube import YouTube, Playlist
    from moviepy.editor import AudioFileClip

failure = []
suggest_url = []
default_output_path = "./YouTubeAudio"


def YoutubeAudioDownload(v, log=None, output_path=default_output_path, output_format='mp3', url=None, n=None):
    if log is not None and url is None:
        log.insert('end', f'{t()}\n')
        log.see('end')

    if output_path == '':
        output_path = default_output_path

    # 指定文件生成目录,如果不存在则创建目录
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 指定YouTube视频的URL
    if url is None:
        url = f'https://www.youtube.com/watch?v={v}'

    # 创建YouTube对象
    yt = YouTube(url)

    print(f'Finding stream of video...')
    if log is not None:
        log.insert('end', f'Finding stream of video\n')
        log.see('end')
    # 获取视频的所有可用流
    videoTitle = yt.title
    try:
        streams = yt.streams
        videopathTitle = re.sub(r"[\\/:*?\"<>|\[\]]", "", videoTitle)

        # 查找音频流
        audio_stream = streams.filter(only_audio=True).first()

        if yt.age_restricted:
            yt.bypass_age_gate()

        print(f'Downloading audio from {videoTitle}')
        if log is not None:
            log.insert('end', f'Downloading audio from {videoTitle}\n')
            log.see('end')

        # 下载音频
        audio_file_path = audio_stream.download(filename=f'{videopathTitle}.mp4', output_path=output_path)

        print(f'Converting audio format to {output_format}')
        if log is not None:
            log.insert('end', f'Converting audio format to {output_format}\n')
            log.see('end')

        audio = AudioFileClip(audio_file_path)
        output_file_path = f'{output_path}/{videopathTitle}.{output_format}'  # Output file path with desired format
        audio.write_audiofile(output_file_path)
        audio.close()

        os.remove(f'{output_path}/{videopathTitle}.mp4')

        print(f'Success. Audio files have been downloaded to {output_path}')
        if log is not None:
            log.insert('end', f'{t()}\n')
            log.insert('end', f'Success. Audio files have been downloaded to {output_path}\n')
            log.see('end')
    except:
        failure.append(n)
        suggest_url.append(f'{url[:19]}pi{url[19:]}')
        print(f'Failure: Episode {n} cannot be downloaded.\n Try going to {suggest_url[-1]} and manually download it')
        if log is not None:
            log.insert('end', f'Failure: Episode {n} cannot be downloaded.\n Try going to {suggest_url[-1]} and manually download it\n')
            log.see('end')


def YoutubeAudioDownloadList(listnum, p_start=1, p_end=1, log=None, output_path=default_output_path, output_format='mp3'):
    if log is not None:
        log.insert('end', f'{t()}\n')
        log.see('end')
    print('fetching playlist data...')
    if log is not None:
        log.insert('end', f'fetching playlist data...\n ')
        log.see('end')
    playlist_url = f'https://www.youtube.com/playlist?list={listnum}'
    playlist = Playlist(playlist_url)
    video_urls = playlist.video_urls # Make sure that p_end does not exceed (especially when there are repetitive videos in the same playlist, it will automatically delete these)
    max_p_end = len(video_urls)
    if p_end > max_p_end:
        p_end = max_p_end
    video_urls = video_urls[p_start-1:p_end]
    video_urls_length = len(video_urls)
    n = 1
    # 循环处理每个视频
    for url in video_urls:
        print(f'Video ({n}/{video_urls_length})')
        if log is not None:
            log.insert('end', f'Video ({n}/{video_urls_length}): ')
            log.see('end')
        # 下载url中的视频
        YoutubeAudioDownload(v=None, log=log, output_path=output_path, output_format=output_format, url=url, n=p_start+n-1)
        n += 1

    print(f'Success. Audio files from the play list {listnum = } have been downloaded to {output_path}')
    if log is not None:
        log.insert('end', f'Success. Audio files from the play list {listnum = } have been downloaded to {output_path}\n')
        log.see('end')
    if len(failure) != 0:
        print(f'However, we encountered errors while crawling episodes {failure}. You might want to manually download them with the links:')
        if log is not None:
            log.insert('end', f'However, we encountered errors while crawling episodes {failure}. You might want to manually download them with the links:\n')
            log.see('end')
        for url_idx in range(len(suggest_url)):
            print(f'    {failure[url_idx]}: {suggest_url[url_idx]}')
            if log is not None:
                log.insert('end',f'    {failure[url_idx]}: {suggest_url[url_idx]}\n')
                log.update()
                log.see('end')


if __name__ == '__main__':
    YoutubeAudioDownloadList('PLjEKzjxXYK-5qm6r6ejfLnF84caseuRnC', p_start=7, p_end=137, output_format='wav') #137
