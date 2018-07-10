import requests 
import time


start_time = time.time()


url_list = ["http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=146", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=156", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=105", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=131", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=133", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=143", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159", "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184"]








req = requests.get(url_list[0])
req1 = requests.get(url_list[1])
req2 = requests.get(url_list[2])
req3 = requests.get(url_list[3])
req4 = requests.get(url_list[4])
req5 = requests.get(url_list[5])
req6 = requests.get(url_list[6])
req7 = requests.get(url_list[7])
req8 = requests.get(url_list[8])
req9 = requests.get(url_list[9])


html = req.text
html1 = req1.text
html2 = req2.text
html3 = req3.text
html4 = req4.text
html5 = req5.text
html6 = req6.text
html7 = req7.text
html8 = req8.text
html9 = req9.text





res = html.encode("utf-8")
res1 = html1.encode("utf-8")
res2 = html2.encode("utf-8")
res3 = html3.encode("utf-8")
res4 = html4.encode("utf-8")
res5 = html5.encode("utf-8")
res6 = html6.encode("utf-8")
res7 = html7.encode("utf-8")
res8 = html8.encode("utf-8")
res9 = html9.encode("utf-8")

print(res + res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8 + res9)

print("------%s seconds ---" %(time.time() - start_time))

