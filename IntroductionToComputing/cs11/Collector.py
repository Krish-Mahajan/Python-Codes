from urllib.parse import  urljoin
from html.parser import  HTMLParser

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'
    def __init__(self,url):
        'initializes hyperlink URLs into a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        
    def handle_starttag(self,tag,attrs):
        'collect hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] =='href':
                    # construct absolute URL
                    absolute = urljoin(self.url,attr[1])
                    if absolute[:4]== 'http' : #collect HTTP URLS
                        self.links.append(absolute)
                        
    
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links 
    
    