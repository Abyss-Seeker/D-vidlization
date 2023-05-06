# Required: moviepy
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy
# Coded by @Abyss_Seeker!
import moviepy.editor as mp
import os

# Basic
path = input('Path of folder / video: ').strip()
config = {
    'output': 'mp3',
    'output_dir': path + '/extracts'
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
        output_dir = input('Please input path of output as an:'
                           ' [absolute directory] or'
                           ' [nothing] to continue with default: ').strip()
        if output_dir == '':
            _ = path.split(dir_mark)
            if len(_) > 1:
                config['output_dir'] = dir_mark.join(_[:-1])
            else:
                print('Probably invalid path')
        else:
            if os.path.exists(output_dir):
                output_dir_confirm = input('The path already exists. Are you sure? [Y/N]: ').strip().upper()
                if output_dir_confirm == 'Y':
                    config['output_dir'] = output_dir
                else:
                    output_dir_pass = 0

    print('-'*50, '\n', config, '\n', '-'*50)

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


# If input is folder
# Decide output dir
else:
    file_names = os.listdir(path)
    output_dir_pass = 0
    while output_dir_pass == 0:
        output_dir_pass = 1
        output_dir = input('Please input path of output as an:'
                           ' [absolute directory] or'
                           ' [nothing] to continue with default: ').strip()
        if output_dir != '':
            if os.path.exists(output_dir):
                output_dir_confirm = input('The path already exists. Are you sure? [Y/N]: ').strip().upper()
                if output_dir_confirm == 'Y':
                    config['output_dir'] = output_dir
                else:
                    output_dir_pass = 0
            else:
                config['output_dir'] = output_dir

    print('-'*50, '\n', config, '\n', '-'*50)

    # Make output dir if needed
    if not os.path.exists(config['output_dir']):
        os.makedirs(config['output_dir'])

    # Convert + write files
    process_len = len(file_names)
    current = 0
    for file_name in file_names:
        if file_name[-4:].lower() in video_file_suffixes:  # This would actually yield issues if folder name ends in webm (lazy)
            file_dir = path + '/' + file_name
            pure_file_name = file_name[:-5] if file_name[-4:].lower() == 'webm' else file_name[:-4]  # No .mp4 only name
            # pure_file_name = file_name[:-4].split('（')[1][:-1]  # For my made in abyss music use only
            video = mp.VideoFileClip(file_dir)
            audio = video.audio
            if audio is not None:
                audio.write_audiofile(f"{config['output_dir']}/{pure_file_name}.{config['output']}")
            else:
                print(f'Video {file_name} does not have audio')
        current += 1
        print(f'Completed {current}/{process_len}')

print('\n'+'='*50)
print(f"Program ended. The files in {path} \n have been written to directory {config['output_dir']}")
