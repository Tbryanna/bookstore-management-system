#importing the item and author class
from Item import Item
from Author import Author
import string

#inheriting the item class
class Book(Item):
    _Genre : string
    _Title : string
    _Author : Author
    _ISBN : string
    _Year : string

    def __init__(self, Genre, Title, Author, Price, Qty, ISBN, YearPublished):
        super().__init__('Book', Price , Qty) #getting the Item class attibutes
        self._Title = Title
        self._Genre = Genre
        self._Author = Author
        self._ISBN = ISBN
        self._Year = YearPublished

#encasuplating the variables
    def getTitle(self): return self._Title
    def getGenre(self): return self._Genre
    def getAuthor(self): return self._Author
    def getISBN(self): return self._ISBN
    def getYear(self): return self._Year
