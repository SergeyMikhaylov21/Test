import requests
import lxml.html
htmltext = requests.get('http://www.sovsport.ru/gazeta/article-item/955606')
targetfile = htmltext.text
tree = lxml.html.fromstring(targetfile)
title = tree.findtext('.//title')
paragraph = tree.xpath('.//p/text()')[0]
print(paragraph)
