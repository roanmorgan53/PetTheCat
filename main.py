import os
import pygame as pg
import pygame.image
from PIL import Image

pg.init()
# pg.mixer.init()

catFiles = [45]

# manually adding in all the sprites into the list
catFiles[0] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile000.png"
catFiles.append(0)
catFiles[1] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile001.png.png"
catFiles.append(1)
catFiles[2] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile002.png.png"
catFiles.append(2)
catFiles[3] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile003.png.png"
catFiles.append(3)
catFiles[4] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile004.png"
catFiles.append(4)
catFiles[5] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile005.png"
catFiles.append(5)
catFiles[6] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile006.png"
catFiles.append(6)
catFiles[7] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile007.png"
catFiles.append(7)
catFiles[8] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile008.png"
catFiles.append(8)
catFiles[9] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile009.png"
catFiles.append(9)
catFiles[10] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile010.png"
catFiles.append(10)
catFiles[11] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile011.png"
catFiles.append(11)
catFiles[12] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile012.png"
catFiles.append(12)
catFiles[13] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile013.png"
catFiles.append(13)
catFiles[14] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile014.png"
catFiles.append(14)
catFiles[15] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile015.png"
catFiles.append(15)
catFiles[16] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile016.png"
catFiles.append(16)
catFiles[17] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile017.png"
catFiles.append(17)
catFiles[18] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile018.png"
catFiles.append(18)
catFiles[19] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile019.png"
catFiles.append(19)
catFiles[20] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile020.png"
catFiles.append(20)
catFiles[21] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile021.png"
catFiles.append(21)
catFiles[22] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile022.png"
catFiles.append(22)
catFiles[23] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile023.png"
catFiles.append(23)
catFiles[24] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile024.png"
catFiles.append(24)
catFiles[25] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile025.png"
catFiles.append(25)
catFiles[26] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile026.png"
catFiles.append(26)
catFiles[27] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile027.png"
catFiles.append(27)
catFiles[28] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile028.png"
catFiles.append(28)
catFiles[29] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile029.png"
catFiles.append(29)
catFiles[30] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile030.png"
catFiles.append(30)
catFiles[31] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile031.png"
catFiles.append(31)
catFiles[32] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile032.png"
catFiles.append(32)
catFiles[33] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile033.png"
catFiles.append(33)
catFiles[34] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile034.png"
catFiles.append(34)
catFiles[35] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile035.png"
catFiles.append(35)
catFiles[36] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile036.png"
catFiles.append(36)
catFiles[37] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile037.png"
catFiles.append(37)
catFiles[38] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile038.png"
catFiles.append(38)
catFiles[39] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile039.png"
catFiles.append(39)
catFiles[40] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile040.png"
catFiles.append(40)
catFiles[41] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile041.png"
catFiles.append(41)
catFiles[42] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile042.png"
catFiles.append(42)
catFiles[43] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile043.png"
catFiles.append(43)
catFiles[44] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile044.png"
catFiles.append(44)
catFiles[45] = "venv/assets/sprites/just-a-few-cats-v1.1.0/sprites/tile045.png"
catFiles.append(45)

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
