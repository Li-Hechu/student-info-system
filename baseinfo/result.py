from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        # 窗口布局
        self.win = Toplevel()
        self.win.title('学生成绩管理')
        Label(self.win, text='考试种类：', width=15).grid(row=0, column=0)
        kinds = ('第一次月考', '期中考试', '第二次月考', '期末考试')
        self.kinds = Combobox(self.win, width=15, values=kinds)
        self.kinds.grid(row=0, column=1)
        Label(self.win, text='选择年级：', width=15).grid(row=0, column=2)
        grades = ('高一', '高二', '高三', '初一', '初二', '初三')
        self.grade = Combobox(self.win, width=15, values=grades)
        self.grade.grid(row=0, column=3)
        Label(self.win, text='选择班级', width=15).grid(row=0, column=4)
        classes = ('一班', '二班', '三班', '四班', '五班', '六班', '七班', '八班', '九班', '十班', '十一班', '十二班', '十三班', '十四班', '十五班')
        self.classes = Combobox(self.win, width=15, values=classes)
        self.classes.grid(row=0, column=5)
        Button(self.win, text='添加', command=self.add, width=15).grid(row=0, column=6)
        Button(self.win, text='修改', command=self.change, width=15).grid(row=0, column=7)
        Button(self.win, text='删除', command=self.delete, width=15).grid(row=0, column=8)
        Button(self.win, text='退出', command=self.win.destroy, width=15).grid(row=0, column=9)
        self.tree = Treeview(self.win, columns=('ID', 'stuID', 'Name', 'Class', 'Course', 'Examkinds', 'Scores'),
                             show='headings')
        self.tree.grid(row=1, column=0, columnspan=10)
        self.tree.heading('ID', text='编号')
        self.tree.heading('stuID', text='学生编号')
        self.tree.heading('Name', text='学生姓名')
        self.tree.heading('Class', text='班级')
        self.tree.heading('Course', text='科目')
        self.tree.heading('Examkinds', text='考试种类')
        self.tree.heading('Scores', text='成绩')
        Label(self.win, text='考试科目：', width=15).grid(row=2, column=4)
        examkinds = ('语文', '数学', '英语', '物理', '化学', '生物', '计算机')
        self.examkinds = Combobox(self.win, values=examkinds, width=15)
        self.examkinds.grid(row=2, column=5)
        Label(self.win, text='学生姓名：', width=20).grid(row=2, column=6)
        self.name = Entry(self.win, width=15)
        self.name.grid(row=2, column=7)
        Label(self.win, text='成绩：', width=15).grid(row=2, column=8)
        self.scores = Entry(self.win, width=15)
        self.scores.grid(row=2, column=9)
        # 显示窗口
        self.query()
        self.win.mainloop()

    # 定义更新方法
    def query(self):
        result = service.query('select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result'
                               ' from v_resultinfo')
        row = len(result)
        if len(self.tree.get_children()) > 0:
            for i in self.tree.get_children():
                self.tree.delete(i)
        else:
            pass
        for i in range(row):
            self.tree.insert('', END, values=result[i])

    # 定义添加方法
    def add(self):
        self._kind = self.kinds.get()
        self._grade = self.grade.get()
        self._class = self.classes.get()
        self._examkinds = self.examkinds.get()
        self._name = self.name.get()
        self._scores = self.scores.get()
        if self._kind != '':
            result1 = service.query('select kindID from tb_examkinds where kindName = %s', self._kind)
            if len(result1) > 0:
                kindID = result1[0][0]
                if self._grade != '' and self._class != '' and self._name != '':
                    result2 = service.query(
                        'select stuID from v_studentinfo where gradeName =%s and stuName =%s and className = %s ',
                        self._grade, self._name, self._class)
                    if len(result2) > 0:
                        stuID = result2[0][0]
                        if self._examkinds != '':
                            result3 = service.query('select subID from tb_subject where subName = %s', self._examkinds)
                            if len(result3) > 0:
                                subID = result3[0][0]
                                if self._scores != '':
                                    result4 = service.exec(
                                        'insert into tb_result(stuID,kindID,subID,result) values (%s,%s,%s,%s)',
                                        (stuID, kindID, subID, self._scores))
                                    if result4 == 1:
                                        self.query()
                                        showinfo('提示', '信息添加完成。')
                                    else:
                                        showwarning('提示', '发生错误，请重试。')
                                else:
                                    showwarning('提示', '请输入分数。')
                            else:
                                showwarning('提示', '未查询到相关考试科目信息，请完善考试科目后重试。')
                        else:
                            showwarning('提示', '请完善考试科目。')
                    else:
                        showwarning('提示', '未查询到该考生信息，请查证后重试。')
                else:
                    showwarning('提示', '请先完善学生年级、班级和姓名后重试。')
            else:
                showwarning('提示', '未查询到相关考试，请先完善考试种类数据。')
        else:
            showwarning('提示', '请先完善考试种类。')

    # 定义修改方法
    def change(self):
        if self.tree.focus() == '':
            showwarning('错误', '请选择要修改的内容。')
        else:
            # 设置窗体
            self.top = Toplevel()
            self.top.title('修改信息')
            self.newscores = Entry(self.top)
            self.newscores.grid(row=0, column=0)
            Button(self.top, text='确认', command=self.confirm).grid(row=1, column=0)
            # 插入数据
            self.a = self.tree.set(self.tree.focus())['Scores']
            self.newscores.insert(END, self.a)

    # 设置修改函数
    def confirm(self):
        self.b = self.newscores.get()
        if self.a == self.b:
            showwarning('提示', '数据一致，无需修改。')
            self.newscores.delete(0, END)
        else:
            result = service.exec('update tb_result set result = %s where stuID = %s',
                                  (self.b, self.tree.set(self.tree.focus())['stuID']))
            if result == 1:
                self.query()
                showinfo('提示', '修改成绩成功。')
                self.top.destroy()
            else:
                showwarning('提示', '发生错误，请重试。')

    # 定义删除方法
    def delete(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择要删除的数据')
        else:
            result = service.exec('delete from tb_result where ID = %s', self.tree.set(self.tree.focus())['ID'])
            if result == 1:
                self.query()
                showinfo('提示', '删除数据成功。')
            else:
                showwarning('提示', '发生错误，请稍后重试。')
