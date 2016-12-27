# -*- coding: utf-8 -*-
from sys import argv # import the sys module

script, input_file = argv # "unpacks" `argv` :Take "script"and"input_file" in argv, unpack them, and assign them to all of these variables on the left in order

def print_all(f):  # define fouction "print_all（f)"
    print f.read() # take print f and .read()

def rewind(f):    # define fouction "rewind(f)"
    f.seek(0)     # take f and .seek(0)
    
def print_a_line(line_count,f):   # define function “print_a_line(line_count,f)"
    print line_count, f.readline()  # take print line_count,and run f.readline

current_file = open(input_file)  # define verious current_file,run open(input_file)

print "First let's print the whole file:\n"

print_all(current_file) # run the function ,use "current_file" as argument,it will run print open(input_file).read()

print "Now let's rewind,kind of like a tape."

rewind(current_file) # run the function ,use "current_file" as argument,it will run open(input_file).seek(0)
# 在以上函数中，open(input_file).seek（0）的作用是将input_file打开，并且将光标重新定位到文件开头,参考https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects
print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file) 

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
