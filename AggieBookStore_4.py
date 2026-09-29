#Trinity Martin
#November 24, 2024
#Comp163.001
#I am creating and importing classes as well as reading a csv file to display information depending on the choice.


import csv #importing the csv file
#importing the Book and Author classes
from Book import Book
from Author import Author

#Displays the genre options to chose from
def displayMenu(options):
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    print(f"{len(options) + 1}) Exit")

    choice = int(input("Enter your choice: "))
    if choice == len(options) + 1:
        return "Exit"
    else:
        return options[choice - 1]

#Displays the genre chosen along with the inventory total and price total based on the inventory
def displayGenreInv(genreOption, booksList):
    print(f'{genreOption}')
    header = ["Author", "Title", "Published", "QTY", "Price"]
    print(f"\t{header[0]:<20}{header[1]:<30}{header[2]:<9} {header[3]:<5}{header[4]:<5}")

    items = inventory.get(options)
    total_qty = 0
    total_value = 0.00
    #Loop through each book in the selected genre
    for book in booksList:
        author_name = book.getAuthor().getName()
        price = book.getPrice()
        if price == 18.00:
            newPrice = f'{price:.1f}'
        else:
            newPrice = f'{price:.2f}'

        item = (author_name, book.getTitle(),book.getQuantity(), newPrice)
        print(f"\t{item[0]:<20}{item[1]:<30}{'2024':<10}{item[2]:<5}{item[3]:<20}")
        total_qty += book.getQuantity()
        total_value += book.getPrice() * book.getQuantity()

    print('\t'+f'='*33)
    print(f'\tInventory count {total_qty} : Total ${total_value:.2f}\n')

#Reads the csv file into a dictionary
def readInv(file):
    inventory = {}
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Loop through each row in the CSV file
        for row in csv_reader:
            genre, fname, mname, lname, title, dob, year, cost, qty, isbn = row
            cost = float(cost)
            qty = int(qty)

            author = Author(fname, lname, mname, dob)
            book = Book(genre, title, author, cost, qty, isbn, year)

            #Add the book to the genre list in the inventory dictionary
            if genre not in inventory:
                inventory[genre] = []
            inventory[genre].append(book)
    return inventory
file = input("Enter inventory file: ")
inventory = readInv(file)
genres = list(inventory.keys())


options = displayMenu(genres)
if options == "Exit":
    print("\nAggie Book Store\nGood Bye")

else:
    displayGenreInv(options, inventory[options])