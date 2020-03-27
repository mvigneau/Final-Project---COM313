from graphics import *
from random import *
from Button import *

def Intro_Draw(win):

    intro_image = Image(Point(400,400), "Images/intro.png")
    intro_image.draw(win)

    intro_text = Text(Point(400,50),"Welcome to the Altruists & Egoists Game")
    intro_text.setSize(24)
    intro_text.draw(win)

    Game1_Button = Button(win, Point(200, 100), 100, 25, "Game 1") #Create a button 
    Game1_Button.activate()

    Game2_Button = Button(win, Point(400, 100), 100, 25, "Game 2") #Create a button 
    Game2_Button.activate()

    Game3_Button = Button(win, Point(600, 100), 100, 25, "Game 3") #Create a button 
    Game3_Button.activate()

    Exit_Button = Button(win, Point(400, 750), 100, 25, "Exit") #Create a button 
    Exit_Button.activate()

    return intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button

def Intro_Undraw(intro_image, intro_text, Game1_Button, Game2_Button, Game3_Button, Exit_Button):

    intro_image.undraw()
    Game1_Button.deactivate()
    Game1_Button.undraw()
    Game2_Button.deactivate()
    Game2_Button.undraw()
    Game3_Button.deactivate()
    Game3_Button.undraw()
    intro_text.undraw()
    Exit_Button.deactivate()
    Exit_Button.undraw()
    
