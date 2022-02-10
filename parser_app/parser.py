import  requests
from  bs4 import  BeautifulSoup
from  django.views.decorators.csrf import csrf_exempt

HOST = "https://megogo.net"
URL = "https://megogo.net/ru/series"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.2.834 Yowser/2.5 Safari/537.36'
}

@csrf_exempt
def get_html(url, params= ''):
    req  = requests.get(url,headers=HEADERS, params=params)
    return  req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_= 'card videoItem orientation-portrait size-normal')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div',class_='video-title card-content-title').get_text(),
                'image': HOST + item.find('div',class_="thumb").find('img')
            }
        )
        return  anime
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0,1):
            html = get_html(URL, params ={'page': page})
            anime.extend(get_data(html.text))
            return  anime
    else:
        raise  ValueError('Error in  parser func')
