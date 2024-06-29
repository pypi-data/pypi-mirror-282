# 枚举类型
import enum


@enum.unique
class Weekday(enum.Enum):
    Sunday = 0  #周日
    Monday = 1  # 周一
    Tuesday = 2  # 周二
    Wednesday = 3 # 周三
    Thursday = 4  #周四
    Friday = 5   # 周五
    Saturday = 6  # 周六

def main():
    print('枚举key值:',Weekday.Friday.name)
    print('枚举key值:', Weekday.Friday.value)


if __name__ == '__main__':
    main()