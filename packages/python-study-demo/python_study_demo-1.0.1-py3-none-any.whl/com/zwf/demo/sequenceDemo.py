if __name__ == '__main__':
 numberw = 'I am chinese boy,and I also SQL Boy!'
 print (numberw[0:18:1])
 print (numberw[-20:-1:1])

 # 定义列表
 arr = ['one','two','three','four','five','six','seven']
 print(arr[0:3:1])
 print(arr[0:4:1])
 print(arr[0:5:])
 print(arr[1::1])

 #定义字符串
 str = ('我是中国公名'\
        '我是一名IT从业者'\
        '我在北京欢迎你的到来'\
        '你在鸟巢吗？不对啊');
 str_1 = 'hello word this is Amercain!'
 print(str)
 index_str = str.find('中国公名')
 print(index_str)
 print("数据分片:"+str_1[str_1.find('hello'):str_1.find('this')+5])
 codes = 65
 print(chr(codes))

 

