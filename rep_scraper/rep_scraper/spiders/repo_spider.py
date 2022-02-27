import scrapy


class GitSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = [
        "https://github.com/scrapy",
    ]

    def parse(self, response, **kwargs):
        yield response.follow(url=f'https://github.com/orgs/scrapy/repositories',
                              callback=self.parse_repo)

    def parse_repo(self, response):
        for name in response.css("div.Box ul a.d-inline-block::attr(href)").getall():
            yield response.follow(url=f'https://github.com{name}', callback=self.parse_repo_content)

    def parse_repo_content(self, response):
        yield {
            'name-rep': response.css("strong.mr-2 a::text").get(),
            'about': response.css("p.my-3::text").get(default='None').strip(),
            'link-site': response.css('span.flex-auto a.text-bold::text').get('None'),
            'stars': response.css("a.Link--muted strong::text").getall()[0],
            'forks': response.css("a.Link--muted strong::text").getall()[2],
            'watching': response.css("a.Link--muted strong::text").getall()[1],
        }