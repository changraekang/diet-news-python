from diet_news_model import DietNewsModel
import requests
from bs4 import BeautifulSoup

DietNews2 =[]
number = 1
url = f"https://www.chosun.com/search/query=%EB%8B%A4%EC%9D%B4%EC%96%B4%ED%8A%B8&siteid=health&sort=1/"
req = requests.get(url)
source = req.text
soup = BeautifulSoup(source, 'html.parser')
diet = soup.select_one("#right-rail > div.flex-chain-wrapper.lg.heading-title.heading-title--top.\|.width--100.box--hidden-sm.box--hidden-md-only > section > div > div > div > div:nth-child(1) > div > div > div > div.story-card.story-card--art-right.\|.flex.flex--wrap > div.story-card-block.story-card-left.\|.grid__col--sm-9.grid__col--md-9.grid__col--lg-9 > div > a > span" )
dietSummury = soup.select_one("#main > div.search-feed > div:nth-child(%d) > div > div.story-card.story-card--art-left.\|.flex.flex--wrap.box--hidden-sm > div.story-card-right.\|.grid__col--sm-8.grid__col--md-8.grid__col--lg-8.box--pad-left-xs > span > span" % number)
dietThumnail = soup.select_one("#main > div.search-feed > div:nth-child(%d) > div > div.story-card.story-card--art-left.\|.flex.flex--wrap.box--hidden-sm > div.story-card-left.story-card-block--art.\|.grid__col--sm-4.grid__col--md-4.grid__col--lg-4.box--pad-right-xs > div > figure > a > div > img" % number)
print(diet)
