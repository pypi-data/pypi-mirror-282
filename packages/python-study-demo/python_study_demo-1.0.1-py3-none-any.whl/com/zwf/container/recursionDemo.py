# 外部实现累加参数
def recu(i):
# 内部实现阶乘操作
    def innRecu(j):
        # 递归头
        if j == 1:
            return 1
        # j!
        return j*innRecu(j-1)
    if i == 1:  # 递归结束
        return innRecu(1)
        # 10!+9!+8!+7!+6!+5!+4!+3!+2!+1;
    return innRecu(i) + recu(i-1)

# 主函数
def main():
    print(recu(10))


if __name__ == '__main__':
    main()
