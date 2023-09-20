from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import asyncio 



async def pars():
    news = []


    base_url = "https:/www.pravda.com.ua"
    news_url = f"{base_url}/news"
    with urlopen(news_url) as r:
        await asyncio.sleep(0.03)
        soup = bs(r.read(), "html.parser")

        headers = soup.select(".aricle_header > a ")

    for item in headers[:4]:
        header = item.text
        link = item.get("href")
        new_link = link if link.starswith("http") else f"{base_url}{link}"
        with urlopen(new_link) as b:
            await asyncio.sleep(0.03)
            soup = bs(b.read(), "html.parser")
            
            body_text = soup.select(".post__text > p")
            body = []
            for tag in body_text:
                body.append(tag.text+"\n") 
        
            
        news.append(
            {
                "body": body,
                "header": header,
                "link": link,
            }
        )
    return news