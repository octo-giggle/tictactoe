#!/usr/bin/python
import turtle
import time

#setting turtle graphic
wn = turtle.Screen()
ei = turtle.Turtle()
wn.setup(600,600)
wn.bgcolor("black")
wn.title("TIC-TAC-TOE")
ei.color("white")
ei.speed(0)

#setting check-win table
check = ['', '', '',
         '', '', '',
         '', '', '']

#drawing table
def table(ei):
    ei.color("slategray")
    ei.pensize(10)
    ei.penup() #paral_down
    ei.setposition(0,-100)
    ei.pendown()
    ei.forward(300)
    ei.backward(600)
    ei.penup() #paral_up
    ei.setposition(0,100)
    ei.pendown()
    ei.forward(300)
    ei.backward(600)
    ei.penup() #ver_left
    ei.setposition(-100,0)
    ei.pendown()
    ei.left(90)
    ei.forward(300)
    ei.backward(600)
    ei.penup() #ver_right
    ei.setposition(100,0)
    ei.pendown()
    ei.forward(300)
    ei.backward(600)

#drawing 'x'
def X(ei, x, y):
    ei.color("slategray")
    ei.pensize(10)
    ei.setposition(x,y)
    ei.pendown()
    ei.left(45)
    ei.forward(90)
    ei.backward(180)
    ei.forward(90)
    ei.left(90)
    ei.forward(90)
    ei.backward(180)
    ei.right(135)
    ei.penup()

#drawing 'o'
def O(ei, x, y):
    ei.color("slategray")
    ei.pensize(10)
    ei.penup()
    ei.setposition(x+75,y)
    ei.pendown()
    ei.circle(75)
    ei.penup()

#drawing win line
def winrow(ei, x, y):
    ei.color("linen")
    ei.pensize(10)
    ei.penup()
    ei.setposition(x, y)
    ei.left(90)
    ei.pendown()
    ei.forward(300)
    ei.backward(600)
    ei.pendown()

def wincolumn(ei, x, y):
    ei.color("linen")
    ei.pensize(10)
    ei.penup()
    ei.setposition(x, y)
    ei.pendown()
    ei.forward(300)
    ei.backward(600)

def winparal(ei, x, y, s):
    ei.color("linen")
    ei.pensize(10)
    ei.penup()
    ei.setposition(x, y)
    ei.right(s)
    ei.pendown()
    ei.forward(410)
    ei.backward(820)

#setting game logic
i = 0

def clicked(x, y):

    global check, i

    #defining square
    ei.penup()
    ei.goto(x, y)
    column = (x + 300) // 200
    row = (-y + 300) // 200
    square = column + row*3
    square = int(square)
    print("you clicked", x, ",", y, " square ", square)

    #setting position 'x' and 'o' (depending on field)
    field = [(-200,200), (0,200), (200,200),
             (-200,0), (0,0), (200,0),
             (-200,-200), (0,-200), (200,-200)]

    #drawing 'x' and 'o' (in turn), limiting one symbol per field
    while True:

        index = square
        x, y = field[index]

        if (check[index] == ''):
            if i % 2 == 0:
                check[index] = 'O'
                O(ei, x, y)
                if_win(i, check)
            else:
                check[index] = 'X'
                X(ei, x, y)
                if_win(i, check)
            i+=1

            #checking if gameover
            if i == 9:
                if_win(i, check)
                print("i guess we have 2 losers, soz mah dudes")
                input()
                exit(0)
            break
        else:
            print("try again")
            break


def if_win(i, check):

    #checking win - row
    for i in range(3):
        if (check[i*3] == check[i*3+1] == check[i*3+2] != ''):
            print("congrats")
            if i == 0:
                winrow(ei, 0, 200)
            elif i == 1:
                winrow(ei, 0, 0)
            else:
                winrow(ei, 0, -200)
            input()
            exit()

    #checking win - column
    for i in range(3):
        if (check[i] == check[i+3] == check[i+6] != ''):
            print("congrats")
            if i == 0:
                wincolumn(ei, -200, 0)
            elif i == 1:
                wincolumn(ei, 0, 0)
            else:
                wincolumn(ei, 200, 0)
            input()
            exit()

    #checking win - diagonally
    if (check[0] == check[4] == check[8] != ''):
        print("congrats")
        winparal(ei, 0, 0, 315)
        input()
        exit()
    elif (check[2] == check[4] == check[6] != ''):
        print("congrats")
        winparal(ei, 0, 0, 45)
        input()
        exit()


def main():
    global index
    table(ei)
    turtle.onscreenclick(clicked)
    wn.mainloop()

if __name__ == '__main__':
    main()
