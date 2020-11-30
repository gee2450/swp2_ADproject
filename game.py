import pygame
import random

scr_size = (600,320)
FPS = 60
finish_cnt = 0

def image_load(filePath):
    return pygame.image.load(filePath)


class Cookie(pygame.sprite.Sprite):
    def __init__(self, character):
        super(Cookie, self).__init__()
        self.finish_cnt = 0
        self.character = character
        self.filePath = "images/CherryBlossom/run1.png"
        self.image = image_load(self.filePath)
        self.mask = pygame.mask.from_surface(self.image)
        self.exRect = self.image.get_rect()
        self.exRect.y = scr_size[1] - 20 - self.exRect.height
        self.filePath = "images/CherryBlossom/slide1.png"
        self.slideImage = image_load(self.filePath)
        self.slideRect = self.slideImage.get_rect()
        self.slideRect.y = scr_size[1] - 20 - self.slideRect.height
        self.rect = self.exRect

    def draw(self, x, y):
        if self.status == 'slide':
            self.slideRect.x = x
            self.rect = self.slideRect
        else:
            self.exRect.x = x
            self.exRect.y = y
            self.rect = self.exRect
        screen.blit(self.image, self.rect)

    def update(self, cnt, status):
        if self.character == '벚꽃맛 쿠키':
            self.filePath = "images/CherryBlossom/"
        elif self.character == '블랙베리맛 쿠키':
            self.filePath = "images/BlackBerry/"
        elif self.character == '양파맛 쿠키':
            self.filePath = "images/Onion/"

        self.filePath += status
        if status == 'run': image_cnt = 4
        elif status == 'jump': image_cnt = 2
        elif status == 'slide': image_cnt = 2
        elif status == 'finish': image_cnt = 6
        elif status == 'landStand': image_cnt = 1

        if (status == 'finish'):
            self.index = (self.finish_cnt % (image_cnt * 8)) // 8 + 1
            self.finish_cnt += 1
            if (self.finish_cnt >= image_cnt * 8):
                self.filePath = self.filePath + str(image_cnt) + ".png"
            else: self.filePath = self.filePath + str(self.index) + ".png"
        else:
            self.index = (cnt % (image_cnt * 4)) // 4 + 1
            self.filePath = self.filePath + str(self.index) + ".png"

        self.image = image_load(self.filePath)
        self.mask = pygame.mask.from_surface(self.image)
        self.status = status


class upObstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(upObstacle, self).__init__()
        num = random.randint(1, 2)
        if num == 1:
            filePath = 'images/obstacle/upper1.png'
            self.image = image_load(filePath)
        else:
            filePath = 'images/obstacle/upper2.png'
            self.image = image_load(filePath)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = scr_size[0]
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self, cnt):
        self.rect.x -= self.speed
        if self.rect.x<=-self.image.get_width(): self.kill()


class midObstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(midObstacle, self).__init__()
        filePath = 'images/obstacle/mid1.png'
        self.image = image_load(filePath)
        self.rect = self.image.get_rect()
        self.rect.x = scr_size[0]
        self.rect.y = scr_size[1]/2 + 20
        self.speed = speed
        self.image_cnt = 5
        self.stop = False
        self.finish_cnt = 0

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, cnt):
        filePath = 'images/obstacle/mid'
        self.index = (self.finish_cnt % (self.image_cnt * 8)) // 8 + 1
        self.finish_cnt += 1
        if (self.finish_cnt >= self.image_cnt * 8):
            filePath = filePath + str(self.image_cnt) + ".png"
        else:
            filePath = filePath + str(self.index) + ".png"

        self.image = image_load(filePath)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x -= self.speed
        if self.rect.x<=-self.image.get_width(): self.kill()


class downObstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        super(downObstacle, self).__init__()
        num = random.randint(1,5)
        self.image = image_load('images/obstacle/down21.png')
        self.rect = self.image.get_rect()
        if num == 1:
            self.filePath = 'images/obstacle/down2'
            self.image_cnt = 2
        else:
            self.filePath = 'images/obstacle/down1'
            self.image_cnt = 4
        self.rect.x = scr_size[0]
        self.speed = speed

    def draw(self):
        ysize = self.image.get_height()
        self.rect.y = scr_size[1] - 20 - ysize
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, cnt):
        filePath = self.filePath
        index = cnt%(self.image_cnt*4)//4 +1
        filePath += str(index)+".png"
        self.image = image_load(filePath)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x -= self.speed
        if self.rect.x<=-self.image.get_width(): self.kill()


# 배경 : 하늘(장애물보다는 속도 느리게)
class backGround():
    def __init__(self):
        self.speed1 = 1
        self.speed2 = 2
        self.speed3 = 3
        self.speed4 = 4
        filePath = 'images/background/background1.png'
        self.image11 = self.image12 = image_load(filePath)
        self.size1 = self.image11.get_size()
        filePath = 'images/background/background2.png'
        self.image21 = self.image22 = image_load(filePath)
        self.size2 = self.image21.get_size()
        filePath = 'images/background/background3.png'
        self.image31 = self.image32 = image_load(filePath)
        self.size3 = self.image31.get_size()
        filePath = 'images/background/background4.png'
        self.image41 = self.image42 = image_load(filePath)
        self.size4 = self.image41.get_size()
        self.x11 = self.x21 = self.x31 = self.x41 = 0
        self.x12 = self.x11 + self.size1[0] - 10
        self.x22 = self.x21 + self.size2[0] - 10
        self.x32 = self.x31 + self.size3[0] - 10
        self.x42 = self.x41 + self.size4[0] - 10

    def draw(self):
        screen.blit(self.image11, (self.x11, -10))
        screen.blit(self.image12, (self.x12, -10))
        screen.blit(self.image21, (self.x21, -10))
        screen.blit(self.image22, (self.x22, -10))
        screen.blit(self.image31, (self.x31, -10))
        screen.blit(self.image32, (self.x32, -10))
        screen.blit(self.image41, (self.x41, -50))
        screen.blit(self.image42, (self.x42, -50))

    def update(self):
        self.x11 -= self.speed1
        self.x12 -= self.speed1
        self.x21 -= self.speed2
        self.x22 -= self.speed2
        self.x31 -= self.speed3
        self.x32 -= self.speed3
        self.x41 -= self.speed4
        self.x42 -= self.speed4

        if self.size1[0]+self.x11<=-1: self.x11 = self.x12 + scr_size[0]
        elif self.size1[0]+self.x12<=-1: self.x12 = self.x11 + scr_size[0]
        if self.size2[0]+self.x21<=-1: self.x21 = self.x22 + scr_size[0]
        elif self.size2[0]+self.x22<=-1: self.x22 = self.x21 + scr_size[0]
        if self.size3[0]+self.x31<=-1: self.x31 = self.x32 + scr_size[0]
        elif self.size3[0]+self.x32<=-1: self.x32 = self.x31 + scr_size[0]
        if self.size4[0]+self.x41<=-1: self.x41 = self.x42 + scr_size[0]
        elif self.size4[0]+self.x42<=-1: self.x42 = self.x41 + scr_size[0]


# 배경 : 땅(장애물과 속도 같게)
class ground():
    def __init__(self, speed):
        self.speed = speed
        filePath = 'images/background/ground.png'
        self.image = image_load(filePath)
        self.x = 0
        self.y = scr_size[1] * 0.7 + 70

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.speed
        if self.x< -self.image.get_width()/2:
            self.x = 0


class score():
    def __init__(self, timeScore):
        self.currentScore = 0
        self.timeScore = timeScore

        self.black = (0, 0, 0)
        self.white = (255,255,255)
        self.font_name = pygame.font.match_font('Fira Code Medium')

    def getScore(self):
        return self.currentScore

    def draw(self):
        font = pygame.font.Font(self.font_name, 24)
        text_surface = font.render(str(self.currentScore), True, self.black)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (scr_size[0] / 2, scr_size[1] * 0.15-1)
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font(self.font_name, 22)
        text_surface = font.render(str(self.currentScore), True, self.white)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (scr_size[0]/2, scr_size[1]*0.15)
        screen.blit(text_surface, text_rect)

    def update(self):
        self.currentScore += self.timeScore


class life():
    def __init__(self, lifeDecrease):
        self.lifeDecrease = lifeDecrease
        filePath = 'images/life/life.jpg'
        self.lifeGauge = image_load(filePath)
        filePath = 'images/life/lifeFinish.png'
        self.lifeFinish = image_load(filePath)
        filePath = 'images/life/EnergyPotion.png'
        self.energy = image_load(filePath)
        self.size = self.lifeGauge.get_size()
        self.energy_x = 0
        self.lifeGauge_x = 15
        self.lifeFinish_x = 5 + self.size[0]
        self.energy_y = 5
        self.lifeGauge_y = 14
        self.lifeFinish_y = self.lifeGauge_y - 1

    def draw(self):
        screen.blit(self.lifeGauge, (self.lifeGauge_x, self.lifeGauge_y),
                    (0, 0, self.lifeFinish_x-10, self.size[1]))
        screen.blit(self.lifeFinish,
                    (self.lifeFinish_x, self.lifeFinish_y))
        screen.blit(self.energy, (self.energy_x, self.energy_y))

    def decrease(self, amount):
        self.lifeFinish_x -= (amount / 20)

    def update(self):
        self.lifeFinish_x -= (self.lifeDecrease/20)

    def isFinish(self):
        if self.lifeFinish_x-10 < self.lifeGauge_x:
            return True
        else: return False


class game():
    def __init__(self, chooseCookie):
        self.cnt = 0
        self.pre_cnt = -30

        self.speed = 6
        lifeDecrease = 1
        timeScore = 100

        if chooseCookie == "벚꽃맛 쿠키":
            self.speed = 7.5
        elif chooseCookie == "블루베리맛 쿠키":
            lifeDecrease = 0.8
        elif chooseCookie == "양파맛 쿠키":
            timeScore = 125

        self.myCookie = Cookie(chooseCookie)
        self.myGround = ground(self.speed)
        self.myBackGround = backGround()
        self.myLife = life(lifeDecrease)
        self.myScore = score(timeScore)

        self.obstacle_sprites = pygame.sprite.Group()

        pygame.display.set_caption('Cookie Run')

        self.clock = pygame.time.Clock()

    def mainGame(self):
        pygame.init()

        global screen

        screen = pygame.display.set_mode(scr_size)

        x = scr_size[0] / 15
        change_y = y = scr_size[1] - 20 - self.myCookie.rect.height
        isJumping = isSliding = up = False
        canJump = True
        jumpCount = 0
        jump_size = 10
        readyToStart = False

        while (readyToStart == False):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    readyToStart = True

        die = False
        while not die:
            if (self.cnt == 9223372036854775800): self.cnt = 0
            self.cnt += 1
            status = 'run'

            for event in pygame.event.get():
                if event.type == pygame.QUIT: die = True
                if event.type == pygame.KEYDOWN:
                    # start slide
                    if event.key == pygame.K_DOWN:
                        isSliding = True
                    # jump
                    if ((event.key == pygame.K_SPACE) |
                        (event.key == pygame.K_z)) & (canJump == True):
                        if canJump:
                            # 두번째 점프일때 aim 설정
                            aim = aim - 90 if (up == True) else change_y - 90
                            isJumping = up = True
                            jumpCount += 1
                            jump_size = 10
                        if jumpCount == 2:
                            jumpCount = 0
                            canJump = False
                elif event.type == pygame.KEYUP:
                    # finish slide
                    if event.key == pygame.K_DOWN:
                        isSliding = False
                        status = 'landStand'

            if isJumping == True:
                status = 'jump'
                if up == True:
                    change_y -= jump_size
                    jump_size -= 1
                    if jump_size < 5: jump_size = 5
                    if change_y <= aim: up = False
                else:
                    change_y += jump_size
                    jump_size += 1
                    if jump_size > 10: jump_size = 10
                    if change_y >= y:
                        change_y = aim = y
                        up = canJump = True
                        isJumping = False
                        status = 'landStand'
            elif isSliding == True:
                status = 'slide'


            if self.pre_cnt+30 <= self.cnt:
                num = random.randint(1, 200)
                if num in [1, 100, 200]:
                    self.canMakeObstacle = False
                    if num == 1:
                        myObstacle = upObstacle(self.speed)
                        self.obstacle_sprites.add(myObstacle)
                    elif num == 100:
                        myObstacle = downObstacle(self.speed)
                        self.obstacle_sprites.add(myObstacle)
                    elif num == 200:
                        myObstacle = midObstacle(self.speed)
                        self.obstacle_sprites.add(myObstacle)
                    self.pre_cnt = self.cnt


            self.myBackGround.update()
            self.myBackGround.draw()
            self.myGround.update()
            self.myGround.draw()

            for obstacle in self.obstacle_sprites:
                obstacle.update(self.cnt)
                obstacle.draw()

            hit = pygame.sprite.spritecollide(
                self.myCookie, self.obstacle_sprites,
                False, pygame.sprite.collide_mask)
            if hit:
                self.myLife.decrease(20)

            self.myScore.update()
            self.myScore.draw()
            self.myCookie.update(self.cnt, status)
            self.myCookie.draw(x, change_y)
            self.myLife.update()
            self.myLife.draw()

            if self.myLife.isFinish() == True: die = True

            pygame.display.update()
            self.clock.tick(FPS)

        self.doFinish()

        pygame.quit()
        return True
        quit()

    def doFinish(self):
        x = scr_size[0] / 15
        y = scr_size[1] * 0.7
        for i in range(0, 100):
            self.myBackGround.draw()
            self.myGround.draw()
            for obstacle in self.obstacle_sprites:
                obstacle.draw()
            self.myCookie.update(self.cnt, 'finish')
            self.myCookie.draw(x, y)
            self.myScore.draw()
            self.myLife.draw()
            pygame.display.update()
            self.clock.tick(FPS)

    def getScore(self):
        return self.myScore.getScore()



if __name__=='__main__':
    mainGame = game('벚꽃맛 쿠키')
    mainGame.mainGame()
    # 블랙베리맛 벚꽃맛 양파맛