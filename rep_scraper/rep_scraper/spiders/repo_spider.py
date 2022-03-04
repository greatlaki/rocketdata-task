import scrapy


class GitSpider(scrapy.Spider):
    handle_httpstatus_list = [404, 500]

    name = "github"
    allowed_domains = ["github.com"]
    start_urls = [f'https://github.com']

    some_link = input("Greet! Enter your link(user or project)- ")
    some_list = []

    def parse(self, response, **kwargs):
        yield response.follow(url=f'https://github.com/orgs/{GitSpider.some_link}/repositories',
                              callback=self.page_validation)

    def page_validation(self, response):
        if response.status in self.handle_httpstatus_list:
            yield response.follow(url=f'https://github.com/{GitSpider.some_link}?tab=repositories',
                                  callback=self.parse_user)
        else:
            yield response.follow(url=f'https://github.com/orgs/{GitSpider.some_link}/repositories?page=1',
                                      callback=self.parse_project)

    def parse_user(self, response):

        if "Next" not in response.css("div.BtnGroup a::text").getall() and len(
                response.css("div.BtnGroup a::text").getall()) < 2:
            GitSpider.some_list.extend(response.css("h3.wb-break-all a::attr(href)").getall())
            for get_repository in GitSpider.some_list:
                yield response.follow(url=f'https://github.com{get_repository}', callback=self.parse_repo_content)
        else:
            GitSpider.some_list.extend(response.css("h3.wb-break-all a::attr(href)").getall())
            if len(response.css("div.BtnGroup a::attr(href)").getall()) > 1:
                yield response.follow(url=response.css("div.BtnGroup a::attr(href)")[1].get(),
                                      callback=self.parse_user)
            else:
                yield response.follow(url=response.css("div.BtnGroup a::attr(href)").get(),
                                      callback=self.parse_user)

    def parse_project(self, response):
        for get in response.css("div.Box ul a.d-inline-block::attr(href)").getall():
            yield response.follow(url=f'https://github.com{get}', callback=self.parse_repo_content)

    def parse_repo_content(self, response):
        yield {
            'name_rep': response.css("strong.mr-2 a::text").get(),
            'about': response.css("p.my-3::text").get(default='None').strip(),
            'link_site': response.css('span.flex-auto a.text-bold::text').get('None'),
            'stars': response.css("a.Link--muted strong::text").getall()[0],
            'forks': response.css("a.Link--muted strong::text").getall()[2],
            'watching': response.css("a.Link--muted strong::text").getall()[1],
            'commits': response.css("span.d-none strong::text").get(),
            'commit_author': response.css("div.css-truncate a.commit-author::text").get(),
            'commit_name': response.css('span.d-none a::text').get(),
            'commit_datetime': response.css('a.Link--secondary relative-time::attr(datetime)').get(),
            'releases': response.css("h2.h4 span::text").get(default='0'),
            'release_version': response.css('div.d-flex span.mr-2::text').get(),
            'release_datetime': response.css('div.color-fg-muted relative-time::attr(datetime)').get(),
        }