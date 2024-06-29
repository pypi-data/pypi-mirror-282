class Person:
    __slots__ =('__name', '__age', '__university', '__address')

   # 公共熟悉不受插槽影响

    __prop = '人类'

    def set_prop(prop):
        Person.__prop = prop

    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__age = kwargs.get('age')
        self.__university = kwargs.get('university')
        self.__address = kwargs.get('address')

    def get(self):
        return self.__name, self.__age, self.__university, self.__address, self.__prop


def main():
    person0 = Person(name='肖总', age= 26, university='深大', address='广东深圳')
    person1 = Person(name='肖总1', age= 28, university='深大', address='广东深圳')
    person2 = Person(name='肖总2', age= 30, university='深大', address='广东深圳')

    print(person0.get())
    print(person1.get())
    print(person2.get())


if __name__ == '__main__':
    main()