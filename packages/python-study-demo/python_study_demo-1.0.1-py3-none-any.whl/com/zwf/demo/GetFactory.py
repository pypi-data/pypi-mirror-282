# 工厂模式
class Book:
    @staticmethod
    def getInstance(clzz=None):
        if clzz=='math':
            return MathBook()
        elif clzz == 'program':
            return ProgramBook()
        else:
            return Book()

    def __str__(self):
        return '纯图书书籍！！'




class MathBook:
    def __str__(self):
        return '数学书籍！！'

class ProgramBook:
    def __str__(self):
        return '编程类书籍！！'

def main():
    print(Book.getInstance('math'))
    print(Book.getInstance('program'))
    print(Book.getInstance())


if __name__ == '__main__':
    main()