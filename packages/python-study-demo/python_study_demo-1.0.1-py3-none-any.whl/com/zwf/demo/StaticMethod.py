# 创建一个工厂模式
class Book:
    # 首先覆写 new方法  不受对象限制
    @staticmethod
    def __new__(cls, *args, **kwargs):
        clazz = kwargs.get('clazz')
        if clazz == 'program':
            return ProgramBook()
        elif clazz == 'math':
            return MathBook()
        else:
            return object.__new__(cls)

    def __str__(self):
        return '书籍已经出版了！！'


class ProgramBook(Book):

    def __str__(self):
        return '编程类图书！！'

class MathBook(Book):
    def __str__(self):
        return '数学类图书！！'

def main():
   mathBook = Book(clazz='math')
   programBook = Book(clazz='program')
   print(mathBook)
   print(programBook)
   print(Book())

if __name__ == '__main__':
    main()