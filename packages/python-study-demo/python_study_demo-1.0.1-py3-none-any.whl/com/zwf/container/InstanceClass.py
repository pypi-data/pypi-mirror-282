# 向上转型案例
class Book:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__author = kwargs.get('author')

    def get(self):
        return f'[图书信息]:图书名:{self.__name},图书作者:{self.__author}'


# 子类图书
class ProgrammerBook(Book):
    def __init__(self, **kwargs):
        self.__type = kwargs.get('type')
        # 调用父类的构造方法
        super().__init__(**kwargs)


    # 覆写get()方法
    def get(self):
        # 由于父类属性是私有的，因此在使用父类属性时不可直接调用私有属性，应该调用方法
        return super().get()+f',图书类型:{self.__type}'


class Press:
    # 设置出版社方法进行类向上转型
    # 为了防止 子类的重要方法的判断过多 最好把子类的方法写入子类本身之中
    def public(self, book):
        return book.get()

    # 向下转型
    def downPublic(self, book):
        if isinstance(book, ProgrammerBook):
            return book.get()
        else:
            return '请检查父类是否正确！'


def main():
    book = Book(name='python开发实战',author='李兴华')
    press = Press()
    pBook = ProgrammerBook(name='python开发实战',author='李兴华',type='python')
    # 向上转型  传递父类对象参数
    print(press.public(book))
    # 向下转型 传递子类对象参数
    print(press.downPublic(pBook))


if __name__ == '__main__':
    main()


