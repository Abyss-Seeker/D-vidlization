# This code is modified from the zhihu article https://zhuanlan.zhihu.com/p/148988473 by 程序猿城南
# There are still some major issues when u want to crawl some of the old videos but
# Yeah.

import json
import os
try:
    import requests
    from lxml import etree
except:
    try:
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests')
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml')
    except:
        os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests')
        os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml')
finally:
    import requests
    from lxml import etree
from ExtractAudio import vid2mp3
from time import asctime as t

# 防止因https证书问题报错
requests.packages.urllib3.disable_warnings()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36',
    'Referer': 'https://www.bilibili.com/'
}

'''
    获取bilibili视频的主要函数
    @param url 视频页面url 结构为:url?参数
    @param p 视频p数
    @param bv 视频bv数
'''

default_output_path = "./BiliAudio"


def getBiliBiliAudio(bv, p, log=None, output_path=default_output_path, output_format='mp3'):
    url = f'https://www.bilibili.com/video/{bv}?p={p}'
    session = requests.session()
    res = session.get(url=url, headers=headers, verify=False)
    _element = etree.HTML(res.content)
    # 获取window.__playinfo__的json对象,[20:]表示截取'window.__playinfo__='后面的json字符串
    videoPlayInfo = str(_element.xpath('//head/script[3]/text()')[0].encode('utf-8').decode('utf-8'))[20:]
    videoJson = json.loads(videoPlayInfo)
    # 获取视频链接和音频链接
    try:
        # 2018年以后的b站视频由.audio和.video组成 flag=0表示分为音频与视频
        audioURL = videoJson['data']['dash']['audio'][0]['baseUrl']
        flag = 0
    except Exception:
        # 2018年以前的b站视频音频视频结合在一起,后缀为.flv flag=1表示只有视频
        videoURL = videoJson['data']['durl'][0]['url']
        flag = 1

    # 指定文件生成目录,如果不存在则创建目录
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 获取每一集的名称
    name = bv + "-" + str(p)


    # 下载
    if flag == 0:
        print(f'Downloading audio of {name}')
        log.insert('end', f'Downloading audio of {name}\n')
        log.see('end')
        log.update()
        fileDownload(homeurl=url, url=audioURL, name=f'{output_path}/{name}_Audio.{output_format}', session=session)  # 记得去. (Output format)
    elif flag == 1:
        print('WARNING!!! THE DOWNLOADED FILE IS PROBABLY FRAGMENTED. JUST ABORT IT IF ANYTHING.')
        log.insert('end', 'WARNING!!! THE DOWNLOADED FILE IS PROBABLY FRAGMENTED. JUST ABORT IT IF ANYTHING.\n')
        log.see('end')
        log.update()
        print(f'Downloading video of {name}')
        print('WARNING!!! THE DOWNLOADED FILE IS PROBABLY FRAGMENTED. JUST ABORT IT IF ANYTHING.')
        log.insert('end', 'WARNING!!! THE DOWNLOADED FILE IS PROBABLY FRAGMENTED. JUST ABORT IT IF ANYTHING.\n')
        log.see('end')
        log.update()
        if not os.path.exists(os.path.join(output_path, 'additional_vids')):
            os.makedirs(os.path.join(output_path, 'additional_vids'))
        fileDownload(homeurl=url, url=videoURL, name=f'{output_path}/additional_vids/{name}_Audio.mp4', session=session)
        print(f'Extracting audio out of video {name}')
        log.insert('end', f'Extracting audio out of video {name}\n')
        log.see('end')
        log.update()
        vid2mp3(path=f'{output_path}/additional_vids/{name}_Audio.mp4', output_path=output_path, output_dir_tail='', output_format=output_format)
        #  os.remove(f'{output_path}/{name}_Audio.mp4')
'''
    使用session保持会话下载文件
    @param homeurl 访问来源
    @param url 音频或视频资源的链接
    @param name 下载后生成的文件名
    @session 用于保持会话
'''


def fileDownload(homeurl, url, name, session=requests.session()):
    # 添加请求头键值对,写上 refered:请求来源
    headers.update({'Referer': homeurl})
    # 发送option请求服务器分配资源
    session.options(url=url, headers=headers, verify=False)
    # 指定每次下载1M的数据
    begin = 0
    end = 1024 * 512 - 1
    flag = 0
    # while True:
    # 添加请求头键值对,写上 range:请求字节范围
    # headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)}) #
    # 获取视频分片
    res = session.get(url=url, headers=headers, verify=False)
    if res.status_code != 416:
        # 响应码不为为416时有数据
        begin = end + 1
        end = end + 1024 * 512
    else:
        #  headers.update({'Range': str(end + 1) + '-'})
        res = session.get(url=url, headers=headers, verify=False)
        flag = 1
    with open(name.encode("utf-8").decode("utf-8"), 'ab') as fp:
        fp.write(res.content)
        fp.flush()
    # data=data+res.content
    if flag == 1:
        fp.close()
        # break


def BilibiliAudioDownload(bv, p_start=1, p_end=1, log=None, output_path=default_output_path, output_format='mp3'):
    log.insert('end', f'{t()}\n')
    log.see('end')
    total_num = p_end - p_start + 1
    n = 1
    if output_path == '':
        output_path = default_output_path
    for i in range(p_start, p_end+1):
        print(f'Video ({n}/{total_num})')
        log.insert('end', f'Video ({n}/{total_num}): ')
        log.see('end')
        getBiliBiliAudio(bv=bv, p=i, log=log, output_path=output_path, output_format=output_format)
        n += 1
    print(f'Success. Audio files have been downloaded to {output_path}')
    log.insert('end', f'{t()}\n')
    log.insert('end', f'Success. Audio files have been downloaded to {output_path}\n')
    log.see('end')


if __name__ == '__main__':
    BilibiliAudioDownload('BV1q24y1C7Ue')
