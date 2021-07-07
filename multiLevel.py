from urllib.request import urlopen
from bs4 import BeautifulSoup


def write_unit(url):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding="GBK")
    table_title = soup.title.text.split('-')[0]
    # title_tags = soup.findAll(name='font', attrs={"class": "style_font"})
    title_url_tags = soup.findAll('a', {'target': '_blank'})
    # table_dict={'page_title':page_title}
    for title_url_tag in title_url_tags:
        if title_url_tag.find('font', {'class': 'style_font'}):
            page_title = title_url_tag.text
            page_url = 'http://read.goodweb.net.cn/news/' + title_url_tag.get('href')
            article_body = read_article(page_url)
            with open(table_title + '.txt', 'a', encoding="utf-8") as f:
                f.write('○' + page_title + '○\n')
                f.write(article_body)


def read_article(url):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding="GBK")
    article_body = soup.find(id='zoom').text
    return article_body


def write_all():
    with open('errURL.txt', 'r') as f:
        url_list = f.readlines()
        for url in url_list:
            write_unit(url)
            print(url + '写入完成')


if __name__ == '__main__':
    write_all()
