class library:
    def __init__(self, books):
        self.books = books

    def listbooks(self):
        print('Available books : ')
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("You get the book")
            self.books.remove(borrow_book)
        else:
            print("This is not available")

    def receive_book(self, receive_book):
        print("You have returned the book")
        self.books.append(receive_book)


books = ['c++', 'python', 'java', 'java script', 'c#']
o = library(books)
msg = """ 
          1. DISPLAY BOOKS
          2. BORROW BOOKS
          3. RETURN BOOKS
          4. QUIT
"""

while True:
    print("_____________LIBRARY MANAGEMENT SYSTEM_____________")
    print(msg)
    ch = int(input("Choose the option: "))
    if ch==1:
        o.listbooks()

    elif ch==2:
        book = input("Enter the book to borrow: ")
        o.borrow_book(book)
    elif ch==3:
        book = input("Enter the book to return: ")
        o.receive_book(book)
    else:
        print("\n\t\tThank you come again")
        quit()


