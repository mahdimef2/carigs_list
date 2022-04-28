import sys
from crawl import LinkCrawler, DataCrawler

if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == 'link':
        crawler = LinkCrawler(cities=['paris', 'munich'])
        crawler.start(store=True)
    elif switch == 'page':
        crawler = DataCrawler()
        crawler.start(store=True)
