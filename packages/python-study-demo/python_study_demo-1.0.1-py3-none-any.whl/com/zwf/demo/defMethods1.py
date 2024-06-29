# * 表示声明命名和值 固定写法

def bookInfo(*, author, bookName):
    return f'[图书]作者:{author},图书名:{bookName},数据类型:'+str(type(author))


def main():
    print(bookInfo(author='李兴华', bookName='《python开发实战》'))


if __name__ == '__main__':
    main()


