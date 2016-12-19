# -*- coding: utf-8 -*-

# 给变量 x 赋值为一个字符串，针对此处的变量“% 10”来说，采用 s% , d% 或者 r% 都可以
x = "There are %s types of people." % 10

# 需要先给要打印的语句中的变量赋值，如将词句移动到赋值之前，运行后显示
# NameError: name 'binary' is not defined
binary = "binary"
do_not = "don't"


# 下句把 %d 改为 %s  后，提示“ TypeError: %d format: a number is required, not str ”
# 下句把 %d 改为 %r 后，打印出的变量中包含引号：Those who knows 'binary' and those who "don't".
y = "Those who knows %s and those who %s." %(binary,do_not)

print x
print y

# 注意此句中 %r 没有加引号，但是打印后的句子自动添加了引号，%r会指向变量的原值
# 打印后的句子：I side: 'There are 10 types of people.'.
print "I side: %r." % x

# 注意此句中 %s 加了单引号，打印的句子不会自动添加引号，%s和 %d 仅用来想使用者显示
print "I also side:'%s'." % y
# I also side:'"Those who knows binary and those who don't."'.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # 为什么在句尾加一个 %r 呢？
# 关键在于 % ，打印时候可以调用 Hilartious 的值
print joke_evaluation % hilarious
# 上句相当于 print "Isn't that joke so funny?! %r " % hilarious，所以如果没有 % ，
# 就无法调用

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

# Q:What is the difference between %r and %s?
# A:Use the %r for debugging, since it displays the "raw" data of the variable,
# but the others are used for displaying to users.
# Q:What's the point of %s and %d when you can just use %r?
# A:The %r is best for debugging, and the other formats are for actually
# displaying variables to users.
