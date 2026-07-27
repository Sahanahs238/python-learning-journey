class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def Show_methods(self):
        print("Title:",self.title)
        print("author:",self.author)
        print("price:",self.price)

book1=Book("love","idk",150)
book1.Show_methods()