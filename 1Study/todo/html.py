# -*- coding: utf-8 -*-
# @Time : 2021/9/6 17:03
# @Author : aupersu
# @File : get_mail_html.py
import sys
import os
# 参数:标题
headline = sys.argv[1]
# headline='test'
# 参数:格式json
# 示例:'["产品号","缺失九要素客户数",{"职业or地址":[{"异常": ["地址异常","职业缺失","职业or地址缺失"]},"职业or地址已管控"]},{"不动户":["客户数","不动户已管控"]}]'
json_arg = sys.argv[2]

# 参数:sql跑数的地址
file = sys.argv[3]
# file = 'sample.txt'

# 参数: 1: 无背景填充 2：全背景填充 3：交叉背景填充
fill_type = sys.argv[4]

# 参数: 表格字段名注释
desc_mess = sys.argv[5]

# 参数: html目标文件
result_file = sys.argv[6]


if not os.path.exists(result_file):
    os.system(r"touch %s"%result_file)

#如果数据为空,退出程序
print('source data size',os.path.getsize(file))
if os.path.getsize(file) == 0:
    sys.exit(0)


col_lv_list = eval(json_arg)
col_lv1_list = []
col_lv2_list = []
col_lv3_list = []
col_dict = {}

def ft(arg, level=1):
    if type(arg) == type('str'):
        col_dict[arg] = level
    else:
        for child_key in arg:
            child_value = arg[child_key]
            col_dict[child_key] = level
            level = level + 1
            for child_arg in child_value:
                ft(child_arg, level)

for col_lv1 in col_lv_list:
    ft(col_lv1)

level_flag = max(col_dict.values())
# print(level_flag)

for col_lv1 in col_lv_list:
    if type(col_lv1) == type('str'):
        # print("一级标题:", col_lv1)
        col_lv1_list.append('<th class="h0" rowspan="' + str(level_flag) + '" colspan="1" >' + col_lv1 + '</th>')
    else:
        for col_lv1_d in col_lv1:
            # print("一级标题", col_lv1_d)
            lv1_child_cnt = 0
            for col_lv2 in col_lv1[col_lv1_d]:
                if type(col_lv2) == type('str'):
                    lv1_child_cnt = lv1_child_cnt + 1
                    # print("二级标题:", col_lv2)
                    col_lv2_list.append(
                        '<th class="h0" rowspan="' + str(level_flag - 1) + '" colspan="1" >' + col_lv2 + '</th>')
                else:
                    for col_lv2_d in col_lv2:
                        # print("二级标题", col_lv2_d)
                        lv2_child_cnt = 0
                        for col_lv3 in col_lv2[col_lv2_d]:
                            lv1_child_cnt = lv1_child_cnt + 1
                            lv2_child_cnt = lv2_child_cnt + 1
                            if type(col_lv3) == type('str'):
                                # print("三级标题:", col_lv3)
                                col_lv3_list.append('<th class="h0">' + col_lv3 + '</th>')
                        col_lv2_list.append(
                            '<th class="h0" rowspan="1" colspan="' + str(lv2_child_cnt) + '" >' + col_lv2_d + '</th>')
            col_lv1_list.append(
                '<th class="h0" rowspan="1" colspan="' + str(lv1_child_cnt) + '" >' + col_lv1_d + '</th>')

html_mess = '''<!DOCTYPE html>
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style>
span {
    font-size:8.0pt;
    font-family:微软雅黑, sans-serif;
    font-style:italic;
    }
.divh{width:3px; height:3px}
.t0 {text-align:left;
    vertical-align:middle;
    color:#000000;
    font-size:15.0pt;
    font-weight:1200;
    font-family:微软雅黑, sans-serif;
    border-left:.5pt solid #FFFFFF;
    border-right:.5pt solid #FFFFFF;
    padding-left:3pt;
    padding-right:3pt;
    padding-top:5pt;
    padding-bottom:5pt;
    }
.h1 {text-align:left;
    vertical-align:middle;
    color:#000000;
    font-size:12.0pt;
    font-weight:800;
    font-family:微软雅黑, sans-serif;
    border-left:.5pt solid #FFFFFF;
    border-right:.5pt solid #FFFFFF;
    padding-left:3pt;
    padding-right:3pt;
    padding-top:5pt;
    padding-bottom:5pt;
    }
.h0 {text-align:center;
    vertical-align:middle;
    background:#275FAC;
    color:#FFFFFF;
    font-size:11.0pt;
    font-weight:700;
    font-family:微软雅黑, sans-serif;
    border-left:.5pt solid #BDBDBD;
    border-right:.5pt solid #BDBDBD;
    border-top:.5pt solid #BDBDBD;
    border-bottom:.5pt solid #BDBDBD;
    padding-left:3pt;
    padding-right:3pt;
    padding-top:4pt;
    padding-bottom:4pt;
    width:120px;
    height:30px;
    }
.l1 {text-align:left;
    vertical-align:middle;
    font-size:11.0pt;
    font-family:微软雅黑, sans-serif;
    border:.5pt solid #BDBDBD;
    padding-left:3pt;
    padding-right:3pt;
    padding-top:4pt;
    padding-bottom:4pt;}
.l2 {text-align:left;
     vertical-align:middle;
     font-size:11.0pt;
     font-family:微软雅黑, sans-serif;
     border:.5pt solid #BDBDBD;
     background:#F2F2F2;
     padding-left:3pt;
     padding-right:3pt;
    padding-top:4pt;
    padding-bottom:4pt;}
.r1 {text-align:right;
    vertical-align:middle;
    font-size:11.0pt;
    font-family:微软雅黑, sans-serif;
    border:.5pt solid #BDBDBD;
    padding-left:3pt;
    padding-right:3pt;
    padding-top:4pt;
    padding-bottom:4pt;}
.r2 {text-align:right;
     vertical-align:middle;
     font-size:11.0pt;
     font-family:微软雅黑, sans-serif;
     border:.5pt solid #BDBDBD;
     background:#F2F2F2;
     padding-left:3pt;
     padding-right:3pt;
    padding-top:4pt;
    padding-bottom:4pt;}
.c1 {text-align:center;
    vertical-align:middle;
    font-size:11.0pt;
    font-family:微软雅黑, sans-serif;
    border:.5pt solid #BDBDBD;
    padding-left:3pt;
    padding-right:3pt;
    padding-top:4pt;
    padding-bottom:4pt;}
.c2 {text-align:center;
     vertical-align:middle;
     font-size:11.0pt;
     font-family:微软雅黑, sans-serif;
     border:.5pt solid #BDBDBD;
     background:#F2F2F2;
     padding-left:3pt;
     padding-right:3pt;
     padding-top:4pt;
     padding-bottom:4pt;}
.r0 {text-align:right;
    vertical-align:bottom;
    color:#000000;
    font-size:8.0pt;
    font-family:微软雅黑, sans-serif;
    border-left:.5pt solid #FFFFFF;
    border-right:.5pt solid #FFFFFF;
    padding-left:3pt;
    padding-right:1pt;
    padding-top:4pt;
    padding-bottom:1pt;}
</style>
</head>
<body>
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
<tr>
<th class=\"h1\" colspan=\"10\" >''' + headline + '''</th>
</tr>
<tr>\n'''

for i in col_lv1_list:
    html_mess = html_mess + i + '\n'
if level_flag >= 2:
    html_mess = html_mess + '</tr>\n<tr>\n'
    for j in col_lv2_list:
        html_mess = html_mess + j + '\n'
if level_flag == 3:
    html_mess = html_mess + '</tr>\n<tr>\n'
    for k in col_lv3_list:
        html_mess = html_mess + k + '\n'

html_mess = html_mess + '</tr>\n'


line_flag = 0
data_file = open(file)
for line in data_file:
    html_mess = html_mess + '<tr>\n'
    line_flag = line_flag + 1
    col_flag = 0
    if fill_type == '1':
        for i in line.split('\t'):
            col_flag = col_flag + 1
            if col_flag == 1:
                html_mess = html_mess + "<th class=\"l1\">%s</th>\n" % i
            else:
                html_mess = html_mess + "<th class=\"r1\">%s</th>\n" % i
    if fill_type == '2':
        for i in line.split('\t'):
            col_flag = col_flag + 1
            if col_flag == 1:
                html_mess = html_mess + "<th class=\"l2\">%s</th>\n" % i
            else:
                html_mess = html_mess + "<th class=\"r2\">%s</th>\n" % i
    elif fill_type == '3' and line_flag % 2 > 0:
        for i in line.split('\t'):
            col_flag = col_flag + 1
            if col_flag == 1:
                html_mess = html_mess + "<th class=\"l1\">%s</th>\n" % i
            else:
                html_mess = html_mess + "<th class=\"r1\">%s</th>\n" % i
    elif fill_type == '3' and line_flag % 2 == 0:
        for i in line.split('\t'):
            col_flag = col_flag + 1
            if col_flag == 1:
                html_mess = html_mess + "<th class=\"l2\">%s</th>\n" % i
            else:
                html_mess = html_mess + "<th class=\"r2\">%s</th>\n" % i

    html_mess = html_mess + '</tr>\n'

html_mess = html_mess + '</table>\n<font color="#FF0000">%s</font>\n</body>\n</html>'%desc_mess

#print(html_mess)

with open(result_file,'w') as file_object:
    file_object.write(html_mess)
file_object.close()