# 定义一个列表
skill = ['python', 'mysql', 'json', 'scrapy爬虫','Node.JS']
# append()函数的名称为追加，追加的概念指的是在已有列表的尾部添加内容
skill.append('linux') # 在列表尾部追加数据
# 列表也属于序列的一种，因此所有的数据都有索引数值
skill.insert(0,'c语言')
print('获取列表的全部数据',skill)
print('获取指定索引数据，索引为0',skill[0])
print('列表数据的分片操作',skill[0 : 2 : 1])
# 字符串拼接
print(', '.join(skill))
# 列表中的数据删除时，是区分大小写的，因此如果没有匹配成功，则无法删除，会直接报错。
print('"remove()"函数删除数据',skill.remove('Node.JS'))
print('"remove()"函数删除之后的列表',skill)
# pop()在弹出的时候是依据索引的编号实现数据的获取的
print('"pop()"弹出之后的列表集合：',skill.pop(5))
print('"pop()"弹出之后的列表集合',skill)
# 在列表之中使用"+"表示的是列表的连接操作，即：若干个不同的列表变为一个完整列表
skill = ['python']*3 + ['java']*5  #定义拼接一个列表
print(skill)
# 拷贝函数
a = ['java','python','c','c#']
b = a.copy()
print(id(a))  # a堆内存地址值
print(id(b))  # b堆内存地址值
# 集合字符串的拼接
c = ['java','python','c','c#','javascript']
print(c)
# 对已有列表的功能进行拓展，等于"+"的功能，将新的数据添加到已有的列表内容之后
c.extend(['Node.JS','Java','Python','C','C++'])
print("拓展后的列表:",c)
print('查找元素的索引值：',c.index('java'))
# 元素排序
srt=[3,5,32,56,7,2,34,5,6]
srt_sort = srt.sort()  # 在原来的集合堆内存地址位置进行排序
print('集合排序后的值：',id(srt_sort),'值为：',srt_sort)
print('集合排序后的值：',id(srt),'值为：',srt)
# 元素排序反转
srt.reverse()
print('集合反转后的值：',srt)