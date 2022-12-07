import os
import pygame as pg
import pygame.image
from PIL import Image

pg.init()
# pg.mixer.init()

catFiles = []

for i in range(46):
    numString = ""
    if(i < 10):
        numString = "0"
    numString += str(i)
    catFiles.append("venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile0" + numString + ".png")

print(catFiles)

pg.display.set_caption("PET THE CAT!")
screenSize = (750, 750)
window = pg.display.set_mode(screenSize)
# image = pg.image.load("venv/assets/images/couchbackground.jpg")
frames = []

# pg.mixer.music.load("")
# pg.mixer.music.set_volume(0.5)
# pg.mixer.music.play()

# image = pg.transform.scale(image, screenSize)
clock = pg.time.Clock()
frameTracker = 1
clicks = 0
color = (50, 50, 50)
catType: int = 0

# process the mouse gif
image = Image.open("venv/assets/images/petpet.gif")
for frame in range(image.n_frames):
    image.seek(frame)
    gifSize = image.size
    data = image.tobytes()
    gameImage = pg.image.fromstring(data, gifSize, image.mode)
    gameImage = pg.transform.scale(gameImage, (64,64))
    frames.append(gameImage)

catType = 34

# initialize the mouse info
pg.mouse.set_visible(False)
mouseImg = pygame.image.load("venv/assets/images/petpet.gif")
mouseImgRect = mouseImg.get_rect()

window.fill(color)

cat = pygame.image.load(catFiles[catType])
cat = pygame.transform.scale(cat, (64,64))
catRect = cat.get_rect()

while (True):
    pg.event.get()

    if frameTracker == image.n_frames:
        frameTracker = 1

    if clicks == 30:
        if catType == 45:
            catType = 0
        else:
            catType += 1

    catRect.center = window.get_rect().center
    window.blit(cat, catRect)
    mouseImgRect.center = pygame.mouse.get_pos()
    framesRect = frames[frameTracker].get_rect()
    framesRect.center = pg.mouse.get_pos()

    window.blit(frames[frameTracker], framesRect)
    frameTracker += 1

    clock.tick(25)

    pg.display.update()
    window.fill(color)
