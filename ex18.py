# -*- coding: utf-8 -*-
#this one is like your scripts with argv
def print_two(*args): #使用def命令创建一个名称为“print_two”的函数
    arg1,arg2 = args  # 在定义函数时，参数名`*args`与脚本的`argv`相似，用途是告诉 Python 把所有的参数带入函数中，然后需要把设定的参数作为 list 放入 args 中。
    print "arg1: %r,arg2: %r" %(arg1,arg2)

#ok,that *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
    print "arg1: %r,arg2: %r" %(arg1,arg2)
# 上述函数与第一个函数打印出的内容相同，原因为在函数中，参数不需要解包


#this just takes one argument
def print_one(arg1):
    print"arg1: %r" % arg1

#this one takes no arguments 函数中参数为空，即括号内没有任何值
def print_none():
    print "I got nothin'."  # 「？猜测不定义参数的函数，作用相当于一个变量」


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
