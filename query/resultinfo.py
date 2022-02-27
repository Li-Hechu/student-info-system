from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        self.win = Toplevel()
        self.win.title('考生成绩查询')
        Label(self.win, text='输入学生姓名：', width=15).grid(row=0, column=0)
        self.name = Entry(self.win, width=15)
        self.name.grid(row=0, column=1)
        Label(self.win, text='考试种类：', width=15).grid(row=0, column=2)
        self.kind = Combobox(self.win, values=('所有', '第一次月考', '期中考试', '第二次月考', '期末考试'), width=15)
        self.kind.grid(row=0, column=3)
        Label(self.win, text='考试科目', width=15).grid(row=0, column=4)
        self.subject = Combobox(self.win, width=15, values=('所有', '语文', '数学', '英语', '物理', '化学', '生物', '计算机'))
        self.subject.grid(row=0, column=5)
        Button(self.win, text='查询', command=self.query).grid(row=0, column=6)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=0, column=7)
        self.tree = Treeview(self.win, columns=('stuID', 'Name', 'Class', 'Course', 'Examkinds', 'Scores'),
                             show='headings')
        self.tree.grid(row=1, column=0, columnspan=8)
        self.tree.heading('stuID', text='学生编号')
        self.tree.heading('Name', text='学生姓名')
        self.tree.heading('Class', text='班级')
        self.tree.heading('Course', text='科目')
        self.tree.heading('Examkinds', text='考试种类')
        self.tree.heading('Scores', text='成绩')
        self.win.mainloop()

    def query(self):
        name = self.name.get()
        kind = self.kind.get()
        sub = self.subject.get()
        if name == '' and kind == '' and sub == '':
            showwarning('错误', '请完善查询条件后重试。')
        elif name == '' and kind == '所有' and sub == '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo')
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            else:
                if len(result) > 0:
                    for i in range(len(result)):
                        self.tree.insert('', END, values=result[i])
                else:
                    showinfo('提示', '抱歉，未查询到相关信息。')
        elif name == '' and kind == '所有' and sub != '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where subName = %s', sub)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            else:
                pass
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        elif name == '' and kind != '所有' and sub != '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where kindName = %s and subName = %s', kind, sub)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            else:
                pass
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        elif name != '' and kind != '所有' and sub != '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where stuName=%s and kindName=%s and subName=%s',
                                   name, kind, sub)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        elif name == '' and kind != '所有' and sub == '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where kindName=%s', kind)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        elif name != '' and kind == '所有' and sub == '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where stuName=%s', name)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        elif name != '' and kind != '所有' and sub == '所有':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where stuName=%s and kindName=%s', name, kind)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        elif name != '' and kind == '' and sub != '':
            result = service.query('select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result '
                                   'from v_resultinfo where stuName=%s and subName=%s', name,sub)
            if len(self.tree.get_children()) > 0:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未查询到相关信息。')
        else:
            showwarning('错误', '没有此查询条件。')
