import socket
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup # Interesting import
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# A very simple web browser using socket
def soc_web_browser():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect( ('data.pr4e.org', 80) )
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())

    mysock.close()

# A very simple web browser using urllib.request
def ulib_web_browser():
    fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhandle: # line is bytes not strings, that's why we need to decode it
        print(line.decode().strip())

# scrap/crawl web page for tags e.g link
def web_scraping_py():
    url = input('Enter web link: ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('link')
    for tag in tags:
        print(tag.get('rel', None))

# soc_web_browser()
# ulib_web_browser()
web_scraping_py()