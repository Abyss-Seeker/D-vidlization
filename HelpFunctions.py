import ExtractAudio
import tkinter as tk


def Show_Default_Path():
    default_path_tab = tk.Toplevel()
    default_path_tab.title('Default_Path')
    default_path_text = tk.Label(default_path_tab, text=f'Your Default Path is: video path{ExtractAudio.tail}')
    default_path_text.pack()
    default_path_text.mainloop()

def BVNumberHelp():
    BV_num_tab = tk.Toplevel()
    BV_num_tab.title('How to find BV Number')
    additional_label = tk.Label(BV_num_tab, text='BV number is the thing that\'s in the position of https://www.bilibili.com/video/____________/blahblahblah')
    additional_label.pack()
    find_BV_img = tk.PhotoImage(file="./Resources/BV_num_find.gif")
    BV_picture = tk.Label(BV_num_tab, image=find_BV_img)
    BV_picture.pack()
    BV_num_tab.mainloop()
