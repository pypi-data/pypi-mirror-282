class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # 重写hash方法生产hashcode
    def __hash__(self):
        str_value = '[图书信息]图书名:'+self.__title+',作者:'+self.__author
        return object.__hash__(str_value)

def main():
    # 相同值对象的hash码可能不同，hash码相同值对象一定相同
    book1 = Book('<<python开发实战>>', '李兴华')
    book2 = Book('<<python开发实战>>', '李兴华')
    print('第一个对象的hash码:'+hash(book1).__str__()+',第二个对象的hash码:'+hash(book2).__str__())


if __name__ == '__main__':
    main()