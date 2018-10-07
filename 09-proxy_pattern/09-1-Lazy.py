

class LazyProperty(object):
    """
    先创建一个Lazyproperty类，用作修饰器当它修饰某个特性时，LazyProperty惰性地加载特性，
    而不是立即进行。__init__方法创建两个变量，用作初始化待修饰特性的方法的别名。
    method变量是一个实际方法的别名，method_name是该方法名称的别名
    """
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        """通过重写构造方法来实现惰性加载"""
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value


class Test(object):
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        """
        使用 LazyProperty 类作为装饰器
        __get__ 方法将 resource() 方法当作一个变量，可以使用 t.resource 代替 t.resource()
        """
        print("当前的self._resource是：", self._resource)
        self._resource = tuple(range(5))  # 假设此处计算成本很大
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    print(t.resource)  # 只有第一次调用经行了初始化，第二次开始就没有再初始化了
    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
