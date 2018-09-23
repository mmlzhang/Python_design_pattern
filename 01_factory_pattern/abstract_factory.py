# -*-coding: utf-8 -*-


class Frog(object):
    """青蛙类"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """和障碍的交互"""
        print('{} 青蛙遇到了 {} 和 {}'.format(self, obstacle, obstacle.action()))


class Bug(object):
    """障碍物，这里是虫子"""
    def __str__(self):
        return 'a bug'

    def acction(self):
        return 'eats it'


class FrogWorld(object):
    """青蛙的世界，创建青蛙和障碍物"""
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '-- Frog World --'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstracle):
        print("{} 术士战斗和 {} and {}".format(self, obstracle, obstracle.action()))


class Obstracle(object):
    """障碍物"""
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld(object):
    """创建术士的场景"""
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "-- 术士的世界 --"

    def make_charcater(self):
        return Wizard(self.player_name)

    def make_obstracle(self):
        return Obstracle()


class GameEnvironment(object):
    """游戏环境"""
    def __init__(self, factory):
        self.hero = factory.make_charcater()
        self.obscale = factory.make_obstracle()

    def play(self):
        self.hero.interact_with(self.obscale)


def Validate_age(name):
    """提示用户提供一个有效的年龄，如果年龄无效返回一个元组，第一个值是False，
                              如果年龄有效返回一个元组，第一个值是True"""
    try:
        age = input("Welcome {}, How old are you?".format(name))
        age = int(age)
    except ValueError as ve:
        print("输入格式有误！")
        return (False, age)
    return (True, age)


def main():
    """用户输入姓名和年龄，更具用户的年龄来决定用户适合玩哪个游戏"""
    name = input("Hello, What's your name!")
    valid_input = False
    while not valid_input:
        valid_input, age = valid_input(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
