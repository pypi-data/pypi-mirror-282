class Student:
    def set(self,name,age):
        self.name = name
        self.age = age

    def get(self):
        return '[学生信息]姓名:'+self.name+',年龄:'+str(self.age)+',对象栈内存地址:'+str(id(self))


def main():
    stu2 = Student()
    stu2.set('张三', 25)
    stu1 = Student()
    stu1.set('李四', 25)
    rep = stu1
    rep2 = stu2
    print(stu1.get())
    print(stu2.get())
    print(id(rep))
    print(id(rep2))


if __name__ == '__main__':
    main()