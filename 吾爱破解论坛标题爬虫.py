import requests
import re
#创建一个回话
#session=requests.Session()
#获取地址
base_url="http://www.52pojie.cn/forum.php?mod=forumdisplay&fid=16&amp;filter=typeid&amp;typeid=232"
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "__htVD_2132_saltkey=A4gjl7j6; htVD_2132_lastvisit=1582772299; __gads=ID=ffefe13a9abf1299:T=1582775910:S=ALNI_MZD5JrBRAQR6hB4FM8y-EAOW7Z_6A; BAIDU_SSP_lcr=https://www.baidu.com/link?url=0PEaawkaXToyLV6UzdxY_EYglDPfw_-pgKmQwmsHknBIl3ULjq4zUdQIPzB3QEAe&wd=&eqid=b5300a8d0003cecf000000025e5741be; Hm_lvt_46d556462595ed05e05f009cdafff31a=1582775907,1582775931,1582776769; htVD_2132_seccode=6195149.26d4fc4d67f8280df1; htVD_2132_ulastactivity=1582776784%7C0; htVD_2132_auth=fcfc510%2BYbgbpdyQBvpzL6MF99wjmotvGZulpgwFfrhzTiDht17tid5kMMg40HX83qU7HSuKKIt%2FH1RyMZ4S%2BJsKUQ; htVD_2132_lastcheckfeed=66375%7C1582776784; htVD_2132_lip=124.133.168.174%2C1582776784; htVD_2132_connect_is_bind=0; htVD_2132_nofavfid=1; htVD_2132_checkpm=1; htVD_2132_lastact=1582776789%09forum.php%09; htVD_2132_ttask=66375%7C20200227; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1582776800",
    "Host": "www.52pojie.cn",
    "Referer": "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

#GET响应地址栏
response=requests.get(base_url,headers=headers)#抬头信息
html=response.text#返回响应信息
html_url=re.compile(r'<a\shref="(.*)".*?class="s xst">(.*?)</a>')#正则匹配到标题信息
h_url=html_url.findall(html)#匹配返回结果
#print(h_url)
ur="http://www.52pojie.cn/"
with open("贴吧标题.text","w") as f:
    h=0
    for i in h_url:
        h=h+1
        # print(i)
        c = str(i[:1])#每个帖子的地址
        url_bs1 = re.compile(r"thread-\d.*?.html")#匹配出每个帖子地址
        d = str(url_bs1.findall(c))#转成字符串
        d = d.strip("['']")#格式化整理
        j = ur + d#域名+帖子地址
        i=(i[1]+"\t"+j)#标题与帖子
        k=str(h)+"."+i#序号转成字符串
        k=str(k)
        k=k.strip("('')")#去除引号等格式
        #print(k)
        p=f.write(k+"\n")#写入text

