# 闭包
def outer_function(x, a):
    print(x, a)

    def inner_function(y, c):
        print(y, c)
        return x + y + a + c

    return inner_function


# 编写一个

def main():
    # 外部函数的传参方式
    # 创建闭包
    add_five = outer_function(5, 4)
    # 内部函数的传参方式
    # 调用闭包
    result = add_five(3, 2)
    print(result)


if __name__ == '__main__':
    main()
