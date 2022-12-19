"""
Replace the contents of this module docstring with your own details
Name:Zar Chi Oo
Date started:12/12/2022
GitHub URL:https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-1-ZarChi123.git
"""
from operator import itemgetter
FILENAME = "books.csv"
INDEX_TITLE = 0
INDEX_AUTHOR = 1
INDEX_PAGE_COUNT = 2
INDEX_STATUS = 3


def main():
    """Main function of the reading tracker program"""
    books = []
    print("Reading Tracker 1.0 - Zar Chi Oo")
    menu_string = "Menu:\nL-List all books\nA-Add new book\nM-Mark a book as completed\nQ-Quit"
    get_books(FILENAME, books)
    if len(books) > 0:
        print("{} books loaded".format(len(books)))
        print(menu_string)
        choice = input(">>>").upper()
        while choice != "Q":
            if choice == "L":
                list_books(books)
            elif choice == "A":
                add_books(books)

            elif choice == "M":
                mark_complete(books)
            else:
                print("Invalid menu choice")
            print(menu_string)
            choice = input(">>>").upper()
        print("Finish")


def list_books(books):
    """Print list of books sorted by author and title"""
    book_count = 0
    required_page_count = 0
    required_book_count = 0
    books.sort(key=itemgetter(1, 0))
    for book in books:
        if book[INDEX_STATUS] == "r":
            print(
                f"*{book_count + 1:>1}. {book[INDEX_TITLE]:45} {'by ' + book[INDEX_AUTHOR]:20} {book[INDEX_PAGE_COUNT]:>5} pages.")

            required_book_count += 1
            required_page_count += int(book[INDEX_PAGE_COUNT])
        else:
            print(
                f"{book_count + 1:>2}. {book[INDEX_TITLE]:45} {'by ' + book[INDEX_AUTHOR]:20} {book[INDEX_PAGE_COUNT]:>5} pages.")
        book_count += 1

    if required_book_count == 0:
        print("No books left to read.Why not add a new book?")
    else:
        print(f"You need to read {required_page_count} pages in {required_book_count} books")


def has_required_book(books):
    """Check if there is any required book"""
    for book in books:
        if book[INDEX_STATUS] == "r":
            return True
    return False


def mark_complete(books):
    """Mark a user selected book as complete"""
    if has_required_book(books):
        list_books(books)
        book_number = get_valid_book_number("Enter the number of a book to mark as completed", books)
        mark_book_index = book_number - 1
        if books[mark_book_index][INDEX_STATUS] == "c":
            print("The book is already completed")
        else:
            books[mark_book_index][INDEX_STATUS] = "c"
            print(f"{books[mark_book_index][INDEX_TITLE]} by {books[mark_book_index][INDEX_AUTHOR]} completed!")
    else:
        print("No required books")


def get_valid_book_number(prompt, books):
    """Get a valid book number """
    print(prompt)
    book_number = get_valid_number(">>>")
    while book_number > len(books):
        print("Invalid book number")
        book_number = get_valid_number(">>>")
    return book_number


def add_books(books):
    """Add a new book to the list of books"""
    book_title = get_valid_string("Title:").title()
    author = get_valid_string("Author:").title()
    pages = get_valid_number("Pages:")
    new_book = [book_title, author, pages, "r"]
    books.append(new_book)
    print(f"{book_title} by {author},({pages}pages) added to the Reading Tracker")
    # print(books)


def get_valid_string(prompt):
    """Get a valid string from the user input"""
    input_string = input(prompt)
    while input_string.strip() == "":
        print("Input can not be blank")
        input_string = input(prompt)
    return input_string


def get_valid_number(prompt):
    """Get a valid number from the user input"""
    valid_input = False
    while not valid_input:
        try:
            input_string = int(input(prompt))
            if input_string <= 0:
                raise KeyError
            valid_input = True
        except ValueError:
            print("Invalid input;enter a valid number")
        except KeyError:
            print("Number must be >0")
    return input_string


def get_books(filename, books):
    """Read the book csv file and split them into separate details"""
    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            for line in in_file:
                # print(line)
                # print(type(line))
                book_details = line.strip().split(",")
                books.append(list(book_details))
                # print(book_details)
                # print(type(book_details))
    except FileNotFoundError:
        print(f"The file \"{filename}\" was not found!")


main()
