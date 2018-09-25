# -*-coding: utf-8 -*-

"""
   创建一个原型方法，通过对传入的对象做深拷贝，
   并且通过内部的更改对象属性的方法来使原始传入的对象的副本进行加工，
   最终在原始对象的原型的基础上得到新的对象

"""

import copy
from collections import OrderedDict


class Book(object):

    def __init__(self, name, authors, price, **rest):
        """rest的例子有：出版商，长度、标签、出版日期"""
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append("{}: {}".format(i, ordered[i]))
            if i == 'price':
                mylist.append("\n")
        return ''.join(mylist)


class Prototype(object):
    """此类实现了原型方法，核心是 clone() 方法,该方法使用我们熟悉的 copy.deepcopy() 函数来完成真正的克隆工作
    但是此类在支持克隆之外还做了一些更多的事情，它包含了方法 register()和unregister()，用于在一个字典中
    追踪被克隆的对象，这只是一个方便之举，并不是所有的都必须实现"""
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('错误属性 {} '.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book(name='The C Programming Language', authors=('Brian W. Kernighan', 'Dennis M.Ritchie'), price=118,
              publisher='Prentice Hall',
              length=228, publication_date='1978-02-22', tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    print('ID b1 : {} != ID b2 : {}'.format(id(b1), id(b2)))


if __name__ == '__main__':
    main()
