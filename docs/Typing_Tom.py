#imports paygame
import pygame as p
#the class handelling the typing 
class Typing:
    #initiating the self.word as word
    def __init__(self, word):
        self.word = word

    #the sets what letters pressed mean what 
    def letters(self):
        #sets letters to a space
        letter = ""
        #if a key is pressed it will be set to keys 
        keys = p.key.get_pressed()
        # if backspace is pressed then it will minus one from self.word then fill it in with a space
        if keys[p.K_BACKSPACE]:
            try:
                self.word = list(self.word)
                del self.word[-1]
                self.word = "".join(self.word)
            except:
                pass
        #if space is pressed then it will plus a space to self.word
        elif keys[p.K_SPACE]:
            letter = " "
        #if a letter is pressed it will be tested through all of the vairables until it matches on of these then add what ever that vartiable equals
        elif keys[p.K_a]:
            letter = "a"
        elif keys[p.K_b]:
            letter = "b"
        elif keys[p.K_c]:
            letter = "c"
        elif keys[p.K_d]:
            letter = "d"
        elif keys[p.K_e]:
            letter = "e"
        elif keys[p.K_f]:
            letter = "f"
        elif keys[p.K_g]:
            letter = "g"
        elif keys[p.K_h]:
            letter = "h"
        elif keys[p.K_i]:
            letter = "i"
        elif keys[p.K_j]:
            letter = "j"
        elif keys[p.K_k]:
            letter = "k"
        elif keys[p.K_l]:
            letter = "l"
        elif keys[p.K_m]:
            letter = "m"
        elif keys[p.K_n]:
            letter = "n"
        elif keys[p.K_o]:
            letter = "o"
        elif keys[p.K_p]:
            letter = "p"
        elif keys[p.K_q]:
            letter = "q"
        elif keys[p.K_r]:
            letter = "r"
        elif keys[p.K_s]:
            letter = "s"
        elif keys[p.K_t]:
            letter = "t"
        elif keys[p.K_u]:
            letter = "u"
        elif keys[p.K_v]:
            letter = "v"
        elif keys[p.K_w]:
            letter = "w"
        elif keys[p.K_x]:
            letter = "x"
        elif keys[p.K_y]:
            letter = "y"
        elif keys[p.K_z]:
            letter = "z"
        #sets self.word to the str that is made up from the keys pressed
        self.word = str(self.word) + str(letter)
        #returns self.word
        return self.word
