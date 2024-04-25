from turtle import *
forward(30)

#rectangle
left(90)
for side in range(2):
  forward(100)
  right(120)
forward(100)

#house
left(90)
for side in range(2):
  forward(100)
  right(120)
forward(100)
left(-30)
for house in range(3):
  forward(100)
  right(90)
right(45)
forward(141.42)
penup()
left(135)
forward(100)
left(135)
pendown()
forward(141.42)

#village
speed(6)
penup()
goto(25,250)
pendown()
for village in range(6):
  forward(100)
  right(45)
  forward(70.71)
  right(90)
  forward(70.71)
  right(135)
  forward(100)
  for diagonal in range(2):
    left(135)
    forward(141.42)
    left(135)
    forward(100)
  penup()
  forward(25)
  pendown()
  left(90)

#it's working but I'm not yet really happy, it feels like there is a smarter way but I dont get it :)
#I have no clue what you wanted me to say that 'square function can be found in math module', how could I have used it, I didn't figure it out.
#I mean from math import I know but how to make the turtle run a square with it I dont know


#pentagon, hexagon, heptagon, octagon
#speed(10)

#sidelength
length = 50

#position turtle
x = 70
penup()
goto(x,250)
right(90)
pendown()

#trying to simplify it, there 4 symbols with the same attributes, only the amount of sides is different
polygones = ['pentagon', 'hexagon', 'heptagon', 'hectagon']
sides = [5, 6, 7, 8]

for i in range(len(polygones)):
  current_polygone = polygones[i]
  side = sides[i]

  for a in range(side):
    forward(length)
    left(360 / side)
  penup()
  x = x + (side * length)/2
  goto(x,250)
  pendown()

#holymacarony I think I'm going to sleep now, this was so much brainwork, the cheetsheet was big help. Only the "len"-function I had to google, couldnt find a way to get the amount of list-items in another way.
# also I couldn't figure out how to use the hint of the inner angle 180 × (1-2/n), I'm really poor in math and trigonometry and stuff -.-


#2 hours und 2 exercises later I feel so dumb. I could have done it like the one with the input function (exercise 5) and only add +1 side at the end of a loop until hectagon.
#Today I'm not going to try it anymore, I will do it by my own the next days because I'm curious but I leave this here now as it was, sorry for wall of text.

# Draw n-gon where n comes as input of user
sides = int(input("How many sides has your polygone?"))
print(sides)
#speed(10)

#sidelength
length = 50

for a in range(sides):
  forward(length)
  left(360 / sides)


  #another try for n-gon but I failed (in the most satanic way with n = 10 :D)
n = int(input("give a number\n"))
#speed(10)
for sides in range(n):
  forward(100)
  right(180 * (1-2/n))
  forward(100)


#Draw this ornament:
speed(10)
for i in range(50):
  length = 10
  forward(length)
  left(90)
  length = length * i
  forward(length)

#mesmerizing with turtlespeed 10 :D

#Using a for loop, write a program which return this (do not write the numbers by yourself)
for i in range(5):
  print('Row', i)

#Using a cycle (loop), write a program which return this:
#honestly I don't know if it is what you meant? A "for cycle"? because the exercise 7 was the same I think?!
for i in range(5):
  print(i, "to power of 2 is", i ** 2)

#print even numbers between 1 and 20 using loop and conditions
for num in range(1, 21):
  if num % 2 == 0:
    print(num)
