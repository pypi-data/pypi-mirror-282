# python字典定义
if __name__ == '__main__':
    base={'python':'python开发实战','go':'go开发实战','java':'java开发实战','mysql':'mysql开发实战'}
    vals=base.get('python')
    print('字典取值：',vals)
    print('获取所有的key：',base.keys())
    print('迭代器：',base.items())
    # key存在就更新值  key不存在就添加字典值
    base.update({'python':'AAAA'})
    base.update({'html': '前端语言'})
    print('更新后的字典：',base)
    print('字典的值：',base)
    print('弹出的字典值：',base.pop('python'))
    print('随机弹出一组字典：',base.popitem())
    # 判断key值是否存在
    print('vue值不存在！','vue' in base.keys())
    print('java值不存在！', 'java' in base.keys())

    dict1=dict(name=['java','go','python'],skill=('打羽毛球','打乒乓球','打桌球'),dept=('技术部','教学部','财务部','市场部'))
    print(dict1.get('name'))
    print(dict1.get('skill'))
    print(dict1.get('dept'))
    dict1.get('name').append('zwf')
    # dict1.get('skill').append('打篮球')  # 元组不能添加元素
    print(dict1)
    # 软拷贝
    dict2 = dict1.copy()
    print(id(dict2),'<====>',id(dict1))
    print(str(dict2))

    print('字典名：'+str(dict1))
