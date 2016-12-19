# -*- coding: utf-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
print "So,you're %r old,%r tall and %r heavy." %(age,height,weight)

# input 其实是通过 raw_input 来实现的，原理参见以下代码：
# def input (prompt)
#     return (eval(raw_input(prompt)))
