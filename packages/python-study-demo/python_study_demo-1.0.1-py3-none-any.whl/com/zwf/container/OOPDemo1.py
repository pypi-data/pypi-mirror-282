class BookInfo:
    # 限定私有属性
    __slots__ = ('__title', '__author', '__year')

    # 构造函数
    def __init__(self,title,author,year):
        self.__title = title
        self.__author = author
        self.__year = year

    # 进行对象析构操作
    def __del__(self):
        print("对象进行GC之前进行的操作！一般用于资源的关闭操作")



    def set_title(self,title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_year(self,year):
        self.__year = year

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year


def main():
    book = BookInfo('python开发实战', '小李', 20)
   # 由于slots插槽的限制，不能在外部对属性进行拓展
   # book.age = 100
    print('书名:', book.get_title(),'作者:', book.get_author(), '年限:', book.get_year())
   # 由于属性名加了前缀__ 表示私有化 外部不能直接访问
   # print(book.__year)
    del book   # 回收对象
if __name__ == '__main__':
    main()