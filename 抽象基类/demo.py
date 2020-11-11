#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 10:42
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : demo.py
# 定义：1.在抽象基类中设定一些方法，所有继承基类的类都需要实现这些方法
#      2.抽象基类是无法实例化的
# 场景：检查某个类是否有某种方法
from collections.abc import Sized


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['Dave1', 'Dave2'])
# 判断某个类是否有某个属性 hasattr
print(hasattr(com, '__len__'))
print(hasattr(com, '__getitem__'))
print(len(com))

# 在某些情况下需要判定某个对象的类型
isinstance(com, Sized)

# 强制子类必须实现某些方法
# 1.使用raise NotImplementedError(类似C# 虚方法)
