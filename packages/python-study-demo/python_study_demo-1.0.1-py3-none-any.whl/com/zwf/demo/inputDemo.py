# input()的使用 你输入的任何内容都可以看成字符串
# a = input("请输入你的姓名：")
# # 类型转换 转为int类型
# a = int(a)
# print(a,type(a))
# # 整型加减乘除
# print(a+100)
# 生日输入
# age=input('请输入你的年龄:')
# birth=2024-int(age)
# print('你出生于',birth)

# 请输入两个值(key和value) 保存到字典中
# ky = input('请输入key的值:')
# vl = input('请输入value值:')
# dict_data={}
# dict_data.update({ky:vl})
# print("请输入的字典值是:"+dict_data.__str__())
# # 设置弹出的key
# pop_data = dict_data.pop(ky)
# print('弹出的值是：', pop_data)
# print('弹出后的字典值 ', dict_data)

# 请判断是否有值输入
flag = bool(input('请输入数据？'))
print('是否输入数据=>', flag.__str__())

# 判断数据是否存在  0表示false  非0表示true
flag_v = bool(int(input('请输入数据？')))
print('布尔类型：'+str(type(flag_v))+'、内容' + flag_v.__str__())



