-  scrapy startproject Scrapy
-  cd Scrapy
-  scrapy genspider quotes quotes.com
	-  quotes is the name of spider, hence inside the class we give quotes as the name of spider
	-  Refer quotes_spider.py file
	 ![[Pasted image 20210906062247.png]]
-  To run spider, 
	-  scrapy crawl quotes
- To extract data with scrapy, scrapy is trying selectorsusing the scrapy shell. Run:
		- scrapy shell http://quotes.toscrape.com/page/1/


- quotes_spider.py
	- start_requests contain the urls to be scraped on
	- parse method in quotes_spider.py file is used to handle the responses which is downloaded for each request that is made
	
![[Pasted image 20210906061526.png]]
![[Pasted image 20210906062802.png]]
![[Pasted image 20210906062958.png]]
![[Pasted image 20210906070524.png]]
![[Pasted image 20210906071456.png]]