# -*- coding: utf-8 -*-
formatter = "%r %r %r %r" #格式化 %r 代表原始数据

print formatter % (1 ,2, 3, 4) # %r 格式化数字
print formatter % ("one", "two","three","four") # %r 格式化 字符串
print formatter % (True, False, False, True) # # %r 格式化关键字
print formatter % (formatter,formatter,formatter,formatter) # %r 格式化变量所指向的原始值
# %r 格式化长字符串，其中的逗号代表空格不换行
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
