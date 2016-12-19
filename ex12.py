# -*- coding: utf-8 -*-
# ex12 与 ex11 在打印的内容和交互方式上，完全相同，但是输入的代码间接很多
# raw_input 呈现给使用者一个提示，获得用户输入的内容，返回给变量
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So you're %r old,%r tall and %r heavy." %(age,height,weight)
# 在 Terminal 输入 pydoc  打开 Python 内建的帮助文档
# 查阅 pydoc raw_input, open , file ,os ,sys 等含义
