import numpy as np
import pyautogui
import time

#Get the size of the primary monitor
screenWidth, screenHeight = pyautogui.size()

#reads image files
book = "notBattle.png"
card1 = "card.png"
zand = "zand.png"
battle = False

while not battle:
    
    try:
        
        #Detect if in battle by looking for mana gauge
        bookLocation = pyautogui.locateOnScreen(book)
        
        print("Not in Battle")
        time.sleep(5)
        
    except pyautogui.ImageNotFoundException:

        battle = True
        
        #In case of issues, end program
        if not battle: break
        
while battle:
    
    try:
         
        #Store from: left, top, width, height
        cardLocation = list(pyautogui.locateOnScreen(card1))
        
        #X position = monitor width - distance across
        cardX = cardLocation.get(2) - cardLocation.get(0)
        
        #Y position = monitor height - distance below
        cardY = cardLocation.get(3) - cardLocation.get(1)
        
        pyautogui.click(cardX, cardY, interval=1)
    
    except pyautogui.ImageNotFoundException:
        
        print("Card not found.")
        
         
    
    