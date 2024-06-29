def main():
    # 单行动态字符串解析器
    statement = 'print(\'动态代码解释器\')'
    eval(statement)

    # 多行代码解释器
    lines = 'total=0\n'\
             'for i in range(4):\n'\
             '   temp=input(\'请输入数字\')\n'\
             '   total += int(temp)\n'\
            'print(total)'
    # 编译代码
    pre_code=compile(lines,'','exec')
    # 执行代码
    exec(pre_code,globals())


if __name__ == '__main__':
    main()
