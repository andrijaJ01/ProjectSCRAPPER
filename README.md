# Story Scrapper  
A Python library that queries Google, Bing, Yahoo and other search engines and collects the results from multiple search engine results pages.  
Please note that web-scraping may be against the Terms of Service of some search engines, and may result in a temporary ban.

## Supported search engines  

_[Google](https://www.google.com)_  
_[Bing](https://www.bing.com)_  
_[Yahoo](https://search.yahoo.com)_  
_[Duckduckgo](https://duckduckgo.com)_  
_[Startpage](https://www.startpage.com)_  
_[Aol](https://search.aol.com)_  
_[Dogpile](https://www.dogpile.com)_  
_[Ask](https://uk.ask.com)_  
_[Mojeek](https://www.mojeek.com)_  
_[Torch](http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi)_  

## Features  

 - Can save output files (html, csv, json).  
 - Search operators (`url`, `title`, `text`) are supported  
 - HTTP and SOCKS proxy support.  
 - Can collect dark web links with Torch.  
 - Easily extensible with new search engines. They(search engines) can be added by creating a new class in `search_engines/engines/` and add it to the  `search_engines_dict` dictionary in `search_engines/engines/__init__.py`. The new class should subclass `SearchEngine`, and override the following methods: `_selectors`, `_first_page`, `_next_page`. 
 - Python2 - Python3 are both supported.  

## Requirements  

git
_Python 2.7 - 3.7_ with  
_[Requests](http://docs.python-requests.org/en/master/)_ and  
_[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)_  

## Installation  

Clone this repository: `$ git clone https://github.com/andrijaJ01/ProjectSCRAPPER/`.  
Change directory to project folder(where setup.py is located): `$ cd ProjectSCRAPPER`.  
Run the setup file (sudo might not be necessary): `$ sudo python setup.py install`.  
Done!  

## Usage  

Can be used as a library:  

```
from search_engines import Google

engine = Google()
results = engine.search("my query")
links = results.links()

print(links)
```

Or as a CLI script:  

```  
$ python search_engines_cli.py -e google,bing -q "my query" -o json,print
```

For Usage please use:
```  
$ python search_engines_cli.py -h
```
