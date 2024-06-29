# 代理函数模式
def log(level = 'INFO'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # func.__name__获取被代理函数名   args:一个元组 第一个值是对象  第二个值是参数
            # kwargs: 命名参数
            print(f'[{func.__name__}]-{level};{args};{kwargs}')
            return func(*args, **kwargs)
        return wrapper  # 返回内部函数
    return decorator  # 返回外部函数


class Message:  # 网络消息
    # 方法覆写
    @log(level='DEBUG')
    def connect(self):
        # 核心代码
        print('建立网络连接....')
        return True

    # 引用装饰器
    @log()
        #方法覆写
    def echo(self, msg,**kwargs):
        name = kwargs.get('name')
        return '[ECHO]' + msg +f',{name}'


def main():
    message = Message()
    if message.connect():
        print(message.echo('Hello I am UDP,TCP', name='xiaoZeng'))


if __name__ == '__main__':
    main()


