# coding=gbk
from urllib.request import urlopen
from bs4 import BeautifulSoup

content_pages = ['http://read.goodweb.net.cn/news/news_more.asp?lm2=351',
                 'http://read.goodweb.net.cn/news/news_more.asp?page=2&lm2=351']


def getHtml(url):
    response = urlopen(url)
    html = response.read().decode('gbk')
    return html

def getTitleAndUrl(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_url_list = soup.find_all(cellpadding="2")
    title_url_dict_list=[]
    for item in title_url_list:
        title_url_tag = item.find_all('a')[1]
        title = title_url_tag.text
        url = title_url_tag.get('href')
        title_url_dict = {'title':title,'url': 'http://read.goodweb.net.cn/news/' + url}
        title_url_dict_list.append(title_url_dict)
    return title_url_dict_list

def get_all_url_title(pages:list):
    all_html=''
    for url in pages:
        html=getHtml(url)
        all_html+=html
    # print(all_html)
    title_url_dict_list=getTitleAndUrl(all_html)
    return title_url_dict_list


# 从这里开始爬取单篇内容
def get_and_write_article(dict_list):
    for item in dict_list:
        try:
            response = urlopen(item['url'])
            html = response.read().decode('gbk')
            soup = BeautifulSoup(html, 'html.parser')
            # article_title = soup.find(id='tt').text
            article_title=item['title']
            article_body = soup.find(id='zoom').text
            with open('files/' + article_title + '.txt', 'w',encoding='utf-8') as f:
                f.write(article_body)
        except Exception as err:
            print(item['url'])
            with open('files/err.txt','a') as errFile:
                errFile.write(str(err) + '\n'+item['url']+'\n\n\n')

# if __name__ == '__main__':
#     dict_list=get_all_url_title(content_pages)
#     get_and_write_article(dict_list)