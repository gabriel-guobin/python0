# -*- coding: utf-8 -*-

#提示输入文件名，并将输入的文件名称返回到变量 filename
filename = raw_input(" Type the filename ")

# 设定变量 txt , 执行 open（） 函数打开 变量 filename 指向的文件
txt = open(filename)
# 执行变量 txt 指向的函数，打开文件，通过 read（）函数 读取，并将文件内容作为字符串返回脚本，打印到屏幕
print txt.read()

print txt.close()
