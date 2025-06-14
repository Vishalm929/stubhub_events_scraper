import scrapy


class SportsSpider(scrapy.Spider):
    name = "sports"
    allowed_domains = ["stubhub.com"]
    start_urls = [
        "https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={"playwright": True,          # Enables Playwright rendering
                       "playwright_include_page": True}, # Gives access to the page object in the response
                callback=self.parse       # Calls the async parser method below
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.wait_for_selector("div.sc-9b40ed01-5")
        await page.close()

        # Select top 5 event containers
        events = response.css("div.sc-9b40ed01-5")[:5]
        for event in events:
            link_elem = event.xpath("../../..")
            # event_url = response.urljoin(link_elem.css("::attr(href)").get())

            title = event.css("p.sc-9b40ed01-6::text").get()
            details = event.css("p.sc-9b40ed01-8::text").getall()
            datetime = details[0] if len(details) > 0 else None
            location = details[1] if len(details) > 1 else None

            image = link_elem.css("img::attr(src)").get()

            yield {
                "title": title,
                "datetime": datetime,
                "location": location,
                "image": image,
                # "event_url": event_url,
            }
