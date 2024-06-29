# 日期时间格式化
import datetime

def main():
    # 获取当前时间
    today= datetime.datetime.now()
    print('日期时间字符串格式化:',today.strftime('%Y-%m-%d %H:%M:%S'))
    # 日期时间运算
    print('昨天日期时间', (today+datetime.timedelta(days=-1)).strftime('%Y-%m-%d %H:%M:%S'))
    print('当前时间前120小时日期时间:', (today+datetime.timedelta(hours=-120)).strftime('%Y-%m-%d %H:%M:%S'))
    print('四个礼拜之前的时间:',(today+datetime.timedelta(weeks=-4)).strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    main()