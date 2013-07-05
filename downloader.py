import re
import urllib  
from bs4 import BeautifulSoup

page=1


def extract_links(soup):
    print '#' + '-'*110 + '#'
    count = 1
    link = soup.findAll('a', {'class' : 'std-btn-small mleft torrentDwl'} , href= re.compile('.torrent'))
    for i in link:
        y =  i.get('href') + '\n' + '#' + '-'*100 + '#' + '\n'
        file = open('links.txt', 'a')
        file.write(y,)
        count = count + 1
        file.close()
        

while page < 142:
    url = "http://yify-torrents.com/browse-movie/0/All/All/0/latest/%s"%str(page)
    request= urllib.urlopen(url)
    response = request.read()
    soup = BeautifulSoup(response)
    extract_links(soup)
    print "%s pages done"%str(page)
    page = page + 1


