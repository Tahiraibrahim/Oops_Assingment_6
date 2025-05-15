# Assingment-11

# Create a class Book with a class variable total_books.
#  Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author =  author

        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
book1 = Book("Kite Runner", "Khalid Hossani")
book2 = Book("Thousands Splended Suns", "Khalid Hossani")
book3 = Book("Namal" , "Nimra Ahmed")

print("Total Books:", Book.get_total_books())
        
