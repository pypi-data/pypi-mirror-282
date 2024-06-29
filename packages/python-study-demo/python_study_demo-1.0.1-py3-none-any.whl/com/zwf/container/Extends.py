class  Book:
     # 父类的属性不能私有 私有属性不能被继承
    __slots__ = ['bookName','price','public']

    # 获取子类信息  使用回调函数
    def __init_subclass__(cls, **kwargs):
        print(f'获取子类信息{cls.__name__.__str__()},子类参数:{kwargs}')



    def __init__(self, **kwargs):
        self.bookName = kwargs.get('bookName')
        self.price = kwargs.get('price')
        self.public = kwargs.get('public')


    def get(self):
        print('*'*10)
        return f'堆内存地址:{id(self)}'


class  ProgramBook(Book,support=['java','mysql','oracle']):

    __slots__ = ['__properties']

   # 如果子类使用构造函数,必须手工调用父类的构造函数
    def __init__(self, **kwargs):
        self.__properties=kwargs.get('properties')
        # 调用父类构造方法
        super().__init__(**kwargs)


    def get(self):
        return f'[图书信息]书名:{self.bookName},价格:{self.price},出版社:{self.public},书籍属性:{self.__properties},堆内存地址:{id(self)}'


class SciencBook(Book,items=['One','Two','Three']):
    __slots__ = ['__author']

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def set_author(self,author):
        self.__author = author

    def get(self):
        return f'[图书信息]书名:{self.bookName},价格:{self.price},出版社:{self.public},图书作者:{self.__author},堆内存地址:{id(self)}'

def main():
    pgBook = ProgramBook(bookName='JAVA从开发到实战',price=79.8,public='清华大学出版社',properties=['编程自学书籍','技术图书类'])
    scienceBook = SciencBook(bookName='JAVA从开发到实战', price=79.8)
    scienceBook.set_author('李兴华')
    bool=Book()
    print(bool.get())
    print(pgBook.get())
    print(scienceBook.get())

    print(f'父类对象信息:{Book.__class__}')
    print(f'programBook继承的第一个父类{ProgramBook.__base__}')
    print(f'programBook继承的所有父类{ProgramBook.__bases__}')
    print(f'programBook继承的第一个父类{ProgramBook.__base__}')
    print(f'programBook属于Book的子类吗?{issubclass(ProgramBook().__class__,Book)}')
    print(f'programBook属于Book的子类吗?{issubclass(ProgramBook, Book)}')



if __name__ == '__main__':
    main()