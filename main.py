import sys


class Library:
    def __init__(self, books):
        self.books = books
        print("                                      ---------------Welcome to vellore library----------------                                      ")

    def display(self):
        print("Available books in library are:")
        for book in self.books:
            print(book)

    def borrow(self, requestbook):
        if requestbook in self.books:
            print("Congratulation your book is successfully borrowed :)")
            self.books.remove(requestbook)
        else:
            print("OOPS!!")
            print("This book is not available in library!!")

    def Return(self, returnbook):
        self.books.append(returnbook)
        print("Thanks for returning your borrowed book")


class Student:
    def requestbook(self):
        print("Enter the name of the book you want to borrow:")
        self.book = input()
        return self.book

    def returnbook(self):
        print("Enter the name of the book you to return:")
        self.book = input()
        return self.book


def main():
    library = Library(["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows", "A Tale of Two Cities", "The Little Prince", "And Then There Were None", "Suppandi", "THE GREAT GATSBY"])
    student = Student()
    done = False
    while done == False:
        print("""library system:
                  1. To display all book press "1"
                  2. To request book press "2"
                  3. To return book press "3"
                  4. To exit press "4"
                  """)
        Input = int(input("Enter input:"))
        if Input == 1:
            library.display()
        if Input == 2:
            library.borrow(student.requestbook())
        elif Input == 3:
            library.Return(student.returnbook())
        if Input == 4:
            sys.exit()
        if (Input > 4):
            print("Wrong input!!!")


main()
