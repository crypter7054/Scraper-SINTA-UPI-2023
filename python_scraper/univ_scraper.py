import scrapy
import re
import json

# data yang akan diambil
#   nama_univ
#   alamat
#   ID 
#   code
#   authors
#   departments
#   journals
#   sinta_score_overall
#   sinta_3yr_score
#   sinta_productivity_score
#   sinta_3yr_productivity_score
#   scopus_q1
#   scopus_q2
#   scopus_q3
#   scopus_q4
#   scopus_undefined_q
#   scopus_ro_article
#   scopus_ro_conference
#   scopus_ro_other
#   scopus_article
#   scopus_citation
#   scopus_cited_document
#   scopus_citation_researcher
#   gs_article
#   gs_citation
#   gs_cited_document
#   gs_citation_researcher
#   wos_article
#   wos_citation
#   wos_cited_document
#   wos_citation_researcher
#   garuda_article
#   garuda_citation
#   garuda_cited_document
#   garuda_citation_researcher

class UnivSpider(scrapy.Spider):
    name = "univ-scraper"

    # requests
    def start_requests(self):

        # initialize the url
        urls = ['https://sinta.kemdikbud.go.id/affiliations/profile/414']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # save to dir
        yield{
            'name' : response.css('body > div > div.col-md-8 > div.content > div > div.univ-profile > div > div > h3 > a::text').extract(),
            'address' : response.css('body > div > div.col-md-8 > div.content > div > div.univ-profile > div > div > div > a.affil-loc::text').extract(),
            'id' : response.css('body > div > div.col-md-8 > div.content > div > div.univ-profile > div > div > div > a.affil-code::text').extract()[0].replace('ID :', '').strip(),
            'code' : response.css('body > div > div.col-md-8 > div.content > div > div.univ-profile > div > div > div > a.affil-code::text').extract()[1].replace('CODE :', '').strip(),
            'author' : response.css('body > div > div.col-md-8 > div.content > div > div.row.stat-card.affil-profile-card.mb-6 > div:nth-child(1) > div > div > div.stat-num::text').extract(),
            'department' : response.css('body > div > div.col-md-8 > div.content > div > div.row.stat-card.affil-profile-card.mb-6 > div:nth-child(2) > div > div > div.stat-num::text').extract(),
            'journal' : response.css('body > div > div.col-md-8 > div.content > div > div.row.stat-card.affil-profile-card.mb-6 > div:nth-child(3) > div > div > div.stat-num::text').extract(),            
            'sinta_score_overall' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(2) > div.pr-num::text').extract(),            
            'sinta_3yr_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(4) > div.pr-num::text').extract(),            
            'sinta_productivity_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(6) > div.pr-num::text').extract(),            
            'sinta_3yr_productivity_score' : response.css('body > div > div.col-md-8 > div.content > div > div.stat-profile > div > div:nth-child(8) > div.pr-num::text').extract(),            
            'scopus_q1' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[1393:-2186].replace(' ', '').replace(',\r\n', ''),
            'scopus_q2' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[1513:-2063].replace(' ', '').replace(',\r\n', ''),
            'scopus_q3' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[1633:-1940].replace(' ', '').replace(',\r\n', ''),
            'scopus_q4' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[1753:-1817].replace(' ', '').replace(',\r\n', ''),
            'scopus_undefined_q' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[1873:-1697].replace(' ', '').replace(',\r\n', ''),
            'scopus_ro_article' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[3127:-424].replace(' ', '').replace(',\r\n', ''),
            'scopus_ro_conference' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[3132:-400].replace(' ', '').replace(',\r\n', ''),
            'scopus_ro_other' : response.css('body > script:nth-child(21)::text').extract()[0].strip()[3170:-386].replace(' ', '').replace(',\r\n', ''),
            'scopus_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.text-warning::text').extract(),            
            'scopus_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(2) > td.text-warning::text').extract(),            
            'scopus_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.text-warning::text').extract(),            
            'scopus_citation_researcher' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td.text-warning::text').extract(),            
            'gs_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.text-success::text').extract(),            
            'gs_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(2) > td.text-success::text').extract(),            
            'gs_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.text-success::text').extract(),            
            'gs_citation_researcher' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td.text-success::text').extract(),            
            'wos_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.text-primary::text').extract(),            
            'wos_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(2) > td.text-primary::text').extract(),            
            'wos_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.text-primary::text').extract(),            
            'wos_citation_researcher' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td.text-primary::text').extract(),                
            'garuda_article' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td.text-danger::text').extract(),            
            'garuda_citation' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(2) > td.text-danger::text').extract(),            
            'garuda_cited_document' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(3) > td.text-danger::text').extract(),            
            'garuda_citation_researcher' : response.css('body > div > div.col-md-4.d-none.d-md-block.d-lg-block.d-xl-block.decor.animate__animated.animate__slideInRight > div.side-content > div:nth-child(2) > div > table > tbody > tr:nth-child(4) > td.text-danger::text').extract(),            
        }

    