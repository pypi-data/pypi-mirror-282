import abc
# 抛出没有覆写方法的异常
class Book:
    @abc.abstractmethod
    def look_up(self):
        raise NotImplemented('没有覆写此方法，请重写覆写此方法！')


class Programmer(Book):
    pass

if __name__ == '__main__':
    try:
        p = Programmer()
        # 没有覆写抽象 而去调用抽象方法就抛出相关异常
        print(p.look_up())
    except Exception as e:
        print(f'异常信息:{e},异常类型:{type(e)}')
    finally:
        print('最终执行的操作！！')
