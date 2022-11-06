# book info from ISBN
def book_info():
    #!pip install isbntools
    import sys # sys module provides information about constants, functions and methods of the Python interpreter
    #from isbntools.app import *

    def bookInfo(bookISBN):
        print(registry.bibformatters['labels'](meta(bookISBN)))

    # user input ISBN of book to get book information
    print("Please Enter the Book ISBN-13 or ISBN-10 Properly to Get the Information of Your Required Book. :) \nKeep in mind that if you give ISBN-10 then book information in return you get ISBN-13.")
    bookISBN = input("Enter the Book ISBN:\t")
    bookInfo(bookISBN)
