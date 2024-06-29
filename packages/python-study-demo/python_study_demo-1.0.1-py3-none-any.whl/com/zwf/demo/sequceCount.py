# 序列统计函数  python不适合进行高并发开发
if __name__ == '__main__':
   list = ['one','two','false','four','five','six','seven','eight','nine',None]
   lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   print('获取列表的长度',len(list))
   print('获取列表的最大值',max(lst1))
   print('获取列表的最小值',min(lst1))
   print('获取列表的总和',sum(lst1))
   # 序列中有一个值为true就为true
   print('序列中有一个内容',any(list))
   # 序列中有一个值为false就为false
   print('序列中有一个内容', all(list))  # 有None值就返回false