# -*- coding: utf-8 -*-
from sys import argv #把 sys模组 import 进来，argv 是所谓的参数变量（argument variable )

script,filename = argv # 将 argv 解包 unpack, 输入脚本名和要打开的文件名

print "We're going to erase %r."% filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?") # 在屏幕上提示？ 获取用户的输入值

print "Opening the file..."
target = open(filename,'w')  # 设定变量 target 的动作：以写入模式打开文件 filename 
print "Truncating the file. Goobye!"
target.truncate()  # 执行变量target的动作，并执行truncate命令，抹掉 filename文件的内容

print "Now I'm going to ask you for three lines."

# 设定三个变量，用raw_input 提示用户输入三次字符串，并将这三组字符串赋值给这三个变量 
line1 = raw_input("line 1: ") 
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# 执行变量target的动作（以写入模式打开filename文件），并执行write命令，写入write( ) 括号内的内容
target.write(line1)
target.write("\n") # 在line1 句后写入 转义字符 \n 执行换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."
target.close() # 执行变量target的动作（以写入模式打开filename文件），并执行close（）命令，关闭filename文档
