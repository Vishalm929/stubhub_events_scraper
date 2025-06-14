# settings.py
BOT_NAME = "stubhub_events"

SPIDER_MODULES = ["stubhub_events.spiders"]
NEWSPIDER_MODULE = "stubhub_events.spiders"

ROBOTSTXT_OBEY = True

# Playwright download handler
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Output in JSON
FEEDS = {
    "sports_events.json": {"format": "json", "overwrite": True},
}

PLAYWRIGHT_BROWSER_TYPE = "chromium"
