import requests
import os

try:
    def test(i):
        # 1.准备url
        url = "https://mooc2vod.stu.126.net/nos/hls/2019/09/18/1215127814_9fa627ccbb7e42d39670869f57a1f326_sd%d.ts" % i

        # 视频存放位置
        root = "G://picture//compose/"

        # 抓取文件起的名字
        path = root + "python%d.mp4" % i
        print(path)

        if not os.path.exists(root):
            # 如果该目录不存在就创建它
            os.mkdir(root)
        if not os.path.exists(path):
            # 获取到目标视频的所有信息
            r = requests.get(url)
            # 打印访问的状态码是否为200
            print(r.status_code)
            # 以二进制写的方式将r的二进制内容写入path
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")


    # 写一个循环方法，获取所有的视频
    # for i in range(99):
    #     test(i)  # 调用爬取视频方法
    test(1)
except:
    print("爬取失败")