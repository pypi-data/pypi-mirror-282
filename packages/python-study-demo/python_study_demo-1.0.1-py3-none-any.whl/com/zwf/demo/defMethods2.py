# 固定命名空间写法
def args(**kwarg):
    for key, value in kwarg.items():
        print(f'编程技术：{key},配套图书：{value}')

# *表示声明表示可变参数

def bookInfo(*author,bookName):
    for ite in author:
        print(ite)
    return f'[图书]作者:{author},图书名:{bookName},数据类型:'+str(type(author))


# 初始化参数默认值
def inits(name, lang='en'):
    print(f'姓名:{name},擅长的语言:{lang}')


def main():
    print(bookInfo('小李', '小王', '小曾',bookName='小王'))
    args(python='《python从入门到实战》', java='《JAVA从入门到精通》', go='《go语言从入门到实战》')
    inits("小王")


if __name__ == '__main__':
    main()


