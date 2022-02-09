from models import (Base, session, Book, engine)


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1) Add book
        \r2) View all books
        \r3) Search for book
        \r4) Book analysis
        \r5) Exit''')
        choice = input("\nWhat would you like to do? ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            "Choose an option from above by entering a number from 1-5 and pressing Enter"
# import models
# main menu - add, search, analysis, exit, view
# add books to db
# edit books
# delete books
# search funct
# data cleaning functions
# loop that runs programven 


if __name__ == '__main__':
    Base.metadata.create_all(engine) # initialize db
    menu()