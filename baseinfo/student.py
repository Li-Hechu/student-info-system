from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sys

sys.path.append('../')
from service import service


class mainWindow:
    def __init__(self):
        # 定义类
        self.classid = ''
        self.gradeid = ''
        # 创建窗口
        self.win = Toplevel()
        self.win.title('学生信息管理')
        # 设置所属年级和班级
        Label(self.win, text='所属年级').grid(row=0, column=0)
        self.gradeoption = ('初一', '初二', '初三', '高一', '高二', '高三', '高四')
        self.Grade = Combobox(self.win, textvariable=StringVar(), values=self.gradeoption)
        self.Grade.grid(row=0, column=1)
        Label(self.win, text='所属班级').grid(row=0, column=2)
        self._classoption_ = [
            '一班', '二班', '三班', '四班', '五班', '六班', '七班', '八班', '九班', '十班', '十一班', '十二班', '十三班', '十四班', '十五班']
        self.Classname = Combobox(self.win, textvariable=StringVar(), values=tuple(self._classoption_))
        self.Classname.grid(row=0, column=3)
        # 设置功能按钮
        Button(self.win, text='添加', command=self.add).grid(row=0, column=4)
        Button(self.win, text='修改', command=self.change).grid(row=0, column=5)
        Button(self.win, text='删除', command=self.delete).grid(row=0, column=6)
        Button(self.win, text='退出', command=self.win.destroy).grid(row=0, column=7)
        # 设置显示栏
        self.tree = Treeview(self.win, columns=('ID', 'Name', 'Class', 'Sex', 'Age', 'Address', 'Phone'),
                             show='headings')
        self.tree.grid(row=1, column=0, columnspan=8)
        self.tree.heading('ID', text='学生编号')
        self.tree.heading('Name', text='学生姓名')
        self.tree.heading('Class', text='班级')
        self.tree.heading('Sex', text='性别')
        self.tree.heading('Age', text='年龄')
        self.tree.heading('Address', text='家庭住址')
        self.tree.heading('Phone', text='联系电话')
        # 编辑栏
        Label(self.win, text='学生编号：').grid(row=2, column=0)
        self.ID = Entry(self.win)
        self.ID.grid(row=2, column=1)
        Label(self.win, text='学生姓名：').grid(row=2, column=2)
        self.Name = Entry(self.win)
        self.Name.grid(row=2, column=3)
        Label(self.win, text='年龄：').grid(row=2, column=4)
        self.Age = Entry(self.win)
        self.Age.grid(row=2, column=5)
        Label(self.win, text='性别：').grid(row=2, column=6)
        self.Sex = Combobox(self.win, textvariable=StringVar(), values=('男', '女'))
        self.Sex.grid(row=2, column=7)
        Label(self.win, text='联系电话：').grid(row=3, column=0)
        self.Phone = Entry(self.win)
        self.Phone.grid(row=3, column=1)
        Label(self.win, text='家庭住址：').grid(row=3, column=5)
        self.Address = Entry(self.win)
        self.Address.grid(row=3, column=6, columnspan=2)
        # 显示窗口
        self.query()
        self.win.mainloop()

    # 定义更新方法
    def query(self):
        result = service.query(
            'select stuID, stuName, CONCAT(gradeName,className), sex, age, address, phone '
            'from v_studentinfo')
        num = len(result)
        if len(self.tree.get_children()) > 0:
            for j in self.tree.get_children():
                self.tree.delete(j)
        for i in range(num):
            self.tree.insert('', END, value=result[i])
        self.ID.delete(0, END)
        self.Name.delete(0, END)
        self.Age.delete(0, END)
        self.Sex.delete(0, END)
        self.Phone.delete(0, END)
        self.Address.delete(0, END)

    # 定义修改方法
    def change(self):
        if self.tree.focus() == '':
            showwarning('提示', '请选择需要修改的内容')
        else:
            # 设置界面
            self.top = Toplevel()
            self.top.title('修改信息')
            Label(self.top, text='学生编号：').grid(row=0, column=0)
            self._ID = Entry(self.top)
            self._ID.grid(row=0, column=1)
            Label(self.top, text='学生姓名：').grid(row=0, column=2)
            self._Name = Entry(self.top)
            self._Name.grid(row=0, column=3)
            Label(self.top, text='班级').grid(row=0, column=4)
            self._Class = Entry(self.top)
            self._Class.grid(row=0, column=5)
            Label(self.top, text='年龄：').grid(row=0, column=6)
            self._Age = Entry(self.top)
            self._Age.grid(row=0, column=7)
            Label(self.top, text='性别：').grid(row=1, column=0)
            self._Sex = Combobox(self.top, textvariable=StringVar(), values=('男', '女'))
            self._Sex.grid(row=1, column=1)
            Label(self.top, text='联系电话').grid(row=1, column=2)
            self._Phone = Entry(self.top)
            self._Phone.grid(row=1, column=3)
            Label(self.top, text='家庭住址：').grid(row=1, column=4)
            self._Address = Entry(self.top)
            self._Address.grid(row=1, column=5)
            Button(self.top, text='确认', command=self.confirm).grid(row=2, column=0, columnspan=8)
            # 获取
            self.result = self.tree.set(self.tree.focus())
            self._ID.insert(0, self.result['ID'])
            self._Name.insert(0, self.result['Name'])
            self._Class.insert(0, self.result['Class'])
            self._Sex.insert(0, self.result['Sex'])
            self._Age.insert(0, self.result['Age'])
            self._Address.insert(0, self.result['Address'])
            self._Phone.insert(0, self.result['Phone'])

    # 设置修改函数
    def confirm(self):
        self._id = self._ID.get()
        self._name = self._Name.get()
        self._age = self._Age.get()
        self._sex = self._Sex.get()
        self._phone = self._Phone.get()
        self._address = self._Address.get()
        self._class = self._Class.get()
        a = self._class[0:2]
        b = self._class[2:4]
        service.exec('delete from tb_student where stuID = %s', (self.tree.set(self.tree.focus())['ID']))
        _classid = service.query('select classID from tb_class where className = %s', b)
        _gradeid = service.query('select gradeID from tb_grade where gradeName = %s', a)
        service.exec(
            'insert into tb_student(stuID,stuName,classID,gradeID,age,sex,phone,address) '
            'values (%s,%s,%s,%s,%s,%s,%s,%s)',
            (self._id, self._name, _classid, _gradeid, self._age, self._sex, self._phone, self._address))
        self.query()
        self.top.destroy()
        showinfo('提示', '修改数据完成。')

        # 定义添加方法

    def add(self):
        self.id = self.ID.get()
        self.name = self.Name.get()
        self.sex = self.Sex.get()
        self.age = self.Age.get()
        self.address = self.Address.get()
        self.phone = self.Phone.get()
        if self.id == '' or self.name == '' or self.sex == '' or self.age == '' or self.address == '' \
                or self.phone == '':
            showwarning('错误', '请完善数据后重试。')
        else:
            gradeid = service.exec('select gradeID from tb_grade where gradeName = %s', (self.Grade.get(),))
            classid = service.exec('select classID from tb_class where className = %s', (self.Classname.get(),))
            result = service.exec(
                'insert into tb_student (stuID,stuName,classID,gradeID,sex,age,phone,address) '
                'values (%s,%s,%s,%s,%s,%s,%s,%s)',
                (self.id, self.name, classid, gradeid, self.sex, self.age, self.phone, self.address))
            if result == 1:
                self.query()
                self.Grade.set('所有')
                self.Classname.set('一班')
                self.ID.delete(0, END)
                self.Name.delete(0, END)
                self.Age.delete(0, END)
                self.Sex.set('男')
                self.Phone.delete(0, END)
                self.Address.delete(0, END)
                showinfo('提示', '数据添加完成')
            else:
                showwarning('警告', '发生错误，请重试。')

    # 定义删除方法
    def delete(self):
        if self.tree.focus() == '':
            showwarning('错误', '请选择要删除的内容。')
        else:
            a = self.tree.set(self.tree.focus())['ID']
            service.exec('delete from tb_student where stuID = %s', a)
            self.query()
            showinfo('提示', '信息删除完成。')
