class Book:
    # 定义内部类的对象
    __Press = None

    __slots__ = ('__name', '__author')

    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')

    def get(self):
        if self.__Press.check:
            print("图书已校稿！")
            self.__Press.distribute()
            return f'[图书信息]图书名:{self.__name},作者名:{self.__author},出版社:{self.__Press.get()}'
        else:
            return None
    def get_press(self):
        Book.__Press = Book.Press('清华大学出版社')

    def set_press(self,press):
        Book.__Press = press

    def get_press_pro(self):
        return self.__Press


    class Press:

        __slots__ = ('__public')

        def __init__(self, public):
            self.__public = public

        def check(self):
            print(f'{self.__public}检查来自作者{Book.__author}的图书出版稿!')
            return True

        def set_public(self, public):
            self.__public = public


        def distribute(self):
            print('分发进行推销....')

        def get(self):
            return self.__public


def main():
    book = Book(name='python开发实战', author='李兴华')
    # 初始化内部类
    # book.get_press()
    # book.get_press_pro().set_public("北京大学出版社")
    press =Book.Press('北京大学出版社')
    book.set_press(press)
    print(book.get())


if __name__ == '__main__':
    main()