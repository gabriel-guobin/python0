# -*- coding: utf-8 -*-
from sys import argv #把sys模组import进来；argv 是所谓的参数变量(argument variable)
#将argv“解包(unpack)”,将每个参数赋予一个变量名:script,user_name 将所有的参数以此赋予左边的变量名
script,user_name = argv
prompt = 'What do you think :' # 为 raw_input 中在屏幕上的提示设定变量，以简化代码

print "Hi %s,I'm the %s script." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) #通过打印在屏幕上的prompt变量的值提示用户输入，将得到的值赋予likes

print "Where do you live %s?" % user_name
lives = raw_input (prompt) #通过打印在屏幕上的prompt变量的值提示用户输入，将得到的值赋予lives

print "What kind of computer do you have?"
computer = raw_input(prompt) #通过打印在屏幕上的prompt变量的值提示用户输入，将得到的值赋予computer
#打印一段话，用格式话字符 %r 指向比变量数组（likes,lives,computer)
print """
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes,lives,computer)
