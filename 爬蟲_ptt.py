import urllib.request as a1
import bs4
class  Test:
    def __init__(self,web):
        self.web=web
    def read(self):
        b=a1.Request(self.web,headers={
            "cookie":"over18=1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })
        with a1.urlopen(b) as lol:
            return lol.read().decode("utf-8")
    def read2(self):
        data=self.read() #獲得網頁內容
        num1=bs4.BeautifulSoup(data, "html.parser")#翻譯html
        num2=num1.find_all("div",class_="title")
        num3=num1.find_all("a",string="最新")
        with open("test.txt","w") as lol2:
            for page in num2:
                if page.a: #檢測page裡有沒有<a
                    lol2.write(page.a.string+"\n")
        if num3:
            return num3[0].get("href")

web="https://www.ptt.cc/bbs/Gossiping/index.html"
a=Test(web)
c=a.read()
d=a.read2()
print("https://www.ptt.cc"+d)