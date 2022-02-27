from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import datetime
from service import service
from settings import classes, examkinds, grade, subject
from baseinfo import result, student
from query import resultinfo, studentinfo
from system import user


class mainWindow:
    def __init__(self):
        self.win = Toplevel()
        self.win.title('学生成绩管理系统')
        self.win.geometry('850x600')
        self.win.after(1000, self.timeUpdate)
        self.image1 = Image.open('E:\\Python程序\\学生成绩管理系统\\images\\窗体背景.jpg')
        self.image2 = ImageTk.PhotoImage(self.image1)
        Label(self.win, image=self.image2).place(x=0, y=0)
        self.labelInfo = Label(self.win,
                               text='当前登录用户：' + service.userName + ' | 登录时间：' + datetime.datetime.now().strftime(
                                   '%Y-%m-%d %H:%M:%S') + ' | 版权所有：思壮股份有限公司', anchor='center')
        self.labelInfo.place(x=0, y=580, width=850,height=20)
        self.menu = Menu(self.win)
        self.menu1_1 = Menu(self.menu, tearoff=False)
        self.menu1_2 = Menu(self.menu, tearoff=False)
        self.menu1_3 = Menu(self.menu, tearoff=False)
        self.menu1_4 = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='基础设置', menu=self.menu1_1)
        self.menu.add_cascade(label='基本信息设置', menu=self.menu1_2)
        self.menu.add_cascade(label='系统查询', menu=self.menu1_3)
        self.menu.add_cascade(label='系统管理', menu=self.menu1_4)
        self.menu1_1.add_command(label='年级设置', command=grade.mainWindow)
        self.menu1_1.add_command(label='班级设置', command=classes.mainWindow)
        self.menu1_1.add_command(label='考试科目设置', command=subject.mainWindow)
        self.menu1_1.add_command(label='考试类别设置', command=examkinds.mainWindow)
        self.menu1_2.add_command(label='学生管理', command=student.mainWindow)
        self.menu1_2.add_command(label='成绩管理', command=result.mainWindow)
        self.menu1_3.add_command(label='学生信息查询', command=studentinfo.mainWindow)
        self.menu1_3.add_command(label='学生成绩查询', command=resultinfo.mainWindow)
        self.menu1_4.add_command(label='管理员维护', command=user.mainWindow)
        self.menu1_4.add_command(label='退出', command=self.win.destroy)
        self.win.config(menu=self.menu)
        self.win.mainloop()

    def timeUpdate(self):
        global labalInfo
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.labelInfo.config(text='当前登录用户：' + service.userName + ' | 登录时间：' + self.time + ' | 版权所有：思壮股份有限公司')
        self.win.after(100, self.timeUpdate)
