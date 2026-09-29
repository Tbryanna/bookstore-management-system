#Trinity Martin
#September 30 ,2024
#Comp163.001
#In this assignment I am modifying my code including nested loops and nested data types
inventory = {}
# Creating a list with genre names as the elements
genre = ['Fiction', 'Narrative', 'Mystery', 'Biography', 'Science Fiction', 'Fantasy' ]

for g in genre:
    genre_count = int(input())
    genreList = [] #Reset list for each genre
    n=0 #Reset counter for book titles for each genre
    while n < genre_count:
        n+=1
        titles = input()
        genreList.append(titles) #Add each title to the current genre's list

    inventory[g] = genreList #Store the list in the inventory for each genre
    
#Outputs the titles for each genre
print('We offer the following genre book titles:')

for g in genre:
    print(f'{g}')
    if len(inventory[g]) > 0:
        for title in inventory[g]:
            print(f'\t{title}')
    else:
        print('\tSorry we have no books in our inventory.')









