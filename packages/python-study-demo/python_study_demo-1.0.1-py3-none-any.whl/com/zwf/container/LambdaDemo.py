# 编写Lambda表达式
def main():
    operation = lambda x, y: x+y
    print(operation(1,2))

    # 定义一个可变参数进行相加
    total = lambda *args: sum(args)
    print(total(1, 2, 3, 4, 5, 6, 7, 8, 9))

    # 编写一个递归累加
    recular = lambda x : 1 if x==1 else x*recular(x-1)
    acculate = lambda y: 1 if y==1 else acculate(y-1)+recular(y)
    print('1!+2!+3!=',acculate(3))

    # 编写一个序列排序
    lst = [1, 2, 3, 4, 56, 7, 8, 9, 10, 12, 14, 15, 16]
    # 列表排序
    sort_list = sorted(lst, key=lambda x: x)
    print(sort_list)

    # 列表过滤出偶数
    digster = list(filter(lambda x: x % 2 == 0, lst))
    print(digster)

    # 数据整体翻倍
    reserver = list(map(lambda x: x*2, lst))
    print(reserver)

    # 列表倒叙
    res = sorted(lst, key=lambda x:-x)
    print(res)

    # 字典倒叙排列
    dic = dict(java=10, go=30, c=20, python=50, mysql=70)
    # dic.items()遍历字典
    dic_res = sorted(dic.items(), key=lambda x: -x[1])
    print(dic_res)




if __name__ == '__main__':
    main()