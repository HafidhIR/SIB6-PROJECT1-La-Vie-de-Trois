from module.book import Book
from module.magazine import Magazine
from module.cd import Cd
from module.dvd import Dvd

class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if type (item) is Magazine:
                        list_result.append(f'Title:{item.title}, volume: {item.volume}, type Catalog: Magazine')
                    elif type (item) is Book:
                        list_result.append(f'Title:{item.title}, DDS Number: {item.dds_number}, type Catalog: Book')
                    elif type (item) is Cd:
                        list_result.append(f'Title:{item.title}, Artist: {item.artist}, type Catalog: Cd')
                    elif type (item) is Dvd:
                        list_result.append(f'Title:{item.title}, Genre: {item.genre}, type Catalog: Dvd')
        return list_result
