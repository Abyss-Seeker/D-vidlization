# Required: moviepy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy
# Coded by @CupofCuppuccino, creds:Abyss_Seeker! for part of the code

import os
import AudioFunctions

try:
    import moviepy.editor as mp
except:
    try:
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy')
    except:
        os.system('pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy')
finally:
    import moviepy.editor as mp
    import moviepy.audio.fx.audio_fadein
    from moviepy.audio.fx.audio_fadeout import audio_fadeout
    from moviepy.editor import *
    import moviepy.audio.fx.all as afx

from time import asctime as t

tail = '/extracts'  # Config this to change the output path

def AudioProcess(path: str, output_path: str, log=None, output_dir_tail=tail,
                 output_format='mp3', length_a=0, length_b=5, volume_num=0.5, fade_a=0, fade_b=0,
                 loop_num=1, speed_up_num=1, effect_num=3, compress_num=4000):
    if log is not None:
        log.insert('end', f'{t()}\n')
        log.see('end')
    # Basic
    config = {
        'output': output_format,
        'output_dir': path + output_dir_tail
    }  # output can be wav or mp3; output dir can be modified, default is inside path/extracts

    # if input is audio
    audio_file_suffixes = ['.mp3', '.wav', '.mp4', '.ogg']  # Edit valid audio format
    dir_mark = '/'
    if '\\' in path:
        dir_mark = '\\'
    if path[-4:].lower() in audio_file_suffixes:
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

        # Find last section of file name (with .mp3), don't know if it works in mac

        file_name = path.split(dir_mark)[-1] #useful
        pure_file_name = file_name[:-5] if file_name[-4:].lower() == 'webm' else file_name[:-4]  # No .mp3 only name
        audio = mp.AudioFileClip(path)
        audio = AudioFunctions.audio_edit(audio, length_a, length_b)
        audio = AudioFunctions.audio_loop(audio, loop_num)
        audio = AudioFunctions.audio_volume2(audio, volume_num)
        audio = AudioFunctions.audio_speed(audio, speed_up_num)
        audio = AudioFunctions.audio_fade(audio, fade_a, fade_b)
        if effect_num != 0:
            audio = AudioFunctions.audio_3D(audio, effect_num)
        audio_output_path = f"{config['output_dir']}/{pure_file_name + '_new'}.{config['output']}"
        audio.write_audiofile(audio_output_path)
        if compress_num != 0:
            AudioFunctions.audio_compress(config['output_dir'], pure_file_name+'_new.'+output_format,
                                          pure_file_name+'_new_compressed.'+output_format, compress_num)
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
            if file_name[-4:].lower() in audio_file_suffixes:  # This would actually yield issues if folder name ends in webm (lazy)
                file_dir = path + '/' + file_name
                pure_file_name = file_name[:-5] if file_name[-4:].lower() == 'webm' else file_name[:-4]  # No .mp4 only name
                audio = mp.AudioFileClip(file_dir)
                #print(file_name, pure_file_name,path,output_format)
                audio = AudioFunctions.audio_edit(audio, length_a, length_b)
                audio = AudioFunctions.audio_loop(audio, loop_num)
                audio = AudioFunctions.audio_volume2(audio, volume_num)
                audio = AudioFunctions.audio_speed(audio, speed_up_num)
                audio = AudioFunctions.audio_fade(audio, fade_a, fade_b)
                if effect_num != 0:
                    audio = AudioFunctions.audio_3D(audio, effect_num)
                audio.write_audiofile(f"{config['output_dir']}/{pure_file_name + '_new'}.{config['output']}")
                if compress_num != 0:
                    #print(path+'/extracts',pure_file_name + '_new.'+output_format,pure_file_name + '_compressed.'+output_format,compress_num)
                    AudioFunctions.audio_compress(config['output_dir'],pure_file_name + '_new.'+output_format,pure_file_name + '_new_compressed.'+output_format,compress_num)

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
