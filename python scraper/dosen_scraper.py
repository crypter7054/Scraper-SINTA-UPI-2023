import scrapy
import requests
import os

# data yang akan diambil
#     nama
#     dept
#     sinta_id
#     Scopus H-index
#     GS H-index
#     SINTA Score 3Yr
#     SINTA Score 
#     Affil Score 3Yr
#     Affil Score
#     photo 

class DosenSpider(scrapy.Spider):
    name = "dosen-scraper"

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
                dept = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-dept > a::text').extract()[0].strip()
                sinta_id = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-id::text').get().replace('ID :', '').replace(' ', '')
                scopus_h_index = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-warning::text').get().replace('Scopus H-Index :', '').replace(' ', '')
                gs_h_index = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-success.ml-3::text').get().replace('GS H-Index :', '').replace(' ', '')
                sinta_3yr_score = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(1) > div.stat-num.text-center::text').extract()
                sinta_score = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(2) > div.stat-num.text-center::text').extract()
                affil_3yr_score = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(3) > div.stat-num.text-center::text').extract()
                affil_score = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(4) > div.stat-num.text-center::text').extract()
                # image_url = dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg-2 > img::attr(src)').extract()

                yield {
                    'nama' : name,
                    'dept' : dept,
                    'sinta_id' : sinta_id,
                    'scopus_h_index' : scopus_h_index,
                    'gs_h_index' : gs_h_index,
                    'sinta_3yr_score' : sinta_3yr_score,
                    'sinta_score' : sinta_score,
                    'affil_3yr_score' : affil_3yr_score,
                    'affil_score' : affil_score,
                }

                # url_str = []
                # img_data = []
                
                # for url_str in image_url:
                #     print(url_str)
                #     img_data = requests.get(url_str).content

                #     filename = str(name).replace("'", "").replace('[', '').replace(']', '') + '.jpg'

                #     dir_path = 'photo'
                #     os.makedirs(dir_path, exist_ok=True)

                #     with open(os.path.join(dir_path, filename), 'wb') as handler:
                #         handler.write(img_data)

                