"""
本代码由[Tkinter布局助手]生成
当前版本:3.4.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
Very Useful, go try
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict
from time import asctime as t
import AudioEdit
import HelpFunctions

class WinGUI(Toplevel):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_label_AudioPath"] = self.__tk_label_AudioPath(self)
        self.widget_dic["tk_text_AudioPathInput"] = self.__tk_text_AudioPathInput(self)
        self.widget_dic["tk_label_AudioOutputPath"] = self.__tk_label_AudioOutputPath(self)
        self.widget_dic["tk_text_AudioOutputPathInput"] = self.__tk_text_AudioOutputPathInput(self)
        self.widget_dic["tk_label_AudioOutputPathNotes"] = self.__tk_label_AudioOutputPathNotes(self)
        self.widget_dic["tk_select_box_AudioOutputFormat"] = self.__tk_select_box_AudioOutputFormat(self)
        self.widget_dic["tk_label_AudioOutputFormat"] = self.__tk_label_AudioOutputFormat(self)
        self.widget_dic["tk_text_Log"] = self.__tk_text_Log(self)
        self.widget_dic["tk_label_LogHistory"] = self.__tk_label_LogHistory(self)
        self.widget_dic["tk_button_audio_editButton"] = self.__tk_button_audio_editButton(self)
        self.widget_dic["tk_label_Actions"] = self.__tk_label_Actions(self)
        self.widget_dic["tk_label_li4f1rwn"] = self.__tk_label_li4f1rwn(self)
        self.widget_dic["tk_label_li4f1zy8"] = self.__tk_label_li4f1zy8(self)
        self.widget_dic["tk_label_li4f6e1n"] = self.__tk_label_li4f6e1n(self)
        self.widget_dic["tk_label_li4fezbs"] = self.__tk_label_li4fezbs(self)
        self.widget_dic["tk_label_li4fgdse"] = self.__tk_label_li4fgdse(self)
        self.widget_dic["tk_label_li4fi5z3"] = self.__tk_label_li4fi5z3(self)
        self.widget_dic["tk_input_AudioVolumeNum"] = self.__tk_input_AudioVolumeNum(self)
        self.widget_dic["tk_label_li5cns1h"] = self.__tk_label_li5cns1h(self)
        self.widget_dic["tk_label_li5cnzjk"] = self.__tk_label_li5cnzjk(self)
        self.widget_dic["tk_input_AudioFadeA"] = self.__tk_input_AudioFadeA(self)
        self.widget_dic["tk_input_AudioFadeB"] = self.__tk_input_AudioFadeB(self)
        self.widget_dic["tk_label_LengthEdit"] = self.__tk_label_LengthEdit(self)
        self.widget_dic["tk_label_li5cuq7p"] = self.__tk_label_li5cuq7p(self)
        self.widget_dic["tk_input_AudioLengthA"] = self.__tk_input_AudioLengthA(self)
        self.widget_dic["tk_label_sss"] = self.__tk_label_sss(self)
        self.widget_dic["tk_input_AudioLengthB"] = self.__tk_input_AudioLengthB(self)
        self.widget_dic["tk_label_li5cw1ou"] = self.__tk_label_li5cw1ou(self)
        self.widget_dic["tk_input_AudioLoopNum"] = self.__tk_input_AudioLoopNum(self)
        self.widget_dic["tk_label_li5d1cft"] = self.__tk_label_li5d1cft(self)
        self.widget_dic["tk_input_AudioSpeedUpNum"] = self.__tk_input_AudioSpeedUpNum(self)
        self.widget_dic["tk_select_box_EffectNum"] = self.__tk_select_box_EffectNum(self)
        self.widget_dic["tk_select_box_CompressNum"] = self.__tk_select_box_CompressNum(self)
        self.widget_dic["tk_label_li5dbdzv"] = self.__tk_label_li5dbdzv(self)
        self.widget_dic["tk_label_li5duwcy"] = self.__tk_label_li5duwcy(self)
        self.widget_dic["tk_button_ShowDefaultPathButton"] = self.__tk_button_ShowDefaultPathButton(self)

        with open('./Resources/info02.txt', 'r') as f:
            open_help_var = int(f.read())
            if open_help_var == 1:
                help_instance = HelpFunctions.AudioEditHelp(self)

    def __win(self):
        self.title("Audio Edit GUI")
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

    def __tk_label_AudioPath(self,parent):
        label = Label(parent,text="Audio Path:",anchor="center", )
        label.place(x=30, y=20, width=128, height=39)
        return label

    def __tk_button_ShowDefaultPathButton(self,parent):
        btn = Button(parent, text="❓", takefocus=False,)
        btn.place(x=590, y=78, width=30, height=30)
        return btn

    def __tk_text_AudioPathInput(self,parent):
        text = Text(parent)
        text.place(x=158, y=20, width=537, height=39)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=682, y=20, width=15, height=39)
        self.scrollbar_autohide(vbar,text)
        text.insert('end','for example, D:\Coding\MyMusic\cup_of_cuppuccino.mp3')
        return text

    def __tk_label_AudioOutputPath(self,parent):
        label = Label(parent,text="Audio Output Path:",anchor="center", )
        label.place(x=30, y=70, width=129, height=39)
        return label

    def __tk_text_AudioOutputPathInput(self,parent):
        text = Text(parent)
        text.place(x=160, y=70, width=419, height=39)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=564, y=70, width=15, height=39)
        self.scrollbar_autohide(vbar,text)
        return text

    def __tk_label_AudioOutputPathNotes(self,parent):
        label = Label(parent,text="Leave it blank if you want to have it output in the default directory",anchor="center", )
        label.place(x=160, y=110, width=419, height=17)
        return label

    def __tk_select_box_AudioOutputFormat(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = (".mp3",".wav",".ogg")
        cb.place(x=445, y=320, width=62, height=40)
        cb.current(0)
        return cb

    def __tk_label_AudioOutputFormat(self,parent):
        label = Label(parent,text="Audio Output Format:",anchor="center", )
        label.place(x=300, y=320, width=143, height=37)
        return label

    def __tk_text_Log(self, parent):
        text = Text(parent)
        text.place(x=0, y=410, width=766, height=100)

        vbar = Scrollbar(parent)
        text.configure(yscrollcommand=vbar.set)
        vbar.config(command=text.yview)
        vbar.place(x=751, y=410, width=15, height=100)
        self.scrollbar_autohide(vbar, text)
        text.insert('end', f'{t()}\n=====Initialization Complete!===== \nThx for using this program ヾ(≧▽≦*)o\nWaiting till you pressed: Edit Audio!!!\n')
        return text

    def __tk_label_LogHistory(self,parent):
        label = Label(parent,text="Log History: ",anchor="center", )
        label.place(x=0, y=380, width=99, height=30)
        return label

    def __tk_button_audio_editButton(self,parent):
        btn = Button(parent, text="Edit Audio!!!", takefocus=False,)
        btn.place(x=140, y=320, width=109, height=40)
        return btn

    def __tk_label_Actions(self,parent):
        label = Label(parent,text="Actions:",anchor="center", )
        label.place(x=50, y=320, width=50, height=39)
        return label


    def __tk_label_li4f1rwn(self,parent):
        label = Label(parent,text="3D sound effect",anchor="center", )
        label.place(x=30, y=260, width=97, height=30)
        return label

    def __tk_label_li4f1zy8(self,parent):
        label = Label(parent,text="Compress",anchor="center", )
        label.place(x=310, y=260, width=65, height=30)
        return label

    def __tk_label_li4f6e1n(self,parent):
        label = Label(parent,text="Volume Edit",anchor="center", )
        label.place(x=30, y=200, width=76, height=30)
        return label

    def __tk_label_li4fezbs(self,parent):
        label = Label(parent,text="Fade in",anchor="center", )
        label.place(x=150, y=200, width=50, height=30)
        return label

    def __tk_label_li4fgdse(self,parent):
        label = Label(parent,text="s, Fade out",anchor="center", )
        label.place(x=220, y=200, width=69, height=30)
        return label

    def __tk_label_li4fi5z3(self,parent):
        label = Label(parent,text="s",anchor="center", )
        label.place(x=310, y=200, width=11, height=30)
        return label

    def __tk_input_AudioVolumeNum(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=108, y=200, width=35, height=30)
        ipt.insert(0, '1')
        return ipt

    def __tk_label_li5cns1h(self,parent):
        label = Label(parent,text="times",anchor="center", )
        label.place(x=280, y=140, width=39, height=30)
        return label

    def __tk_label_li5cnzjk(self,parent):
        label = Label(parent,text="ex. type in 2 to increase volume by a factor of two",anchor="center", )
        label.place(x=25, y=230, width=320, height=25)
        return label

    def __tk_input_AudioFadeA(self,parent):
        ipt = Entry(parent)
        ipt.place(x=200, y=200, width=20, height=30)
        ipt.insert(0,'0')
        return ipt

    def __tk_input_AudioFadeB(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=290, y=200, width=20, height=30)
        ipt.insert(0, '0')
        return ipt

    def __tk_label_LengthEdit(self,parent):
        label = Label(parent,text="Length Edit",anchor="center", )
        label.place(x=30, y=140, width=69, height=30)
        return label

    def __tk_label_li5cuq7p(self,parent):
        label = Label(parent,text="ex. type in 2 and 5 to cut the Audio from 2sec~5sec",anchor="center", )
        label.place(x=30, y=170, width=320, height=20)
        return label

    def __tk_input_AudioLengthA(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=100, y=140, width=35, height=30)
        ipt.insert(0, '0')
        return ipt

    def __tk_label_sss(self,parent):
        label = Label(parent,text="s ~",anchor="center", )
        label.place(x=135, y=140, width=28, height=30)
        return label

    def __tk_input_AudioLengthB(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=160, y=140, width=35, height=30)
        ipt.insert(0, '10')
        return ipt

    def __tk_label_li5cw1ou(self,parent):
        label = Label(parent,text="s, loop for",anchor="center", )
        label.place(x=195, y=140, width=66, height=30)
        return label

    def __tk_input_AudioLoopNum(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=260, y=140, width=20, height=30)
        ipt.insert(0, '1')
        return ipt

    def __tk_label_li5d1cft(self,parent):
        label = Label(parent,text="Speed up by a factor of",anchor="center", )
        label.place(x=340, y=140, width=144, height=30)
        return label

    def __tk_input_AudioSpeedUpNum(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=486, y=140, width=31, height=30)
        ipt.insert(0, '1')
        return ipt

    def __tk_select_box_EffectNum(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("0","0.1","0.5","1.0","2.0","3.0","5.0")
        cb.place(x=130, y=250, width=143, height=40)
        cb.current(0)
        return cb

    def __tk_select_box_CompressNum(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("0","8000","24000")
        cb.place(x=385, y=250, width=150, height=40)
        cb.current(0)
        return cb

    def __tk_label_li5dbdzv(self,parent):
        label = Label(parent,text="*choose a smaller number for lower quality (0 for no compress)",anchor="center", )
        label.place(x=300, y=290, width=420, height=20)
        return label

    def __tk_label_li5duwcy(self,parent):
        label = Label(parent,text="*smaller number for lower looping speed",anchor="center", )
        label.place(x=30, y=290, width=250, height=20)
        return label


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

        self.config(menu=self.create_menu())
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="Help",command=self.AudioEditHelp)
        return menu
    def AudioEditHelp(self):
        help_instance = HelpFunctions.AudioEditHelp(self)
    def audio_edit(self,evt):
        input_path = self.widget_dic["tk_text_AudioPathInput"].get("1.0", 'end').strip()
        output_path = self.widget_dic["tk_text_AudioOutputPathInput"].get("1.0", 'end').strip()
        output_format = self.widget_dic["tk_select_box_AudioOutputFormat"].get().lstrip('.')
        audio_length_a = self.widget_dic["tk_input_AudioLengthA"].get()
        audio_length_b = self.widget_dic["tk_input_AudioLengthB"].get()
        audio_volume_num = self.widget_dic["tk_input_AudioVolumeNum"].get()
        audio_fade_a = self.widget_dic["tk_input_AudioFadeA"].get()
        audio_fade_b = self.widget_dic["tk_input_AudioFadeB"].get()
        audio_loop_num = self.widget_dic["tk_input_AudioLoopNum"].get()
        audio_speed_up_num = self.widget_dic["tk_input_AudioSpeedUpNum"].get()
        audio_effect_num = self.widget_dic["tk_select_box_EffectNum"].get()
        audio_compress_num = self.widget_dic["tk_select_box_CompressNum"].get()
        log = self.widget_dic["tk_text_Log"]
        if output_format != '':
            try: #-------改过-------
                AudioEdit.AudioProcess(path=input_path, output_path=output_path, log=log, output_format=output_format,
                                       length_a=eval(audio_length_a), length_b=eval(audio_length_b),
                                       volume_num=eval(audio_volume_num), fade_a=eval(audio_fade_a), fade_b=eval(audio_fade_b),
                                       loop_num=eval(audio_loop_num), speed_up_num=eval(audio_speed_up_num),
                                       effect_num=eval(audio_effect_num), compress_num=eval(audio_compress_num))
            except Exception as e:
                # Log the error message
                self.widget_dic["tk_text_Log"].insert('end', f"Error: {e}\n")
                self.widget_dic["tk_text_Log"].see('end')
                print('An Error has occurred. Please check the log.')
        else:
            try:
                AudioEdit.AudioProcess(path=input_path, output_path=output_path, log=log, output_format=output_format,
                                       length_a=eval(audio_length_a), length_b=eval(audio_length_b),
                                       volume_num=eval(audio_volume_num), fade_a=eval(audio_fade_a),
                                       fade_b=eval(audio_fade_b),
                                       loop_num=eval(audio_loop_num), speed_up_num=eval(audio_speed_up_num),
                                       effect_num=eval(audio_effect_num), compress_num=eval(audio_compress_num))
            except Exception as e:
                # Log the error message
                self.widget_dic["tk_text_Log"].insert('end', f"Error: {e}\n")
                self.widget_dic["tk_text_Log"].see('end')
                print('An Error has occurred. Please check the log.')

    def Show_Default_Path(self,evt):
        HelpFunctions.Show_Default_Path_AudioEdit()

    def __event_bind(self):
        self.widget_dic["tk_button_audio_editButton"].bind('<Button-1>',self.audio_edit)
        self.widget_dic["tk_button_ShowDefaultPathButton"].bind('<Button-1>', self.Show_Default_Path)

if __name__ == "__main__":
    win = Win()
    win.mainloop()
