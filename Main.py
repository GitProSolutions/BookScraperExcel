import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class BookSpider(scrapy.Spider):
    name = "BookScraperExcel"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        book_divs = response.xpath("//div[@class='image_container']")
        for book in book_divs:
            title = book.xpath("./h3/a/@title").extract_first()
            price = book.xpath("./div/p[@class='price_color']/text()").extract_first()
            self.book_data.append({
                'title': title,
                'price': price
            })

    def __init__(self):
        self.book_data = []
        self.crawler = None
        self.proxy_list = []

    def start_crawler(self):
        process = CrawlerProcess(get_project_settings()) # Get the crawler settings
        process.crawl(BookSpider) # Add the spider to the crawler
        self.crawler = process.create_crawler() # Create the crawler

        # Set up the downloader middlewares to use proxies
        if self.proxy_list:
            self.crawler.settings.set('DOWNLOADER_MIDDLEWARES', {
                'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
                'book_crawler.randomproxy.RandomProxy': 100,
            })

        # Set the crawler to use the proxy list
        self.crawler.settings.set('PROXY_LIST', self.proxy_list)

    def stop_crawler(self):
        if self.crawler:
            self.crawler.stop()
            self.crawler = None

    def get_book_data(self):
        self.proxy_list = self.get_proxy_list()
        self.book_data = []
        self.start_crawler()
        self.crawler.start()
        self.stop_crawler()
        return self.book_data

    def get_proxy_list(self):
        proxies = ['http://127.0.0.1:8888']
        # You can add more proxies here or read them from a file or database
        return proxies


class API:
    def __init__(self):
        self.spider = BookSpider()

    def get_book_data(self):
        book_data = self.spider.get_book_data()
        self.export_to_excel(book_data)
        return book_data

    def export_to_excel(self, book_data):
        df = pd.DataFrame(book_data)
        df.to_excel('book_data.xlsx', index=False)


api = API()
book_data = api.get_book_data()

print(book_data)

# Easter egg message
print("Hiii did we met before ahhh just let it go nice to meet you fellow fwend")
