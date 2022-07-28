import scrapy

# data yang akan diambil
#   dept
#   dept_code
#   sinta_score_overall
#   sinta_3yr_score

class DeptSpider(scrapy.Spider):
    name = "dept-scraper"

    def start_requests(self):
        urls = []
        
        for i in range (1, 19):
            urll = 'https://sinta.kemdikbud.go.id/affiliations/departments/414/001034?page=' + str(i)
            urls.append(urll)   
            print(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in range (3, 13):
            for dept in response.css('body > div > div.col-md-8 > div.content > div > div.au-list-affil.mt-3 > div.content-list-no-filter'):

                yield{
                    'dept' : dept.css('div:nth-child(' + str(a) + ') > div.col-lg-1.tbl-content-meta.mb-2 > span::text').extract() + dept.css('div:nth-child(' + str(a) + ') > div.col-lg.tbl-content-name > a::text').extract(),
                    'sinta_score_overall' : dept.css('div:nth-child(' + str(a) + ') > div.col-lg.tbl-content-name > div.profile-hindex > span.profile-id.text-warning::text').get().replace('SINTA Score Overall : ', '').strip(),
                    'sinta_3yr_score' : dept.css('div:nth-child(' + str(a) + ') > div.col-lg.tbl-content-name > div.profile-hindex > span.profile-id.text-success.ml-3::text').get().replace('SINTA Score 3Yr : ', '').strip(),
                }