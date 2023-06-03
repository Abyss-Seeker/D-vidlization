import ExtractAudio
import tkinter as tk
import os
import BilibiliCrawler
import YoutubeCrawler
from tkinter import ttk
from time import sleep
import webbrowser
import AudioEdit


def Show_Default_Path():
    default_path_tab = tk.Toplevel()
    default_path_tab.title('Default_Path')
    default_path_text = tk.Label(default_path_tab, text=f'Your Default Path is: path_of_input/{ExtractAudio.tail}')
    default_path_text.pack()
    default_path_text.mainloop()


def BVNumberHelp():
    from PIL import Image, ImageTk
    import tkinter as tk

    BV_num_tab = tk.Toplevel()
    BV_num_tab.title('How to find BV/V/List Number')

    additional_label = tk.Label(BV_num_tab,
                                text="BV number is the thing that's in the position of https://www.bilibili.com/video/____________/blahblahblah\n"
                                     "The BV number is exclusive to Bilibili")
    additional_label.pack()

    find_BV_img = Image.open("./Resources/BV_num_find.gif")
    find_BV_img = find_BV_img.resize((600, 180))  # 指定缩小后的图片尺寸
    find_BV_img = ImageTk.PhotoImage(find_BV_img)

    BV_picture = tk.Label(BV_num_tab, image=find_BV_img)
    BV_picture.pack()

    additional_label_YT = tk.Label(BV_num_tab,
                                   text="V number is the thing that's in the position of https://www.youtube.com/watch?v=___________\n"
                                        "It can also be at the position of https://www.youtube.com/watch?v=___________&list=blahblahblahb\n"
                                        "The V number is exclusive to YouTube")
    additional_label_YT.pack()

    find_BV_img_YT = Image.open("./Resources/V_num_find.png")
    find_BV_img_YT = find_BV_img_YT.resize((650, 158))  # 指定缩小后的图片尺寸
    find_BV_img_YT = ImageTk.PhotoImage(find_BV_img_YT)

    BV_picture_YT = tk.Label(BV_num_tab, image=find_BV_img_YT)
    BV_picture_YT.pack()

    additional_label_YT_List = tk.Label(BV_num_tab,
                                        text="List number is the thing that's in the position of https://www.youtube.com/watch?v=blahblahbla&list=____________&blahblahblah\n"
                                             "The list number should be real long (typically 31 characters). Please mind that, if this is shorter it may be a mix!\n"
                                             "===The mix can't be crawled!===\n"
                                             "The List number is exclusive to YouTube")
    additional_label_YT_List.pack()

    find_List_img_YT = Image.open("./Resources/List_num_find.png")
    find_List_img_YT = find_List_img_YT.resize((583, 126))  # 指定缩小后的图片尺寸
    find_List_img_YT = ImageTk.PhotoImage(find_List_img_YT)

    List_picture_YT = tk.Label(BV_num_tab, image=find_List_img_YT)
    List_picture_YT.pack()

    BV_num_tab.mainloop()


def Show_Default_Path_Bilibili():
    default_path_tab = tk.Toplevel()
    default_path_tab.title('Default_Path')
    default_path_text = tk.Label(default_path_tab,
                                 text=f'Your Default Path for Bilibili audios is: {os.path.abspath(BilibiliCrawler.default_output_path)}')
    default_path_text_YT = tk.Label(default_path_tab,
                                    text=f'Your Default Path for YouTube audios is: {os.path.abspath(YoutubeCrawler.default_output_path)}')
    default_path_text.pack()
    default_path_text_YT.pack()
    default_path_tab.mainloop()


class BilibiliCrawlerHelp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Bilibili / YouTube Audio Crawler - HELP")
        self.geometry("600x400")
        self.resizable(False, False)

        # Create notebook widget to hold multiple pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create and add pages
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()

    def create_page1(self):
        def alter_show():
            with open('./Resources/info.txt', 'r') as f:
                auto_open_var = int(f.read())
            with open('./Resources/info.txt', 'w') as f:
                if auto_open_var == 0:
                    f.write('1')
                else:
                    f.write('0')

        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="Welcome!")

        title_label = tk.Label(frame, text='A Brief Introduction', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''Hi there! Welcome to Bilibili / Youtube Audio Crawler!
This is a major widget created for project "D-vidlization"!''', font=('Arial', 16), anchor='w')
        label.pack()

        labellink = tk.Label(frame, text="D-vidlization", fg="blue", cursor="hand2", font=('Arial', 16), width=9, height=1)
        labellink.place(x=430, y=75)
        labellink.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Abyss-Seeker/D-vidlization"))

        can = tk.Label(frame, text='What I can do:')
        can.pack()

        self.text01 = tk.Text(frame, height=5, width=60)
        self.text01.pack()
        self.text01.insert(tk.END,
                           "1. Crawl audio files in .mp3, .wav, .ogg format from bilibili / youtube videos\n2. Support bilibili videos and playlists, youtube (single) videos and playlists\n3. Automatic download of the playlists and you can choose between range of episodes\n 4. Custom output directory in your computer")

        cannot = tk.Label(frame, text='What I cannot do:')
        cannot.pack()

        self.text02 = tk.Text(frame, height=5, width=60)
        self.text02.pack()
        self.text02.insert(tk.END,
                           "1. Crawl video files\n2. Crawl audio files in .m4a format\n3. Crawl audio files form Youtube mixes or bilibili 番剧\n4. Crawl videos in Youtube / bilibili mirror sites or other websites\n5. (Possibly) Error crawling very very old bilibili videos")

        note = tk.Label(frame,
                        text='Feel free to click around the top tabs of this page to view more instructions!\n You can always access to this help by clicking "Help" at the top of the crawler widget.')
        note.pack()

        note2 = tk.Label(frame,
                        text='Good Luck, and HAVE FUN!!!', font=('Arial', 8))
        note2.pack()

        cb1 = tk.Checkbutton(frame, text='Don\'t automatically show this again', command=alter_show)
        with open('./Resources/info.txt', 'r') as f:
            state_num = int(f.read())
            if state_num == 1:
                cb1.deselect()
            elif state_num == 0:
                cb1.select()
        cb1.pack(side=tk.RIGHT, anchor=tk.SE)

    def create_page2(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="Instructions")

        title_label = tk.Label(frame, text='How to Use - Detailed Instructions', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''Instructions for to use the widget:
1. Run file TryInitFFmpeg.py (in the same folder) with admin
   (Or directly add the path of ffmpeg in this folder (./ffmpeg-master-latest-win64-gpl-shared/bin) to system path
    1.0 following instructions works if you are using windows
    1.1 Search up cmd in 开始. Click 以管理员身份运行
    1.2 Redirect the directory to the folder of the project. Search on web if you don't know how, it's easy
    1.3 type in cmd: python tryinitffmpeg.py
2. Make sure your proxy/VPN is off if crawling from bilibili, make sure proxy/VPN is on if crawling from YouTube
3. Input the BV num on the top entry if you are crawling bilibili. Input the v num / list num if Youtube
    3.1 If you don't know what the numbers are, click the '?' button beside
4. Input the output directory in the following entry textbox. If you leave it blank, it will be outputted in the default folder.
    4.1 You can click on the '?' beside it to see which folder will be the output for default.
    4.2 Do not leave " or ' on the ends of the directory, or else, there may be errors
5. Input the p_numbers of videos you want in the next 2 entry boxes. 
    5.1 This stands for simply the P number (分P) in Bilibili or episodes in lists for YouTube.
    5.2 Make sure the p_numbers are correct! The default p_numbers (if you leave them blank) would be P1~P1
    5.3 If you are crawling a single video you can leave them blank
6. Select the output format
    6.1 The default (if you leave it blank) would be .mp3. You can choose between mp3, wav and ogg.
7. Click the download button! You are all set!
    7.1 Again, make sure to turn proxy off if you are crawling Bilibili!
    7.2 And turn proxy on when you are crawling YouTube!
''', anchor='w', justify='left', font=('Arial', 8))
        label.pack()


    def create_page3(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="FAQ")

        label = tk.Label(frame, text="Frequently Asked Questions:", font=('Arial', 8, 'bold'))
        label.pack()

        faqs = [
            ("Q1. Where would the output be saved at?", """It would be saved at the folder of your input of 'Audio Output Path'. 
If you leave it blank, it would be in the default output directory (click the '?' button beside it to check)."""),
            ("Q2. When do I open VPN/proxy?", """You do that only before you click the Download! Button before CRAWLING YOUTUBE!
On other times, like when running other     programs / crawling Bilibili, make sure to keep VPN/proxy off."""),
            ("Q3. What is the BV/V/List number? How can I find them?", """They are all numbers from the link of the video / list you want to extract.
            For detailed directions, click the '?' button in the user interface beside 'How to find the numbers'"""),
            ("Q4. Why is there error: 'Error: check_hostname requires server_hostname'?", "You probably left VPN/proxy on when crawling bilibili. Turn them off and try again."),
            ("Q5. Why is there error: 'Error: 'NoneType' object has no attribute 'text''?", "You probably inputted the wrong BV/V/List number. Try again with this input."),
            ("Q6. Why is there error: 'Error: [WinError 123] 文件名、目录名或卷标语法不正确。'?", "It is either you have the wrong output directory (check if the \" and ' are deleted) or there is a bug (vid name not correct)"),
            ("Q7. Why is there error: 'OSError: [Errno 22] Invalid argument' when converting video format?", "Maybe you haven't added ffmpeg to path yet. Go check the first step of 'Instructions' page of the help."),
            ("Q8. Where do I report bugs / questions? / My question isn't solved here.", "You are welcomed to visit the ISSUES page of this project! Thanks a lot for that!")
        ]

        for question, answer in faqs:
            q_label = tk.Label(frame, text=question, font=("Arial", 8, "bold"), anchor='w', justify='left')
            q_label.pack()
            a_label = tk.Label(frame, text=answer, font=("Arial", 8), anchor='w', justify='left')
            a_label.pack()

        labellink = tk.Label(frame, text="ISSUES", fg="blue", cursor="hand2", font=('Arial', 8), width=6, height=1)
        labellink.place(x=251, y=357)
        labellink.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Abyss-Seeker/D-vidlization/issues"))

    def create_page4(self):
        from PIL import Image, ImageTk
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="About")
        title_label = tk.Label(frame, text='About', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''This widget is coded by Jasper, tested by Lydia, Tony, Henry.
Originally finished on 23/05/20.
You can contact us via wechat num:
    Jasper: jasperSHSID
    Lydia: CallMeSigma
Or by Email (seldom used):
    Jasper: jaspershsid@gmail.com / abyssseekersss@gmail.com
Or by github, of course
    Jasper: Abyss-seeker
    Lydia: CupofCuppucino
Thank you so much for using it. If there is any issues, please report it to the 
github project page - ISSUES
        ''', anchor='w', justify='left', font=('Arial', 12))
        label.pack()

        labellink = tk.Label(frame, text="ISSUES", fg="blue", cursor="hand2", font=('Arial', 12), width=6, height=1)
        labellink.place(x=188, y=250)
        labellink.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Abyss-Seeker/D-vidlization/issues"))


    # def get_text_from_page1(self):
    #     # Get the reference to Page 1
    #     page1 = self.notebook.tabs()[0]
    #
    #     # Convert the reference to the corresponding frame widget
    #     page1_frame = self.notebook.nametowidget(page1)
    #
    #     # Access the children of the frame widget
    #     page1_children = page1_frame.winfo_children()
    #
    #     # Assuming the text widget is the second child of the frame,
    #     # retrieve the reference to the text widget
    #     page1_text = page1_children[1]
    #
    #     # Get the content of the text widget from line 1, character 0 (start) to the end
    #     text_content = page1_text.get("1.0", tk.END)
    #
    #     # Print the retrieved text content from Page 1
    #     print("Text content from Page 1:", text_content)

def Show_Default_Path_AudioEdit():
    default_path_tab = tk.Toplevel()
    default_path_tab.title('Default_Path')
    default_path_text = tk.Label(default_path_tab,
                                 text=f'Your Default Path for Audio Edited audios is: audio_file_path/{AudioEdit.tail}')
    default_path_text.pack()
    default_path_tab.mainloop()


class AudioEditHelp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("AudioEdit - HELP")
        self.geometry("600x400")
        self.resizable(False, False)

        # Create notebook widget to hold multiple pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create and add pages
        self.create_page1()
        self.create_page2()
        self.create_page3()
        self.create_page4()

    def create_page1(self):
        def alter_show():
            with open('./Resources/info02.txt', 'r') as f:
                auto_open_var = int(f.read())
            with open('./Resources/info02.txt', 'w') as f:
                if auto_open_var == 0:
                    f.write('1')
                else:
                    f.write('0')

        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="Welcome!")

        title_label = tk.Label(frame, text='A Brief Introduction', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''Hi there! Welcome to AudioEdit!
This is a major widget created for project "D-vidlization"!''', font=('Arial', 16), anchor='w')
        label.pack()

        labellink = tk.Label(frame, text="D-vidlization", fg="blue", cursor="hand2", font=('Arial', 16), width=9, height=1)
        labellink.place(x=430, y=75)
        labellink.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Abyss-Seeker/D-vidlization"))

        can = tk.Label(frame, text='What I can do:')
        can.pack()

        self.text01 = tk.Text(frame, height=5, width=60)
        self.text01.pack()
        self.text01.insert(tk.END,
                           "To be added")

        cannot = tk.Label(frame, text='What I cannot do:')
        cannot.pack()

        self.text02 = tk.Text(frame, height=5, width=60)
        self.text02.pack()
        self.text02.insert(tk.END,
                           "To be added")

        note = tk.Label(frame,
                        text='Feel free to click around the top tabs of this page to view more instructions!\n You can always access to this help by clicking "Help" at the top of the crawler widget.')
        note.pack()

        note2 = tk.Label(frame,
                        text='Good Luck, and HAVE FUN!!!', font=('Arial', 8))
        note2.pack()

        cb1 = tk.Checkbutton(frame, text='Don\'t automatically show this again', command=alter_show)
        with open('./Resources/info02.txt', 'r') as f:
            state_num = int(f.read())
            if state_num == 1:
                cb1.deselect()
            elif state_num == 0:
                cb1.select()
        cb1.pack(side=tk.RIGHT, anchor=tk.SE)

    def create_page2(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="Instructions P1")

        title_label = tk.Label(frame, text='How to Use - Detailed Instructions', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''Instructions for to use the widget:
How to use Audio Edit:
1. Run file TryInitFFmpeg.py (which is in the same folder) with admin authority
   (Or directly add the path of ffmpeg in this folder (./ffmpeg-master-latest-win64-gpl-shared/bin) to system path if you are familiar with IT)
    1.0 the following instructions works if you are using windows
    1.1 Search up cmd in 开始. Click 以管理员身份运行 (or for some computers, 搜索 on the left down corner of your screen)
    1.2 Redirect the directory to the folder of the project. Search on web if you don't know how, it's easy
    1.3 type in cmd: python tryinitffmpeg.py
2. open AudioEditGUI and run the program (you should be able to see a tkinter page on your screen)
3. "Audio Path" box
1) if you want to edit only one audio:
- find the file in your folder, and copy its path, then paste it to the box (*replace the original content)
2) if you want to edit multiple audio:
- find the audios you want to edit and put them under the same folder, then, copy the path of the folder and paste it to the box (*replace the original content)
4. "Audio Output Path" box:
1) leave it blank if you want the program to output the editted file into a folder caller "extracts" under the same path as your input
2) find the folder you want it to output to and copy paste its path into the box
5. "Length Edit" boxes:
- there are two boxes in total, which marks the start second of your intended clip and the ending second (for ex. 0s~10s for a clip of 10 seconds) 
- beware that the numbers have to be within the time length of your audio (which you can check by playing your audio)
- for convinience, you can input -1 to the second box to set the ending second to be the end of the original audio, and 0 for the first box to start from the very beginning
6. "Loop" box:
- after editing the length, you can let the clip loop for multiple times by typing a positive integer into the box (for ex. looping a clip with 10 seconds for 2 times results with a 20 seconds long audio)
*beware that the looping function works after the length edit, so your clip resulted from the previous Length Edit will loop
''', anchor='w', justify='left', font=('Arial', 8))
        label.pack()


    def create_page3(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="Instructions P2")

        title_label = tk.Label(frame, text='How to Use - Detailed Instructions', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''Instructions for to use the widget:
7. "Speed Up" box:
- input a positive number (does not have to be integer) to change the speed of the clip (for example input 2 for double the speed and input 0.5 for half the speed, similar to the changing speed function you see in Bilibili and Youtube)
8. "Volume Edit" box:
- works the same as the previous "Speed Up" box, but with volume
- for the sake of your ear, please make sure you know how loud your audio will be after editting, or else turn down the volume of your computer before listening
9. "Fade In and Fade Out" boxes:
- The fisrt box is for how many seconds the audio starts from 0 audio and gradually increase volume till it reaches the original volume to make the audio more start and end more smoothly(ex. Fade in 2 seconds, Fade out 3 seconds)
- beware that this works after all the above functions (length, loop, speed up, volume)
10. "3D Sound Effect" box:
- if you want a the audio to loop around your head (3D looping sound effect), choose a number that is not 0
- choose a larger number to let the music spin (loop) faster
11. "Compress" box:
- if you want to save a compressed copy of your newly editted audio, choose a number that is not 0
- choose a smaller number for more compress (that is, occupying less space)
12. Finally, choose the Audio Output Format you want and then press the "Edit Audio!!!" button and wait for program to finish (the tab will not close automatically, and you can continue editing but you may need to change your input)
''', anchor='w', justify='left', font=('Arial', 8))
        label.pack()

    def create_page4(self):
        from PIL import Image, ImageTk
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text="About")
        title_label = tk.Label(frame, text='About', font=('Arial', 30))
        title_label.pack()

        label = tk.Label(frame, text='''This widget is coded by Lydia.
Originally finished on 23/05/20.
You can contact us via wechat num:
    Lydia: CallMeSigma
Or by github, of course
    Lydia: CupofCuppucino
Thank you so much for using it. If there is any issues, please report it to the 
github project page - ISSUES
        ''', anchor='w', justify='left', font=('Arial', 12))
        label.pack()

        labellink = tk.Label(frame, text="ISSUES", fg="blue", cursor="hand2", font=('Arial', 12), width=6, height=1)
        labellink.place(x=188, y=178)
        labellink.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Abyss-Seeker/D-vidlization/issues"))

def init_ffmpeg_help(): # TODO, 但是懒得写
    return

