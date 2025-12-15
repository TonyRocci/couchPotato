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

while not battle:
    
    try:
        
        #Detect if in battle by looking for mana gauge
        bookLocation = pyautogui.locateOnScreen(book, confidence=0.7)
        
        print("Not in Battle")
        time.sleep(3)
        
    except pyautogui.ImageNotFoundException:

        battle = True
        
        #In case of issues, end program
        if not battle: break
        
while battle:
    
    try:
         
        #Store from: left, top, width, height
        cardLocation = pyautogui.locateOnScreen(card, confidence=0.7)
        
        #Click at card location, interval of 1 sec travel time
        pyautogui.click(cardLocation, interval=1)
        pyautogui.click()
        time.sleep(1)
        
    except pyautogui.ImageNotFoundException:
        
        print("Card not found.")
        time.sleep(3)
         
    
    