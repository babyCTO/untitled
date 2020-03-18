import requests
import re
#创建一个回话
session=requests.Session()
#获取地址
base_url="https://www.52pojie.cn/member.php?mod=logging&action=login"
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "Cookie: htVD_2132_saltkey=rSzPbiiO; htVD_2132_lastvisit=1579705761; htVD_2132_connect_is_bind=0; htVD_2132_nofavfid=1; htVD_2132_smile=1D1; BAIDU_SSP_lcr=https://www.baidu.com/link?url=ZAScYogajXHrTTRa5xjpUYNs_YkaVbiTdISeKxk1w38ZzGSfDg_q6FsVZ1y7CxOz&wd=&eqid=e472452f00357d4e000000025e2eb0e2; Hm_lvt_46d556462595ed05e05f009cdafff31a=1580118283,1580118285,1580118479,1580118637; __gads=ID=e977ea8b6aade3cc:T=1580118651:S=ALNI_Maoy11NwokbXI3H3vbAdkndLSoTjA; htVD_2132_visitedfid=13D8D16; htVD_2132_viewid=tid_98585; htVD_2132_ulastactivity=1580120346%7C0; htVD_2132_auth=2430Cn680v42FuufAmMzr2kcSr0c%2BjKcgjE39S4fS21GoRdmGmTVysk6Il7JcyioGoBjdGfapb3c7lt4EsaXT61yYQ; htVD_2132_lip=124.133.168.174%2C1580120346; htVD_2132_seccode=1133797.34ac2ba5f8ed4b05c4; htVD_2132_checkpm=1; htVD_2132_ttask=66375%7C20200127; htVD_2132_st_p=66375%7C1580120397%7Ce475a1fe2ef3409e4e54c705359e7d94; htVD_2132_lastact=1580120415%09home.php%09spacecp; htVD_2132_lastcheckfeed=66375%7C1580120415; htVD_2132_checkfollow=1; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1580120424",
    #"Host": "www.52pojie.cn",
    #"Referer": "https://www.52pojie.cn/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

#GET响应地址栏
#response=requests.get(base_url,headers=headers)
#print(response.text)

data={
    "username":"a86350703",
    "password":"ZQa86350703"
}

#__name__=="__main__"
#POST响应请求
response=session.post(base_url,data=data,headers=headers)
print(response.text)
"""
html=response.text
html1=re.compile(r"<iframe src='(.*?)'")
img=html1.findall(html)
print(img)
"""
