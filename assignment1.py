"""
Replace the contents of this module docstring with your own details
Name:Zar Chi Oo
Date started:12/12/2022
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-ZarChi123.git
"""
from operator import itemgetter

FILENAME = "books1.csv"


def main():
    books = []
    print("Reading Tracker 1.0 - Zar Chi Oo")
    menu_string = "Menu:\nL-List all books\nA-Add new book\nM-Mark a book as completed\nQ-Quit"
    get_books(FILENAME, books)
    if len(books) > 0:
        print("{} books loaded".format(len(books)))
        print(menu_string)
        choice = input(">>>")
        while choice != "Q":
            if choice == "L":
                list_books(books)
            elif choice == "A":
                pass
            elif choice == "M":
                pass
            print(menu_string)
            choice = input(">>>")
        print("Finish")


def list_books(books):
    """Print list of books sorted by author and title"""
    print(books)
    books.sort(key=itemgetter(1, 0))
    print(books)


def get_books(filename, books):
    """Read the book csv file and split them into separate details"""
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            for line in in_file:
                # print(line)
                # print(type(line))
                book_details = line.strip().split(",")
                books.append(list(line))
                # print(book_details)
                # print(type(book_details))
    except FileNotFoundError:
        print(f"The file \"{filename}\" was not found!")


main()
