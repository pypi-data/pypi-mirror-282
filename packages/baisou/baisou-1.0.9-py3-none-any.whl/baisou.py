import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse, parse_qs
def sou(keyword=None):
    if len(sys.argv)>1:
      keyword=" ".join(sys.argv[1:])
    if not keyword:
        return {"error": "未提供搜索内容"}
    search_url = "http://www.baidu.com/s"
    params = {'wd': keyword}
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        span_element = soup.find('span', class_='cos-line-clamp-7')
        div_element = soup.find('div', class_='daq-content_wahha')
        zongjie = span_element.get_text().strip() if span_element else (div_element.get_text().strip() if div_element else "")
        search_results = []
        for result in soup.find_all('h3'):
            title = result.get_text().strip()
            link = result.find('a', href=True)['href'] if result.find('a', href=True) else ""
            if urlparse(link).scheme is not "":
             link2=requests.head(link).headers.items()
             if "Location" in dict(link2):
               link=dict(link2)["Location"]
            search_results.append({
                "title": title,
                "url": link
            })
        search_results.insert(0,zongjie)
        return search_results
    else:
        return {"error": "搜索失败"}