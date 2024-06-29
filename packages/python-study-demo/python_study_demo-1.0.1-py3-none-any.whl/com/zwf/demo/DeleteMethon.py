class Book:
    # 私有属性的访问
    __slots__ = ('__name')

     # 必须放在第一个  把name当做变量 实际上返回self.__name
    @property
    def name(self):
        return self.__name

    @name.deleter
    def name(self):
        del self.__name

    @name.setter
    def name(self,name):
        self.__name = name


def main():
    book = Book()
    # 直接通过函数名赋值属性值
    book.name = 'python开发实战！'
    # 直接获取私有属性值
    print(book.name)
    # 删除私有属性值
    del book.name


if __name__ == '__main__':
    main()