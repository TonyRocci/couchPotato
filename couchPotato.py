import pyautogui as gui
import time
from tkinter import *
from tkinter import ttk
import threading as thr

def battle(spell):
    
    #reads image files
    path = "Spells\\" + str(spell) + ".png"
    book = "notBattle.png"
    card = path 
    inBattle = False

    while True:
        while not inBattle:
            
            try:
                #Detect if in inBattle by looking for mana gauge
                bookLocation = gui.locateOnScreen(book, confidence=0.5)
                
                try:
                    #If empty mana gauge is detected, try to potion
                    noMana = gui.locateOnScreen('noMana.png', confidence=0.9)
                    potionLocation = gui.locateOnScreen('potion.png', confidence=0.5)
                    gui.click(potionLocation, interval=1)
                    
                except gui.ImageNotFoundException:
                    
                    print("Not in Battle")
                    gui.keyDown('w')
                    time.sleep(0.1)
                    gui.keyUp('w')
                    time.sleep(5)
                
            except gui.ImageNotFoundException:

                inBattle = True

                
        while inBattle:
            
            try:
                
                #Store from: left, top, width, height
                cardLocation = gui.locateOnScreen(card, confidence=0.5)
                
                #Click at card location, interval of 1 sec travel time
                gui.click(cardLocation, interval=1)
                gui.click()
                time.sleep(1)
                
            except gui.ImageNotFoundException:
                
                print(spell + " not found.")
                time.sleep(5)
                
                try:
                    
                    bookLocation = gui.locateOnScreen(book, confidence=0.5)
                    inBattle = False
                    
                except gui.ImageNotFoundException:
                    
                    inBattle = True
                    pass
                
#Get list of spells
spell = "Zand the Bandit"
aoes = list()
listOfAOEs = open('AOEs.csv')

with open('AOEs.csv') as f:
    for x in f:
        aoes.append(x.replace(',', '').replace('\n', ''))


# Create the main window (root widget)
root = Tk()

# Set the window title and size
root.title("Wizard101 Couch Potato")

mainframe = ttk.Frame(root, padding=(100,100,100,100))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#Create dropdown to choose spell
ttk.Label(mainframe, text="Choose Your Spell:").grid(column=2, row=1, sticky=N)
spellDropdown = ttk.Combobox(mainframe, textvariable=spell, values=aoes, state="readonly")
spellDropdown.grid(column=2, row=2, sticky=W)

#Create button to start program
ttk.Label(mainframe, text="Press to Begin").grid(column=1, row=1, sticky=N)
ttk.Button(mainframe, text="Start", command=lambda: thr.Thread(target=battle, args=(spellDropdown.get(),), daemon=True).start()).grid(column=1, row=2, sticky=E)


#Add padding and reactive resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()