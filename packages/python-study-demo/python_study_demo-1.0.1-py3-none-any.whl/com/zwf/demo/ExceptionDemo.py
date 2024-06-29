def sub(num1, num2=0):
    # num2为0 才能抛出断言异常
    assert num2!= 0 ,'被除数有误，请重新输入！'
    return num1/num2

if __name__ == '__main__':
    try:
        print(sub(10, 2))
    # 最大的异常类是 BaseException 所有的异常类一般都继承exception异常类 exception异常类继承BaseException
    except Exception as e:
        print(e)
    else:
        print('没有异常输出结果！！')
    # 不管有没异常  最终一定会执行
    finally:
        print('关闭数据库连接池')
