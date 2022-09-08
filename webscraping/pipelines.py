# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from google.cloud import bigquery
from webscraping.credentials import Credentials
# from itemadapter import ItemAdapter


class TheGuardianPipeline:

    def __init__(self):
        self.TABLE_ID = "<<PUT YOUR TABLE HERE>>"
        self.items = set()
        self.client = bigquery.Client.from_service_account_json(Credentials.credentials)

    def process_item(self, item, spider):
        # aqui acontece data cleansed, deduplicaçoes, etc...
        item['text'] = ' '.join(item['text'])
        item['tags'] = ','.join(item['tags'])

        self.client.insert_rows_json(self.TABLE_ID, [dict(item)])

        return item
