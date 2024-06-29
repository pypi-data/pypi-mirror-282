# 数据格式化输出
if __name__ == '__main__':
    name = '李兴华'
    bookName = '《python从入门到实战》'
    price = 39.1278
    print(f'[作者:]{name};[图书名称:]{bookName};[图书价格:]%{price}')
    print('价格的四舍五入：%5.2f'%price)  # 自动四舍五入对数据进行处理
    print('价格的特定格式处理：%+010.2f'%price)
    print('价格的特定格式处理：%+10.2f' % price)
    # 对字符串进行处理
    name = '动物'
    skill = '吃食物'
    fs = '名称:{},技能:{}'.format(name, skill)
    print(fs)
    fs = '名称:{0},技能:{1}'.format(name, skill)
    print(fs)
    fs = '主键:{id},名称:{name}'.format(id=109092, name='zhangsan')
    print(fs)
    # 通过列表和字典传输数据
    arr = ['one', 'two', 'three', 'four', 'five']
    print('取列表中第一个元素:{s[0]}'.format(s=arr))
    print(f'取列表中第一个元素:{arr[0]}')
    # 打印字典的值
    dict_data = {'name':'张三', 'age':'78', 'skill':'A'}
    print('提取字典中的第一个value值:{name}'.format(**dict_data))
    print(f'提取字典中的第一个value值:{dict_data['name']}')
    # 编码转换
    base_code = 'sasdsasa'
    print('unicode编码=>{comp!a}'.format(comp = 'sasdsasa'))
    digist = 10086
    print(f'转为二进制数是=>{digist:b}')
    print(f'转为八进制数是=>{digist:o}')
    print(f'转为十六进制数是=>{digist:x}')
    # 数据分割
    msg = '李兴华,python'
    num = 91528763567267.2453562776275673527
    num_a= 915
    print(f'[数据居中]{msg:^30}')
    print(f'[数据填充]{msg:=^30}')
    print(f'[数据对齐]{num_a:>30}')
    print(f'[数据分割]{num:>30,}')
    # 保留两位数并用科学计数法显示
    print(f'[数据精度]{num:.2}')