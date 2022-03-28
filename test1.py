"""
 * Project name(项目名称)：Python迭代器
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:00
 * Version(版本): 1.0
 * Description(描述)：
 __next__(self)：返回容器的下一个元素。
__iter__(self)：该方法返回一个迭代器（iterator）。
 """


class List:
    def __init__(self):
        self.__date = []
        self.__step = 0

    def __next__(self):
        if self.__step <= 0:
            raise StopIteration
        self.__step -= 1
        # 返回下一个元素
        return self.__date[self.__step]

    def __iter__(self):
        # 实例对象本身就是迭代器对象，因此直接返回 self 即可
        return self

    # 添加元素
    def __setitem__(self, key, value):
        self.__date.insert(key, value)
        self.__step += 1


if __name__ == '__main__':
    l = List()
    l[0] = 1
    l[1] = 2
    l[2] = 3
    l[3] = 4
    l[2] = 5
    for i in l:
        print(i)
    l = List()
    l[0] = 1
    l[1] = 2
    l[2] = 3
    l[3] = 4
    l[2] = 5
    print("---")
    print(l.__next__())
    print(l.__next__())
    print(l.__next__())
    print(l.__next__())
    print(l.__next__())
