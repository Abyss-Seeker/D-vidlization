"""
本代码由[Tkinter布局助手]生成
当前版本:3.3.0
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict
import HelpFunctions
import BilibiliCrawler

class WinGUI(Toplevel):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_label_BVNumber"] = self.__tk_label_BVNumber(self)
        self.widget_dic["tk_input_BVNumberInput"] = self.__tk_input_BVNumberInput(self)
        self.widget_dic["tk_button_BVNumberHelp"] = self.__tk_button_BVNumberHelp(self)
        self.widget_dic["tk_label_BVNumberHelpNote"] = self.__tk_label_BVNumberHelpNote(self)
        self.widget_dic["tk_label_OutputPath"] = self.__tk_label_OutputPath(self)
        self.widget_dic["tk_text_AudioOutputPathInput"] = self.__tk_text_AudioOutputPathInput(self)
        self.widget_dic["tk_label_AudioOutputNote"] = self.__tk_label_AudioOutputNote(self)
        self.widget_dic["tk_button_ShowDefaultPath"] = self.__tk_button_ShowDefaultPath(self)
        self.widget_dic["tk_label_PNumberLabel"] = self.__tk_label_PNumberLabel(self)
        self.widget_dic["tk_input_StartPInput"] = self.__tk_input_StartPInput(self)
        self.widget_dic["tk_label_MiddleLabel"] = self.__tk_label_MiddleLabel(self)
        self.widget_dic["tk_input_EndPInput"] = self.__tk_input_EndPInput(self)
        self.widget_dic["tk_label_RightLabel"] = self.__tk_label_RightLabel(self)
        self.widget_dic["tk_label_AudioOutputFormat"] = self.__tk_label_AudioOutputFormat(self)
        self.widget_dic["tk_select_box_lhoqevnz"] = self.__tk_select_box_lhoqevnz(self)  # select output format
        self.widget_dic["tk_label_PNumberNote"] = self.__tk_label_PNumberNote(self)
        self.widget_dic["tk_label_ActionsLabel"] = self.__tk_label_ActionsLabel(self)
        self.widget_dic["tk_button_DownloadButton"] = self.__tk_button_DownloadButton(self)
        self.widget_dic["tk_label_LogNote"] = self.__tk_label_LogNote(self)
        self.widget_dic["tk_text_Log"] = self.__tk_text_Log(self)

    def __win(self):
        self.title("Bilibili Audio Crawler")
        # 设置窗口大小、居中
        width = 600
        height = 400
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

    def __tk_label_BVNumber(self,parent):
        label = Label(parent,text="BV number:",anchor="center")
        label.place(x=30, y=20, width=116, height=30)
        return label

    def __tk_input_BVNumberInput(self,parent):
        ipt = Entry(parent)
        ipt.place(x=170, y=20, width=268, height=30)
        return ipt

    def __tk_button_BVNumberHelp(self,parent):
        btn = Button(parent, text="❓")
        btn.place(x=460, y=20, width=30, height=30)
        return btn

    def __tk_label_BVNumberHelpNote(self,parent):
        label = Label(parent,text="How to find \nBV Number",anchor="center")
        label.place(x=500, y=10, width=80, height=54)
        return label

    def __tk_label_OutputPath(self,parent):
        label = Label(parent,text="Audio Output Path:",anchor="center")
        label.place(x=30, y=60, width=116, height=30)
        return label

    def __tk_text_AudioOutputPathInput(self,parent):
        text = Text(parent)
        text.place(x=170, y=60, width=326, height=61)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=481, y=60, width=15, height=61)
        self.scrollbar_autohide(vbar,text)
        return text

    def __tk_label_AudioOutputNote(self,parent):
        label = Label(parent,text="Leave it blank if you want to have it output in the default directory",anchor="center")
        label.place(x=170, y=117, width=397, height=30)
        return label

    def __tk_button_ShowDefaultPath(self,parent):
        btn = Button(parent, text="❓")
        btn.place(x=510, y=80, width=30, height=30)
        return btn

    def __tk_label_PNumberLabel(self,parent):
        label = Label(parent,text="P number:",anchor="center")
        label.place(x=30, y=160, width=116, height=30)
        return label

    def __tk_input_StartPInput(self,parent):
        ipt = Entry(parent)
        ipt.place(x=170, y=160, width=62, height=30)
        return ipt

    def __tk_label_MiddleLabel(self,parent):
        label = Label(parent,text="P    ~    ",anchor="center")
        label.place(x=224, y=160, width=50, height=30)
        return label

    def __tk_input_EndPInput(self,parent):
        ipt = Entry(parent)
        ipt.place(x=270, y=160, width=62, height=30)
        return ipt

    def __tk_label_RightLabel(self,parent):
        label = Label(parent,text="P",anchor="center")
        label.place(x=310, y=160, width=50, height=30)
        return label

    def __tk_label_AudioOutputFormat(self,parent):
        label = Label(parent,text="Audio Output Format: ",anchor="center")
        label.place(x=367, y=160, width=142, height=30)
        return label

    def __tk_select_box_lhoqevnz(self,parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = (".mp3",".wav",".ogg")
        cb.place(x=510, y=160, width=83, height=30)
        return cb

    def __tk_label_PNumberNote(self,parent):
        label = Label(parent,text="*If you are only crawling one video's audio or only crawling the first P, you can leave these two blank",anchor="center", font=('Arial',8))
        label.place(x=10, y=190, width=581, height=30)
        return label

    def __tk_label_ActionsLabel(self,parent):
        label = Label(parent,text="Actions:",anchor="center")
        label.place(x=30, y=230, width=116, height=30)
        return label

    def __tk_button_DownloadButton(self,parent):
        btn = Button(parent, text="Download!")
        btn.place(x=170, y=230, width=102, height=30)
        return btn

    def __tk_label_LogNote(self,parent):
        label = Label(parent,text="Log:",anchor="center")
        label.place(x=0, y=270, width=56, height=30)
        return label

    def __tk_text_Log(self,parent):
        text = Text(parent)
        text.place(x=0, y=300, width=600, height=100)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=585, y=300, width=15, height=100)
        self.scrollbar_autohide(vbar,text)
        return text

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

        self.config(menu=self.create_menu())
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="Help",command=self.BilibiliAudioCrawlerHelp)
        return menu
    def BilibiliAudioCrawlerHelp(self):  # TODO
        print("点击了菜单")

    def BVNumberHelp(self,evt):
        HelpFunctions.BVNumberHelp()

    def ShowDefaultPathBilibili(self,evt):  # TODO
        print("<Button-1>事件未处理",evt)

    def Download(self,evt):
        BV_num = self.widget_dic["tk_input_BVNumberInput"].get()
        output_path = self.widget_dic["tk_text_AudioOutputPathInput"].get("1.0", 'end').strip()
        output_format = self.widget_dic["tk_select_box_lhoqevnz"].get().lstrip('.')
        p_start = self.widget_dic["tk_input_StartPInput"].get()
        if p_start == '':
            p_start = 1
        else:
            p_start = int(p_start)
        p_end = self.widget_dic["tk_input_EndPInput"].get()
        if p_end == '':
            p_end = 1
        else:
            p_end = int(p_end)
        log = self.widget_dic["tk_text_Log"]
        if output_format != '':
            try:
                BilibiliCrawler.BilibiliAudioDownload(bv=BV_num, p_start=p_start, p_end=p_end, log=log, output_path=output_path, output_format=output_format)
            except Exception as e:
                # Log the error message
                log.insert('end', f"Error: {e}\n")
                log.see('end')
                print('An Error has occurred. Please check the log.')
            # BilibiliCrawler.BilibiliAudioDownload(bv=BV_num, p_start=p_start, p_end=p_end, log=log,
            #                                       output_path=output_path, output_format=output_format)
        else:
            try:
                BilibiliCrawler.BilibiliAudioDownload(bv=BV_num, p_start=p_start, p_end=p_end, log=log, output_path=output_path)
            except Exception as e:
                # Log the error message
                log.insert('end', f"Error: {e}\n")
                log.see('end')
                print('An Error has occurred. Please check the log.')
            # BilibiliCrawler.BilibiliAudioDownload(bv=BV_num, p_start=p_start, p_end=p_end, log=log,
            #                                       output_path=output_path)

    def __event_bind(self):
        self.widget_dic["tk_button_BVNumberHelp"].bind('<Button-1>',self.BVNumberHelp)
        self.widget_dic["tk_button_ShowDefaultPath"].bind('<Button-1>',self.ShowDefaultPathBilibili)
        self.widget_dic["tk_button_DownloadButton"].bind('<Button-1>',self.Download)

if __name__ == "__main__":
    win = Win()
    win.mainloop()
