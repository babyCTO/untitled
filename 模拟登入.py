import requests
from bs4 import BeautifulSoup



#建立浏览器cookie
#session=requests.session()
#获取登入网址
base_url="https://www.52pojie.cn/home.php?mod=task&do=draw&id=2"
#浏览器登入抬头数据
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "htVD_2132_saltkey=A4gjl7j6; htVD_2132_lastvisit=1582772299; __gads=ID=ffefe13a9abf1299:T=1582775910:S=ALNI_MZD5JrBRAQR6hB4FM8y-EAOW7Z_6A; BAIDU_SSP_lcr=https://www.baidu.com/link?url=0PEaawkaXToyLV6UzdxY_EYglDPfw_-pgKmQwmsHknBIl3ULjq4zUdQIPzB3QEAe&wd=&eqid=b5300a8d0003cecf000000025e5741be; Hm_lvt_46d556462595ed05e05f009cdafff31a=1582775907,1582775931,1582776769; htVD_2132_seccode=6195149.26d4fc4d67f8280df1; htVD_2132_ulastactivity=1582776784%7C0; htVD_2132_auth=fcfc510%2BYbgbpdyQBvpzL6MF99wjmotvGZulpgwFfrhzTiDht17tid5kMMg40HX83qU7HSuKKIt%2FH1RyMZ4S%2BJsKUQ; htVD_2132_lip=124.133.168.174%2C1582776784; htVD_2132_connect_is_bind=0; htVD_2132_nofavfid=1; htVD_2132_checkpm=1; htVD_2132_ttask=66375%7C20200227; htVD_2132_lastact=1582776816%09home.php%09spacecp; htVD_2132_lastcheckfeed=66375%7C1582776816; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1582776827",
    #"Host": "www.52pojie.cn",
    "Referer": "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
#pos登入数据
# data={
#     "username":"a86350703",
#     "password":"ZQa51650703"
# }
#创建登入连接
response=requests.get(base_url,headers=headers)

#获取响应信息
html=response.text
data1=BeautifulSoup(html,"lxml")
print(html)