#  正则表达式
import re

def main():
    # 邮箱格式字符串匹配
    pattern = r'^\w+(@)\w+\.{1}(com|cn|com.cn|gov|net)$'
    print(re.match(pattern,'1872694955@qq.com',re.I))
    print('获取匹配后的字符串索引:', re.match(pattern, '1872694955@qq.com', re.I).span())
    print('获取匹配后的字符串索引:', re.search(pattern, '1872694955@qq.com', re.I).string)


if __name__ == '__main__':
    main()