__copyright__ = "(c) Thomas Rampton 2019"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Tom"
__version__ = "1.0"
#importing pygame, and the ability for asteroids to spawn random
import pygame as p
import random
from PlayerMovement_Tom import Player
from Button_Tom import Button
from Message_Tom import message 

#used to send and recieve between modules 
player = Player()

#starts the pygame window
p.init()

#creates the variable of clock
clock = p.time.Clock()

#defines what the dimensions of the width and hieght are
width_display = 800
height_display = 600

#displays those dimensions 
gamedisplay = p.display.set_mode((width_display, height_display))

#creates the title for your game
p.display.set_caption("Space Invaders")

#variables that have been used regularly through out the code
ship_side = 60
spaceship_Y = 500
pos = [(width_display/2)-(ship_side)/2,spaceship_Y]
bullet_side = 15


#bullets array

bullets = []

delay_count =0

#imports your images for your space ship and background
millenniumfalcon = p.image.load("spaceship.png")
Galaxy = p.image.load("space background.jpg")
bullet_img = p.image.load("bullet.png")

#scales those images to the appropriate sizes 
millenniumfalcon = p.transform.scale(millenniumfalcon, (ship_side, ship_side))
Galaxy = p.transform.scale(Galaxy, (width_display, height_display))
bullet_img = p.transform.scale(bullet_img, (bullet_side, bullet_side))

def menu_screen():
    menu_buttons = []
    
#creates a function to display your images in the appropriate spot 
def display_update(bullets):
    gamedisplay.blit (Galaxy, (0, 0))
    gamedisplay.blit (millenniumfalcon, pos)

    for bullet in bullets:
        gamedisplay.blit(bullet_img, (bullet[0], bullet[1]))

#creates a function for your game to be exited 
def quit_game():
    p.quit()
    quit()

# this is the main function
def main():
    global delay_count
#reads for any button pressing or actions 
    game_exit = False
    while not game_exit:
        for event in p.event.get():
            if event.type == p.QUIT:
                quit_game()

        direction = 0
#giving an instruction for when a button is pressed 
        keys = p.key.get_pressed()
        if keys [p.K_LEFT] or keys[p.K_a]:
            direction = -1
        if keys [p.K_RIGHT] or keys[p.K_d]:
            direction = 1
#sending this functions outputs to player movement module
        player.ship_movement(pos,direction)

        delay_count += 1
#registers the mouse click or space bar pressing and setting up a timer between shooting
        if delay_count >= 25:
            mouse = p.mouse.get_pressed()
            if mouse[0] or keys[p.K_SPACE]:
                    delay_count = 0
                    player.create_bullet(pos, ship_side, bullet_side, bullets)

        player.update_bullet(bullets)
        
#updates the display and events that have occured 
        display_update(bullets)
        clock.tick(60)
        p.display.update()

#just checking to see if main is main 
if __name__ =="__main__":
    main()


