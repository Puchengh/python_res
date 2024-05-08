import os


def exec_loop(keyword):
    exec_scan_files('D:\\chenpu\\item\\BDP-Hive', keyword)
    exec_scan_files('D:\\chenpu\\item3\\daf-dm', keyword)
    exec_scan_files('D:\\chenpu\\pebble\\pebble', keyword)
    exec_scan_files('D:\\chenpu\\item2\\BDP-Hive', keyword)
    exec_scan_files('D:\\chenpu\\item4\\asset-report', keyword)


def exec_scan_files(dir_path, keyword):
    file_list = set()
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(root, file).replace('\\', '/')
            if not path.startswith('.') and not path.endswith('.zip') and not 'git' in path and os.path.isfile(path) and (path.endswith('.hql') or path.endswith('.sh')):
                if os.path.isfile(path):
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            for line in f:
                                if keyword in line:
                                    # file_list.add(os.path.basename(file))
                                    # print(path)
                                    file_list.add(path)
                    except Exception as e:
                        pass
    for files in file_list:
        print(files)

exec_loop('.wfts_core_user_account_info')



# def exec_scan_files(dir_path, keyword):
#
#     dict1={}
#     for root, dirs, files in os.walk(dir_path):
#         file_list=[]
#         for file in files:
#             path = os.path.join(root, file).replace('\\', '/')
#             if not path.startswith('.') and not path.endswith('.zip') and not 'git' in path and os.path.isfile(path):
#                 if os.path.isfile(path):
#                     try:
#                         with open(path, 'r') as f:
#                             for line in f:
#                                 if keyword in line:
#                                     file_list.append(os.path.basename(file))
#                                     print(path,dir_path + "   " + keyword + "  " + line)
#                                     file_list.append(path.replace(dir_path,''))
#                                     file_list=list(set(file_list))
#                                     print(file_list)
#                     except Exception as e:
#                         print(e)
#
#     # for line in file_list:
#     #     print(line)
#
#
# if __name__ == '__main__':
#     exec_loop('send_alert_info.sh')



