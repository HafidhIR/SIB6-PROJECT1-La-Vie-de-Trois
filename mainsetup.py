from module.book import Book
from module.magazine import Magazine
from module.cd import Cd 
from module.dvd import Dvd

book1 = Book(
    title='Test book',
    upc='',
    subject='this is subject',
    issbn = '',
    authors= '',
    dds_number = '')

print(book1.title)

magazine1 = Magazine(
    title='Test Magazine',
    upc='',
    subject='',
    volume='',
    issue='')

print(magazine1.title)