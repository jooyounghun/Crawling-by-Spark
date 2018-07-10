from multiprocessing import Pool
import time
import requests

def Tfunc1(url):
    req = requests.get(url)
    html = req.text
    res = html.encode("utf-8")
    print(res) 



start_time = time.time()

url_list = ["http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=146", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=156", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=105", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=131", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=133", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=143", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184"]

pool = Pool(processes=4)
pool.map(Tfunc1,url_list)


print("------%s seconds ---" %(time.time() - start_time))


