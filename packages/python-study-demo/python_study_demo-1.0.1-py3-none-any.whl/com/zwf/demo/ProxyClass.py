# 代理类
class Log:
    # 设置参数
    def __init__(self, level='INFO'):
        self.__level = level

    # 设置代理内容
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'[被代理的方法名:{func.__name__}]:参数:{args},命名参数:{kwargs}')
            return func(*args, **kwargs)
        return wrapper


class Message:
    @Log(level='DEBUG')
    def connect(self):
        print('网络连接成功！！')
        return True

    @Log()
    def echo(self, msg, **kwargs):
        return f'[网络发送消息]:{msg},发送方:{kwargs.get('person')}'


def main():
    message = Message()
    if message.connect():
        print(message.echo('你好，我是代理类！', person='小曾'))


if __name__ == '__main__':
    main()



