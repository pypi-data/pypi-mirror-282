# 懒加载机制
def test1():
    params = yield f'ID-000000' # next()操作返回值
    print('懒加载生成的ID值:', params) # 返回send()后的结果
    yield f'ID-{params}' # 返回send()后的结果

# 委派机制
def delegate(): #代码生成器
    yield from sub_generator()

def sub_generator():
    data = yield # 等待send()传送数据
    yield 'yootk-{num:0>5}'.format(num = data * 2)
def main():
    vas = test1()
    # 迭代使用
    print('next()调用的函数值', next(vas))
    vas.send(10000)

    test=delegate()
    # 操作委派生成器
    next(test)
    # 继续执行
    result = test.send(100)
    print(result)

if __name__ == '__main__':
    main()