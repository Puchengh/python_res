# 安装pandas
import pandas as aa
import pandas as pd

data = aa.read_excel('E:/study/py/python_study/3Spider/file/MOCK_DATA.xlsx')
# data['pre'] = data['email'].apply(lambda x:x.split('@')[0].strip())
# data['houzhui'] = data['email'].apply(lambda x:x.split('@')[1].strip())

# write = pd.ExcelWriter('E:/study/py/python_study/3Spider/file/temp1.xlsx')
# data.to_excel(write,sheet_name='原始数据')
# write.close()

# print(data[data['gender']=='Female'])
# print(data['gender'].unique())

#根据性别区别
# write = pd.ExcelWriter('E:/study/py/python_study/3Spider/file/temp1.xlsx')
# for i in data['gender'].unique():
#     data[data['gender']==i].to_excel(write,sheet_name=i)
# write.close()


print(data[data['gender'].str.contains('Female')])

type_list=set(z for i in data['gender'] for z in i.split(' '))
print(type_list)
type_list.remove('Agender')
print(type_list)