if __name__ == '__main__':
    print("helo word! ")
    age = 19
    if age > 18 or age < 20:
        print("恭喜你，成年了！")

    sum = 0
    count = 0
    while count<=100:
        sum+=count
        count+=1
    else:
        print("循环结束后的操作！")
    print(f"循环后的计算结果是:{sum}")

    # 存储20以内的能被3整除的值
    val = 0
    lst = []
    while val <= 20:
        if val % 3 == 0:
            lst.append(val)
        else:
            print('其他操作！的值', val)
        val += 1
    print('小于20能被3整除的元素有', lst)
