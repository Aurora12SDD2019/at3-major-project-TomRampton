import pygame as p

p.font.init()

class message():
    def __init__(self, text, x, y, color, size):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
                
    def draw(self, gameDisplay):
        text_font = p.font.SysFont("comicsansms", self.size)
        text_surface = text_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)
        gamDisplay.blit(text_surface, text_rect)
