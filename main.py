class Book():

    def __init__(self, name, publication, genre, author, price):
        self.name = name
        self.publication = publication
        self.genre = genre
        self.autor = author
        self.price = price

    def show(self):
        print(f"It is book a: Book title - {self.name}, Autor name: {self.publication}, Genre a book: {self.genre}, Year of publication: {self.autor}, Price: {self.price}")

b = Book("The richest man in Babylon", "George Samuel Clayson", "Business Books", 1926, 230)
b.show()
