from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

url = input('Enter - ')

html = urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup("span")
count=0
sum=0
for i in tags:
	x=int(i.text)
	count+=1
	sum = sum + x
print(count)
print(sum)
