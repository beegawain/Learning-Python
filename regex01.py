import re
#[]表示一个范围，在[a-z]/[0-9]里去搜索指定内容
#.search()找到第一个就停止
#.findall()全部检索

msg = 'aa5a565yud5ad56ada'
a=re.findall('[a-z][0-9]+[a-z]',msg)   # '+'表示匹配一次或多次
print(a)

#验证QQ号
qq = '456456'
b=re.match('[1-9][0-9]{4,10}$',qq)
print(b.group())

username = '#$admin520'
c=re.search('^[a-zA-Z]\w$',username)   #\w 任意字母加数字
#注意用search时要加'^'
print(c)

msg0 = 'py ab . ad .ds py'
d = re.findall(r'py\b',msg0)
print(d)

'''
. 任意字符，除\n
^ 开头
$ 结尾
[] 范围   [a-z*&$]

正则预定义
\s 空白
\S not space
\b 边界
\d digit
\D not digit
出现 \ 就在里面加‘r’
\w word 表示[0-9a-zA-Z_]
\W [^0-9a-zA-Z_]

量词：
* >=0
+ >=1
? 0,1    [1-9]? 表示1-9可匹配也可不匹配

{m} 固定m位
{m,} >=m
{m,n}  m<= <=n
~~~~~~~~~~~~~~~~~~~~~~~~~~~
    或者关系
（163|162|qq）：整体
[a|b|c]:单个字母
~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

email = '345892679@qq.com'
e = re.match(r'^\w{5,20}@(163|162|qq)\.(com|cn)$',email)
print(e.group())
