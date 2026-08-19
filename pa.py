# import requests
# url="http://www.baidu.com"
# response=requests.get(url)
# print(response.content.decode())
# import requests
from shlex import quote

import requests

# url="https://b0.bdstatic.com/488e4c8190ddd3827c028c30d31fea82.jpg"
# t=requests.get(url)#响应对象
# print(t.url)#打印响应的url
# print(t.request.headers)#打印响应对象的请求头
# print(t.headers)#打印响应头
# print(t.apparent_encoding)
# with open("五条.jpg","wb") as f:#保存响应+
#     f.write(t.content)

#构建请求头
# url="http://www.baidu.com"
# res=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
# print(res.content.decode())

#users-agent池 随机调用UA
# import random
# UAlist=[
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.3131 SLBChan/115 SLBVPV/64-bit",
# "Mozilla/5.0"]
# print(random.choice(UAlist))

#https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=68018901_58_oem_dg&wd=%E5%AD%A6%E4%B9%A0&fenlei=256&rsv_pq=0xdfbce6d60170613c&rsv_t=48830mh4DR48c4eISSh5DjX1ph6%2B4Yd%2FNXooYg7eSJzlOxBa6XriulBPt3dp&rqlang=en&rsv_dl=tb_enter&rsv_enter=1&rsv_sug3=6&rsv_sug1=5&rsv_sug7=101&rsv_btype=t&inputT=2596&rsv_sug4=2596
from urllib.parse import quote, unquote

from gevent import timeout
from pip._internal.network import session

# print(quote("学习"))
# # print(unquote("%E7%8E%8B%E8%80%85%E8%8D%A3%E80)

# url="https://www.baidu.com/s?"
# headers={"User-Agent":"User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.3131 SLBChan/115 SLBVPV/64-bit"}
# kw={"wd":"python"}
# session=requests.session()
# res=session.get(url,headers=headers,params=kw)
# print(res.content.decode())

#mv的爬取
# url="https://cn-gdjm-cm-01-03.bilivideo.com/upgcxcode/74/06/40588280674/40588280674_qe1-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=0x24098a5ca6404fd0a82e5a2452af564b&trid=00000009fc0b307940449c303b8f44f23ddh&deadline=1785908133&nbs=1&platform=html5&gen=playurlv3&os=bcache&og=hw&mid=3546601551301506&uipk=5&upsig=cd4d83e4ae3aed87f09d90c55702bcf8&uparams=e,oi,trid,deadline,nbs,platform,gen,os,og,mid,uipk&cdnid=88503&bvc=vod&nettype=0&bw=494720&lrs=100&buvid=&build=0&dl=0&f=h_0_0&agrr=0&orderid=0,1"
# res2=requests.get(url)
# with open("火影视频.mp4","wb") as f:
#     f.write(res2.content)

#贴吧的获取
# url="https://tieba.baidu.com/f?kw=%E8%A5%BF%E5%AE%89%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6&fr=pb"
# headers={"User-Agent":"User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.3131 SLBChan/115 SLBVPV/64-bit"}
# res=requests.get(url,headers=headers)
# with open("大学，html","wb") as f:
#     f.write(res.content)

#贴吧的翻页
# url="https://tieba.baidu.com/f?"
# headers = {
#     "User-Agent": "User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 SLBrowser/9.0.8.3131 SLBChan/115 SLBVPV/64-bit"}
# word=input("输入贴吧名字：")
# page=int(input("输入贴吧页数："))
# for i in range(page):
#     param={"kw":word,"pn":i*50}
#     res=requests.get(url,headers=headers,params=param)
#     with open(f"{word}{i+1}.html",'wb') as f:
#         f.write(res.content)

# #cookie来爬取贴吧
# url="https://m.toutiao.com/article/7444036938295788047/?wid=1785903510640&upstream_biz=toutiao_pc"
# headers = {
#  "User-Agent":"Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Edg/151.0.0.0 Mobile Safari/537.36","Cookie":"tt_webid=7670397134555137588; _ga=GA1.1.1826212889.1785903513; ttwid=1%7CqCD3EN5YFi8lpDFvAm2D6vDwFQ4LJ4ijf204Q1-rxFY%7C1785903515%7C342377f3c40673e05773f611ced20165ed856a08759262e44c2c81a1bc72ecd7; request_id=58858787285903533356; locationCountry=%E4%B8%AD%E5%9B%BD; locationProvince=%E5%B9%BF%E8%A5%BF; locationCity=%E8%B4%BA%E5%B7%9E; _ga_QEHZPBE5HH=GS2.1.s1785903512$o1$g1$t1785903531$j41$l0$h0; x-web-secsdk-uid=ecffc6c3-04a6-4d21-814e-6d63f7d64b37"}
# res=requests.get(url,headers=headers)
# print(res.text)

#session 自动处理cookie
#requests.session() 实例化session对象
# ses=requests.session()
# response=ses.post(url,data=data,headers=headers)
#使用session访问登录以后的页面
# session.get(url.text)

#cookie池 代表账号 cookie有有效期
#cookie数据放在客户的浏览器上，session数据放在服务器上

#代理ip
#proxies形式+字典 ip:端口号
# proxies={"http":"http://12.34.56.79:9527",
# "https":"https://12.34.56.79:9527"}
# response=requests.get(url,proxies=proxies)
#也可去http://

#爬取数据保存到csv文件
from lxml import html
from urllib.parse import urljoin
import csv
import requests
import time
import re
from zope.interface import document

# all_rows=[]
# url="https://www.tiobe.com/tiobe-index/"
# res=requests.get(url)
# document=html.fromstring(res.text)
# th_list=document.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()")
# tr_list=document.xpath("/html/body/section/div/article/table[1]/tbody/tr")
# for tr in tr_list:
#     td_list=tr.xpath("./td/text()")
#     row_dict=dict(zip(th_list,td_list))
#     all_rows.append(row_dict)
# with open("csv_data/tiobe_index.csv","w",encoding="utf-8",newline="")as f:
#     writer=csv.DictWriter(f,fieldnames=th_list)
#     writer.writeheader()
#     writer.writerows(all_rows)
#     print("数据保存成功")
#
# with open("csv_data/tiobe_index.csv","r",encoding="utf-8")as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#         print(row)

#常量
MOVIE_LIST_FILE="csv_data/movie_list.csv"
BASE_URL="https://www.themoviedb.org/"
TOP_URL_1="https://www.themoviedb.org/movie"
TOP_URL_2="https://www.themoviedb.org/movie"

def get_movie_year(movie_year):
    movie_years = movie_year[0].strip() if movie_year else ""
    return movie_years.replace("(","").replace(")","")
def get_movie_R_year(movie_R_year):
    movie_R_years = movie_R_year[0].strip() if movie_R_year else ""
    return re.search(r"\d{4}-\d{2}-\d{2}", movie_R_years).group()
def get_movie_time(movie_time):
    movie_times = movie_time[0].strip() if movie_time else ""
    h_res=re.search(r"(\d+)h", movie_times)
    m_res=re.search(r"(\d+)m", movie_times)
    h=int(h_res.group(1)) if h_res else "0"
    m=int(m_res.group(1)) if m_res else "0"
    return h*60+m
#保存电影数据
def save_movie_data(all_movie):
    with open(MOVIE_LIST_FILE,"w",encoding="utf-8",newline="")as f:
        writer=csv.DictWriter(f,fieldnames=["电影名","电影年份","电影上映时间","电影评分","电影类型","电影时长","电影导演","电影宣传语","电影简介"])
        writer.writeheader()
        writer.writerows(all_movie)
        print("数据保存成功")


#获取电影数据
def get_movie_data(movie_info_url):
    movie_response=requests.get(movie_info_url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Edg/151.0.0.0 Mobile Safari/537.36"},timeout=60)
    print(f"正在爬取{movie_info_url}")
    movie_doc=html.fromstring(movie_response.text)
    movie_name=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[1]/div/a/h2/text()")#电影名
    movie_year=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[1]/div/a/h2/span/text()")#电影年份
    movie_R_year=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[4]/div/span[@class='release']/text()")#电影上映时间
    movie_score=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[2]/div[1]/div[1]/div/div/div/@data-percent")#电影评分
    movie_tag=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[4]/div/span[@class='genres']/a/text()")#电影类型
    movie_time=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div[4]/div/span[@class='runtime']/text()")#电影时长
    movie_author=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[3]/p[1]/a/text()")#电影导演
    movie_slogen=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")#电影宣传语
    movie_descriptions=movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")#电影简介
    if not movie_name:
        print(f"该页面未提取到有效电影名，跳过空数据：{movie_info_url}")
        return None
    #返回电影数据
    movie_info={
        "电影名":movie_name[0].strip() if movie_name else "",
        "电影年份":get_movie_year(movie_year),
        "电影上映时间":get_movie_R_year(movie_R_year),
        "电影评分":movie_score[0].strip() if movie_score else "",
        "电影类型":",".join(movie_tag).strip() if movie_tag else "",
        "电影时长":get_movie_time(movie_time),
        "电影导演":",".join(movie_author).strip() if movie_author else "",
        "电影宣传语":movie_slogen[0].strip() if movie_slogen else "",
        "电影简介":movie_descriptions[0].strip() if movie_descriptions else ""
    }
    return movie_info
#主函数
def main():
    all_movie = []
    # 先确认网站分页URL规则，比如第一页也可以用page=1统一处理
    BASE_LIST_URL = "https://www.themoviedb.org/movie?page={page_num}"
    for page_num in range(1, 6):
        try:
            # 统一用GET请求所有分页，替换成你抓包得到的真实请求头
            response = requests.get(
                BASE_LIST_URL.format(page_num=page_num),
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
                timeout=60
            )
            # 先捕获404再抛错，避免直接崩溃
            if response.status_code == 404:
                print(f"第{page_num}页不存在，停止爬取")
                break
            response.raise_for_status()

            document = html.fromstring(response.text)
            # 抛弃原来的page_N ID定位，改用截图里稳定的class路径提取电影列表
            movie_list = document.xpath("//div[@class='media-card-list contents w-full']//div[@data-object-id]")

            for movie in movie_list:
                movie_url = movie.xpath(".//a/@href")
                if movie_url:
                    movie_full_url = BASE_URL + movie_url[0]
                    movie_info = get_movie_data(movie_full_url)
                    if movie_info is not None:
                        all_movie.append(movie_info)
            print(f"第{page_num}页爬取完成，当前累计{len(all_movie)}条数据")
            # 加个翻页延时，避免被封
            time.sleep(1)
        except Exception as e:
            print(f"第{page_num}页爬取出错: {e}")
            continue
    all_movie = [movie for movie in all_movie if any(movie.values())]
    save_movie_data(all_movie)
    print("全部数据保存成功")

# def main():
#     all_movie = []
#     BASE_LIST_URL = "https://www.themoviedb.org/movie?page={page_num}"
#     for page_num in range(1,6):
#         try:
#             response=requests.get(BASE_LIST_URL.format(page_num=page_num),headers={"User-Agent":"Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Edg/151.0.0.0 Mobile Safari/537.36"} ,timeout=60)
#             if response.status_code == 404:
#                print(f"第{page_num}页不存在，停止爬取")
#                break
#         except Exception as e:
#             print(f"第{page_num}页爬取出错: {e}")
#             continue
#         document=html.fromstring(response.text)
#         movie_list = document.xpath("//div[@class='media-card-list contents w-full']//div[@data-object-id]")
#         for movie in movie_list:
#             movie_url=movie.xpath(".//a/@href")
#             if movie_url:
#                movie_info_url=BASE_URL+movie_url[0]
#                movie_info=get_movie_data(movie_info_url)
#                all_movie.append(movie_info)
#         save_movie_data(all_movie)
#         print(f"第{page_num}页爬取完成，当前累计{len(all_movie)}条数据")
if __name__=="__main__":
    main()





