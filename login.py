from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
from service import service
import main


class loginStudent:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('940x630')
        self.win.title('系统登录')
        self.image = Image.open(r'E:\Python程序\学生成绩管理系统\images\登录背景.jpg')
        self.image1 = ImageTk.PhotoImage(self.image)
        Label(self.win, image=self.image1).pack()
        Label(self.win, text='欢迎使用学生成绩管理系统', font=150, anchor='center').place(x=300, y=100, width=350, height=50)
        Label(self.win, text='用户名：', anchor='center').place(x=320, y=250)
        Label(self.win, text='密码：', anchor='center').place(x=320, y=350)
        self.user = Entry(self.win)
        self.user.place(x=400, y=250)
        self.password = Entry(self.win)
        self.password.place(x=400, y=350)
        Button(self.win, text='登录', command=self.panduan).place(x=280, y=450)
        Button(self.win, text='退出', command=self.back).place(x=600, y=450)
        label = Label(self.win, text='没有账号密码？点击注册')
        label.place(x=405, y=500)
        label.bind('<Button-1>', self.register)
        self.win.mainloop()

    def panduan(self):
        self.userName = self.user.get()
        self.pss = self.password.get()
        if self.userName == '' or self.pss == '':
            showerror('错误', '请输入用户名或密码')
        else:
            result = service.query('select * from tb_user where userName = %s and userPwd = %s', self.userName, self.pss)
            if len(result) > 0:
                main.mainWindow()
            else:
                self.user.delete(0, END)
                self.password.delete(0, END)
                showwarning('警告', '请输入正确的用户名和密码')

    def back(self):
        boo = askyesno('关闭窗口', '确定退出系统？')
        if  boo == True:
            self.win.destroy()
        else:
            pass

    def register(self, event):
        self.top = Toplevel()
        self.top.title('用户注册')
        Label(self.top, text='请输入用户名：').grid(row=0, column=0)
        self.user = Entry(self.top)
        self.user.grid(row=0, column=1)
        Label(self.top, text='请输入密码：').grid(row=1, column=0)
        self.psw = Entry(self.top)
        self.psw.grid(row=1, column=1)
        Label(self.top, text='请再次输入密码：').grid(row=2, column=0)
        self._psw = Entry(self.top)
        self._psw.grid(row=2, column=1)
        Button(self.top, text='确定', command=self.confirm).grid(row=3, column=0, columnspan=2)

    def confirm(self):
        if self.psw.get() == self._psw.get():
            data = (self.user.get(), self.psw.get())
            result = service.exec('insert into tb_user(userName,userPwd) values (%s,%s)', data)
            print(data, result)
            if result == 1:
                self.top.destroy()
                showinfo('提示', '用户注册完成。')
            else:
                self.top.destroy()
                showwarning('错误', '发生错误，请稍后重试。')
        else:
            self._psw.delete(0, END)
            showwarning('错误', '两次输入的密码不一致，请重新输入')


loginStudent()
