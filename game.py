import random
import os
import pygame
from classer import*


pygame.init()

win =pygame.display.set_mode((500, 500))
pygame.display.set_caption("Trump Game")
clock = pygame.time.Clock()


score = 0

#music.play()

def drawWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)  
    goblin2.draw(win) 
    goblin3.draw(win) 
    goblin4.draw(win)   
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

#bullet_sound = pygame.mixer.Sound('Game_bullet_2.mp3') 
#hit_sound = pygame.mixer.Sound('Game_hit.mp3')
music = pygame.mixer.Sound('music.mp3')
#pygame.mixer.music.play()

music.play()


#main loop
font = pygame.font.SysFont('comicsans', 15, True)
man = player(300, 410, 60, 71)
goblin = enemy(100, 410, 64, 64, 450)
goblin2 = enemy(10, 410, 64, 64, 450)
goblin3 = enemy(50, 410, 64, 64, 450)
goblin4 = enemy(75, 410, 64, 64, 450)
shootLoop = 0
bullets = []
run = True
while run:
    #drawWindow()
    clock.tick(30)
    if not goblin.visible and  not goblin2.visible and not goblin3.visible and not goblin4.visible:
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
    if goblin3.visible and man.hitbox[1] < goblin3.hitbox[1] + goblin3.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin3.hitbox[1] and man.hitbox[0] + man.hitbox[2] > goblin3.hitbox[0] and man.hitbox[0] < goblin3.hitbox[0] + goblin3.hitbox[2]:
        man.hit()
        score -= 5
        goblin3.vel = -goblin3.vel
    if goblin4.visible and man.hitbox[1] < goblin4.hitbox[1] + goblin4.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin4.hitbox[1] and man.hitbox[0] + man.hitbox[2] > goblin4.hitbox[0] and man.hitbox[0] < goblin4.hitbox[0] + goblin4.hitbox[2]:
        man.hit()
        score -= 5
        goblin4.vel = -goblin4.vel


     
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
                score += 1
                bullets.pop(bullets.index(bullet))
        elif goblin2.visible and bullet.y - bullet.radius < goblin2.hitbox[1] + goblin2.hitbox[3] and bullet.y + bullet.radius > goblin2.hitbox[1] and bullet.x + bullet.radius > goblin2.hitbox[0] and bullet.x - bullet.radius < goblin2.hitbox[0] + goblin2.hitbox[2]:
                goblin2.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        elif goblin3.visible and bullet.y - bullet.radius < goblin3.hitbox[1] + goblin3.hitbox[3] and bullet.y + bullet.radius > goblin3.hitbox[1] and bullet.x + bullet.radius > goblin3.hitbox[0] and bullet.x - bullet.radius < goblin3.hitbox[0] + goblin3.hitbox[2]:
                goblin3.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        elif goblin4.visible and bullet.y - bullet.radius < goblin4.hitbox[1] + goblin4.hitbox[3] and bullet.y + bullet.radius > goblin4.hitbox[1] and bullet.x + bullet.radius > goblin4.hitbox[0] and bullet.x - bullet.radius < goblin4.hitbox[0] + goblin4.hitbox[2]:
                goblin4.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0 :
        #bullet_sound.play()
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

 