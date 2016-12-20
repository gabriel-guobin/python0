# -*- coding: utf-8 -*-
from sys import argv   #把 sys模组 import 进来，argv 是所谓的参数变量（argument variable )
from os.path import exists  #把 os.path模组 import 进来，使用exists来判断文件在当前路径中是否存在
script,from_file,to_file = argv #将argv解包unpack，输入脚本、要复制的文件和被覆盖的文件

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line,how?  indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata) # 使用len()函数作为实参，将文件indata的字节长度返回到语句中的格式字符
print "Does the output file exist? %r" % exists(to_file) # 使用exists()函数 判断 to_file 文件是否在当前路径，并将判断值Ture/False返回语句中的格式字符
print "Ready,hit RETURN to continue, CTRL-C to abort."

raw_input() # 无返回值函数，作用是等待客户输入任意键后开始执行下一项命令

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,all done."

out_file.close()
in_file.close()
