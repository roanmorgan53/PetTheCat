# imports
import pygame as pg
import pygame.image
import constants

from gif import Gif

from PIL import Image

# Game Data
catImages = []

gameClock = pg.time.Clock()
frameTracker = 1

# Player Variables
clicks = 0
lastMilestone = -1
catType = 0

# initialize pygame
pg.init()

# Fill the array with cat images
for i in range(46):
    filePath = "assets/sprites/cats/sprites/tile0" + "{:02d}".format(i) + ".png"
    catImages.append(pygame.image.load(filePath))

# Window Setup
pg.display.set_caption("PET THE CAT!")
SCREEN_SIZE = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
gameWindow = pg.display.set_mode(SCREEN_SIZE)
pg.mouse.set_visible(False)

iconGif = Gif("icon.gif", 15, (0, 0), (32, 32))
cursorGif = Gif("cursor.gif", 20, (0, 0), (64, 64))

cat = pygame.Rect((0, 0), (constants.CAT_SIZE, constants.CAT_SIZE))
cat.center = (int(constants.SCREEN_WIDTH/2),int(constants.SCREEN_HEIGHT/2))

while True:

    # Set the background color
    gameWindow.fill(constants.BACKGROUND_COLOR)

    # Set the icon
    pg.display.set_icon(iconGif.current_frame)

    # cycle through different cats every 30 iterations

    # move cursor
    cursorGif.rect.center = pygame.mouse.get_pos()

    # search for mouse collision with exit button
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cat.collidepoint(pygame.mouse.get_pos()):
                clicks += 1

    # Progress Cat
    if clicks % 30 == 0 and clicks != lastMilestone:
        lastMilestone = clicks
        catType += 1
    if catType == 46:
        catType = 0

    # update Gifs
    iconGif.update()
    cursorGif.update()

    # draw cat
    gameWindow.blit(pygame.transform.scale(catImages[catType], cat.size), cat.topleft)

    # draw cursor
    gameWindow.blit(cursorGif.current_frame, cursorGif.rect.topleft)

    # Keep the frame rate
    gameClock.tick(constants.FRAME_RATE)

    # Update the display
    pg.display.update()
