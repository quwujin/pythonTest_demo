#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 10:29
# @Author  : Dave
# @Email   : sdlzqwj@163.com
# @File    : demo.py

# 解释鸭子类型：多个类共同实现了同一个方法，这些类就可以归为一类，他们可以共同实现同一个方法
class Duck(object):
    def say(self):
        print("i am a duck")


class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
