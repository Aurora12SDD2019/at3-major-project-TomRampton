__copyright__ = "(c) Thomas Rampton 2019"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Tom"
__version__ = "1.0"
#importing pygame, and the ability for asteroids to spawn random
import pygame as p
import random
from PlayerMovement_Tom import Player
from Button_Tom import Button
from Message_Tom import Message
from Enemy_Tom import Enemy 

#used to send and recieve between modules 
player = Player()
enemy = Enemy()

#starts the pygame window
p.init()

#sounds imported
p.mixer.music.load("Big_Explosion_Cut_Off.wav")
shoot_sound = p.mixer.Sound("shooting.wav")
explosion_sound = p.mixer.Sound("The_Nexus_Riddim.wav")


#creates the variable of clock
clock = p.time.Clock()

#defines what the dimensions of the width and height are
width_display = 800
height_display = 600

#displays those dimensions 
gamedisplay = p.display.set_mode((width_display, height_display))

#creates the title for your game
p.display.set_caption("Space Invaders")

#the background image loaded and transformed
Galaxy = p.image.load("space background.jpg")
Galaxy = p.transform.scale(Galaxy, (width_display, height_display))

#variables that have been used regularly through out the code
blue = (0, 0, 255)
red = (255, 0, 0)
pink = (255,182,193)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255,165,0)
green =  (0,0,200)

pause = False

#function for The starting menu screen
def menu_screen():
    global delay_count
   
#this sets the layout of the button of play quit and the instructions 
    menu_buttons = [Button("Play", 140, 280, 150, 100, blue, 60),
                    Button("Quit", 460, 280, 150, 100, red, 60),
                    Button("Instructions", 180, 420, 400, 100, pink, 60)]
# sets the title of space invaders up 
    menu_title = Message("Space Invaders", 400, 60, white, 100)
# set the run to true 
    run = True
# the while this is true 
    while run:
# displays the background, buttons, and the title
        gamedisplay.blit(Galaxy, (0, 0))
        menu_title.draw(gamedisplay)
        for btn in menu_buttons:
            btn.draw(gamedisplay)
# if though you press the X in the top 
        for event in p.event.get():
            if event.type == p.QUIT:
# it will quit the game 
                quit_game()
# this here will read your event if the mouse is pressed 
            if event.type == p.MOUSEBUTTONDOWN:
                position = p.mouse.get_pos()
# states if it is pressed in any of the menu_ buttons 
                for btn in menu_buttons:
                    if btn.click(position):
# if clicked in play, then will go to the main function and play the game 
                        if btn.text == "Play":
                           main()
# if clicked in quit, then will quit 
                        elif btn.text == "Quit":
                            quit_game()
# if clicked in instructions, then will go to the def instuctions
                        elif btn.text == "Instructions":
                            instructions()
# sets the clcck speed, and the rate it is being updated at 
        clock.tick(60)
        p.display.update()
# The instructions function 
def instructions():


# imports the images for the instructions 
    left_click = p.image.load("Mouse.png")
    keys = p.image.load("Keys.png")
    WASD = p.image.load ("WASD.png")
    SpaceBar= p.image.load("Spacebar.png")
    
    
# sets where the back and title re placed 
    back = Button("Back", 300, 420, 150, 100, red, 60)
    title = Message("Instructions", 300, 40, black, 100)

# sets run to true 
    run = True
# then while it is fills the backgrouond white, draws the title and the back button
    while run:
        gamedisplay.fill(white)

        title.draw(gamedisplay)

        back.draw(gamedisplay)
# determines if event has occured 
        for event in p.event.get():
# and if it is the X 
            if event.type == p.QUIT:
# quits the game 
                quit_game()
# then if a mouse button has been pressed
            if event.type == p.MOUSEBUTTONDOWN:
# grabs its position
                position = p.mouse.get_pos()
# and if it is in the back button 
                if back.click(position):
# then sends it back to the main menu
                    if back.text == "Back":
                        menu_screen()
# this displays the back and the title 
        back.draw(gamedisplay)
        title.draw(gamedisplay)
# this displays the images in the coordinates 
        gamedisplay.blit(left_click, (100, 150))
        gamedisplay.blit(SpaceBar, (400, 150))
        gamedisplay.blit(keys, (60, 375))
        gamedisplay.blit(WASD, (490, 375))
# this sets the rate of which it is being updated 
        clock.tick(60)
        p.display.update()

def death():
    p.mixer.music.pause()
    died = True
    while died:
        death_buttons = [Button("Retry", 125, 280, 200, 100, orange, 60),
                         Button("Quit", 535, 280, 150, 100, red, 60)]
        title = Message ("GAMEOVER!!", 400, 140, white, 100)

        for event in p.event.get():
            if event.type == p.QUIT:
                quit_game()
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                for btn in death_buttons:
                    if btn.click(pos):
                        if btn.text == "Retry":
                            main()
                        elif btn.text == "Quit":
                            quit_game()

        for btn in death_buttons:
            btn.draw(gamedisplay)
        title.draw(gamedisplay)

        clock.tick(60)
        p.display.update()

def unpause():
    global pause
    p.mixer.music.unpause()
    pause = False

def paused():
    p.mixer.music.pause()
    while pause:
        pause_buttons = [Button("Back", 215, 280, 150, 100, green, 60),
                         Button("Quit", 535, 280, 150, 100, red, 60)]
        title = Message("Paused", 400, 140, white, 100)

        for event in p.event.get():
            if event.type == p.QUIT:
                quit_game()
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                for btn in pause_buttons:
                    if btn.click(pos):
                        if btn.text == "Back":
                            unpause()
                        elif btn.text == "Quit":
                            quit_game()

        for btn in pause_buttons:
            btn.draw(gamedisplay)
        title.draw(gamedisplay)

        clock.tick(60)
        p.display.update()
        
    
#creates a function to display your images in the appropriate spot 
def display_update(bullets, pos, aliens, millenniumfalcon, kill_count, bullet_img):
    
    gamedisplay.blit (Galaxy, (0, 0))
    gamedisplay.blit (millenniumfalcon, pos)

    for bullet in bullets:
        gamedisplay.blit(bullet_img, (bullet[0], bullet[1]))
        
    for alien in aliens:
        img = alien[0]
        pos = alien[1]
        x = pos[0]
        y = pos[1]
        gamedisplay.blit(img, (x, y))

    score_message = [Message("Score:", 650, 40, white, 40), Message(kill_count, 750, 40, white, 40)] 
    for message in score_message:
        message.draw(gamedisplay)

#creates a function for your game to be exited 
def quit_game():
    p.quit()
    quit()

# this is the main function
def main():

    global pause

    p.mixer.music.play(-1)
    
#variables used in the function
    ship_side = 60
    spaceship_Y = 500
    pos = [(width_display/2)-(ship_side)/2,spaceship_Y]
    bullet_side = 15
    alien_side = 35
    delay_count = 0
#imports the images 
    Tom = p.image.load("alien 1.png")
    Bailey = p.image.load("alien 2.png")
    Matt = p.image.load("alien 3.png")
    explosion = p.image.load("explosion.png")
    millenniumfalcon = p.image.load("spaceship.png")
    bullet_img = p.image.load("bullet.png")

#scales those images to the appropriate sizes 
    millenniumfalcon = p.transform.scale(millenniumfalcon, (ship_side, ship_side))
    explosion = p.transform.scale(explosion, (ship_side, ship_side))
    bullet_img = p.transform.scale(bullet_img, (bullet_side, bullet_side))
    Tom = p.transform.scale(Tom, (alien_side, alien_side))
    Bailey = p.transform.scale(Bailey, (alien_side, alien_side))
    Matt = p.transform.scale(Matt, (alien_side, alien_side))

#sets all the alien images to 1 variable 
    alien_imgs = [Tom, Bailey, Matt]

    player_current = millenniumfalcon
#sets the delay up for the aliens and bullets
    shooting_delay = 0
    alien_delay = 0
    
#sets kill count to 0
    kill_count = 0
# the arrays 
    bullets =[]
    aliens =[]

#reads for any button pressing or actions 
    game_exit = False
    while not game_exit:
        for event in p.event.get():
            if event.type == p.QUIT:
                quit_game()

        if player_current == explosion:
            p.mixer.Sound.play(explosion_sound)
            death()

        direction = 0

#giving an instruction for when a button is pressed 
        keys = p.key.get_pressed()
        if keys[p.K_p] or keys[p.K_ESCAPE]:
            pause = True
            paused()
        if keys [p.K_LEFT] or keys[p.K_a]:
            direction = -1
        if keys [p.K_RIGHT] or keys[p.K_d]:
            direction = 1
#sending this functions outputs to player movement module
        player.ship_movement(pos,direction)

        delay_count += 1
        alien_delay += 1
#registers the mouse click or space bar pressing and setting up a timer between shooting
        if delay_count >= 25:
            mouse = p.mouse.get_pressed()
            if mouse[0] or keys[p.K_SPACE]:
                    delay_count = 0
                    player.create_bullet(pos, ship_side, bullet_side, bullets)

        player.update_bullet(bullets)


        if alien_delay >= 50:
            aliens = enemy.alien_spawn(aliens, alien_imgs)
            alien_delay = 0
        aliens, kill_count = enemy.alien_movement(aliens, kill_count)

        player_current = player.check_hit(pos, player_current, millenniumfalcon, explosion, aliens, ship_side, alien_side)
        
        bullets, aliens, kill_count = enemy.check_hit(bullets, aliens, alien_imgs, kill_count)

        if kill_count < 0:
            kill_count = 0
            death()

#updates the display and events that have occured
        display_update(bullets, pos, aliens, millenniumfalcon, kill_count, bullet_img)
        clock.tick(60)
        p.display.update()
#just checking to see if main is main 
if __name__ =="__main__":
    menu_screen()


