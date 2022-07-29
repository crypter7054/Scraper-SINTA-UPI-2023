import requests
import scrapy
import os

class PhotoSpider(scrapy.Spider):
    name = "photo-scraper"

    def start_requests(self):
        urls = []
        
        for a in range (1, 175):
            urll = 'https://sinta.kemdikbud.go.id/affiliations/authors/414?page=' + str(a)
            urls.append(urll)   

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # first index is 4
        for i in range (4, 14):
            for dosen in response.css('body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3'):
                
                name = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.profile-name > a::text').extract()
                image_url = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg-2 > img::attr(src)').extract()
                
                for url_str in image_url:
                    print(url_str)
                    img_data = requests.get(url_str).content

                    filename = str(name).replace("'", "").replace('[', '').replace(']', '') + '.jpg'

                    dir_path = 'photo'
                    os.makedirs(dir_path, exist_ok=True)

                    with open(os.path.join(dir_path, filename), 'wb') as handler:
                        handler.write(img_data)
                

                
                


        