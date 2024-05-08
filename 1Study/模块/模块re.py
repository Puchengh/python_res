import re

"""
python里面数量默认是贪婪的(在少数语言里面可能是非贪婪的)  总是尝试匹配尽可能多的字符
非贪婪则相反  总是尝试匹配尽可能少的字符
如果想将贪婪模式变成非贪婪模式 则需要加？


re.sub(parttern, '新的内容', str)  表示用新的内容替换str
re.split(parttern,str)  切分

正则预定义:
\A：表示从字符串的开始处匹配
\Z：表示从字符串的结束处匹配，如果存在换行，只匹配到换行签前的结束字符串
\b：匹配一个单词边界，也就是指单词和空格间的位置，例如'py\b'可以匹配'python'中的'py' 但是不能匹配'openpyxl'中的'py'
\B：匹配非单词边界 'py\b'可以匹配'openpyxl'中的'py' 但是不能匹配'python'中的'py' 
\d: 匹配任意数据 等价于[0-9]
\D: 匹配任意非数据字符 等价于[^\d]
\s: 匹配任意空白字符,等价于[\t\n\r\f]
\S: 匹配任意非空白字符，等价于[^\s]
\w: 匹配任意字母数据以及下划线 等价于[a-zA-Z0-9_]
\W：匹配任意非字母数字以及下划线 等价于[^\w]
\\: 匹配愿意的反斜杠 \

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

# msg = '佟丽娅娜扎热巴戴斯佟丽娅'
#
# pattern = re.compile('佟丽娅')
#
# print(pattern.match(msg))  # 当没有匹配的时候就会返回None 从头开始匹配
#
# # 使用正则表达是re模块
# s = '娜扎热巴戴斯佟丽娅'
# ss = re.match('佟丽娅',s)
# print(ss)
#
# sss = re.search('佟丽娅',s)  # search进行正则字符串匹配方法  匹配的是
# print(sss.span())
#
# print(sss.groups())
# print(sss.group())  #使用group提取匹配带的内容


# s = '哈哈7i'
# result = re.search('[0-9][a-z]',s)
# if result is not None:
#     print(result.group())

# a2b h6k
# msg = 'abcddasdfjkalsdf21asdf1dsdf'
# # sss = re.search('[a-z][0-9][a-z]',msg)  # 只要匹配到就返回，只要找到一个就会停止
# sss = re.findall('[a-z][0-9][a-z]',msg)  # 找到所有的,返回的是一个列表
# print(sss)


# # a7aasdf88dasf787asd
# msg = 'a7aasdf88dasf787asd'
#
# result = re.findall('[a-z][0-9]+[a-z]',msg)
# print(result)
#
#
# # qq号码验证 开头不能是0
# qq = '1234567895'
# result = re.match('^[1-9][0-9]{4,}10$',qq)
# print(result)
#
# # 用户名可以是字母或者数字  不能是数字开头 用户名必须是6为以上 [0-9a-zA-Z]
# username = 'a001admin'
# result = re.match('^[a-zA-Z]\w{5,}$',username)  # 需要验证整体的用户名
# print(result)
#
# msg = 'aa*.py ab.txt bb.py kk.png'
# result = re.findall(r'\w*\.py\b',msg)
# print(result)



'''
| 或者
'''
# 分组 匹配数组0-100数字
n = '100'
# reslut = re.match(r'[1-9]?\d*',n)
reslut = re.match(r'^[1-9]?\d?$|100$',n)

print(reslut)

# 验证数据的邮箱 163 126 qq
#(word|word1|word2)  区别 [abc] 表示的一个字母而不是一个单词
email = '740945380@qq.com'
reslut = re.match(r'\w{5,20}@(163|126|qq)\.com$',email)
print(reslut)


# 不是以4 7结尾的手机号码(11位)
phone = '15901018869'
result = re.match(r'1\d{9}[0-35-68-9]$',phone)
print(result)


# 爬虫提取
phone = '010-12345678'

result = re.match(r'(\d{3}|\d{4})-(\d{8})$',phone)
print(result)
# 分别提取数据
# ()表示分组  group(1)表是提取第一组的内容 group(2表是提取第二组的内容
print(result.group())   #010-12345678
print(result.group(1))  #010
print(result.group(2))  #12345678


msg = '<html>abc</html>'
msg1 = '<h1>hello</h1>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>',msg)
print(result)
print(result.group(1))

#标签要成对匹配 不然表示不成功 \1表是引用第一组的内容
msg2 = '<html><h1>hello</h1>'
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg1)
print(result)
print(result.group(1))  #h1
print(result.group(2))  #hello


msg2 = '<html><h1>hello</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg2)
print(result)
print(result.group(1))  #html
print(result.group(2))  #h1
print(result.group(3))  #hello


msg = 'abc123abc'
result = re.match(r'abc(\d+)',msg)
print(result)  #abc123 默认是贪婪的 会拿到所有符合条件的数据