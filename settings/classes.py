from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        self._choosegrade = ''
        self._chooseclass = ''
        self._classname = ''
        self.data = ''
        self.win = Toplevel()
        self.tree = Treeview(self.win, columns=('classID', 'gradeID', 'className'), show='headings')
        self.tree.heading('classID', text='班级编号')
        self.tree.heading('gradeID', text='所属年级')
        self.tree.heading('className', text='班级名称')
        self.tree.grid(row=0, column=0, columnspan=4)
        Label(self.win, text='选择年级：').grid(row=1, column=0)
        self.choosegrade = Combobox(self.win, textvariable=StringVar(), values=('初一', '初二', '初三', '高一', '高二', '高三'))
        self.choosegrade.grid(row=1, column=1)
        Label(self.win, text='班级编号：').grid(row=2, column=0)
        self.chooseclass = Entry(self.win)
        self.chooseclass.grid(row=2, column=1)
        Label(self.win, text='班级名称：').grid(row=2, column=2)
        self.classname = Entry(self.win)
        self.classname.grid(row=2, column=3)
        Button(self.win, text='添加', command=self.add).grid(row=3, column=0)
        Button(self.win, text='修改', command=self.change).grid(row=3, column=1)
        Button(self.win, text='删除', command=self.delete).grid(row=3, column=2)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=3, column=3)
        self.tree.bind('<<TreeviewSelect>>', self.edt)
        self.query()
        self.win.mainloop()

    def query(self):
        result = service.query('select * from tb_class')
        row = len(result)
        if len(self.tree.get_children()) > 0:
            for j in self.tree.get_children():
                self.tree.delete(j)
        else:
            pass
        for i in range(row):
            self.tree.insert('', END, values=result[i])

    def edt(self, event):
        self.chooseclass.delete(0, END)
        self.chooseclass.delete(0, END)
        self.classname.delete(0, END)
        temp = self.tree.set(self.tree.focus())
        self.chooseclass.insert(0, temp['classID'])
        self.choosegrade.insert(0, temp['gradeID'])
        self.classname.insert(0, temp['className'])

    def add(self):
        self.data = (self.chooseclass.get(), self.choosegrade.get(), self.classname.get())
        if self.chooseclass.get() == '' or self.choosegrade.get() == '' or self.classname.get() == '':
            showwarning('提示', '请完善数据后再填入。')
        else:
            result = service.exec('insert into tb_class(classID,gradeID,className) values (%s,%s,%s)', self.data)
            if result == 1:
                self.chooseclass.delete(0, END)
                self.choosegrade.delete(0, END)
                self.classname.delete(0, END)
                self.query()
                showinfo('提示', '添加数据成功！')
            else:
                showwarning('警告', '发生错误，请重试。')

    def change(self):
        if self.tree.focus() == '':
            showerror('提示', '请选择要修改的内容')
        else:
            self._choosegrade = self.choosegrade.get()
            self._chooseclass = self.chooseclass.get()
            self._classname = self.classname.get()
            if self._chooseclass == self.tree.set(self.tree.focus())['classID'] and self._choosegrade == \
                    self.tree.set(self.tree.focus())['gradeID'] and self._classname == \
                    self.tree.set(self.tree.focus())['className']:
                showwarning('提示', '请修改相应内容！')
            else:
                service.exec('delete from tb_class where className = %s',
                             self.tree.set(self.tree.focus())['className'])
                service.exec('insert into tb_class(classID,gradeID,className) values (%s,%s,%s)',
                             (self._chooseclass, self._choosegrade, self._classname))
                self.choosegrade.delete(0, END)
                self.chooseclass.delete(0, END)
                self.classname.delete(0, END)
                self.query()

    def delete(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择要删除的内容')
        else:
            a = self.tree.set(self.tree.focus())['className']
            service.exec('delete from tb_class where className = %s', a)
            self.query()
            self.chooseclass.delete(0, END)
            self.choosegrade.delete(0, END)
            self.classname.delete(0, END)
            showinfo('提示', '信息删除完成')
