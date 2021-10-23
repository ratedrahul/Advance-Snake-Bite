import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
gray = (126, 126, 126)
blue = (0, 0, 255)
orange = (255, 128, 0)

display_width = 1300
display_height = 620

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Rinku bhai Slither')


icon = pygame.image.load('app.png')
pygame.display.set_icon(icon)

img = pygame.image.load('snakeheadNEW.png')


clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def song(dhun):
    # pygame.mixer.init()
    gaana = pygame.mixer.Sound(dhun)

    gaana.play()
    # pygame.mixer.pause()
    # return None


def imagefunc(photo_apple):
    # if photo_apple == 5:
    global snakeLength
    if photo_apple == 3:
        appleimg = pygame.image.load('bjp.png')
        song('vikass.mp3')
        # from time import
        # sleep(2)
        snakeLength+=1
    elif photo_apple == 7:
        appleimg = pygame.image.load('cong.png')
        song('bataomc.wav')
        snakeLength+=1
        # gaana.play()
    elif photo_apple == 9:
        appleimg = pygame.image.load('bjp.png')
        appleimg = pygame.image.load('modi.png')
        appleimg = pygame.image.load('chicken40.jpg')
    elif photo_apple == 15:
        appleimg = pygame.image.load('model.png')
        # appleimg = pygame.image.load('chicken40.jpg')
        # song('in.wav')
        # gaana = pygame.mixer.Sound('bataomc.wav')
        # gaana.play()

    else:
        appleimg = pygame.image.load('chicken40.jpg')

    return appleimg


def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Paused", gray, -100, size='large')
        message_to_screen("Press C to continue or Q to quit",
                          blue, 100, size='medium')
        pygame.display.update()
        clock.tick(5)


def score(x):
    text = smallfont.render("Score: " + str(x), True, white)
    gameDisplay.blit(text, [0, 0])
    if x == 3:
        mc = medfont.render("Arre bhai Vikas ", True, white)
        gameDisplay.blit(mc, [100, 100])
    if x == 10:
        aise = medfont.render("Kese hoga Vikas ", True, orange)
        gameDisplay.blit(aise, [300, 200])
    if x == 16:
        aise = medfont.render("Bulaati he magar Jaane ka nahi ", True, orange)
        gameDisplay.blit(aise, [250, 200])
    if x == 20:
        aise = medfont.render("Kitne Murge Khayega", True, orange)
        gameDisplay.blit(aise, [200, 200])
    if x == 26:
        aise = medfont.render("Ab tak 26", True, orange)
        gameDisplay.blit(aise, [200, 200])
    if x == 50:
        aise = medfont.render("Shandar Jaandar Jabardast 50", True, orange)
        gameDisplay.blit(aise, [200, 200])
    if x == 100:
        aise = medfont.render("100 Shatak ho chuki he", True, orange)
        gameDisplay.blit(aise, [200, 200])
    if x == 105:
        aise = medfont.render("Bas band karo ye khel", True, orange)
        gameDisplay.blit(aise, [200, 200])
        

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))

    return randAppleX, randAppleY


def randImgGen():
    randimgx = round(random.randrange(0, 122))
    randimgy = round(random.randrange(0, 122))

    return randimgx, randimgy


randimgx, randimgy = randImgGen()


def game_intro():

    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen('Welcome to Saap wala Game', green, -180, 'medium')
        message_to_screen(
            "The objective in the game is to eat eat eat ", black, -80, 'small')
        message_to_screen(
            "Bas Saap ko Khilao Khilao Khilao ", red, -60, 'small')
        message_to_screen(
            "The more apple you eat more big you become ", black, -40, 'small')
        message_to_screen(
            "Press C to Play, P to pause, Q to quit", black, 120, 'small')

        saapimg = pygame.image.load('saapfrontleft2.jpg')
        gameDisplay.blit(saapimg, (0, 100))
        rightwali = pygame.image.load('saapfrontright.jpg')
        gameDisplay.blit(rightwali, (900, 150))

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    if direction == "up":
        head = pygame.transform.rotate(img, 0)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [
                         XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    if size == 'medium':
        textSurface = medfont.render(text, True, color)
    if size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displacement, size):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (
        display_width / 2), (display_height / 2) + y_displacement
    gameDisplay.blit(textSurf, textRect)


snakeLength = 1
def gameLoop():
    global snakeLength
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:
        if gameOver == True:
            # gameDisplay.fill(black)
            message_to_screen("GAME OVER ", white, -50, size='large')
            message_to_screen(
                "press q to quit or c to play again ", red, 50, size='medium')

            pygame.display.update()
            while gameOver == True:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        elif event.key == pygame.K_c:
                            gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = - block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = - block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            # lead_x = 100
            # lead_y = 300
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)

        # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(imagefunc(snakeLength), (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        # print(snakeHead[])

        if len(snakeList) > snakeLength:
            del snakeList[0]
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver == True

        snake(block_size, snakeList)

        score(snakeLength - 1)
        x = snakeLength

        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            # print('x cross')
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                song('step.wav')
                # print('Y cross')
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                # song('step.wav')
                song('in1.wav')
                # print('X and Y Crossover')
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        clock.tick(FPS)
    pygame.quit()
    quit()



game_intro()
gameLoop()
