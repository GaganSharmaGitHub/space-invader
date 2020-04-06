# Space Invader
    Classic space invader game using pygame.
## Credits
    This project was possible because of:
        1. Pygame
        2. Flaticon artists
            1. Spaceship:
            2. Enemy1: www.flaticon.com/authors/phatplus
            3. Enemy2: www.flaticon.com/authors/smashicons
            4. Enemy3:www.flaticon.com/authors/smashicons
            5. Enemy4: www.flaticon.com/authors/smashicons
            6. Enemy5: www.flaticon.com/authors/smashicons
        3. Background Artist: www.freepik.com/vectorpouch
## Code </>

### GameProps
    Global dictionary for basic game properties
```GameProps = {'height': 600,'width': 1000, 'name': 'Space Invader', 'icon':'icon.png'} ```
    
    Other global variables
        running = True\
        playing = True\
        gameO= False\
        backg = pygame.image.load('1876.jpg')\
        enemiesdata=[{'file':'enemy1.png','points':6},{'file':'enemy2.png','points':5},{'file':'enemy3.png','points':9},{'file':'enemy4.png','points':3},{'file':'enemy5.png','points':7}]


###  Player Class
Creating Object:

 ```Player(img='imagePath',score=0, pos=(x,y), speed=(dx,dy ), size=(width, height))```

Default values:

    1. img='error.png'
    2. score=0
    3. pos=(GameProps['width']/2, GameProps['height']/2)
    4.speed=(0, 0)
    5.size=(64, 64)

Player.draw(): 
    Draws image at the taking the current coordinates of player as centre of image.

Player.moveBounce((upperXlimit,upperYlimit),(lowerXlimit, lowerYlimit)):
    Player bounces back when it hits lower or upper limits

Player.moveStop((upperXlimit,upperYlimit),(lowerXlimit, lowerYlimit)):
    Player stops when it hits lower or upper limits

Player.moveTele((upperXlimit,upperYlimit),(lowerXlimit, lowerYlimit)):
    Player teleports to other end when it hits lower or upper limits

###  Bullet Class
Creating Object:

```Bullet(x,y,image, size=(height,width)):```
 

Default values:\
    1. x=0\
    2. y=0\
    3. image='laser.png'\
    4. size=(32,32)

Bullet.draw(): 
    Draws image at the taking the current coordinates of bullet as centre of image.

Bullet.move(): makes bullet move if it is fired

Bullet.trigger():
    Fires of the bullet

Bullet.hit():
    Reloads bullet


