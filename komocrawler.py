from bs4 import BeautifulSoup
import requests

# SCRAPING WEBSITES
source=requests.get('http://coreyms.com').text
soup=BeautifulSoup(source, 'lxml')
article=soup.find('article')
headline=article.h2.a.text
summary=article.find('div', class_="entry-content").p.text
# print(summary)

# GETTING VIDEOS
video_source=article.find('iframe', class_='youtube-player')
vid_src=article.find('iframe', class_='youtube-player')['src']
vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]
yt_link=f'https://youtube.com/watch?v={vid_id}'
print(yt_link)



# SCRAPING HTML FILE
# with open('simple.html') as html_file:
#     soup=BeautifulSoup(html_file, 'lxml')
   
#     for article in soup.find_all('div', class_='article'):
#         headline=article.h2.a.text
#         print(headline)
#         summary=article.p.text
#         print(summary)
  