# requests --> newpaper의 article
# 왜냐면 html 파싱할때, 잘 안된다.

import pickle
with open("/home/intern/data/url_list_before/iter_list_8000000", "rb") as f:
    urllst = pickle.load(f)

print(urllst[10])

    #url list -> csv


# pickle -> pyspark input or pickle -> list
# 한글 안해도 됨
# 피클 -> url list
# beautiful soup 로 가져오고 html 이랑 text로 만들어 보기.
# timeout option <- requests config
# code 분석




import findspark
findspark.init()
from pyspark import SparkContext
import re
import requests
from bs4 import BeautifulSoup
import time
import datetime

file_name = "file:///home/intern/data/url_list_before/iter_list_8000000"
sc = SparkContext()

rdd = sc.parallelize(urllst)

# hangle filter function from Regular expression
def hanglefunc(docx):
    hangle = re.compile('[^ ㄱㅡ|가-힣]+')
    result = hangle.sub("",docx)
    print(result)
    return result

def crawler(url):
        print("in crawler")
        if "http://" in url:
            print("http://")
            try:
                req = requests.get(url,timeout=5)
            except requests.exceptions.Timeout as errt:
                return
            except requests.exceptions.HTTPError as errh:
                return
            except requests.exceptions.ConnectionError as errc:
                return
            except requests.exceptions.RequestException as err:
                return
            html = req.text
            res = html.encode("utf-8")
            soup = BeautifulSoup(res,'html.parser')
            docx = soup.get_text()
            print(docx)
            #hangle = hanglefunc(docx)
            print("before save")
            with open("/home/intern/data/output_text/" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f') + ".txt", "w") as output:
                print("doing save")
                output.write(docx)
            return docx
        elif "https://" in url:
            print("https://")
            try:
                req = requests.get(url,timeout=5)
            except requests.exceptions.Timeout as errt:
                return
            except requests.exceptions.HTTPError as errh:
                return
            except requests.exceptions.ConnectionError as errc:
                return
            except requests.exceptions.RequestException as err:
                return
            html = req.text
            res = html.encode("utf-8")
            soup = BeautifulSoup(res,'html.parser')
            docx = soup.text
            print(docx)
            #hangle = hanglefunc(docx)
            with open("/home/intern/data/output_text/" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f') + ".txt", "w") as output:
                output.write(docx)
            return
        else:
            return


#실행예시
rdd.map(crawler).take(10)

print("2")
