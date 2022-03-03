# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RepScraperItem(scrapy.Item):
    name_rep = scrapy.Field()
    about = scrapy.Field()
    link_site = scrapy.Field()
    stars = scrapy.Field()
    forks = scrapy.Field()
    watching = scrapy.Field()
    commits = scrapy.Field()
    commit_author = scrapy.Field()
    commit_name = scrapy.Field()
    commit_datetime = scrapy.Field()
    releases = scrapy.Field()
    release_version = scrapy.Field()
    release_datetime = scrapy.Field()

