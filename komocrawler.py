from bs4 import BeautifulSoup
import requests
import csv

# SCRAPING WEBSITES
source=requests.get('http://coreyms.com').text
soup=BeautifulSoup(source, 'lxml')

# WRITING TO CSV
csv_file=open('komo_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

article=soup.find('article')
headline=article.h2.a.text
summary=article.find('div', class_="entry-content").p.text
# print(summary)

# GETTING VIDEOS
video_source=article.find('iframe', class_='youtube-player')
vid_src=article.find('iframe', class_='youtube-player')['src']
vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]
try:
    yt_link=f'https://youtube.com/watch?v={vid_id}'
except ex as e:
    yt_link=None
# print(yt_link)

# ITERATING THROUGH ALL CONTENT
for article in soup.find_all('article'):
    headline=article.h2.a.text
    summary=article.find('div', class_='entry-content').p.text
    video_source=article.find('iframe', class_='youtube-player')
    vid_src=article.find('iframe', class_='youtube-player')['src']
    vid_id=vid_src.split('/')[4]
    vid_id=vid_id.split('?')[0]
    try:
        yt_link=f'https://youtube.com/watch?v={vid_id}'
    except ex as e:
        yt_link=None
    # print(yt_link)
    # print()
    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()


# SCRAPING HTML FILE
# with open('simple.html') as html_file:
#     soup=BeautifulSoup(html_file, 'lxml')
   
#     for article in soup.find_all('div', class_='article'):
#         headline=article.h2.a.text
#         print(headline)
#         summary=article.p.text
#         print(summary)
  