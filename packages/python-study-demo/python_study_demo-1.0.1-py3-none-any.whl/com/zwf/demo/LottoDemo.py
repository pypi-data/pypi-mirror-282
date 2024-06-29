import random
# 编写一个中奖系统
def main():
    # 存放中奖号码集合
    sltos=[]

    while len(sltos)!=7:
        temp_number = random.randint(1,37)  # 随机生产1~36随机数包括1,36
        sltos.append(temp_number)

    # 排序
    sltos.sort()

    # 打印中奖号码
    print(f'打印中奖号码:{sltos}')


if __name__ == '__main__':
    main()

