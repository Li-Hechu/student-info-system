from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        self.win = Toplevel()
        self.win.title('学生信息查询')
        Label(self.win, text='选择查询条件:', width=15).grid(row=0, column=0)
        conditions = ('学生编号', '姓名', '年级', '班级', '性别', '年龄', '家庭住址', '联系电话')
        self.conditions = Combobox(self.win, values=conditions, width=15)
        self.conditions.grid(row=0, column=1)
        Label(self.win, text='输入关键字：').grid(row=0, column=2)
        self.keywords = Entry(self.win, width=15)
        self.keywords.grid(row=0, column=3)
        Button(self.win, text='查询', command=self.query).grid(row=0, column=4)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=0, column=5)
        self.tree = Treeview(self.win, columns=('ID', 'Name', 'Class', 'Sex', 'Age', 'Address', 'Phone'),
                             show='headings')
        self.tree.grid(row=1, column=0, columnspan=7)
        self.tree.heading('ID', text='学生编号')
        self.tree.heading('Name', text='学生姓名')
        self.tree.heading('Class', text='班级')
        self.tree.heading('Sex', text='性别')
        self.tree.heading('Age', text='年龄')
        self.tree.heading('Address', text='家庭住址')
        self.tree.heading('Phone', text='联系电话')
        self.win.mainloop()

    def query(self):
        condition = self.conditions.get()
        keyword = self.keywords.get()
        if condition == '学生编号':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where stuID = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '姓名':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where stuName = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '班级':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where className = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '年级':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone'
                'from v_studentinfo where gradeName = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '性别':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where sex = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '年龄':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where age = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '家庭住址':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where address = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        elif condition == '联系电话':
            result = service.query(
                'select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone '
                'from v_studentinfo where phone = %s',
                keyword)
            if len(result) > 0:
                for i in range(len(result)):
                    self.tree.insert('', END, values=result[i])
            else:
                showinfo('提示', '抱歉，未找到相关信息。')
        else:
            showwarning('错误', '没有此查询条件。')
        self.conditions.delete(0, END)
        self.keywords.delete(0, END)


