"""
So, this code is simple enough.
I am sure this can run on Windows systems well.
Basically, what it does is to add the ffmpeg app (downloaded from GitHub) under the folder:
    ./ffmpeg-master-latest-win64-gpl-shared/bin/
into your system path, thus the other programs that may need to utilize it can run properly.
All you need to do is:
1. Run this file -WITH ADMIN-. If you are using anaconda there is a chance you see 乱码 within the output. Don't worry, it is bcz the output message is in GBK
2. EXIT the programs (close their tabs) and RESTART THEM!!! (not restarting your laptop, just all your python programs)
3. Go to the file that needs ffmpeg and just run them! You can now neglect this program.
* IMPORTANT: if you moved the path of the folder of the project, you might need to run this file again!!! Or else the old path would expire and things won't work properly.
** ALSO: if you're using macOS or this does not work, you would prob need to go search up a tutorial of
        添加系统变量
    and add ffmpeg in manually
    the path should still be
        ./ffmpeg-master-latest-win64-gpl-shared/bin/
    Just change the "." at the front to the path of the project folder (the folder this program is in right now)
*** If you already have ffmpeg in your path (downloaded and used it before, maybe), you can neglect this.
"""


import os
import winreg


def add_ffmpeg_to_path():
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_dir = os.path.join(script_dir, 'ffmpeg-master-latest-win64-gpl-shared', 'bin')

    if os.name == 'nt':  # Windows
        # 构建setx命令
        # 注册表路径
        reg_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"

        # 打开注册表项
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

        # 读取环境变量
        path_value, _ = winreg.QueryValueEx(reg_key, "Path")

        # 关闭注册表项
        winreg.CloseKey(reg_key)

        # 打印 PATH 值
        print(path_value)
        final_dir = fr'{ffmpeg_dir};{path_value}'
        print(final_dir)
        command = fr'setx Path "{final_dir}" /m'
        print(command)

        # 运行setx命令
        os.system(command)

        print('ffmpeg added to PATH successfully.')

    else:
        print('This script is only supported on Windows.')


add_ffmpeg_to_path()
