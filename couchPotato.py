import numpy as np
import pyautogui
import time
import tkinter as tk


#Get the size of the primary monitor
screenWidth, screenHeight = pyautogui.size() 

#Code for window

# Create the main window (root widget)
root = tk.Tk()

# Set the window title
root.title("Wizard101 Couch Potato")

#Window width/height set to 1/3 of monitor resolution
root.geometry(str(int(screenWidth / 3)) + "x" + str(int(screenHeight / 3)))

#  Start the main event loop
# root.mainloop()

#reads image files
book = "notBattle.png"
card = "zand.png"
battle = False
while True:
    while not battle:
        
        try:
            #Detect if in battle by looking for mana gauge
            bookLocation = pyautogui.locateOnScreen(book, confidence=0.5)
            
            try:
                
                noMana = pyautogui.locateOnScreen('noMana.png', confidence=0.9)
                potionLocation = pyautogui.locateOnScreen('potion.png', confidence=0.5)
                pyautogui.click(potionLocation, interval=1)
                
            except pyautogui.ImageNotFoundException:
                
                print("Not in Battle")
                pyautogui.keyDown('w')
                time.sleep(0.1)
                pyautogui.keyUp('w')
                time.sleep(5)
            
        except pyautogui.ImageNotFoundException:

            battle = True

            
    while battle:
        
        try:
            
            #Store from: left, top, width, height
            cardLocation = pyautogui.locateOnScreen(card, confidence=0.5)
            
            #Click at card location, interval of 1 sec travel time
            pyautogui.click(cardLocation, interval=1)
            pyautogui.click()
            time.sleep(1)
            
        except pyautogui.ImageNotFoundException:
            
            print("Card not found.")
            time.sleep(5)
            
            try:
                
                bookLocation = pyautogui.locateOnScreen(book, confidence=0.5)
                battle = False
                
            except pyautogui.ImageNotFoundException:
                
                battle = True

         
    
    