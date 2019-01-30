from turtle import *  #Importing every func from turtle file
from random import randint
speed(10)  #Speeding up the turtle
penup()  #Lifts up the pencil, so no markings are done
goto(-140,140)  #Goes to the specified location

for step in range(15): #Writes step no. at each 20 distance

    write(step,align='center')
    right(90)   #Change of direction
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada=Turtle()   #Creating a red turtle called Ada
ada.color('red')
ada.shape('turtle')

ada.penup()    #Moving Ada to starting point
ada.goto(-160,100)
ada.pendown()

bob=Turtle()   #Creating a blue turtle called Bob
bob.color('blue')
bob.shape('turtle')

bob.penup()    #Moving Bob to starting point
bob.goto(-160,70)
bob.pendown()

greg=Turtle()   #Creating a green turtle called Greg
greg.color('green')
greg.shape('turtle')

greg.penup()    #Moving Greg to starting point
greg.goto(-160,40)
greg.pendown()

for move in range(100):
    ada.forward(randint(1,5))
    greg.forward(randint(1, 5))
    bob.forward(randint(1, 5))

done() #or exitonclick() Helps user to close turtle window explicitly
