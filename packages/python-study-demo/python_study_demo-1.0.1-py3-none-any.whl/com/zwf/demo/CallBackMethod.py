class Book: # 创建图书类
    def __init__(self,** kwargs):
        self.__name = kwargs['name']
        self.__author = kwargs['author']
    # 覆写__call__(self,*args,**kwargs)方法，对象可调用
    def __call__(self, *args, **kwargs):
        return self.__str__()+f'核心内容:{args}、标记:{kwargs}'

    def __str__(self):
        return f'图书名称:{self.__name}、作者:{self.__author}'
def main():
    pass

if __name__ == '__main__':
    book = Book(name='python项目实战', author='李兴华')
    # 对象可调用
    print(book('a','b','c',type='keyword'))
    print('是否可调用：',callable(book))
    print(callable(main))  # 只写上函数名字 可调用
    print(callable(print))  # 内置函数可调用
    print(callable('hello'))  # 字符串不可调用