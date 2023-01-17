import pygame 
import random
import time

pygame.init()
pygame.font.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Boing")
clock = pygame.time.Clock()

running=True

red=(255,0,0)
yellow=(255,255,0)
green=(0,255,0)
grass=(11,102,35)
black=(0,0,0)
white=(255,255,255)
brown=(150,75,0)

is_movingL = False
is_movingR = False
is_jumping = False
is_dashing = False

y=200
x=25

jumptime=0
GameScreen=1

class Level: 
    GroundY=525.0
    RightWall=775
    LeftWall=0
    sent=0
    startupTF=0
    NewRoom=0

NumB=20
EneY=0
EnemyPostListRef=[]
EnemyPostList=[]
CurrentEnemyListRef=[]
CurrentEnemyList=[]
EnemyXList=[]
EnemyYList=[]
CurrentPosEnemyX=0
CurrentPosEnemyY=0


myfont = pygame.font.SysFont('Impact',30)








def EnemyMove():
    global EnemyXList
    global EnemyYList
    global EneY
    global EneX
    
    global EnemyAlive
    
    
    for x in range(NumB):
        if EnemyYList[x] == 0:
            NewY=random.randint(-600,0)
            NewX=random.randint(0,770)
            Index=EnemyYList.index(0)
            EnemyXList[Index]=NewX
            EnemyYList[Index]=NewY
        
        
    
    EnemyYList = [x+0.1 for x in EnemyYList]
    
    for x in range (NumB):
        EneX=EnemyXList[x]
        EneY=EnemyYList[x]
        pygame.draw.rect(screen,black, [EneX,EneY,10,10])
    
    
        
        
    
    return(EnemyXList,EnemyYList)



def startupBullet():

    global EnemyYList
    global EnemyXList
    global EnemyPostListRef
    global CurrentEnemyListRef
    
    
    
    EnemyXList=[]
    EnemyYList=[]
    CurrentEnemyListRef=[]
    EnemyPostListRef=[]

    for x in range(NumB):
        RandomStartUpX=random.randint(0,800)
        RandomStartUpY=random.randint(-400,0)
        EnemyXList.append(RandomStartUpX)
        EnemyYList.append(RandomStartUpY)
    EnemyMove()



    for x in range(NumB):
        place="EnemyX" + str(x)
        place2="EnemyY" + str(x)
        CurrentEnemyListRef.append(place)
        CurrentEnemyListRef.append(place2)



        
        place="CurrentPosEnemyX" + str(x)
        place2="CurrentPosEnemyY" + str(x)
        EnemyPostListRef.append(place)
        EnemyPostListRef.append(place2)
    
    
    
def BulletTime(Floor):


    global EnemyYList
    global x 
    global y




    for i in range (NumB):
        
        CurrentPosEnemyX=EnemyXList[i]
        CurrentPosEnemyY=EnemyYList[i]
        
        if CurrentPosEnemyY <= y and CurrentPosEnemyY +10 >= y and CurrentPosEnemyX+25 > x and CurrentPosEnemyX < x+25:
                        
            startupBullet()
            y=300
            x=75
            EnemyYList[i]=0
        
        elif CurrentPosEnemyY>Floor:
            
            EnemyYList[i]=0
            
        else:
            EnemyMove() 



def drawGround(q,x,y,z,a):
    pygame.draw.rect(q, green, [x,y-20,z,a-10])
    pygame.draw.rect(q, brown, [x,y,z,a])
    
    
    
def CheckDeath(ResetX,ResetY):
    global x
    global y
    
    
    if y == 600:
        y=ResetY
        x=ResetX



def groundCol():
    global jumptime
    global is_jumping
    global y

    
    if is_jumping==True and y == LevelContext.GroundY:
        y == LevelContext.GroundY
        jumptime=0
        is_jumping=False
        
        
        
def screenCol(LevelContext):
    global GameScreen
    global x
    global jumptime
    global is_jumping
    

    if x > 770:
        GameScreen+=1
        x=75
        jumptime=0
        is_jumping=False
        LevelContext.NewRoom=0
    elif x < 10 and GameScreen>1:
        GameScreen-=1
        x=750
        jumptime=0
        is_jumping=False
        LevelContext.NewRoom=0



def CheckScreen():
    if GameScreen==1:
        screen1(LevelContext)
    elif GameScreen==2:
        screen2(LevelContext)
    elif GameScreen==3:
        screen3(LevelContext)
    elif GameScreen==4:
        screen4(LevelContext)
    elif GameScreen==5:
        screen5(LevelContext)
    elif GameScreen==6:
        screen6(LevelContext)
    elif GameScreen==7:
        screen7(LevelContext)
    elif GameScreen==8:
        screen8(LevelContext)
    elif GameScreen==9:
        screen9(LevelContext)
    elif GameScreen==10:
        screen10(LevelContext)
    elif GameScreen==11:
        screen11(LevelContext)
    elif GameScreen==12:
        screen12(LevelContext)
    elif GameScreen==13:
        screen13(LevelContext)
    elif GameScreen==14:
        screen14(LevelContext)
    elif GameScreen==15:
        screen15(LevelContext)
    elif GameScreen==16:
        screen16(LevelContext)
    elif GameScreen==17:
        screen17(LevelContext)
    elif GameScreen==18:
        screen18(LevelContext)
    elif GameScreen==19:
        screen19(LevelContext)
    elif GameScreen==20:
        screen20(LevelContext)
    elif GameScreen==21:
        screen21(LevelContext)
    elif GameScreen==22:
        screen22(LevelContext)
    elif GameScreen==23:
        screen23(LevelContext)
    elif GameScreen==24:
        screen24(LevelContext)
    elif GameScreen==25:
        screen25(LevelContext)
    elif GameScreen==26:
        screen26(LevelContext)
    elif GameScreen==27:
        screen27(LevelContext)
    elif GameScreen==28:
        screen28(LevelContext)
    elif GameScreen==29:
        screen29(LevelContext)
        


def screen1(LevelContext):
    drawGround(screen, 0,570,800,30)
    
    
    
    helpText = myfont.render('Use arrow keys to move', False, (0, 0, 0))
    screen.blit(helpText,(250,200))



def screen2(LevelContext):
    
    
    drawGround(screen, 0,570,350,30)
    drawGround(screen, 450,520,450,80)
    
    
    
    
    #hitdetect
    if x <350:
        LevelContext.GroundY=525
    
    elif x >350 and x <425:
        LevelContext.GroundY=600
    
    elif x > 425:
        LevelContext.GroundY=475.0
    
    
    
    
    if x > 350 and x < 450 and y>476:
        LevelContext.RightWall=424
        
    else:
        LevelContext.RightWall=775
    
    
    if x > 325 and x < 450 and y>526:   
        LevelContext.LeftWall=351
    
        
    else:
        
        LevelContext.LeftWall=0


    
def screen3(LevelContext):


    
    for i in range(5):
        
        i+=1
        drawGround(screen, (i-1)*200,550-(i*30),200,100+(i*30))
    
     
    #hitdetect
    if x > 0 and x<175:
        LevelContext.GroundY=475
    
    elif x >175  and x <375:
        LevelContext.GroundY=445
    
    elif x >375  and x <575:
        LevelContext.GroundY=415
    
    elif x > 575:
        LevelContext.GroundY=385

    
    if x > 0 and x<200 and y>445:
        LevelContext.RightWall=174
    
    elif x >200  and x <400 and y>415:
        LevelContext.RightWall=374
    
    elif x >400  and x <600 and y>385:
        LevelContext.RightWall=574
    
    else:
        LevelContext.RightWall=774



def screen4(LevelContext):




    drawGround(screen, 0,430,200,220)
    
    for i in range(3):
        i+=1
        drawGround(screen, 150+i*200, 430 ,50,250)


    

    #hitdetect

    if x > 200 and x < 325 or  x > 400 and x < 525 or  x > 600 and x < 725:
        
        LevelContext.GroundY=600
        
    else:
        LevelContext.GroundY=385
        
        
        
    if x > 200 and x < 325 and y>385:
        LevelContext.RightWall=323
        LevelContext.LeftWall=202
        
    elif x > 400 and x < 525 and y>385:
        LevelContext.RightWall=523
        LevelContext.LeftWall=402
    elif x > 600 and x < 725 and y>385:
        LevelContext.RightWall=723
        LevelContext.LeftWall=602
        
    else:
        LevelContext.RightWall=775
        LevelContext.LeftWall=0
    


def screen5(LevelContext):
    

    global jumptime

    drawGround(screen, 0,430,300,220)
    
    pygame.draw.rect(screen, green, [425,00,50,375])
    pygame.draw.rect(screen, brown, [425, 0, 50, 355])
    
    drawGround(screen, 600,430,200,220)

    #hitdetect
    if 0 < x < 300 or 575 < x:
        LevelContext.GroundY=385
    else: 
        LevelContext.GroundY=600
        
      
    if  x > 300 and x < 600 and y > 385:
        LevelContext.RightWall=574
        LevelContext.LeftWall=301
        
        
    elif x  > 400 and x < 475 and y <400:
        LevelContext.RightWall=400
        LevelContext.LeftWall=476
        
        
    else:
        LevelContext.RightWall=775
        LevelContext.LeftWall=0
    

    
    if x  > 375 and x < 500 and  y < 375:
        jumptime=50
        


def screen6(LevelContext):

    
    drawGround(screen, 0,430,800,220)
    LevelContext.GroundY=385
    
    
    
    
    helpText = myfont.render('Watch out for falling bullets!', False, (0, 0, 0))
    screen.blit(helpText,(250,200))
    

    
def screen7(LevelContext):
    
 



    
    
    BulletTime(LevelContext.GroundY+25)
    
    
    
    drawGround(screen, 0,430,800,220)
    LevelContext.GroundY=385



def screen8(LevelContext):
    
  
    
    
    
    
    
    
    global NumB
    
    
    if LevelContext.NewRoom==0:
        NumB=15
        startupBullet()
        LevelContext.NewRoom=1
    
    BulletTime(600)

    drawGround(screen, 0,430,200,220)
    
    for i in range(3):
        i+=1
        drawGround(screen, 150+i*200, 430 ,50,250)


    

    #hitdetect

    if x > 200 and x < 325 or  x > 400 and x < 525 or  x > 600 and x < 725:
        
        LevelContext.GroundY=600
        
    else:
        LevelContext.GroundY=385
        
        
        
    if x > 200 and x < 325 and y>385:
        LevelContext.RightWall=323
        LevelContext.LeftWall=202
        
    elif x > 400 and x < 525 and y>385:
        LevelContext.RightWall=523
        LevelContext.LeftWall=402
    elif x > 600 and x < 725 and y>385:
        LevelContext.RightWall=723
        LevelContext.LeftWall=602
        
    else:
        LevelContext.RightWall=775
        LevelContext.LeftWall=0
    
    
    
def screen9(LevelContext):

    
    
    
    
    LevelContext.RightWall=800
    LevelContext.LeftWall=0
    drawGround(screen, 0,430,800,220)
    
    LevelContext.GroundY=385
    
    
    
    
    helpText = myfont.render('Moving between screens resets your jump', False, (0, 0, 0))
    screen.blit(helpText,(250,200))
    


def screen10(LevelContext):

    
    if x > 175:
        LevelContext.GroundY=255
    else:
        LevelContext.GroundY=385
    
    if x < 176 and y > 225:
        LevelContext.RightWall=175
    else:
        LevelContext.RightWall=800
    
    
    
    drawGround(screen, 0,430,200,220)
    drawGround(screen, 200,300,700,420)
    
    
    
def screen11(LevelContext):

 

    if x < 100:
        LevelContext.GroundY=255
    elif x > 575:
        LevelContext.GroundY=385
    else:
        LevelContext.GroundY=600


    if 100 < x < 600 and y > 385:
        LevelContext.LeftWall=101
        LevelContext.RightWall=574
    elif 100 < x < 600 and y > 255:
        LevelContext.LeftWall=101
        LevelContext.RightWall=800
    else:
        LevelContext.LeftWall=0
        LevelContext.RightWall=800
    







    drawGround(screen, 0,300,100,420)
    drawGround(screen, 600,430,200,220)
    
    CheckDeath(75,200)
    
    

   
startupBullet()
LevelContext = Level()


while running:


    
    
    
    clock.tick(300)    
    
    
    
    
    
    screen.fill((135,206,235))
        
    pygame.draw.rect(screen, white, [100,100,100,50])
    pygame.draw.rect(screen, white, [275,75,100,50])   
    pygame.draw.rect(screen, white, [500,150,100,50])
    
    
    pygame.key.set_repeat(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            is_movingL = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            is_movingL = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            is_movingR = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            is_movingR = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            is_jumping = True
        
        
            
            
    
    
    
    
        
    
    
    
    if is_movingL==True and x> LevelContext.LeftWall:
        x-=2
    
    if is_movingR==True and x< LevelContext.RightWall:
        x+=2
    
    if is_jumping==True and jumptime <50 and y>0:
        y-=2
        jumptime+=1
    
    elif y<LevelContext.GroundY:
        
        y+=1.0
    
    
    
   
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    CheckScreen()
    groundCol()
    screenCol(LevelContext)
    CheckDeath(75,300)
    pygame.draw.rect(screen, red, [x,y,25,25])



























    pygame.display.update()