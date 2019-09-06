from dask.array.ufunc import absolute 
from urllib.parse import  urljoin


def analyze(url):
    '''prints the frequency of every word in web page and
    prints and returns the list of http links, in absolute format, in it.'''
    
    print('Visiting' , url)   #for testing 
    
    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()      # get list of links
    
    # compute word frequencies
    content = collector.getData()   # get text data as a string 
    freq = frequency(content)
    
    # print the frequency of every text data word in web page
    print('\n{:50} {:10} {:5}'.format('URL','word','count'))
    for word in freq:
        print('{:50}{:10}{:5}'.format(url,word,freq[word]))
        
    # print the http links found in web page
    print('\n{:50} {:10}'.format('URL','link'))  
    
    for link in urls:
        print('{:50} {:10}'.format('URL','link'))  
        
        
    return urls
        
        
        
visited = set()


def crawl2(url):
    ''' a recursive web crawler that calls analyze() on every visited web page'''
    
    # add url to set of visited pages
    global visited   # while not necessary, warns the programmer
    visited.add(url)  
    
    # analyze() returns a list of hyperlinks URLs in web page URL
    links = analyze(url)
    
    #recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass
            
            
crawl2('http://reed.cs.depaul.edu/lperkovic/one.html')    
    
    