import scrapy


class SintaSpider(scrapy.Spider):
    name = 'sinta'
    start_urls = ['https://sinta.kemdikbud.go.id/affiliations/authors/414?page=1']

    def parse(self, response):
        raw_image_urls = response.css('.univ-name img ::attr(src)').getall()
        clean_image_urls = []
        test = ['https://scholar.googleusercontent.com/citations?view_op=small_photo&user=ZjfgPLMAAAAJ&citpid=13']
        for img_url in test:
            clean_image_urls.append(response.urljoin(img_url))

        # print(clean_image_urls)
        yield {
            'image_urls' : clean_image_urls
        }
               




