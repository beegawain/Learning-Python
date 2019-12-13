#过滤

import re
msg='佟丽娅古力娜扎郑爽'
pattern = re.compile('佟丽娅')

result = pattern.match(msg)   #没有匹配
print(result)

#使用正则re模块方法：match

s='古力娜扎佟丽娅郑爽'
result1 = re.match('佟丽娅',s)
print(result1)

result2 = re.search('佟丽娅',s)
print(result2)

print(result2.span())   #放回位置

print(result2.group())