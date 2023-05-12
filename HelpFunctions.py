import ExtractAudio
import tkinter as tk


def Show_Default_Path():
    default_path_tab = tk.Tk()
    default_path_tab.title('Default_Path')
    default_path_text = tk.Label(default_path_tab, text=f'Your Default Path is: video path{ExtractAudio.tail}')
    default_path_text.pack()
    default_path_text.mainloop()
