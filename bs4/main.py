from bs4 import BeautifulSoup
import requests
respond = requests.get("https://news.ycombinator.com/")

yc_web_page = respond.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)
largest_number = max(article_upvotes)
print(largest_number)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])


# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, features="html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.a)
# print(soup.p)
# #print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one("#name")
# print(name)
# headings = soup.select(".heading")
# print(headings)