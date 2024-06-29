if __name__ == '__main__':
    for item in range(101):
        print(item)

    # 打印三角形

    for i in range(1, 11):
        # 打印空格的数量 第一行打印9个空格 1个*
        for j in range(1, 10-i+1):
            print(' ', end='')

        # 打印*的数量
        for j in range(1, i+1):
            print('* ', end='')
        print('')

    # python打印三角形的做法
    triangle_line = 5 # 三角形打印总行数
    format_str = '{:^'+ str(triangle_line * 2)+'}' # 设置居中对齐和打印长度 10个空格
    for x in range(1,triangle_line + 1): # 打印5行
        print(format_str.format('* ' * x))  # 数据填充

    # 打印乘法口诀表
    a = 10
    for b in range(1, a):
        for d in range(1, b+1):
            print(b, '*', d, '=', (b*d), end='\t')
        print()

