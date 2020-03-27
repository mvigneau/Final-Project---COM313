################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support an introduction interface and three different game or setup that allows the user to;
##    1. Play Game 1, the regular altruists and egoists game where every agent has 2 neighbors and only consider the two neighbors to make a decision
##    2. Play Game 2, where the agents still have only 2 neighbors, but this time consider there 2 closest neighbors on each side to make a decision
##    3. Play Game 3, where some agents have up to 4 neighbors and consider their 4 neighbors to make a decision.
##    The file contains the main function, which primary function is to make sure the game runs properly and
##    efficiently in a logical manner for the user. It fetches from Intro, Game1, Game2, and Game3 files to run.  
#################################################


## some important files being imported ##
from graphics import *
from Intro import *
from Game1 import *
from Game2 import *
from Game3 import *

## The method allows the game to work in its entirety ##
def main():

    ### Upload the window & the Intro menu ###
    win = GraphWin("Final Project 313", 800, 800)
    intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button = Intro_Draw(win)

    ### Give a click to the user ###
    pt = win.getMouse()
    
    while(Exit_Button.isClicked(pt) == False):

        if(Game1_Button.isClicked(pt)): ## if game 1 button is clicked then game 1 is being played
            Intro_Undraw(intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button)
            Game1(win)
            intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button = Intro_Draw(win)

        elif(Game2_Button.isClicked(pt)): ## if game 2 button is clicked then game 2 is being played
            Intro_Undraw(intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button)
            Game2(win)
            intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button = Intro_Draw(win)

        elif(Game3_Button.isClicked(pt)): ## if game 3 button is clicked then game 3 is being played
            Intro_Undraw(intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button)
            Game3(win)
            intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button = Intro_Draw(win)

        pt = win.getMouse()  ## Another click is given to the user in case he/she doesn't hit any buttons

    win.close() ## if quit button click then the window is closed and the game ends.
    sys.exit()
  
main()
