
class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price

        self.no_of_pages = no_of_pages

    def display_info(self):
        print("Publisher:", self.name)
        print("Title:", self.title)

        print("Author:", self.author)
        print("Price:", self.price)
        print("Number of Pages:", self.no_of_pages)


publisher_name = input("Enter the publisher's name: ")
book_title = input("Enter the book title: ")
book_author = input("Enter the book author: ")
book_price = float(input("Enter the book price: "))

book_pages = int(input("Enter the number of pages: "))

python_book = Python(publisher_name, book_title, book_author, book_price,book_pages)

python_book.display_info()

    
        
