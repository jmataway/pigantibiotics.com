import urllib
import requests
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "fitter happier radiohead"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}
r = requests.get(URL, headers=headers)

soup = BeautifulSoup(r.text, 'lxml')

result = soup.find('div', class_='zloOqf PZPZlf')
print(result.text)