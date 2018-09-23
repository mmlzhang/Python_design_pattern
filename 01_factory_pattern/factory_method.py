# -*-coding: utf-8 -*-

import xml.etree.ElementTree as etree
import json


class JSONContainer(object):
    """加载 json 格式的数据文件"""
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parse_data(self):
        return self.data


class XMLContainer(object):
    """加载 xml 的数据文件"""
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """根据文件的不同的扩展名来选择相对应的 connector"""
    if filepath.endwith("json"):
        connector = JSONContainer
    elif filepath.endwith("xml"):
        connector = XMLContainer
    else:
        raise ValueError("Cannot connect to {}".format(filepath))
    return connector(filepath)


def connect_to(filepath):
    """对 connection_factory() 进行包装，添加异常处理"""
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    """演示如何使用工厂方法设计模式"""
    sqlite_factory = connect_to('filepath/example.sq3')

    xml_factory = connect_to('filepath/example.xml')
    xml_data = xml_factory.parse_data
    print(xml_data)

    json_factory = connect_to("filepath/example.json")
    json_data = json_factory.parse_data
    print(json_data)


if __name__ == "__main__":
    main()

