import urllib.request as request
from bs4 import BeautifulSoup
URL = "https://www.amazon.in"
page = request.urlopen(URL)
soup=BeautifulSoup(page,'html.parser')
#print(soup.prettify())
results=soup.find_all('div',class_='navFooterLinkCol')
#print(results)
for result in results:
    one=result.find('a',class_='nav_a')
    print(one.text)
