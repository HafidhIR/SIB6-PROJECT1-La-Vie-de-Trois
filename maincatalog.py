from module.book import Book
from module.magazine import Magazine
from module.cd import Cd
from module.dvd import Dvd
from module.catalog import Catalog
import json

f = open('catalog/catalog.json')
data_json = json.load(f)
books = []
magazines = []

for item in data_json:
    if item ['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            Magazine(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                volume=item['volume'],
                issue=item['issue']
            )
        )


catalog_all = [books, magazines]
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index , result in enumerate(results):
    print(f'resukt ke-{index+1} | {result}')