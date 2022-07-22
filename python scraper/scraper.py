import scrapy

# logging.getLogger('scrapy').propagate = False

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

class SINTASpider(scrapy.Spider):
    name = "sinta-upi"

    def start_requests(self):
        
        urls = []
        for a in range (1, 174):
            urll = 'https://sinta.kemdikbud.go.id/affiliations/authors/414?page=' + str(a)
            urls.append(urll)   

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # first index is 4
        for i in range (4, 14):
            for dosen in response.css('body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3'):
                yield {
                    'nama': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.profile-name > a::text').extract(),
                    'dept': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-dept > a::text').extract()[0].strip(),
                    'sinta_id': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-id::text').get().replace('ID :', '').replace(' ', ''),
                    'scopus_h_index': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-warning::text')
                    .get().replace('Scopus H-Index :', '').replace(' ', ''),
                    'gs_h_index': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-success.ml-3::text')
                    .get().replace('GS H-Index :', '').replace(' ', ''),
                    'sinta_3yr_score': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(1) > div.stat-num.text-center::text').extract(),
                    'sinta_score': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(2) > div.stat-num.text-center::text').extract(),
                    'affil_3yr_score': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(3) > div.stat-num.text-center::text').extract(),
                    'affil_score': dosen.css('div:nth-child(' + str(i) + ') > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(4) > div.stat-num.text-center::text').extract(),
                } 

# nama       
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.profile-name > a
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(5) > div > div.col-lg > div.profile-name > a
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(6) > div > div.col-lg > div.profile-name > a

# dept
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-dept > a
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(5) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-dept > a

# sinta_id
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-id
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(5) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-id

# scopus_h_index
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-warning

# gs_h_index
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(1) > div.profile-hindex > span.profile-id.text-success.ml-3

# sinta_3yr_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(1) > div.stat-num.text-center

# sinta_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(2) > div.stat-num.text-center

# affil_3yr_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(3) > div.stat-num.text-center

# affil_score
# body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div:nth-child(4) > div > div.col-lg > div.row > div:nth-child(2) > div > div:nth-child(4) > div.stat-num.text-center