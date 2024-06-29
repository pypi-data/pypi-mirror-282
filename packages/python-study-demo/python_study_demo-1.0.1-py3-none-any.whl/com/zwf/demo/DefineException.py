# 自动异常类
class BreakDownException(Exception):

    def __init__(self,**kwargs):
        self.__msg = kwargs.get('msg')

    def __str__(self):
        return f'[异常信息]=>{self.__msg}'


class DoHomeWork:

    def __init__(self,**kwargs):
        self.__count = kwargs.get('count')

    def get_count(self):
        return self.__count
def main():
    homework = DoHomeWork(count=300)
    if homework.get_count()>=300:
        raise BreakDownException(msg='作业太多了，崩溃了，请尽快解决！')

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print('立即减少作业数量！！！！',err)
    else:
        print('作业量今天属于正常，不需要调整！')
    finally:
        print('收拾好课桌，早点睡觉，明天还要上学！！')
