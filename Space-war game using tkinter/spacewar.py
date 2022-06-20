      
 
import turtle
import math
import random
import os
screen=turtle.Screen()
# screen.bgcolor('blue ')
screen.bgpic("space.jpg")
boundry=turtle.Turtle()

 
# boundries of space
boundry.penup()
boundry.color('blue')
boundry.ht()
boundry.setposition(-190,-190)
boundry.st()
boundry.pendown()
boundry.speed(0)
for i in range(4):
  boundry.forward(380)
  boundry.left(90)
boundry.ht()

# score for hits
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-175,175)
scorestring="Score: %s" %score
score_pen.write(scorestring,False,align="Left",font=("Arial",14,"normal"))
score_pen.ht()

# gun
frog=turtle.Turtle()
frog.shape("turtle")
frog.color('blue')
frog.penup()
frog.ht()
frog.setposition(0,-175)
frog.st()
frog.speed(10)
frog.setheading(90)
 
# enemy
# numberof enemies
enemiesnumber=5
enemies=[]
for i in range(enemiesnumber):
  enemies.append(turtle.Turtle())
for enemy in enemies: 
  enemy.color('red')
  enemy.shape("circle")
  
  enemy.penup()
  enemy.ht()
  enemy.setposition(random.randint(-170,170),random.randint(160,170))
  enemy.st()
enemyspeed=3  
 
# gun bullet
bullet=turtle.Turtle()
bullet.color('white')
bullet.shape('rocketship.png')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
# bullet.shapesize(0.5,0.5)
# bullet.turtle size(1,1)
bullet.hideturtle()
bulletspeed=20
# bullet state ready or not
bulletstate="ready"
bullet.ht()
 
 
#moving left and  right
frogspeed=10
def left():
  x=frog.xcor()
  x-=frogspeed
  if x<-175:
    x=-175
  frog.setx(x)
def right():
  x=frog.xcor()
  x+=frogspeed
  if x>175:
    x=175
  frog.setx(x)
 
# fire_bullet
def fire_bullet():
  global bulletstate
  # move bullet
  if bulletstate== "ready":
    bulletstate="fire"
    x=frog.xcor()
    y=frog.ycor()+10
    bullet.setposition(x,y)
    bullet.st()
   
    # collision detection
def iscollsion(d1,d2):
  d=math.sqrt(math.pow(d1.xcor()-d2.xcor(),2) + math.pow(d1.ycor()-d2.ycor(),2))
  if d<15:
    return True
  else:
    return False    
 
  # player input
screen.listen()  
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(fire_bullet,"Space")
 
# main loop of game
while True:
  # for enemies movement
  for enemy in enemies:
    x=enemy.xcor()
    x+=enemyspeed
    enemy.setx(x)
    
    
      # move all enemies dowwn
    if x>170:
      for e in enemies:
        y=e.ycor()
        y-=20
        e.sety(y)
      enemyspeed*=-1
    if x<-170:
      # move all enemies down
      for e in enemies:
        y=e.ycor()
        y-=20
        e.sety(y)
      enemyspeed*=-1
      
      # check for collision  happen
    if iscollsion(bullet,enemy):
      bullet.ht()
      enemy.ht()
      enemy.setposition(random.randint(-170,170),random.randint(160,170))
      enemy.st()
      bulletstate="ready"
      score+=5
      scorestring="Score: %s" %score
      score_pen.clear()
      score_pen.write(scorestring,False,align="Left",font=("Arial",14,"normal"))
      
      
     # check out that bullet has gone to boundry
    if iscollsion(frog,enemy):
        frog.hideturtle()     
        enemy.ht()
        print('GAME OVER')
        break
  
   
      
  if bullet.ycor()>170:
    bullet.ht()
    bulletstate="ready"
      
    # bullet movement
  if bulletstate=="fire":
    y=bullet.ycor()
    y+=bulletspeed
    bullet.sety(y)
   
        # bullet.setpositiom(200,200)