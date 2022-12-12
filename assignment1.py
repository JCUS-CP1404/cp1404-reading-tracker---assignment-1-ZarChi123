"""
Replace the contents of this module docstring with your own details
Name:Zar Chi Oo
Date started:12/12/2022
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-ZarChi123.git
"""
import csv


def main():
    books = []
    print("Reading Tracker 1.0 - Zar Chi Oo")
    books = read_csv("books.csv")
    print("{} books loaded".format(len(books)))
    print_menu()
    choice = input(">>>")
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "A":
            pass
        elif choice == "M":
            pass
        print_menu()
        choice = input(">>>")
    print("Bye")


def read_csv(filename):
    """Read the book csv file"""
    books = []
    in_file = open(filename, "r")
    csv_file = csv.reader(in_file)
    for line in csv_file:
        books.append(list(line))
    in_file.close()
    return books


def print_menu():
    """Print the menu options """
    menu_options = "Menu:\nL-List all books\nA-Add new book\nM-Mark a book as completed\nQ-Quit"
    print(menu_options)


main()
