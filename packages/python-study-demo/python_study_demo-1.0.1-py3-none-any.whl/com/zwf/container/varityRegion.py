# 全局变量
num = 10
# 更改全局变量
def update_num():
# 这样num只是局部变量 无法修改全局变量
# num = 13
# 修改全局变量值
    global num
    num = 13
    return num



def outerlate():
    count = 1
# 编写一个累加器
    def acculate():
        nonlocal count
        count += 1
        return count
    return acculate



def main():
# 调用修改方法
    update_num()
    print('全局变量:%d'%num)
# 累加器 创建闭包
    count=outerlate()
# 调用闭包
    print(count())



if __name__ == '__main__':
  main()