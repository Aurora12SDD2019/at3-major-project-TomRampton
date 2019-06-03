import pygame as p

p.font.init()

class Button():
    def __init__(self, text, x, y, w, h, color, size):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.size = size
                
    def draw(self, gameDisplay):
        p.draw.rect(gameDisplay, self.color (self.x, self.y, self.w, self.h))
        text_font = p.font.SysFont("comicsansms", self.size)
        text_surface = text_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + (self.w/2)) + (self.y + (self.h/2)))
        gamDisplay.blit(text_surface, text_rect)

    def click (self, pos):
        x_pos = pos[0]
        y_pos = pos[1]

        if self.x <= x_pos <= self.x + self.w and self.y <= y_pos <= self.y + self.h:
            return True
        else:
            return False
    
