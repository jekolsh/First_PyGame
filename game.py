import pygame
import random

pygame.init()

win =pygame.display.set_mode((500, 500))

pygame.display.set_caption("Trump Game")


walkRight = [pygame.image.load("pygame_right_1.png"), 
pygame.image.load("pygame_right_2.png"), pygame.image.load("pygame_right_3.png"),
pygame.image.load("pygame_right_4.png"), pygame.image.load("pygame_right_5.png"),
pygame.image.load("pygame_right_1.png")]

walkLeft = [pygame.image.load("pygame_left_1.png"), 
pygame.image.load("pygame_left_2.png"), pygame.image.load("pygame_left_3.png"),
pygame.image.load("pygame_left_4.png"), pygame.image.load("pygame_left_5.png"),
pygame.image.load("pygame_left_6.png")]

bg = pygame.image.load("pygame_bg_7.jpg")
playerStand = pygame.image.load("pygame_idle.png")

clock = pygame.time.Clock()

#bulletSound = pygame.mixer.Sound('Game_bullet_2.mp3')
#hitSound = pygame.mixer.Sound('Game_hit.mp3')

#music = pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play(-1)

score = 0

class player(object): 
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.animCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw (self, win):
        if self.animCount + 1 >= 30:
            self.animCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft [self.animCount // 5], (self.x, self.y))
                self.animCount += 1
            elif self.right:
                win.blit(walkRight [self.animCount // 5], (self.x, self.y))
                self.animCount += 1

        else:
            if self.right:
                win.blit(walkRight [0], (self.x, self.y))
            else:
                win.blit(walkLeft [0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
                    

            #for bullet in bullets:
                #bullet.draw(win)
    
    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(3)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()



class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y 
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing #hastighet
        

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.animCount = 0
        self.vel = random.randint(1, 5)
        self.hitbox = (self.x + 17, self.y +2, 31, 57)
        self.health = random.randint(3, 10)
        self.visible = True

    def draw(self, win):
        if  not self.visible:
            return 
        self.move()
        if self.animCount + 1 >= 33:
            self.animCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.animCount//3], (self.x,self.y))
            self.animCount += 1
        else:
            win.blit(self.walkLeft[self.animCount//3], (self.x,self.y))
            self.animCount += 1

        
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31,57)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                #self.x += self.vel
                self.animCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.animCount = 0

    def hit(self):
        if self.health >= 0:
            self.health  -=1
        else:
            self.health <= 0
            self.visible = False
            goblin.draw(win)

        print("hit")


def drawWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)  
    goblin2.draw(win)  
    for bullet in bullets:
        bullet.draw(win)


    pygame.display.update()

#main loop
font = pygame.font.SysFont('comicsans', 15, True)
man = player(300, 410, 60, 71)
goblin = enemy(100, 410, 64, 64, 450)
goblin2 = enemy(10, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    #drawWindow()
    clock.tick(30)
    if not goblin.visible and  not goblin2.visible:
        print("Win-win!")
                
    if score < -1:
        print("You are looser :(")
        


    if goblin.visible and man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
        man.hit()
        score -= 5
        goblin.vel = -goblin.vel
    if goblin2.visible and  man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin2.hitbox[1] and man.hitbox[0] + man.hitbox[2] > goblin2.hitbox[0] and man.hitbox[0] < goblin2.hitbox[0] + goblin2.hitbox[2]:
        man.hit()
        score -= 5
        goblin2.vel = -goblin2.vel


     
    if shootLoop > 0:
        shootLoop +=1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        
        if goblin.visible and bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1] and bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                #goblin2.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        elif goblin2.visible and bullet.y - bullet.radius < goblin2.hitbox[1] + goblin2.hitbox[3] and bullet.y + bullet.radius > goblin2.hitbox[1] and bullet.x + bullet.radius > goblin2.hitbox[0] and bullet.x - bullet.radius < goblin2.hitbox[0] + goblin2.hitbox[2]:
                # goblin.hit()
                goblin2.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0 :
        #bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 5,(255,0 ,0), facing ))

        shootLoop = 1

    if keys [pygame.K_LEFT] and man.x > 5: #restirctions for actions
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys [pygame.K_RIGHT] and man.x < 500 - man.width - 5:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.animCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.animCount = 0
    else:
        if man.jumpCount >= -10:
            if man.jumpCount < 0:
                man.y +=  (man.jumpCount **2) / 2
            else:
                man.y-= (man.jumpCount **2) / 2
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    drawWindow()


pygame.quit()