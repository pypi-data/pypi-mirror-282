import collections

# 编写双端队列
def main():
    deq=collections.deque() #创建双端队列
    # 向右边追加元素
    deq.append('JAVA')
    deq.appendleft('C++')  #向左边边追加C++元素
    print(deq.pop())
    print(deq)

if __name__ == '__main__':
    main()