import re
#起名方式：(?P<名字>正则)    (?P=名字)
msg = '<html><h1>abc</h1><html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
print(result)

'''
只要有（） 就是分组，只要是分组就可以用group
'''
'''
                 总结
match
search
findall
sub(正则表达式，‘新内容’，string)  替换          
例子：re.sub(r'\d+','100','java:99')

re.split(r'[:;]','Java:99;Py:100')


'''

a=re.split(r'[:;]','Java:99;Py:100')
print(a)
