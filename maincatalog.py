import json
from module.book import Book
from module.magazine import Magazine
from module.cd import Cd
from module.dvd import Dvd
from module.catalog import Catalog

# Membaca data dari file JSON
with open('catalog/catalog.json') as f:
    data_json = json.load(f)

books = []
magazines = []
dvds = []
cds = []

# Membuat objek berdasarkan data JSON
for item in data_json:
    if item['source'] == 'book':
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
    elif item['source'] == 'cd':
        cds.append(
            Cd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                artist=item['artist']
            )
        )
    elif item['source'] == 'dvd':
        dvds.append(
            Dvd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                directors=item['directors'],
                actors=item['actors'],
                genre=item['genre']
            )
        )

# Menggabungkan semua item ke dalam satu katalog
catalog_all = [books, magazines, cds, dvds]

# Membuat katalog
catalog = Catalog(catalog_all)

# Mencari item yang sesuai dengan kata kunci
input_search = 'test'
results = catalog.search(input_search)

# Mencetak hasil pencarian
for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')

book1 = Book(
    title='Test book',
    upc='1234567890',
    subject='Fiction',
    issbn='978-0-00-000000-0',
    authors='John Doe',
    dds_number='123.45'
)

print("Book Title:", book1.title)

magazine1 = Magazine(
    title='Test Magazine',
    upc='0987654321',
    subject='Science',
    volume='Vol. 1',
    issue='Issue 1'
)

print("Magazine Title:", magazine1.title)

cd1 = Cd(
    title='Test CD',
    upc='1357924680',
    artist='Some Artist',
)

print("CD Title:", cd1.title)

dvd1 = Dvd(
    title='Test DVD',
    upc='2468135790',
    directors='Some Director',
)

print("DVD Title:", dvd1.title)
