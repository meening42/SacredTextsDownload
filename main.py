from urllib.request import (
    urlopen, urlparse, urlunparse, urlretrieve)
from bs4 import BeautifulSoup as bs
import textwrap

print('Beginning file download')

url = 'https://www.sacred-texts.com/download.htm'
destinationFolderPath = 'C:/Users/.../'
soup = bs(urlopen(url))

for link in soup.find_all('a'):
    if link.get('href')[-3:] == ".gz":
        fileName = textwrap.shorten(str(link.string).replace(":","_"), width=50, placeholder="")+".gz"
        fileUrl = "https://www.sacred-texts.com/" + link.get('href')
        filePath = destinationFolderPath + fileName
        try:
            urlretrieve(fileUrl, filePath)
        except:
            print("An exception occurred probably 404")
