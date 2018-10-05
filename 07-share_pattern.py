
import random
from enum import Enum

TreeType = Enum("Tree", "apple_tree cherry_tree peach_tree")


class Tree(object):
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print("render  a tree of type {} and age {} at ({}, {})".format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30  # 年为单位
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    t4 = Tree(TreeType.cherry_tree)
    tree_counter += 1
    t5 = Tree(TreeType.cherry_tree)
    tree_counter += 1
    t6 = Tree(TreeType.apple_tree)
    tree_counter += 1

    print("树的数量：", tree_counter)
    print("真实创建的树的数量：", len(t6.pool))
    print("Tree 的 pool 属性:", tuple(t6.pool))


if __name__ == "__main__":
    main()
