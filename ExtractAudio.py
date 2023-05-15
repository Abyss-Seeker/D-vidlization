# Required: moviepy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy
# Coded by @Abyss_Seeker!

import os

try:
    import moviepy.editor as mp
except:
    try:
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy')
    except:
        os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy')
finally:
    import moviepy.editor as mp

from time import asctime as t

# This is just a note
# log.insert('end', f'ERROR: Probably invalid path: {path}\n')
# log.see(END)
# log.update()

tail = '/extracts'  # Config this to change the output path


def vid2mp3(path: str, output_path: str, log=None, output_dir_tail=tail,
            output_format='mp3'):  # input_path, output_path, log text box path, output_dir, output_format
    if log is not None:
        log.insert('end', f'{t()}\n')
        log.see('end')
    # Basic
    config = {
        'output': output_format,
        'output_dir': path + output_dir_tail
    }  # output can be wav or mp3; output dir can be modified, default is inside path/extracts

    # if input is video
    video_file_suffixes = ['webm', '.mov', '.mp4', '.avi', '.ogv', '.mkv']  # Extract valid video formats
    dir_mark = '/'
    if '\\' in path:
        dir_mark = '\\'
    if path[-4:].lower() in video_file_suffixes:
        # Decide output dir
        output_dir_pass = 0
        while output_dir_pass == 0:
            output_dir_pass = 1
            output_dir = output_path.strip()
            if output_dir == '':
                _ = path.split(dir_mark)
                if len(_) > 1:
                    config['output_dir'] = dir_mark.join(_[:-1])
                else:
                    print('ERROR: Probably invalid path')
                    if log is not None:
                        log.insert('end', f'ERROR: Probably invalid path: {path}\n')
                        log.see('end')
                        log.update()
            else:
                if os.path.exists(output_dir):
                    config['output_dir'] = output_dir

        print('-' * 50, '\n', config, '\n', '-' * 50)
        if log is not None:
            log.insert('end', f'{"-" * 50}\n{config}\n{"-" * 50}\n')
            log.see('end')
            log.update()

        # Find last section of file name (with .mp4), don't know if it works in mac

        file_name = path.split(dir_mark)[-1]
        pure_file_name = file_name[:-5] if file_name[-4:].lower() == 'webm' else file_name[:-4]  # No .mp4 only name
        # pure_file_name = file_name[:-4].split('（')[1][:-1]  # For my made in abyss music use only
        video = mp.VideoFileClip(path)
        audio = video.audio
        if audio is not None:
            audio.write_audiofile(f"{config['output_dir']}/{pure_file_name}.{config['output']}")
        else:
            print('This video does not have audio')
            if log is not None:
                log.insert('end', 'This video does not have audio\n')
                log.see('end')
                log.update()

    # If input is folder
    # Decide output dir
    else:
        file_names = os.listdir(path)
        output_dir_pass = 0
        while output_dir_pass == 0:
            output_dir_pass = 1
            output_dir = output_path.strip()
            if output_dir != '':
                config['output_dir'] = output_dir

        print('-' * 50, '\n', config, '\n', '-' * 50)
        if log is not None:
            log.insert('end', f'{"-" * 50}\n{config}\n{"-" * 50}\n')
            log.see('end')
            log.update()

        # Make output dir if needed
        if not os.path.exists(config['output_dir']):
            os.makedirs(config['output_dir'])

        # Convert + write files
        process_len = len(file_names)
        current = 0
        for file_name in file_names:
            if file_name[
               -4:].lower() in video_file_suffixes:  # This would actually yield issues if folder name ends in webm (lazy)
                file_dir = path + '/' + file_name
                pure_file_name = file_name[:-5] if file_name[-4:].lower() == 'webm' else file_name[
                                                                                         :-4]  # No .mp4 only name
                # pure_file_name = file_name[:-4].split('（')[1][:-1]  # For my made in abyss music use only
                video = mp.VideoFileClip(file_dir)
                audio = video.audio
                if audio is not None:
                    audio.write_audiofile(f"{config['output_dir']}/{pure_file_name}.{config['output']}")
                else:
                    print(f'Video {file_name} does not have audio')
                    if log is not None:
                        log.insert('end', f'Video {file_name} does not have audio\n')
                        log.see('end')
                        log.update()

            current += 1
            print(f'Completed {current}/{process_len}')
            if log is not None:
                log.insert('end', f'Completed {current}/{process_len}\n')
                log.see('end')
                log.update()

    print('\n' + '=' * 50)
    if log is not None:
        log.insert('end', f"\n{'=' * 50}\n")
        log.update()
        log.see('end')
    print(f"Success. The files in {path} \n have been written to directory {config['output_dir']}")
    if log is not None:
        log.insert('end', f'{t()}\n')
        log.insert('end', f"Success. The files in {path} have been written to directory {config['output_dir']}\n")
        log.see('end')
        log.update()
