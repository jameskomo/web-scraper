from bs4 import BeautifulSoup
import requests
import csv
import time
import lxml

# SETTING WEBSITE SOURCE
url='https://flashdeals.aliexpress.com/en.htm'

# MIMIC BROWSER VISIT TO AVOID BOT RESPONSE BUT BROWSER LIKE RESPONSE
headers={'User-Agent': 'Mozilla/5.0'}

# GETTING RESPONSE OBJECT
page=requests.get(url, headers=headers)

# CREATING SYNTAX TREE TO HELP FIND SPECIFIC TAGES BY SEARCHING FOR ANY COMBINATION OF CLASSES, IDS OR TAG NAMES
soup=BeautifulSoup(page.text, 'lxml')



# # WRITING TO CSV
# csv_file=open('komo_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])

deal=soup.find_all('div', class_='item-details')
print(deal)
# headline=article.h2.a.text
# summary=article.find('div', class_="entry-content").p.text
# # print(summary)

# # GETTING VIDEOS
# video_source=article.find('iframe', class_='youtube-player')
# vid_src=article.find('iframe', class_='youtube-player')['src']
# vid_id=vid_src.split('/')[4]
# vid_id=vid_id.split('?')[0]
# try:
#     yt_link=f'https://youtube.com/watch?v={vid_id}'
# except ex as e:
#     yt_link=None
# # print(yt_link)

# # ITERATING THROUGH ALL CONTENT
# for article in soup.find_all('article'):
#     headline=article.h2.a.text
#     summary=article.find('div', class_='entry-content').p.text
#     video_source=article.find('iframe', class_='youtube-player')
#     vid_src=article.find('iframe', class_='youtube-player')['src']
#     vid_id=vid_src.split('/')[4]
#     vid_id=vid_id.split('?')[0]
#     try:
#         yt_link=f'https://youtube.com/watch?v={vid_id}'
#     except ex as e:
#         yt_link=None
#     # print(yt_link)
#     # print()
#     csv_writer.writerow([headline, summary, yt_link])
# csv_file.close()



  