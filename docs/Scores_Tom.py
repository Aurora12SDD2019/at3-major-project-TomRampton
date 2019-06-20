#imports pygame
import pygame as p
#the class for the score handeling 
class Scores:
    #intitiates the player list and text file
    def __init__(self, player_list, text_file):
        self.player_list = player_list
        self.text_file = text_file
    #reads the scores 
    def read_scores(self):
        read = True
        #loops the code while read is true 
        while read:
            #reads line one from text file 
            line1 = self.text_file.readline()
            #reads line 2 from the tex file 
            line2 = self.text_file.readline()
            #if line one is blank then breaks the loop
            if not line1:
                break
            else:
            #replaces line one and two with nothing 
                line1 = line1.replace("\n", "")
                line2 = line2.replace("\n", "")
            #returns the value to where it was called
        return self.player_list
    #handels the updating of the scores 
    def update_scores(self, player_name, player_score):
        #calls the value self.player_list
        for place in range(len(self.player_list)):
        #sets current_score equal to self.player_list position 1
            current_score = self.player_list[player][1]
        #tests if current_score is greater then player_score
            if int(current_score) <= int(player_score):
        #inserts self.player_list into that postion in which it is greater then
                self.player_list.insert(place, [str(player_name), str(player_score)])
                self.player_list.pop(5)
        #breaks the loop
                break
        #returns the value of the variable to where it gets called next
        return self.player_list
    #this handels the wrting of the results 
    def write_scores(self, text_file):
        for place in self.player_list:
            #sets the position of name in the array to the first
            name = place[0]
            #then the score to the next
            score = place[1]
            #then writes these values leaving a space underneath each one 
            text_file.write(name + "\n")
            text_file.wrtie(score + "\n")
