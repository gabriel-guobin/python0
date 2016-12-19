# -*- coding: utf-8 -*-
cars = 100  # 给变量赋值 整数
space_in_a_car = 4.0 # 给变量赋值 浮点数
drivers = 30 # 给变量赋值 整数
passengers = 90 # 给变量赋值 整数

# 为变量设定公式（与基本的赋值变量的关系），在基本变量的数值变化后也没有影响
cars_not_driven = cars - drivers # 设定新变量为两个变量的差
cars_driven = drivers  ## 给新变量赋值 指向另一个变量
carpool_capacity = cars_driven * space_in_a_car # 给变量赋值为两个变量的乘机
average_passengers_per_car = passengers / cars_driven # 给变量赋值为两个变量的商

# 在打印的内容中插入固定的字符串，以及特定的变量
print "There are", cars, "cars available."
print "There are only",drivers,"drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
