# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3


class ScrapygithubPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = sqlite3.connect("github.db")
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS content""")
        self.cur.execute("""CREATE TABLE content 
                           (name_rep TEXT, about TEXT, link_site TEXT,
                            stars TEXT, forks TEXT, watching TEXT,
                            commits TEXT, commit_author TEXT, commit_name TEXT,
                            commit_datetime TEXT, releases TEXT, release_version TEXT,
                            release_datetime TEXT )""")

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.cur.execute("""INSERT OR IGNORE INTO content VALUES (?,?,?,
                                                                  ?,?,?,
                                                                  ?,?,?,
                                                                  ?,?,?,
                                                                  ?)""",
                         (item["name_rep"], item["about"], item["link_site"],
                          item["stars"], item["forks"], item["watching"],
                          item["commits"], item["commit_author"], item["commit_name"],
                          item["commit_datetime"], item["releases"], item["release_version"],
                          item["release_datetime"]))
        self.con.commit()
