# 内部函数
def outer_function():
    def inner_function():
        # 内部函数的实现
        pass
    # 外部函数的实现
    inner_function()


def sum_inner(x):
    print('外部函数的和'+str(x+x))

    def sub_outer(y):
        print('内部函数的值'+str(y*3))

    sub_outer(x)


def backbag(a):
    def inner_function(b=5):
        return a*b
    return inner_function


# 主函数
def main():
    outer_function()
    sum_inner(3)
    result = backbag(23)
    print(result())


# 程序入口
if __name__ == '__main__':
    main()
