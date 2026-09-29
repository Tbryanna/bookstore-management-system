#Trinity Martin
#October 27 ,2024
#Comp163.001
#In this assignment I am reading contents from other files and displaying them

import csv

inventory = {}

#Function to display the menu
def displayMenu(options):
    index = 1
    for option in options:
        print(f'{index}) {option}')
        index += 1
    print('6) Exit')
    choice = int(input('Enter your choice: '))
    if choice == 6:  # Exits the program if user chooses 6
        print('Aggie Book Store\nGood Bye')
        return None
    elif 1 <= choice <= len(options):
        return options[choice - 1]

#Function to read the genre text file into a list
def readGenre(genreFile):
    with open(genreFile, 'r') as file:
        options = file.readline().split()
    genres = [genre.strip() for genre in options] #Adds the read genres to the list
    return genres

#Function to add the inventory csv file to the dictionary from a list
def popInv(invList):
    for item in invList:
        genre, author, title, year, price = item
        inventory.setdefault(genre, []).append((title, author, year, float(price))) #Adds the data from the csv file to the dict

#Function to display genre inventory with the total count and price
def displayGenreInv(genreOption):
    print(f'{genreOption}')
    print(f'    {'Author':<20}{'Title':<30}{'Published':<9} {'Cost':<5}')
    books = inventory.get(genreOption, [])
    total_quantity = len(books)
    total_price = 0.0
    for title, author, year, price in books:
        total_price += price
        print(f'    {author:<20}{title:<30}{year:<9}{price:<5.2f}')
    equal = "================================="
    space = "    " + equal
    print(space)
    print(f'    Inventory count {total_quantity} : Total ${total_price:.2f}')

def readInv(): #Reads the csv file and places the data in a list
    data = []
    filename = 'Inventory1.csv'
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row) #Adds the data to the list
    return data

genres = readGenre(input('Enter genre file: '))
invList = readInv()
popInv(invList)


genreOption = displayMenu(genres)

displayGenreInv(genreOption)
