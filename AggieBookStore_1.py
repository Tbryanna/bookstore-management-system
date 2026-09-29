#Trinity Martin
#October 1, 2024
#Comp163.001

inventory = {}

genreList = []
# Creating a list with genre names as the elements
genre = ['Fiction', 'Narrative', 'Mystery', 'Biography', 'Science Fiction', 'Fantasy' ]
print('Welcome to the Aggie Book Store')

# Creating prompts for the user to input an int
fiction = int(input('What is the inventory count of Fiction: '))
narrative = int(input('What is the inventory count of Narrative: '))
mystery = int(input('What is the inventory count of Mystery: '))
biography = int(input('What is the inventory count of Biography: '))
science_fiction = int(input('What is the inventory count of Science Fiction: '))
fantasy = int(input('What is the inventory count of Fantasy: '))


print('\nWe offer the following genre:')

# if statements that will execute if the condition is true from the inputted numbers
if fiction>0:
    print('Fiction')
if narrative>0:
    print('Narrative')
if mystery>0:
    print('Mystery')
if biography>0:
    print('Biography')
if science_fiction>0:
    print('Science Fiction')
if fantasy>0:
    print('Fantasy')
if fiction<=0 and narrative<=0 and mystery<=0 and biography<=0 and science_fiction<=0 and fantasy<=0:
    print('Sorry we have no genres in our inventory')




f'What is the inventory count of {g}: '
f'What is the {n} book title:'
