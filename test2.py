"""
 * Project name(项目名称)：Python迭代器
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:10
 * Version(版本): 1.0
 * Description(描述)： 迭代器实现字符串的逆序输出
 """


class Reverse:
    def __init__(self, string):
        self.__string = string
        self.__index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__string[self.__index]


if __name__ == '__main__':
    reverse = Reverse('Python')
    for c in reverse:
        print(c, end="")
    print()
    reverse = Reverse('hello world')
    for c in reverse:
        print(c, end="")
