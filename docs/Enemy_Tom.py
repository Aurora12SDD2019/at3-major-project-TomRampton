import pygame as p
import random

class Enemy:

    def __init__ (self):
        self.alien_side = 35
        self.alien_speed = 0.5
        self.bullet_side = 15

    def alien_spawn(self, aliens, alien_imgs):
        x = random.randrange(20 + self.alien_side, 780 - self.alien_side)
        y = -35
        img = random.randrange (0, 3)
        img = alien_imgs[img]
        aliens.append([img, [x, y]])
        return aliens

    def alien_movement(self, aliens, kill_count):
        for alien in aliens[:]:
            pos = alien[1]
            y = pos[1]
            if y > 600:
                aliens.remove(alien)
                kill_count -= 20 

        for alien in range(len(aliens)):
            pos = aliens[alien][1]
            y = pos[1]
            y = y + self.alien_speed
            aliens[alien][1][1] = y

        return aliens, kill_count

    def check_hit(self, bullets, aliens, alien_imgs, kill_count):
        for alien in aliens:
            img = alien[0]
            pos = alien[1]
            alien_x = pos[0]
            alien_y = pos[1]

            for bullet in bullets[:]:
                bullet_x = bullet[0]
                bullet_y = bullet[1]

                if (bullet_y <= (alien_y + self.alien_side)) and (bullet_y >= alien_y):
                    if (bullet_x >= (alien_x - self.bullet_side)) and (bullet_x <= (alien_x + self.alien_side)):
                        if img == alien_imgs[0]:
                            kill_count += 10
                        if img == alien_imgs[1]:
                            kill_count += 20
                        if img == alien_imgs[2]:
                            kill_count += 40
                        bullets.remove(bullet)
                        aliens.remove(alien)
                        self.alien_speed += 0.01
                        
        return bullets, aliens, kill_count 
            
                        


