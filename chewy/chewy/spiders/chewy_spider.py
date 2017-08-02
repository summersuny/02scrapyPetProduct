from chewy.items import ChewyItem
from scrapy import Spider, Request

class ChewySpider(Spider):
	name='chewy_spider'
	allowed_urls=['https://www.chewy.com']	
	start_urls=['https://www.chewy.com/b/food-332']
	index = 1

	def parse(self,response):
		print ("Crawling page "+str(self.index))
		
		links=response.xpath('.//article[@class="product-holder  cw-card cw-card-hover"]/a/@href').extract()
		for link in links:
			url='https://www.chewy.com'+link
			request = Request(url,callback=self.parse_detail)
			request.meta['page'] = self.index
			yield request

		self.index = self.index + 1

		next_link = response.xpath('.//li[@class="next "]/a/@href').extract_first()
		if type(next_link) == type(''):
			url='https://www.chewy.com'+next_link
			yield Request(url,callback=self.parse)
		else:
			print("waiting for pending tasks")


	def parse_detail(self,response):
		category=response.xpath('.//nav[@class="breadcrumbs container"]//li/a/text()').extract()
		name=response.xpath('.//div[@id="product-title"]/h1/text()').extract_first()
		brand=response.xpath('.//div[@id="brand"]/a/text()').extract_first()
		rating=response.xpath('.//div[@class="ugc ugc-head"]//img/@src').extract_first()
		reviews_number=response.xpath('.//div[@class="ugc ugc-head"]//span/text()').extract_first()
		price=response.xpath('.//span[@class="ga-eec__price"]/text()').extract_first()
		unit=response.xpath('.//span[@class="attribute-selection__value js-selection-value"]/text()').extract_first()
		ingredient=response.xpath('.//div[@class="cw-bullets"]//tbody//td/text()').extract()

		
		item=ChewyItem()
		#if type(price) == type(None):
		#	print("response:")
		#	print(response)
		#	print(response.body)

		item['category']=category
		item['name']=name
		item['brand']=brand
		item['rating']=rating
		item['reviews_number']=reviews_number
		item['price']=price
		item['unit']=unit
		item['ingredient']=ingredient
		item['page'] = response.meta['page']

		yield item	



