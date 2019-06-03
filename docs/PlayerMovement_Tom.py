#imported pygame
import pygame as p
#created a class used to create velocity of the player, and the barriers for when to stop
class Player:
    def __init__(self):
#sets the speed of the player and the length of sides of the player
        self.player_speed = 3
        self.ship_side = 60
        self.bullet_speed = 8
        
# this function process the outputs from the main function
    def ship_movement (self, player_pos, direction):
#X velocity is set by timsing the direction worked out from the main, by the speed set above
        x_velocity = direction * self.player_speed
#then this sets the players current postion of x to 0        
        current_x = player_pos [0]
#this is then work out the future movements in advance before moving your player by plusing your velocity with the current of x 
        potential_x = x_velocity + current_x
# this final if statement sets the barriers or the walls the players can't move through 
        if (potential_x +self.ship_side) < 800 and potential_x > 0:
            player_pos[0] = potential_x
#this assigns the spawn point of the bullet
    def create_bullet (self, position, ship_side, bullet_side, bullets):
        x = (position[0] + (ship_side/2)) - (bullet_side/2)
        y = position[1]
        bullets.append([x, y])
#this alows the bullet to move at a certain speed 
    def update_bullet (self, bullets):
        for bullet in range(len(bullets)):
            bullets[bullet][1] -= self.bullet_speed
# deletes the bullet at the end of the screen
        for bullet in bullets[:]:
            if bullet[1] < 0:
                bullets.remove(bullet)
