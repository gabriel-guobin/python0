# -*- coding: utf-8 -*-
# 将我的基本信息作为基础变量的值
my_name = 'Gabriel.Guo'
my_age = 33 #
my_height = 174 # mm
my_weight = 70 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

# 打印的字符串中包含变量
# 相比ex4中字符串中打印变量的方法，引入了 %s 和 %d，用来提取变量的值，
print "Let's talk about %s." % my_name
print "He's %d mm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
