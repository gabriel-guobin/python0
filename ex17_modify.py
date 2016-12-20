# -*- coding: utf-8 -*-
from sys import argv # 把 sys模组 import 进来，argv 是所谓的参数变量（argument variable )
from os.path import exists  # import the os module, and access this module as os.path  官方文档 https://docs.python.org/2.7/library/os.path.html
script,from_file,to_file = argv  # 将 argv 解包 unpack, 输入脚本名、复制文件名和被复制文件名

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line,how?
# in_file = open(from_file) # 源程序中，定义变量in_file 执行打开 from_file 文件
# indata = in_file.read()  # 源程序中，定义变量 indate 先执行变量in_file的动作，再执行read命令

# 以下是将源程序中两行代码改写为一行
indata = open(from_file).read()  # 定义变量 indata 的实参为 打开 from_file，然后读取 from_file

out_file = open(to_file,'w') # 定义变量 out_file 为 以写入模式打开 to_file 文件
out_file.write(indata) # 执行变量 out_file 的动作（已写入模式打开 to_file文件）,然后将实参 indate 指向的内容（打开并读取from_fiel） 写入out_file

out_file.close()

