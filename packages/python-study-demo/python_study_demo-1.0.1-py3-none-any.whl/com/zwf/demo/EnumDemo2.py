import enum
# 对象作为枚举选项
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'图书信息:{self.title},作者:{self.author}'

# 定义枚举类型
class BookInfo(enum.Enum):
    PYTHON = Book('python入门到实战','python')
    JAVA = Book('JAVA入门到实战', '詹姆斯.高斯林')
    CPP = Book('c++入门到实战','c++')


def main():
    print('枚举选项的值',BookInfo.JAVA.value)
    print('枚举选项的键',BookInfo.JAVA.name)


if __name__ == '__main__':
    main()



