class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        return f"The Book '{self.title}' by {self.author} was published in {self.year}."

book = Book("Ramayan", "valmiki", 1800)
print(book.get_description())
