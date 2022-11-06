# book ISBN from book title
def isbn_search():
    !pip install isbntools 
    from isbntools import *
        
    def isbnFinder(bookTile):
        book_isbn = isbn_from_words(bookTitle)
        print("Book Name: ", bookTitle, "\nISBN: ", book_isbn)

    # user input book title
    print("\nPlease Enter the Book Title Properly to Get the ISBN of Your Required Book :)")
    bookTitle = input("\nEnter the Book Title:\t")
    isbnFinder(bookTitle)
