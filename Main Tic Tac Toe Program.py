import turtle
import math

#This function draws the grid the game will be played on
def drawBoard():
    #Draws both of the horizontal lines, starting from different heights
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    #Draw both of the vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)

    #Add numbers to the top corner of each square
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()

            drawer.write(num, font=("Arial", 12))
            num += 1
    #Update the screen with new changes
    screen.update()


#This Function draws an "x" centered at the inputted coordinates
def drawX(x, y):
    #Move to the correct spot
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    drawer.setheading(60)

    #draw the lines of the x
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    #Update the screen
    screen.update()


#This function draws an "x" centered at the inputted coordinates
def draw0(x, y):
    #Move to the correct spot
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()

    drawer.setheading(0)

  #Draw a circle with the correct size
    for i in range(180):
      drawer.forward((150 * math.pi)/180)
      drawer.right(2)

    #Update the screen
    screen.update()

#This function will check if the inputted player won
def checkWon(letter):
  #Check if there are three in a row horizontally
  for i in range(3):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
      return True
    
    if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
      return True

    #Check if there are three in a row diagonally down
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
       return True

     #Check if there are three in a row diagonally up
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
       return True

    #If at this point, the given letter has not won
    return False
  #Check what the value of count was
  #This function checks if the game is a tie
def checkDraw():
  #Count the number of x's on the board
  count = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] == "x":
        count += 1
  
  if count > 3:
    return True
  else:
    return False
    #This Function will add an o to the board in the best place

def add0():
  #Check if any places would result in a win for o 
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "o"
        if checkWon("o"):
          draw0(-200 + 200 * j, 200 - 200 * i)
          return
        board[i][j] = " "

 # Check if there is any place that o should block x 
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "x"
        if checkWon("x"):
          board[i][j] = "o"
          draw0(-200 + 200 * j, 200 - 200 * i)
          return
        board[i][j] = " "

  #Try to place an o in one of the corners
  for i in range(0, 3, 2):
    for j in range(0, 3, 2):
      if board[i][j] == " ":
        board[i][j] = "o"
        draw0(-200 + 200 * j, 200 - 200 * i)
        return

  #Place an o in any open spot
  for i in range(3):
    for j in range():
      if board[i][j] == " ":
        board[i][j] = "o"
        draw0(-200 + 200 * j, 200 - 200 * i)
        return


      #This function activates all the event listeners
def activate(functions):
  for i in range(9):
    screen.onkey(functions[i], str(i + 1))

#This function deactivates all event listeners
def deactivate(functions):
  for i in range(9):
    screen.onkey(None, str(i + 1))

#This function will try to add an x to the inputted location
def addX(row, column):
  #Clear any announcements on the screen
  announcer.clear()

  #Check if the space they want to add to is full
  if board[row][column] == "x" or board[row][column] == "o":
    #Tell them they cant take that spot
    announcer.write("That spot is taken!", font = ("Arial", 36))
    screen.update()
  else:
    #Draw an x in the correct spot
    drawX(-200 + 200 * column, 200 - 200 * row)

    #Add an x to the computers board
    board[row][column] = "x"

    #Check if that new x made x win
    if checkWon("x"):
      #Tell the user they won
      announcer.goto(-97, 0)
      announcer.write("You Won!", font = ("Arial", 36))

      #Update the screen and deactivate the event listeners
      screen.update()
      deactivate()
    else:
      #If they didnt win, then an o gets added to the board
      add0()

      #Check if that new o made o win
      if checkWon("o"):
        #Tell the player that they lost
        announcer.goto(-90, 0)
        announcer.write("You lost!", font = ("Arial", 36))

        #Update the screen and deactivate the event listeners
        screen.update()
        deactivate()
      #Check if theres a tie
      elif checkDraw():
        #Tell the player they tied with the computer
        announcer.goto(-90, 0)
        announcer.write("Its a Tie!", font = ("Arial", 36))

       #Update the screen and deactivate the event listeners
        screen.update()
        deactivate()

#Define functions for the event listeners
def squareOne():
  addX(0 , 0)
def squareTwo():
  addX(0 , 1)
def squareThree():
  addX(0 , 2)
def squareFour():
  addX(1 , 0)
def squareFive():
  addX(1 , 1)
def squareSix():
  addX(1 , 2)
def squareSeven():
  addX(2 , 0)
def squareEight():
  addX(2 , 1)
def squareNine():
  addX(2 , 2)

#Create a list of event listener functions
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive, squareSix, squareSeven, squareEight, squareNine]
#Create turtle
drawer = turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")

#Create screen
screen = turtle.Screen()
screen.tracer(0)

#Draw the Board
drawBoard()

#Create the board
board = []
for i in range (3):
  row = []
  for j in range(3):
    row.append(" ")
  board.append(row)

#Activates the event listeners
activate(functions)
screen.listen()


