import requests
import scrapy
import os
import time

class PhotoSpider(scrapy.Spider):
    name = "photo-scraper"

    # requests
    def start_requests(self):
        urls = []
        
        # get the url start from page 1 to page 175
        for a in range (1, 176):

            # initialize url + page number link
            urll = 'https://sinta.kemdikbud.go.id/affiliations/authors/414?page=' + str(a)
            urls.append(urll)       
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # first index of css selector is 4
        for i in range (4, 14):

            # loop css selector
            for dosen in response.css('body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3'):
                
                # get the name and image url
                name = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.profile-name > a::text').extract()
                image_url = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg-2 > img::attr(src)').extract()
                
                # fill the value of url str to image_url
                for url_str in image_url:
                    # request
                    img_data = requests.get(url_str).content
                    
                    # set the filename
                    filename = str(name).replace("'", "").replace('[', '').replace(']', '') + '.jpg'

                    # create the dir
                    dir_path = 'photo'
                    os.makedirs(dir_path, exist_ok=True)

                    # create file with spesific dir
                    with open(os.path.join(dir_path, filename), 'wb') as handler:
                        handler.write(img_data)
                    
                    # time.sleep(1)
                

                
                


        