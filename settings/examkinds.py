from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        self._ID = ''
        self._name = ''
        self.win = Toplevel()
        self.win.title('考试类别设置')
        self.tree = Treeview(self.win, columns=('ID', 'Name'), show='headings')
        self.tree.heading('ID', text='类别编号', anchor='center')
        self.tree.heading('Name', text='类别名称', anchor='center')
        self.tree.grid(row=0, column=0, columnspan=4)
        Label(self.win, text='类别编号').grid(row=1, column=0)
        Label(self.win, text='类别名称').grid(row=1, column=2)
        self.ID = Entry(self.win)
        self.ID.grid(row=1, column=1)
        self.name = Entry(self.win)
        self.name.grid(row=1, column=3)
        Button(self.win, text='添加', command=self.add).grid(row=2, column=0)
        Button(self.win, text='修改', command=self.change).grid(row=2, column=1)
        Button(self.win, text='删除', command=self.delete).grid(row=2, column=2)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=2, column=3)
        self.tree.bind('<<TreeviewSelect>>', self.edt)
        self.query()
        self.win.mainloop()

    def query(self):
        result = service.query('select * from tb_examkinds')
        if self.tree.get_children != '':
            for j in self.tree.get_children():
                self.tree.delete(j)
        else:
            pass
        for i in range(len(result)):
            self.tree.insert('', END, values=result[i])

    def edt(self, event):
        self.ID.delete(0,END)
        self.name.delete(0,END)
        temp = self.tree.set(self.tree.focus())
        self.ID.insert(0, temp['ID'])
        self.name.insert(0, temp['Name'])

    def add(self):
        if self.ID.get() == '' or self.name.get() == '':
            showwarning('提示', '请完善数据。')
        else:
            data = (self.ID.get(), self.name.get())
            result = service.exec('insert into tb_examkinds(kindID,kindName) values (%s,%s)', data)
            if result == 1:
                self.ID.delete(0, END)
                self.name.delete(0, END)
                self.query()
                showinfo('提示', '数据添加成功')
            else:
                showwarning('警告', '发生错误，请重试')

    def change(self):
        self._ID = self.ID.get()
        self._name = self.name.get()
        if self._ID == self.tree.set(self.tree.focus())['ID'] \
                and self._name == self.tree.set(self.tree.focus())['Name']:
            showwarning('提示', '信息一致，无法修改。')
        else:
            service.exec('delete from tb_examkinds where kindID = %s', (self.tree.set(self.tree.focus())['ID'],))
            result = service.exec('insert into tb_examkinds(kindID,kindName) values (%s,%s)', (self._ID, self._name))
            if result == 1:
                self.query()
                showinfo('提示', '修改数据成功。')
                self.ID.delete(0, END)
                self.name.delete(0, END)
            else:
                pass

    def delete(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择')
        else:
            result = service.exec('delete from tb_examkinds where kindID = %s', (self.tree.set(self.tree.focus())['ID'],))
            if result == 1:
                self.query()
                showinfo('提示', '信息删除完成。')
                self.name.delete(0, END)
                self.ID.delete(0, END)
