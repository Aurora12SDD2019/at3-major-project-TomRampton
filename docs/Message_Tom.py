#imports pyagme 
import pygame as p
# initiates pygame 
p.font.init()
#the class for messages 
class Message():
#Sets the values to be used from self to the normmal
    def __init__(self, text, x, y, color, size):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
#function for establishiing the kind of message to be typed  
    def draw(self, gamedisplay):
#the Font to be used 
        text_font = p.font.SysFont("comicsansms", self.size)
#renders the text with colour 
        text_surface = text_font.render(str(self.text), True, self.color)
# gets the rectangle from the Text surface 
        text_rect = text_surface.get_rect()
#sets the center to the current x and y values
        text_rect.center = (self.x, self.y)
        gamedisplay.blit(text_surface, text_rect)
