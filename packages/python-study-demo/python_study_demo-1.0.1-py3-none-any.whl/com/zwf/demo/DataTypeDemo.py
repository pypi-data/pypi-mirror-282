"""
  python常见的数据类型包括：整型、浮点型、布尔型、复数型、序列结构(字符串、列表、元组、字典等集合)
  使用type()方法放回的数据类型前面有个 class 原因是数据类型的常量值会在堆内存中进行
  数据的保存 类本身就是引用传递
"""
if __name__ == '__main__':
    num_a = 99E5
    num_b = 99E6
    print(num_a+num_b)
# 定义复数,复数分为虚部和实部;
values = complex(6,3)
print(values * 2)
print(values.conjugate())  # 计算共轭复数值
# python中可以用0表示布尔类型的false 非0表示true

s1 = None
print("定义None，堆内存为None开辟一个内存空间，但是不参与计算，代表该变量临时不参加任何运算")


# 进制转换
print(bin(123))  # 求数值的二进制运算
print(oct(456))  # 求数值的八进制运算
print(hex(789))  # 求数值的十六进制运算

# 位运算 移位操作
num_c = 234
num_d = 789
print(num_c | num_d) # 或运算
print(num_c & num_d) # 与运算
print(num_c << 2) # 左移2位 就是乘以2^2次方  右移2位 就是除以2^2次方

