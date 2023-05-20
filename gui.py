"""
本tkinter代码有一部分由[Tkinter布局助手]生成(笑
当前版本:3.3.0
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
有一说一，这个做的是真好。鼎力推荐。
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict
import ExtractAudio
import HelpFunctions
from time import asctime as t
import BilibiliCrawlerGUI

class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_label_VideoPath"] = self.__tk_label_VideoPath(self)
        self.widget_dic["tk_text_VideoPathInput"] = self.__tk_text_VideoPathInput(self)
        self.widget_dic["tk_label_VideoOutputPath"] = self.__tk_label_VideoOutputPath(self)
        self.widget_dic["tk_text_VideoOutputPathInput"] = self.__tk_text_VideoOutputPathInput(self)
        self.widget_dic["tk_label_VideoOutputPathNotes"] = self.__tk_label_VideoOutputPathNotes(self)
        self.widget_dic["tk_select_box_OutputFormatInput"] = self.__tk_select_box_OutputFormatInput(self)
        self.widget_dic["tk_label_VideoOutputFormat"] = self.__tk_label_VideoOutputFormat(self)
        self.widget_dic["tk_text_Log"] = self.__tk_text_Log(self)
        self.widget_dic["tk_label_LogHistory"] = self.__tk_label_LogHistory(self)
        self.widget_dic["tk_button_ExtractAudioButton"] = self.__tk_button_ExtractAudioButton(self)
        self.widget_dic["tk_label_Actions"] = self.__tk_label_Actions(self)
        self.widget_dic["tk_button_ShowDefaultPathButton"] = self.__tk_button_ShowDefaultPathButton(self)


    def __win(self):
        self.title("Extract-mp3 GUI")
        # 设置窗口大小、居中
        width = 768
        height = 512
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))

    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)

    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)

    def __tk_label_VideoPath(self,parent):
        label = Label(parent,text="Video Path:",anchor="center")
        label.place(x=30, y=20, width=128, height=39)
        return label

    def __tk_text_VideoPathInput(self,parent):
        text = Text(parent)
        text.place(x=160, y=20, width=537, height=39)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=682, y=20, width=15, height=39)
        self.scrollbar_autohide(vbar,text)
        text.insert('end', 'Put the path of your video here. REMEMBER TO DELETE THE \" or \' AT THE ENDS!!! An example would be C:\\Users\\Desktop\\Sample.mp4')
        return text

    def __tk_label_VideoOutputPath(self,parent):
        label = Label(parent,text="Video Output Path:",anchor="center")
        label.place(x=30, y=70, width=129, height=39)
        return label

    def __tk_text_VideoOutputPathInput(self,parent):
        text = Text(parent)
        text.place(x=160, y=70, width=419, height=39)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=564, y=70, width=15, height=39)
        self.scrollbar_autohide(vbar,text)
        return text

    def __tk_label_VideoOutputPathNotes(self,parent):
        label = Label(parent,text="Leave it blank if you want to have it output in the default directory",anchor="center")
        label.place(x=160, y=110, width=419, height=17)
        return label

    def __tk_select_box_OutputFormatInput(self,parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = (".mp3",".wav",".ogg")
        cb.place(x=440, y=140, width=62, height=40)
        return cb

    def __tk_label_VideoOutputFormat(self,parent):
        label = Label(parent,text="Video Output Format:",anchor="center")
        label.place(x=290, y=141, width=141, height=37)
        return label

    def __tk_text_Log(self,parent):
        text = Text(parent)
        text.place(x=0, y=410, width=766, height=100)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=751, y=410, width=15, height=100)
        self.scrollbar_autohide(vbar,text)
        text.insert('end', f'{t()}\n=====Initialization Complete!===== \n少女折寿中。。。Waiting for your first actions\n')
        return text

    def __tk_label_LogHistory(self,parent):
        label = Label(parent,text="Log History: ",anchor="center")
        label.place(x=0, y=380, width=99, height=30)
        return label

    def __tk_button_ExtractAudioButton(self,parent):
        btn = Button(parent, text="Extract Audio!")
        btn.place(x=160, y=140, width=109, height=40)
        return btn

    def __tk_label_Actions(self,parent):
        label = Label(parent,text="Actions:",anchor="center")
        label.place(x=30, y=140, width=129, height=39)
        return label

    def __tk_button_ShowDefaultPathButton(self,parent):
        btn = Button(parent, text="❓")
        btn.place(x=590, y=78, width=30, height=30)
        return btn

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        self.iconbitmap('./Resources/icon.ico')

        self.config(menu=self.create_menu())
    def menu_lhk7lvjf(self,parent):
        menu = Menu(parent,tearoff=False)
        menu.add_command(label="Audio edit",)
        menu.add_command(label="bilibili / youtube web crawl",command=self.LaunchBilibiliCrawlerGUI)
        return menu
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="Basic",)
        menu.add_cascade(label="More widgets",menu=self.menu_lhk7lvjf(menu))
        menu.add_command(label="Help",)
        return menu
    def LaunchBilibiliCrawlerGUI(self):
        Bilibiliwin = BilibiliCrawlerGUI.Win()
        Bilibiliwin.mainloop()
    def vid2mp3(self,evt):
        input_path = self.widget_dic["tk_text_VideoPathInput"].get("1.0", 'end').strip()
        output_path = self.widget_dic["tk_text_VideoOutputPathInput"].get("1.0", 'end').strip()
        output_format = self.widget_dic["tk_select_box_OutputFormatInput"].get().lstrip('.')
        log = self.widget_dic["tk_text_Log"]
        if output_format != '':
            try:
                ExtractAudio.vid2mp3(path=input_path, output_path=output_path, log=log, output_format=output_format)
            except Exception as e:
                # Log the error message
                self.widget_dic["tk_text_Log"].insert('end', f"Error: {e}\n")
                self.widget_dic["tk_text_Log"].see('end')
                print('An Error has occurred. Please check the log.')
        else:
            try:
                ExtractAudio.vid2mp3(path=input_path, output_path=output_path, log=log)
            except Exception as e:
                # Log the error message
                self.widget_dic["tk_text_Log"].insert('end', f"Error: {e}\n")
                self.widget_dic["tk_text_Log"].see('end')
                print('An Error has occurred. Please check the log.')

    def Show_Default_Path(self,evt):
        HelpFunctions.Show_Default_Path()

    def __event_bind(self):
        self.widget_dic["tk_button_ExtractAudioButton"].bind('<Button-1>',self.vid2mp3)
        self.widget_dic["tk_button_ShowDefaultPathButton"].bind('<Button-1>',self.Show_Default_Path)

if __name__ == "__main__":
    win = Win()
    win.mainloop()
