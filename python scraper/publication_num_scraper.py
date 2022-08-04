import scrapy
import re
import time

class DosenSpider(scrapy.Spider):
    name = "dosen-scraper"
    
    def start_requests(self):
        urls = []
        
        # get the url start from page 1 to page 175
        for a in range (1, 176):

            # initialize url + page number 
            urll = 'https://sinta.kemdikbud.go.id/affiliations/authors/414?page=' + str(a)
            urls.append(urll)   

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('div.profile-name a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_publication)
          
    def parse_publication(self, response):

        checkPub = re.findall("data: (.+?)],\n", response.body.decode("utf-8"), re.S)[0].replace(' ','')
        pattern = re.compile('Q[1234]')

        if pattern.search(checkPub):
            pub_year = ''
            pub_num = ''
        else:
            pub_year = re.findall("data: (.+?)],\n", response.body.decode("utf-8"), re.S)[0].replace(' ','').replace('\n','').replace("'","").replace('[','')
            pub_num = re.findall("data: (.+?)],\n", response.body.decode("utf-8"), re.S)[1].replace('\n','').replace('[','').replace(' ','')

        yield{
            'name' : response.css('body > div > div.col-md-8 > div.content > div > div.row.p-3 > div.col-lg.col-md > h3 > a::text').get(),
            'sinta_id' : response.css('body > div > div.col-md-8 > div.content > div > div.row.p-3 > div.col-lg.col-md > div.meta-profile > a:nth-child(5)::text').get().replace('SINTA ID :', '').replace(' ', ''),
            'pub_year' : pub_year,
            'pub_num' : pub_num,
        }

        # time.sleep(5)