'''
加密算法
md5 sha1 sha256 不可逆的加密方式
base64 可以双向，加密和解密
'''

import hashlib
md5 = hashlib.md5('123456'.encode('utf-8'))
print(md5.hexdigest().upper())

print(hashlib.sha1('123456'.encode('utf-8')).hexdigest().upper())

