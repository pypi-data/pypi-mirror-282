# 元组中的元素不能被修改
if __name__ == '__main__':
    author=('李兴华','沐言优拓','出版社','北大出版社')
    print(author)
    # 元组也可以通过索引查找元素
    print('下标索引查找数据：',author[0])
    print(type(author))
    # 定义元组的时候 如果只有一个元素 要在后面加一个逗号
    # 否则得出的元素是其他数据类型
    age = (12,)
    print(type(age))
    list1=['one','two','three','four','five','six']
    t1=tuple(list1)
    # 元组放在连续内存空间 而 集合在不同的内存的碎片块
    print('列表转元素=>',t1,'数据类型=>',type(t1))
    # 字符串转元组  字符串转元组 会把每个字符拆开组成元组元素
    strs=('java程序设计,python开发实战,mysql开发实战')
    ls1=list(strs)
    tp=tuple(strs)
    print('字符串转元组=>',tp,type(tp))
    print('字符串转集合=>',ls1,type(ls1))