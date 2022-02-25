import os
import random


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
    input("Press enter to start...")
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

def adding_mines(grid):
    counter=0    
    while counter<mines:
        x = random.randint(0,columns-1)
        y = random.randint(0,rows-1)
        if grid[y][x]!=9:
            grid[y][x]=9
            counter+=1
    return grid

def place_clues(grid):
    row = len(grid[0])
    col = len(grid[row-1])
    for y in range(row):
        for x in range(col):
            if grid[y][x]==9:
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0<= y+i <= row-1 and 0<= x+j <= col-1:
                            if grid[y+i][x+j]!=9:
                                grid[y+i][x+j]+=1
    return grid

def show_white_cells(grid, user_grid, y,x):
    row = len(grid[0])
    col = len(grid[row-1])
    whites=[(y,x)]
    while len(whites) >0:
        y, x= whites.pop()
        for i in [-1,0, 1]:
            for j in [-1,0,1]:
                if 0<= y+i <= row-1 and 0<= x+j <= col-1:
                    if grid[y+i][x+j]==0 and user_grid[y+i][x+j]=="-":
                        user_grid[y+i][x+j]=" "
                        if (y+i, x+j) not in whites:
                            whites.append((y+i, x+j))
                    else:
                        user_grid[y+i][x+j]=grid[y+i][x+j]
                    if user_grid[y+i][x+j]==0:
                        user_grid[y+i][x+j] = " "                        

    return user_grid

def board_completed(grid):
    row = len(grid[0])
    col = len(grid[row-1])
    for y in range(row):
        for x in range(col):
            if grid[y][x]=="-" or grid[y][x]=="X":
                return False
    return True


#GAME 
columns, rows, mines = game_presentation()
instructions()

grid= creating_grid(columns, rows, 0)
user_grid = creating_grid(columns, rows, "-")
adding_mines(grid)

#User position

x= random.randint(0, rows-1)
y= random.randint(0,columns-1)
real = user_grid[y][x]
user_grid[y][x] = "X"

os.system("cls")

show_grid(user_grid)

grid= place_clues(grid)


#Loop
flagged_mines=[]
play = True
while play:
    move = menu()
    if move=="a":
        if x==0:
            x=0
        else:
            user_grid[y][x]=real
            x= x-1
            real= user_grid[y][x]
            user_grid[y][x] = "X"
    elif move =="d":    
        if x==columns-1:
            x=columns-1
        else:
            user_grid[y][x]=real
            x= x+1
            real= user_grid[y][x]
            user_grid[y][x] = "X"
    elif move == "w":
        if y==0:
            y=0
        else:
            user_grid[y][x]=real
            y= y-1
            real= user_grid[y][x]
            user_grid[y][x] = "X"
    elif move == "s":
        if y==rows-1:
            y=rows-1
        else:
            user_grid[y][x]=real
            y= y+1
            real= user_grid[y][x]
            user_grid[y][x] = "X"

    elif move == "f":
        if real =="F":
            user_grid[y][x]= "-"
            real = user_grid[y][x]
        elif real =="-":
            user_grid[y][x]= "F"
            real = user_grid[y][x]    

    elif move == "o":
        if grid[y][x]== 9:
            user_grid[y][x] = "*"            
            play=False
            os.system("cls")
            show_grid(user_grid)
            print("GAME OVER!!")
            break            
        
        elif grid[y][x]== 0:
            user_grid[y][x]= str(" ") 
            user_grid = show_white_cells(grid, user_grid, y,x)
            real=" "
        elif grid[y][x]!= 9: 
            user_grid[y][x]=grid[y][x]
            real= user_grid[y][x]

    if board_completed(user_grid):  
        os.system("cls")
        show_grid(user_grid)      
        print("CONGRATULATIONS!! YOU WIN!!")
        break
        

    os.system("cls")

    show_grid(user_grid)

    
    
    