# -*-coding: utf-8 -*-


# 原始对象创建方法
class Computer(object):
    """创建一个类，显示计算机的基本信息"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Synthesizer(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return "says hello"


# 适配器类
class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


# 主函数
def main():
    """将不同的对象实例化，并且赋予同样的接口指向对象内部不同的方法，实现统一方法不同的返回的适配器效果"""
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human("Bob")
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print("{} {}".format(str(i), i.execute()))


if __name__ == '__main__':
    main()
