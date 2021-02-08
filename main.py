import pygame
import random
import time
width = 1000
height = 1000
mazeWidth = int(input("Maze Width. "))
mazeHeight = int(input("Maze Height. "))
wallThick = 1
distanceA = 0
squareWidth = width / mazeWidth
squareLength = height / mazeHeight
area = mazeWidth * mazeHeight

drawX = int(mazeWidth / 2)
drawY = int(mazeHeight / 2)
xCount = 0

board = []
while mazeWidth > xCount:
    yCount = 0
    colum = []
    while mazeWidth > yCount:
        colum.append(None)
        yCount += 1
    board.append(colum)
    xCount += 1

path = []
done = False
total = 0
addToList = True
timesBacked = 0
direction = "up"
startTime = time.time()
while not done:
    board[drawX][drawY] = 1
    if addToList:
        total += 1
        path.append((drawX,drawY,direction))
        timesBacked = 0
    else:
        addToList = True
        timesBacked -= 1
    directions = []
    try:
        if drawX + 1 < mazeWidth and board[drawX + 1][drawY] == None:
            directions.append("right")
    except Exception:
        pass
    try:
        if drawX - 1 >= 0 and board[drawX - 1][drawY] == None:
            directions.append("left")
    except Exception:
        pass
    try:
        if drawY + 1 < mazeHeight and board[drawX][drawY + 1] == None:
            directions.append("up")
    except Exception:
        pass
    try:
        if drawY -1 >= 0 and board[drawX][drawY-1] == None:
            directions.append("down")
    except Exception:
        pass
    if len(directions) != 0:
        direction = random.choice(directions)
    else:
        direction = "Fail move back"
    if direction == "up":
        drawY += 1
    elif direction == "down":
        drawY -= 1
    elif direction == "left":
        drawX -= 1
    elif direction == "right":
        drawX += 1
    elif direction == "Fail move back":
        drawX = path[-2+timesBacked][0]
        drawY = path[-2+timesBacked][1]
        addToList = False
    if total % 500 == 0:
        print(total,"/",area,"Iterations complete in",time.time()-startTime)
    if total >= area:
        done = True
print("Complete in ",time.time()-startTime,"Secconds")
input("Press enter to start drawing. ")
done = False
distanceA = 0
counter = 0
screen = pygame.display.set_mode((width,height))

screen.fill((0,0,0))
for item in path:
    pygame.display.flip()
    print(item)
    if item[2] == "up":
        pygame.draw.rect(screen,(255,255,255),(item[0]*squareWidth,item[1] * squareLength-wallThick,squareWidth -wallThick,squareLength))
    elif item[2] == "down":
        pygame.draw.rect(screen,(255,255,255),(item[0]*squareWidth,item[1] * squareLength,squareWidth -wallThick,squareLength))
    elif item[2] == "left":
        pygame.draw.rect(screen,(255,255,255),(item[0]*squareWidth,item[1] * squareLength,squareWidth,squareLength-wallThick))
    elif item[2] == "right":
        pygame.draw.rect(screen,(255,255,255),(item[0]*squareWidth - wallThick,item[1] * squareLength,squareWidth,squareLength-wallThick))
    else:
        pygame.draw.rect(screen,(255,255,255),(item[0]*squareWidth,item[1] * squareLength,squareWidth,squareLength -wallThick))
    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            done = True
    counter += 1
pygame.image.save_extended(screen,"maze.png")
print("Saved as maze.png")
while not done:
    pygame.display.flip()
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            done = True
