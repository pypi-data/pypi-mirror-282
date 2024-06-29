def main():
    # set序列一般用于集合运算和元素去重
    element_1 = set(['java','python','javascript','c++'])
    element_2 = set(['javascript','c++'])
    print('集合交集：', element_1.intersection(element_2))
    print('集合并集：', element_1.union(element_2))
    print('集合差集：', element_1.difference(element_2))
    print('集合差集', element_2.symmetric_difference(element_1))

if __name__ == '__main__':
    main()
