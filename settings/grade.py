from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        self._gradeID = ''
        self._gradeName = ''
        self.win = Toplevel()
        self.win.title('年级设置')
        self.tree = Treeview(self.win, columns=('gradeID', 'gradeName'), show='headings')
        self.tree.heading('gradeID', text='年级编号', anchor='center')
        self.tree.heading('gradeName', text='年级名称', anchor='center')
        self.tree.grid(row=0, column=0, columnspan=4)
        Label(self.win, text='年级编号：').grid(row=1, column=0)
        self.gradeID = Entry(self.win)
        self.gradeID.grid(row=1, column=1)
        Label(self.win, text='年级名称：').grid(row=1, column=2)
        self.gradeName = Entry(self.win)
        self.gradeName.grid(row=1, column=3)
        Button(self.win, text='添加', command=self.add).grid(row=2, column=0)
        Button(self.win, text='修改', command=self.change).grid(row=2, column=1)
        Button(self.win, text='删除', command=self.delete).grid(row=2, column=2)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=2, column=3)
        self.tree.bind('<<TreeviewSelect>>', self.edt)
        self.query()
        self.win.mainloop()

    def query(self):
        self.gradeID.delete(0, END)
        self.gradeName.delete(0, END)
        result = service.query('select * from tb_grade')
        row = len(result)
        if len(self.tree.get_children()) > 0:
            for j in self.tree.get_children():
                self.tree.delete(j)
        else:
            pass
        for i in range(row):
            self.tree.insert('', END, values=result[i])

    def edt(self, event):
        self.gradeID.delete(0, END)
        self.gradeName.delete(0, END)
        temp = self.tree.set(self.tree.focus())
        self.gradeID.insert(0, temp['gradeID'])
        self.gradeName.insert(0, temp['gradeName'])

    def add(self):
        self._gradeID = self.gradeID.get()
        self._gradeName = self.gradeName.get()
        if self.gradeID != '' and self.gradeName != '':
            result = service.exec('insert into tb_grade (gradeID,gradeName) values (%s,%s)',
                                      (self._gradeID, self._gradeName))
            if result == 1:
                self.gradeID.delete(0, END)
                self.gradeName.delete(0, END)
                self.query()
                showinfo('成功', '信息添加成功')
            else:
                pass
        else:
            showwarning('错误', '请输入数据后，再进行相关操作')

    def change(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择需要修改的数据')
        else:
            self._gradeID = self.gradeID.get()
            self._gradeName = self.gradeName.get()
            if self._gradeID == self.tree.set(self.tree.focus())['gradeID'] and self._gradeName == \
                    self.tree.set(self.tree.focus())['gradeName']:
                showwarning('提示', '未做出修改。')
            else:
                service.exec('delete from tb_grade where gradeName = %s', self.tree.set(self.tree.focus())['gradeName'])
                service.exec('insert into tb_grade (gradeID,gradeName) values (%s,%s)',
                             (self._gradeID, self._gradeName))
                self.gradeID.delete(0, END)
                self.gradeName.delete(0, END)
                self.query()
                showinfo('提示', '信息修改完成')

    def delete(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择要删除的数据')
        else:
            a = self.tree.set(self.tree.focus())['gradeID']
            service.exec('delete from tb_grade where gradeID = %s', a)
            service.exec('delete from tb_class where gradeID = %s', a)
            self.query()
            showinfo('提示', '数据删除完成')