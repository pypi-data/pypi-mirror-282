# 格式化输出
year = 2024
month = 2
day = 2
weekday = "一"
tempoary = 15.4
# %s字符串 %f浮点型  %d整型 %02d 显示两位数据 不足的位数用0表示
print("格式化字符串 %d " %(year))
print("今天是 %d 年 %02d 月 %02d 日,星期%s,今天的天气 晴,气温 %f 度"%(year,month,day,weekday,tempoary))