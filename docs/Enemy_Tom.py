#imports pygame and random
import pygame as p
import random
#class handeling enemies
class Enemy:
    #initiating alien_side,speed, and bullet_side to their values 
    def __init__ (self):
        self.alien_side = 35
        self.alien_speed = 0.5
        self.bullet_side = 15
    #this handels the aliens spawning
    def alien_spawn(self, aliens, alien_imgs):
        #sets the x a random spot between 20 and 780
        x = random.randrange(20 + self.alien_side, 780 - self.alien_side)
        # then y to -35
        y = -35
        #sets the x variable to img
        img = random.randrange (0, 3)
        #sets img to the alien image
        img = alien_imgs[img]
        #appends the aliens image, then their x, and y 
        aliens.append([img, [x, y]])
        #reurns aliens 
        return aliens
    #handels the movemnt of the aliens 
    def alien_movement(self, aliens, kill_count):
        for alien in aliens[:]:
            #sets the pos to alien[1] in the array
            pos = alien[1]
            #sets y to pos[1]
            y = pos[1]
            #tests if the alien has reached below the player, then removes the aliens and -20 from the score
            if y > 600:
                aliens.remove(alien)
                kill_count -= 20 
        #seperates the pos from alien, and y from pos then updates the y to animate and then sets the new pos to the alien
        for alien in range(len(aliens)):
            pos = aliens[alien][1]
            y = pos[1]
            y = y + self.alien_speed
            aliens[alien][1][1] = y
        #returns aliens and kill_count
        return aliens, kill_count
    ##checks if the alien is hit by the bullet 
    def check_hit(self, bullets, aliens, alien_imgs, kill_count):
        for alien in aliens:
            #seperates the alien from the list
            img = alien[0]
            #seperates pos from the list
            pos = alien[1]
            #seperates the x from the list
            alien_x = pos[0]
            #seperates the y from the list
            alien_y = pos[1]

            #looks at all the bullet in bullets and seperates the x and y for bullet
            for bullet in bullets[:]:
                bullet_x = bullet[0]
                bullet_y = bullet[1]

            #tests if the bullet is within the alien hit box and y
                if (bullet_y <= (alien_y + self.alien_side)) and (bullet_y >= alien_y):
            #tests if the bullet is within the alien hit box and x
                    if (bullet_x >= (alien_x - self.bullet_side)) and (bullet_x <= (alien_x + self.alien_side)):
                       # if the img hit is the first img, then +10 
                        if img == alien_imgs[0]:
                            kill_count += 10
                        if img == alien_imgs[1]:
                        #if the img hit is the second, then +20
                            kill_count += 20
                        if img == alien_imgs[2]:
                        #if the img hit is the third, then +40
                            kill_count += 40
                        #then removes the bullets, and aliens and increases the aliens speed by 0.01
                        bullets.remove(bullet)
                        aliens.remove(alien)
                        self.alien_speed += 0.01
        #returns the variables of bullets, aliens, and kill_count                
        return bullets, aliens, kill_count 
            
                        


