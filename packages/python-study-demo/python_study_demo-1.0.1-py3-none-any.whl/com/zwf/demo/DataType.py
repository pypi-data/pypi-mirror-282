class DataType:
    __slots__ = ('__title', '__type', '__price')

    def __init__(self, **kwargs):
        self.__title = kwargs.get('title')
        self.__type = kwargs.get('type')
        self.__price = kwargs.get('price')

    def __index__(self):
        return len(self.__title)

    def get_price(self):
        return self.__price/100

    def __round__(self, n=None):
        return round(self.__price, n)

    def __str__(self):
        return f'变量名:{self.__title},数据类型:{self.__type},价格:{self.__price}'

def main():
    dtype = DataType(title='python开发实战',type='字符串类型',price=7980)
    # 对象作为切片的其实位置 对字符串进行截取
    print('变量名:python开发实战,数据类型:字符串类型,价格:7980'[dtype::])
    # 对象四舍五入 保留一位小数
    print(round(dtype.get_price(),1))


if __name__ == '__main__':
   main()

