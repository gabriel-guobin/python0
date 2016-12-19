# -*- coding: utf-8 -*-
from sys import argv #把sys模组import进来；argv 是所谓的“参数变量(argument variable)
#将argv“解包(unpack)”,将每个参数赋予一个变量名:script,first,second,third 将所有的参数以此赋予左边的变量名
script,first,second,third = argv

print "The script is called:", script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third
