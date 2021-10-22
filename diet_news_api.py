
from diet_news_model import DietNewsModel
import requests
from bs4 import BeautifulSoup
a = range(10)
numder = 1
DietNews = []
DietNews2 = []
for i in a:
    numder = numder +2
    try:
        url = f"http://www.mdtoday.co.kr/news/search.php?q=%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8&sfld=subj&period=MONTH%7C1"

        req = requests.get(url)
        source = req.text
        soup = BeautifulSoup(source, 'html.parser')
        diet = soup.select_one("#listWrap > div:nth-child(%d) > dl > dt > a " % numder )
        dietSummury = soup.select_one("#listWrap > div:nth-child(%d) > dl > dd.conts" % numder)
        dietThumnail = soup.select_one("#listWrap > div:nth-child(%d) > p > a > img" % numder)
        dhead = diet.text
        dsummary = dietSummury.text
        dhref = "http://www.mdtoday.co.kr" + diet.attrs["href"]
        dthumnail = "http://www.mdtoday.co.kr" + dietThumnail.attrs["src"]
        
        
        Diets = DietNewsModel(head=dhead,summary=dsummary,href=dhref,thumnail=dthumnail)
        DietNews.append(Diets.__dict__)
    except :
        print("1")


