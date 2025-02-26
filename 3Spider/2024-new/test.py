page = 50
url = f"https://movie.douban.com/top250?start={page}&filter="

flag = True
page = 0
while flag:
    print(page)
    page = page + 25
    if(page>226):
        flag = False