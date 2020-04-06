import pygame
import random
GameProps = {'height': 600, 'width': 1000, 'name': 'Space Invader', 'icon':'icon.png'}
pygame.init()
screen = pygame.display.set_mode((GameProps['width'], GameProps['height']))
pygame.display.set_caption(GameProps['name'])
icon = pygame.image.load(GameProps['icon'])
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)
fontBig = pygame.font.Font('freesansbold.ttf', 64)
running = True
playing = True
gameO= False
backg = pygame.image.load('1876.jpg')
enemiesdata=[{'file':'enemy1.png','points':6},{'file':'enemy2.png','points':5},{'file':'enemy3.png','points':9},{'file':'enemy4.png','points':3},{'file':'enemy5.png','points':7}]
def isColliding(player, bullet):
    if(abs(player.x-bullet.x<=25) and abs(player.y-bullet.y)<=16):
        print(ship.score(player.points))
        player.reset()

def showScore(x):
    text = font.render('Score:'+ str(x),True,(255,255,255))
    screen.blit(text,(10,10))
def gameOver():
    text = fontBig.render('Game Over',True,(255,255,255))
    text2 = font.render('Score:'+ str(ship.points),True,(255,255,255))
    screen.blit(text,(300,300))
    screen.blit(text2,(400,400))
    global playing
    playing=False
    global gameO
    gameO= True


class Player:
    def __init__(self, img='error.png',score=0, pos=(GameProps['width']/2, GameProps['height']/2), speed=(0, 0), size=(64, 64)):
        self.x = pos[0]
        self.y = pos[1]
        self.dx = speed[0]
        self.dy = speed[1]
        self.points= score
        self.width = size[0]
        self.height = size[1]
        self.image = pygame.image.load(img)
        self.movement = 'stop'

    def draw(self):
        screen.blit(self.image, (self.x-(self.width/2), self.y-(self.height/2)))

    def right(self):
        self.movement ='right'
    def score(self,inc):
        self.points+=inc
        return self.points
    def left(self):
        self.movement ='left'
    def reset(self):
        self.x= random.randint(100,GameProps['width']-100)
        self.y=50+ random.randint(0,5)*30
    def stop(self):
        self.movement='stop'

    def moveStop(self, upper= (GameProps['width'], GameProps['height']), lower=(0, 0)):
        self.y += self.dy
        if(self.movement=='left'):
            self.x-=self.dx
        if(self.movement=='right'):
            self.x+=self.dx
        
        # upper limit
        if self.x > upper[0] - self.width/2:
            self.x = upper[0] - self.width/2

        if self.y > upper[1] - self.height/2:
            self.y = upper[1] - self.height/2

        # lower limit
        if self.x < lower[0] + (self.width / 2):
            self.x = lower[0] + (self.width / 2)

        if self.y < lower[1] + (self.height / 2):
            self.y = lower[1] + (self.height / 2)

    def moveTel(self):
        self.x += self.dx
        self.x %= GameProps['width']
        self.y += self.dy
        self.y %= GameProps['height']


    def moveBounce(self, upper= (GameProps['width'], GameProps['height']), lower=(0, 0)):
        self.x += self.dx
        self.y += self.dy
        # upper limit
        if self.x > upper[0]-self.width/2:
            self.dx *= -1
            self.y+=10
            self.x = upper[0]-self.width/2

        if self.y > 600:
            gameOver()

        # lower limit
        if self.x < lower[0]+(self.width/2):
            self.dx *= -1
            self.x = lower[0]+(self.width/2)
            self.y+=10


        if self.y < lower[1]+(self.height/2):
            self.dy *= -1
            self.y = lower[1]+(self.height/2)


class Bullet():
    def __init__(self,x=0,y=0,image='laser.png', size=(32,32)):
        self.x=x
        self.yorg=y-size[1]
        self.y= self.yorg
        self.ready= True
        self.fire=False
        self.dy=20
        self.dx=0
        self.size=size
        self.image=pygame.image.load(image)

    def draw(self):
        screen.blit(self.image, (self.x-(self.size[0]/2), self.y-(self.size[1]/2)))
    
    def move(self, x):
        if(self.fire):
            self.y-=self.dy
            if(self.y<0 or self.ready):
                self.hit()
        else:
            self.y= self.yorg
            self.x= x

    def hit(self):
            self.fire=False
            self.y= self.yorg
            self.ready=True

    def trigger(self):
        if self.ready:
            self.fire=True
            self.ready=False


ship = Player(img='ship.png', speed=(4, 0), pos=(400,650))
enemies=[]
for i in enemiesdata:
    enemies.append(Player(speed=(random.randint(6,10),1),score=i['points'], img=i['file'], pos=(random.randint(32,GameProps['width']-30),40+ random.randint(0,5)*30)))
#enemy=Player(speed=(2,0), img='enemy.png', pos=(random.randint(100,GameProps['width']-100),100))
laser= Bullet(x=ship.x,y=ship.y)
print('game started')
while running:
    screen.fill((9, 10, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('bye bye')
            running = False
        if not gameO:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    playing= not playing
                if playing:
                    if event.key == pygame.K_LEFT:
                        ship.left()
                    if event.key == pygame.K_RIGHT:
                        ship.right()
                    if event.key == pygame.K_SPACE:
                        laser.trigger()
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    ship.stop()

    if playing:
        screen.blit(backg,(0,0))
        ship.draw()
        ship.moveStop()
        laser.draw()
        showScore(ship.points)
        laser.move(ship.x)
        for i in enemies:
            i.draw()
            isColliding(i, laser)
            i.moveBounce()
        pygame.display.update()
        pass
