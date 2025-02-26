import re

"""
python里面数量默认是贪婪的(在少数语言里面可能是非贪婪的)  总是尝试匹配尽可能多的字符
非贪婪则相反  总是尝试匹配尽可能少的字符
如果想将贪婪模式变成非贪婪模式 则需要加?

re.sub(parttern, '新的内容', str)  表示用新的内容替换str
re.split(parttern,str)  切分

正则预定义:
\A：表示从字符串的开始处匹配 不能匹配换行符
\Z：表示从字符串的结束处匹配，如果存在换行，只匹配到换行签前的结束字符串
\b：匹配一个单词边界，也就是指单词和空格间的位置，例如'py\b'可以匹配'python'中的'py' 但是不能匹配'openpyxl'中的'py'
\B：匹配非单词边界 'py\b'可以匹配'openpyxl'中的'py' 但是不能匹配'python'中的'py' 
\d: 匹配任意数字 等价于[0-9]
\D: 匹配任意非数字字符 等价于[^\d]
\s: 匹配任意空白字符,等价于[\t\n\r\f]
\S: 匹配任意非空白字符，等价于[^\s]
\w: 匹配任意字母数字以及下划线 等价于[a-z A-Z 0-9 _]
\W：匹配任意非字母数字以及下划线 等价于[^\w]
\\: 匹配愿意的反斜杠

量词:
'.' 用于匹配除了换行符(\n)之外的所有字符
'^' 用于匹配字符串的开始 既行首
'$' 用于匹配字符串的末尾(末尾如果有换行符\n 就匹配\n前面的那个字符)，既行尾

定义正则验证次数
'*' 用于将前面的模式匹配0次或者多次(贪婪模式 即尽可能多的匹配)  >=0
'+' 用于将前面的模式匹配1次或者多次(贪婪模式)   >=1
'?' 用于将前面的模式匹配0次或者1次(贪婪模式)    1,0
'*?,=?,??' 即上面三种特殊字符的非贪婪模式(尽可能少的匹配)
'{m,n}' 用于将前面的模式匹配m次或者n次(贪婪模式)，既最小匹配m次 最大匹配n次,n可以不写就是多次
'{m,n}?' 即上面'{m,n}'的非贪婪模式
'\\' '\'是转义字符 在特殊字符前面加上\ 特殊字符就失去了所代表的含义 比如\+就仅仅代表了加了+本身
'[]' 用于表示一组字符，如果^是第一个字符，则表示的是一个补集，比如[0-9]代表所有的数字，[^0-9]表示除了数字外的字符
'|' 比如A|B用于匹配A或者B
'(...)' 用于匹配括号中的模式 可以在字符串中检索或者匹配我们所需要的内容
"""

# lit = re.findall(r"\d+", "我的电话是:10086, 我女友的电话是:10010")
# print(lit)
#
# # finditer: 返回迭代器  group()方法返回内容
# it = re.finditer(r"\d+", "我的电话是:10086, 我女友的电话是:10010")
# for i in it:
#     print(i.group())


# search返回的是match对象 找到一个结果就返回
# s = re.search(r"\d+", "我的电话是:10086, 我女友的电话是:10010")
# print(s.group())

# 从头开始匹配
# s = re.match(r"\d+", "我的电话是:10086, 我女友的电话是:10010")
# print(s.group())

# 预加载正则表达式
# re_compile = re.compile(r"\d+")
#
# lit = re_compile.findall("我的电话是:10086, 我女友的电话是:10010")
#
# print(lit)

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋体</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""


# (?P<id>.*?)
obj = re.compile(r"<div class='(?P<el>.*?)'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S)  # re.S让点能匹配换行符
result = obj.finditer(s)

for it in result:
    print(it.group("wahaha"))
    print(it.group("id"))
    print(it.group("el"))
