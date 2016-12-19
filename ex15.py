# -*- coding: utf-8 -*-
from sys import argv #把 sys模组 import 进来，argv 是所谓的参数变量（argument variable )

script,filename = argv # 将 argv 解包 unpack, 输入脚本名和要打开的文件名

txt = open(filename) # 设定变量 txt 执行函数 open() , 打开内容为刚才输入的 filename

print "Here's your file %r:" % filename

# 执行变量 txt 设定的函数，打开 filename 文件,
# 并执行 read（）函数，读取文件内容以字符串格式返回到当前脚本打印到屏幕
print txt.read()

print "Type the filename again:"
file_again = raw_input(" > ")

txt_again = open(file_again)

print txt_again.read()
