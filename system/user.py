from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title('用户信息维护')
        self.tree = Treeview(self.win, columns=('UserName', 'Password'), show='headings')
        self.tree.grid(row=0, column=0, columnspan=4)
        self.tree.heading('UserName', text='用户名称：')
        self.tree.heading('Password', text='用户密码：')
        Label(self.win, text='用户名称：', width=10).grid(row=1, column=0)
        self.username = Entry(self.win, width=10)
        self.username.grid(row=1, column=1)
        Label(self.win, text='用户密码：', width=10).grid(row=1, column=2)
        self.password = Entry(self.win, width=10)
        self.password.grid(row=1, column=3)
        Button(self.win, text='添加', command=self.add).grid(row=2, column=0)
        Button(self.win, text='修改', command=self.change).grid(row=2, column=1)
        Button(self.win, text='删除', command=self.delete).grid(row=2, column=2)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=2, column=3)
        self.query()
        self.win.mainloop()

    def query(self):
        result = service.query('select * from tb_user')
        row = len(result)
        if len(self.tree.get_children()) > 0:
            for i in self.tree.get_children():
                self.tree.delete(i)
        else:
            pass
        for j in range(row):
            self.tree.insert('', END, values=result[j])

    def add(self):
        self.name = self.username.get()
        self.pwd = self.password.get()
        if self.name == '' or self.pwd == '':
            showwarning('提示', '请完善数据。')
        else:
            result = service.exec('insert into tb_user(userName,userPwd) values(%s,%s)', (self.name, self.pwd))
            if result == 1:
                self.query()
                self.username.delete(0, END)
                self.password.delete(0, END)
                showinfo('提示', '信息添加完成。')
            else:
                showwarning('错误', '发生错误，请重试。')

    def change(self):
        if self.tree.focus() == '':
            showinfo('提示', '请选择要修改的数据。')
        else:
            self.name_ = self.tree.set(self.tree.focus())['UserName']
            self.pwd_ = self.tree.set(self.tree.focus())['Password']
            self.top = Toplevel()
            self.top.title('修改')
            Label(self.top, text='用户名称：', width=10).grid(row=0, column=0)
            self._name = Entry(self.top, width=10)
            self.name.grid(row=0, column=1)
            Label(self.top, tetx='用户密码：').grid(row=0, column=2)
            self._pwd = Entry(self.top, width=10)
            self._pwd.grid(row=0, column=3)
            Button(self.top, text='确定', command=self.confirm).grid(row=1, column=0, columnspan=4)
            # 填入数据
            self._name.insert(0, self.name_)
            self._pwd.insert(0, self.pwd_)

    def confirm(self):
        if self._name.get() == self.name_ and self._pwd.get() == self.pwd_:
            showwarning('提示', '信息一致，无需修改。')
        else:
            service.exec('delete from tb_user where userName = %s', self.name_)
            result = service.exec('insert into tb_user(userName,userPwd) values(%s,%s)',
                                  (self._name.get(), self._pwd.get()))
            if result == 1:
                self.query()
                self.top.destroy()
                showinfo('提示', '修改数据完成。')
            else:
                showwarning('错误', '发生错误，请重试。')

    def delete(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择要删除的数据')
        else:
            result = service.exec('delete from tb_user where userName=%s', self.tree.set(self.tree.focus())['UserName'])
            if result == 1:
                self.query()
                showinfo('提示', '数据删除完成。')
            else:
                showwarning('错误', '发生错误，请稍后重试。')
