#importing pygame
import pygame as p
#initiate pygame
p.font.init()
#The class for button 
class Button():
#funciton for the values of the variables 
    def __init__(self, text, x, y, w, h, colour, size):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
        self.size = size
#draws the rectangle using the variables set              
    def draw(self, gamedisplay):
        p.draw.rect(gamedisplay, self.colour, (self.x, self.y, self.w, self.h))
#sets the font, where to posititon the text, then telling the text to surface on the rectangle      
        text_font = p.font.SysFont("comicsansms", self.size)
        text_surface = text_font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        
       
        text_rect.center = ((self.x + (self.w/2)), (self.y + (self.h/2)))
        
        gamedisplay.blit(text_surface, text_rect)
#seperating the X an Y postitions 
    def click (self, pos):
        x_pos = pos[0]
        y_pos = pos[1]
#if it is clicked within the boundaries 
        if self.x <= x_pos <= self.x + self.w and self.y <= y_pos <= self.y + self.h:
            return True # returns it as true that the button as clicked  
        else:
            return False # returns false that the button was clicked 
    
