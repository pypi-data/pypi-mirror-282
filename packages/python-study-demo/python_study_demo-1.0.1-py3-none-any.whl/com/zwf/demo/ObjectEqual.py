# 对象值进行比较,如果要比较对象eq lt gt le ge时要覆写object类方法
class Book:
    __slots__ = ['__title', '__author', '__price']

    def __init__(self, **kwargs):
        self.__title = kwargs.get('title')
        self.__author = kwargs.get('author')
        self.__price = kwargs.get('price')

    # 覆写str()方法  打印字符串
    def __str__(self):
        return f'[图书信息]图书名:{self.__title},作者:{self.__author},价格:{self.__price}'

    # # 覆写eq方法实现对象比较
    # def __eq__(self, other):
    #     # 如果内存地址值相等就返回True
    #     if id(self) == id(other):
    #         return True
    #     # 如果对象hash值相同就返回True
    #     if hash(self) == hash(other):
    #         return True
    #
    #     return self.__title == other.__title and self.__author == other.__author and self.__price == other.__price

   # 对象小于比较
    def __lt__(self, other):
        if id(self) < id(other):
            return True
        if hash(self) < hash(other):
            return True
        return self.__price < other.__price

    # 覆写hash值的方法
    def __hash__(self):
        result = self.__title+self.__author+str(self.__price)
        return object.__hash__(result)


def main():
    book1 = Book(title='Python开发实战', author='李兴华', price=3789)  # self
    book2 = Book(title='Python开发实战', author='李兴华', price=9999)  # other
    # print(book1 == book2)
    print(book1 < book2)


if __name__ == '__main__':
    main()