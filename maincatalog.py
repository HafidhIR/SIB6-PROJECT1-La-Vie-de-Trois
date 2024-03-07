from module.book import Book
from module.magazine import Magazine
from module.cd import Cd
from module.dvd import Dvd

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
    number_of_tracks=10
)

print("CD Title:", cd1.title)

dvd1 = Dvd(
    title='Test DVD',
    upc='2468135790',
    director='Some Director',
    duration=120
)

print("DVD Title:", dvd1.title)
