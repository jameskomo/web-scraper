from bs4 import BeautifulSoup
import requests
import csv
import time
import lxml

# SETTING WEBSITE SOURCE
url='https://old.reddit.com/r/datascience/'

# MIMIC BROWSER VISIT TO AVOID BOT RESPONSE BUT BROWSER LIKE RESPONSE
headers={'User-Agent': 'Mozilla/5.0'}

# GETTING RESPONSE OBJECT
page=requests.get(url, headers=headers)

# CREATING SYNTAX TREE TO HELP FIND SPECIFIC TAGES BY SEARCHING FOR ANY COMBINATION OF CLASSES, IDS OR TAG NAMES
soup=BeautifulSoup(page.text, 'lxml')

# SETTING CSV FILE
csv_file=open('reddit_crawler.csv', 'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['counter', 'title', 'author', 'likes', 'comments'])

# FIND TAGS WITH CLASS INTERESTED IN
domains=soup.find_all('span', class_="domain")

# PASSING MULTIPLE PARAMETERS
# soup.find_all("span", {"class": "domain", "height", "100px"})

# SKIPPING TAGS THAT DO NOT MATCH INTEREST TAGS
for domain in domains:
    if domain!="(self.datascience)":
        continue

# FINDING PARENT OF INTEREST CLASS USING BEAUTIFULSOUP
for domain in soup.find_all("span", class_="domain"):
    if domain!="(self.datascience)":
        continue
    parent_div=domain.parent.parent.parent.parent
    # THERE ARE FOUR LEVELS ABOVE THE CLASS INTERESTED IN THE DOM STRUCTURE
   

# SEARCHING FOR TAGS WITH COMBINATION OF ATTRIBUTES
attrs={'class': 'thing', 'data-domain': 'self.datascience'}

# EXTRACTING INFORMATION FROM SOUP
for post in soup.find_all('div', attrs=attrs):
    posts=soup.find_all('div', attrs=attrs)
    title=post.find('p', class_="title").text
    author = post.find('a', class_='author').text
    comments = post.find('a', class_='comments').text
    comments = post.find('a', class_='comments').text.split()[0]
    if comments == "comment":
        comments = 0
    likes = post.find("div", attrs={"class": "score likes"}).text
    if likes == "•":
        likes = "None"
         
# WRITING TO CSV FILE
counter = 1
for post in posts:
    title=post.find('p', class_="title").text
    author = post.find('a', class_='author').text
    comments = post.find('a', class_='comments').text
    comments = post.find('a', class_='comments').text.split()[0]
    if comments == "comment":
        comments = 0
    likes = post.find("div", attrs={"class": "score likes"}).text
    if likes == "•":
        likes = "None"
    post_line = [counter, title, author, likes, comments]
    with open('reddit.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(post_line)

    counter += 1

    # CSV WRITER 2
    csv_writer.writerow([counter, title, author, likes, comments])
csv_file.close()

# # TOGGLING BETWEEN PAGES
# counter = 1

# while (counter <= 100):
#     for post in posts:
#         title=post.find('p', class_="title").text
#         author = post.find('a', class_='author').text
#         comments = post.find('a', class_='comments').text
#         comments = post.find('a', class_='comments').text.split()[0]
#         if comments == "comment":
#             comments = 0
#         likes = post.find("div", attrs={"class": "score likes"}).text
#         if likes == "•":
#             likes = "None"
#         post_line = [counter, title, author, likes, comments]
#         with open('output.csv', 'a') as f:
#             writer = csv.writer(f)
#             writer.writerow(post_line)

#         next_button = soup.find("span", class_="next-button")
#         next_page_link = next_button.find("a").attrs['href']
#         time.sleep(2)
#         page = requests.get(next_page_link, headers=headers)
#         soup = BeautifulSoup(page.text, 'lxml')



