import math
import pygame
import constants
from PIL import Image, ImageSequence


# Class for a gif that can handle its own frame rate
class Gif:
    def __init__(self, image_name, frame_rate, pos, size):
        self.image_name = image_name
        self.frame_rate = frame_rate
        self.pos = pos

        self.baseGif = Image.open("assets/images/" + image_name)

        self.gifFrames = []

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        for i, frame in enumerate(ImageSequence.Iterator(self.baseGif)):
            filePath = "assets/images/gif-splits/" + image_name + '{:02d}.png'.format(i)
            frame.save(filePath)
            self.gifFrames.append(pygame.transform.scale(pygame.image.load(filePath), size))

        self.frame_number = 0
        self.gif_progression = 0

        self.current_frame = self.gifFrames[self.frame_number]

    def update(self):
        self.gif_progression += self.frame_rate / constants.FRAME_RATE
        shownFrame = math.floor(self.gif_progression)
        if shownFrame > self.baseGif.n_frames - 1:
            self.gif_progression = 0
            shownFrame = 0

        self.current_frame = self.gifFrames[shownFrame]
