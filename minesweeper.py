import os


columns=0
rows=0
mines=0

#FUNCTIONS

def game_presentation():
    
    os.system("cls")
  
    print("Welcome to Minesweeper!!")
    print("Let's see if you can find all the mines. Are your ready??")
    print()
    print("Let's create the boardgame...")   
    col = int(input("Please enter the number of columns: "))
    row = int(input("Now enter the number of rows: "))    
    bomb = int(input("And now, how many mines do you want to find? "))
    return col, row, bomb
    
    
def instructions():
    
    os.system("cls")
    print("     To move:")
    print("             Up:    w")
    print("             Down:  s")
    print("             Right: d")
    print("             Left:  a")
    print()
    print("     To open the cell:")
    print("             Open:   o")
    print()
    print("     To flag a mine:")
    print("             Flag:   f")
    print()
    print("Press enter to start...")
    print()


def menu():
    print()
    print("Enter your move: ")
    selected = input("w/s/a/d - o - f ?")
    return selected

def creating_grid(columns, rows, val):
    grid=[]
    for i in range(rows):
        grid.append([])
        for j in range(columns):
            grid[i].append(val)
    return grid
    
def show_grid(grid):
    for row in grid:
        for elem in row:
            print(elem, end=" ")
        print()

def adding_mines():
    pass

def place_flag():
    pass

#Testing 

columns, rows, mines = game_presentation()
instructions()

print(columns)
print(rows)
print(mines)

grid= creating_grid(columns, rows, 0)
user_grid = creating_grid(columns, rows, "-")

show_grid(grid)
print()
show_grid(user_grid)