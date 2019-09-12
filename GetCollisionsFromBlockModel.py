####### Done by KiroTheBlueFox #########
#                                      #
#  This is free to use                 #
#  You can redistribute it with proper #
#  credits (keep the credits)          #
#  Do not claim it as your program !   #
#  Credits to me (in your mod) are     #
#  very welcomed !                     #
#  You can modify the program but keep #
#  these credits !                     #
#  Please do not remove this comment ! #
#                                      #
########################################

import platform
import subprocess
import json
import os
import re
from tkinter import *
from tkinter import filedialog

try: 
    from PIL import Image, ImageTk
except:
    subprocess.call(['py','-m','pip', 'install', "Pillow"])
    from PIL import Image, ImageTk
FOLDER = os.path.dirname(os.path.abspath(__file__))

OPEN = True

### Screensize ###

ScreensizeWindow = Tk()
ScreensizeWindow.update_idletasks()
ScreensizeWindow.attributes("-fullscreen", True)
ScreensizeWindow.state("iconic")
Screensize = ScreensizeWindow.winfo_geometry()
ScreensizeWindow.destroy()
Screensize = Screensize[:-4]
Screensize = re.split("x",Screensize)
ScreensizeX = int(Screensize[0])
ScreensizeY = int(Screensize[1])
CenterX = ScreensizeX//2
CenterY = ScreensizeY//2




def on_closing():
    global OPEN
    OPEN = False
    currentWindow.destroy()
    exit()

def CenterWindow(window, windowSizeX = 300, windowSizeY = 200):
    window.state("iconic")
    windowSize = window.winfo_geometry()
    windowSize = windowSize[:-4]
    windowSize = re.split("x",windowSize)
    if windowSizeX == 300:
        windowSizeX = 300
    if windowSizeY == 200:
        windowSizeY = 200
    windowCenterX = windowSizeX//2
    windowCenterY = windowSizeY//2
    windowGeometry = str(windowSizeX)+"x"+str(windowSizeY)+"+"+str(CenterX-windowCenterX)+"+"+str(CenterY-windowCenterY)
    window.geometry(windowGeometry)
    window.state("normal")

while OPEN == True:
    CONFIG = open(os.path.join(FOLDER, "config.txt"),"r", encoding="utf8")
    for line in CONFIG:
        if line.lower().startswith("#     mcversion = "):
            value = line[18:].lower()
            if value.startswith("1.14"):
                VERSIONCHECK = False
                VERSION = "1.14"
            elif value.startswith("1.12"):
                VERSIONCHECK = False
                VERSION = "1.12"
            else:
                VERSIONCHECK = True
    
    ### Title Bar ###
    
    def setTitleBar(window,method="pack",SizeY=0):
        TitleBarLabel = Label(window,text="Collision Generator",background="#17191d",relief="flat",foreground="#cacad4",font=("Arial",-24,"bold"))
        TitleBarLabel.pack(fill="x")
        
    class HoverButton(Button):
        def __init__(self, master, **kw):
            Button.__init__(self,master=master,**kw)
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, e):
            self["foreground"] = "#ffffff"
            self["background"] = "#282c34"

        def on_leave(self, e):
            self["foreground"] = "#cacad4"
            self["background"] = "#20242c"
    
    

    ### MC Version Selection versionSelectionWindow ###

    def select14():
        global VERSION
        global dm
        VERSION = "1.14"
        dm = 0.5
        versionSelectionWindow.destroy()

    def select12():
        global VERSION
        global dm
        VERSION = "1.12"
        dm = 8
        versionSelectionWindow.destroy()
    
    versionSelectionWindow = Tk()
    CenterWindow(versionSelectionWindow, windowSizeY=150)
    currentWindow = versionSelectionWindow
    versionSelectionWindow.iconbitmap(r'icon.ico')
    setTitleBar(versionSelectionWindow)
    versionSelectionWindow.configure(background="#282c34")
    versionSelectionWindow.protocol("WM_DELETE_WINDOW", on_closing)
    versionSelectionWindow.title("Collisions Generator")
    versionSelectionWindow.resizable(width=False, height=False)
    
    versionSelectionLabel = Label(versionSelectionWindow, text="Choose the minecraft version\nyou want to use",font=("Arial",-16,"bold") ,justify="center",background="#282c34",foreground="#ffffff", pady=10)
    version14Button = HoverButton(versionSelectionWindow, text="1.14.x", command=select14, relief="flat",font=("Arial",-16,"bold") , overrelief="flat",background="#20242c",foreground="#cacad4", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    version12Button = HoverButton(versionSelectionWindow, text="1.12.x", command=select12, relief="flat",font=("Arial",-16,"bold") , overrelief="flat",background="#20242c",foreground="#cacad4", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    
    versionSelectionLabel.pack()
    version14Button.pack()
    version12Button.pack()

    if VERSIONCHECK == True:
        versionSelectionWindow.mainloop()



    ### File Selection Window ###

    def ExplanationsContinue():
        FileSelectionWindow.destroy()

    BaseFile = ""
    
    def BrowseFile():
        global MODEL
        global BaseFile
        SelectedFile = filedialog.askopenfilename(initialdir="/", title="Browse",filetypes=(("Json files (.json)",".json"),("All files","*.*")))
        if SelectedFile.endswith(".json"):
            with open(os.path.join(SelectedFile), "r") as file:
                try:
                    MODEL = json.load(file)
                    if "elements" in MODEL:
                        BaseFile = SelectedFile
                        MODEL = MODEL["elements"]
                        FileSelectionWindow.destroy()
                    else:
                        if "parent" in MODEL:
                            FileSelectionLabel["text"] = "This file is a child of another\nblock model file ! Please retry"
                        else:
                            FileSelectionLabel["text"] = "This file is not a block model file !\nPlease retry"
                except:
                    FileSelectionLabel["text"] = "This json file is broken !\nPlease retry"
        else:
            FileSelectionLabel["text"] = "This file is not a json file !\nPlease retry"

    FileSelectionWindow = Tk()
    CenterWindow(FileSelectionWindow,windowSizeY=230)
    currentWindow = FileSelectionWindow
    FileSelectionWindow.iconbitmap(r'icon.ico')
    setTitleBar(FileSelectionWindow)
    FileSelectionWindow.configure(background="#282c34")
    FileSelectionWindow.protocol("WM_DELETE_WINDOW", on_closing)
    FileSelectionWindow.title("Collisions Generator")
    FileSelectionWindow.resizable(width=False, height=False)

    ExplanationsLabel = Label(FileSelectionWindow, text="""This program will allow you to get
the collisions of a minecraft custom
block model by reading its .json file.
The model has to contain an
"elements" category (It must not be
the child of another model !)""",font=("Arial",-16,"bold") , background="#282c34", foreground="#ffffff")
    FileSelectionLabel = Label(FileSelectionWindow, text="\nSelect your block model file",font=("Arial",-16,"bold") ,justify="center", background="#282c34", foreground="#ffffff")
    BrowseFileButton = HoverButton(FileSelectionWindow, text="Browse",font=("Arial",-16,"bold") , command=BrowseFile, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)

    ExplanationsLabel.pack()
    FileSelectionLabel.pack()
    BrowseFileButton.pack()
    FileSelectionWindow.mainloop()



    ### Collision Calculator Window ###
    
    LIST = []

    for i in range(len(MODEL)):
        CUBOID = MODEL[i]
        POS = CUBOID["from"]+CUBOID["to"]
        if VERSION == "1.12":
            for i in range(6):
                POS[i] = POS[i] / 16
        LIST.append(POS)

    CollisionCalculatorWindow = Tk()
    CenterWindow(CollisionCalculatorWindow, windowSizeX=339, windowSizeY=370)
    currentWindow = CollisionCalculatorWindow
    CollisionCalculatorWindow.iconbitmap(r'icon.ico')
    CollisionCalculatorWindow.configure(background="#282c34")
    CollisionCalculatorWindow.protocol("WM_DELETE_WINDOW", on_closing)
    CollisionCalculatorWindow.title("Collisions Generator")
    CollisionCalculatorWindow.resizable(width=False, height=False)
    
    TitleBarLabel = Label(CollisionCalculatorWindow,text="Collision Generator",background="#17191d",relief="flat",foreground="#cacad4",font=("Arial",-24,"bold"))    
    
    BLOCKTOPFACING = "Top"
    BLOCKROTATION = "North"
    REVERSEDX = False
    REVERSEDY = False
    REVERSEDZ = False
    AlreadyInFinishMode = False
    
    def MirrorX():
        for i in range(len(LIST)):
            x1 = LIST[i][0]
            x2 = LIST[i][3]
            dx1 = x1 - dm
            dx2 = x2 - dm
            x1 -= 2*dx1
            x2 -= 2*dx2
            tempx = x1
            x1 = x2
            x2 = tempx
            LIST[i][0] = x1
            LIST[i][3] = x2

    def MirrorY():
        for i in range(len(LIST)):
            y1 = LIST[i][1]
            y2 = LIST[i][4]
            dy1 = y1 - dm
            dy2 = y2 - dm
            y1 -= 2*dy1
            y2 -= 2*dy2
            tempy = y1
            y1 = y2
            y2 = tempy
            LIST[i][1] = y1
            LIST[i][4] = y2

    def MirrorZ():
        for i in range(len(LIST)):
            z1 = LIST[i][2]
            z2 = LIST[i][5]
            dz1 = z1 - dm
            dz2 = z2 - dm
            z1 -= 2*dz1
            z2 -= 2*dz2
            tempz = z1
            z1 = z2
            z2 = tempz
            LIST[i][2] = z1
            LIST[i][5] = z2

    def FlipYZ():
        for i in range(len(LIST)):
            y1 = LIST[i][1]
            y2 = LIST[i][4]
            z1 = LIST[i][2]
            z2 = LIST[i][5]
            tempy1 = y1
            y1 = z1
            z1 = tempy1
            tempy2 = y2
            y2 = z2
            z2 = tempy2
            LIST[i][1] = y1
            LIST[i][4] = y2
            LIST[i][2] = z1
            LIST[i][5] = z2

    def FlipZX():
        for i in range(len(LIST)):
            x1 = LIST[i][0]
            x2 = LIST[i][3]
            y1 = LIST[i][1]
            y2 = LIST[i][4]
            tempx1 = x1
            x1 = y1
            y1 = tempx1
            tempx2 = x2
            x2 = y2
            y2 = tempx2
            LIST[i][0] = x1
            LIST[i][3] = x2
            LIST[i][1] = y1
            LIST[i][4] = y2

    def FlipXY():
        for i in range(len(LIST)):
            x1 = LIST[i][0]
            x2 = LIST[i][3]
            z1 = LIST[i][2]
            z2 = LIST[i][5]
            tempx1 = x1
            x1 = z1
            z1 = tempx1
            tempx2 = x2
            x2 = z2
            z2 = tempx2
            LIST[i][0] = x1
            LIST[i][3] = x2
            LIST[i][2] = z1
            LIST[i][5] = z2

    def MirrorXVisual():
        global BLOCKTOPFACING
        global BLOCKROTATION
        global REVERSEDX
        if BLOCKTOPFACING in ["Top","Bottom","North","South"]:
            if BLOCKROTATION == "West":
                BLOCKROTATION = "East"
            elif BLOCKROTATION == "East":
                BLOCKROTATION = "West"
            else:
                if REVERSEDX == True:
                    REVERSEDX = False
                else:
                    REVERSEDX = True
        elif BLOCKTOPFACING == "East":
            BLOCKTOPFACING = "West"
        elif BLOCKTOPFACING == "West":
            BLOCKTOPFACING = "East"

    def MirrorYVisual():
        global BLOCKTOPFACING
        global BLOCKROTATION
        global REVERSEDY
        if BLOCKTOPFACING in ["West","East","North","South"]:
            if BLOCKROTATION == "Top":
                BLOCKROTATION = "Bottom"
            elif BLOCKROTATION == "Bottom":
                BLOCKROTATION = "Top"
            else:
                if REVERSEDY == True:
                    REVERSEDY = False
                else:
                    REVERSEDY = True
        elif BLOCKTOPFACING == "Top":
            BLOCKTOPFACING = "Bottom"
        elif BLOCKTOPFACING == "Bottom":
            BLOCKTOPFACING = "Top"
            
    def MirrorZVisual():
        global BLOCKTOPFACING
        global BLOCKROTATION
        global REVERSEDZ
        if BLOCKTOPFACING in ["West","East","Top","Bottom"]:
            if BLOCKROTATION == "North":
                BLOCKROTATION = "South"
            elif BLOCKROTATION == "South":
                BLOCKROTATION = "North"
            else:
                if REVERSEDZ == True:
                    REVERSEDZ = False
                else:
                    REVERSEDZ = True
        elif BLOCKTOPFACING == "North":
            BLOCKTOPFACING = "South"
        elif BLOCKTOPFACING == "South":
            BLOCKTOPFACING = "North"

    def FlipYZVisual():
        global BLOCKTOPFACING
        global BLOCKROTATION
        BLOCKFULLINFO = BLOCKTOPFACING+BLOCKROTATION
        if BLOCKTOPFACING in ["West","East"]:
            if BLOCKROTATION == "Top":
                BLOCKROTATION = "South"
            elif BLOCKROTATION == "South":
                BLOCKROTATION = "Top"
            elif BLOCKROTATION == "Bottom":
                BLOCKROTATION = "North"
            elif BLOCKROTATION == "North":
                BLOCKROTATION = "Bottom"
            else:
                return
        if BLOCKROTATION in ["West","East"]:
            if BLOCKTOPFACING == "Top":
                BLOCKTOPFACING = "South"
            elif BLOCKTOPFACING == "South":
                BLOCKTOPFACING = "Top"
            elif BLOCKTOPFACING == "Bottom":
                BLOCKTOPFACING = "North"
            elif BLOCKTOPFACING == "North":
                BLOCKTOPFACING = "Bottom"
            else:
                return
        elif BLOCKFULLINFO == "SouthTop":
            BLOCKTOPFACING = "Top"
            BLOCKROTATION = "South"
        elif BLOCKFULLINFO == "TopSouth":
            BLOCKTOPFACING = "South"
            BLOCKROTATION = "Top"
        elif BLOCKFULLINFO == "SouthBottom":
            BLOCKTOPFACING = "Top"
            BLOCKROTATION = "North"
        elif BLOCKFULLINFO == "BottomSouth":
            BLOCKTOPFACING = "North"
            BLOCKROTATION = "Top"
            
        elif BLOCKFULLINFO == "NorthTop":
            BLOCKTOPFACING = "Bottom"
            BLOCKROTATION = "South"
        elif BLOCKFULLINFO == "TopNorth":
            BLOCKTOPFACING = "South"
            BLOCKROTATION = "Bottom"
        elif BLOCKFULLINFO == "NorthBottom":
            BLOCKTOPFACING = "Bottom"
            BLOCKROTATION = "North"
        elif BLOCKFULLINFO == "BottomNorth":
            BLOCKTOPFACING = "North"
            BLOCKROTATION = "Bottom"

    def FlipZXVisual():
        global BLOCKTOPFACING
        global BLOCKROTATION
        BLOCKFULLINFO = BLOCKTOPFACING+BLOCKROTATION
        if BLOCKTOPFACING in ["Top","Bottom"]:
            if BLOCKROTATION == "East":
                BLOCKROTATION = "South"
            elif BLOCKROTATION == "South":
                BLOCKROTATION = "East"
            elif BLOCKROTATION == "West":
                BLOCKROTATION = "North"
            elif BLOCKROTATION == "North":
                BLOCKROTATION = "West"
            else:
                return
        if BLOCKROTATION in ["Top","Bottom"]:
            if BLOCKTOPFACING == "East":
                BLOCKTOPFACING = "South"
            elif BLOCKTOPFACING == "South":
                BLOCKTOPFACING = "East"
            elif BLOCKTOPFACING == "West":
                BLOCKTOPFACING = "North"
            elif BLOCKTOPFACING == "North":
                BLOCKTOPFACING = "West"
            else:
                return
        elif BLOCKFULLINFO == "WestSouth":
            BLOCKTOPFACING = "South"
            BLOCKROTATION = "West"
        elif BLOCKFULLINFO == "SouthWest":
            BLOCKTOPFACING = "West"
            BLOCKROTATION = "South"
        elif BLOCKFULLINFO == "WestNorth":
            BLOCKTOPFACING = "South"
            BLOCKROTATION = "East"
        elif BLOCKFULLINFO == "NorthWest":
            BLOCKTOPFACING = "East"
            BLOCKROTATION = "South"
            
        elif BLOCKFULLINFO == "EastSouth":
            BLOCKTOPFACING = "North"
            BLOCKROTATION = "West"
        elif BLOCKFULLINFO == "SouthEast":
            BLOCKTOPFACING = "West"
            BLOCKROTATION = "North"
        elif BLOCKFULLINFO == "EastNorth":
            BLOCKTOPFACING = "North"
            BLOCKROTATION = "East"
        elif BLOCKFULLINFO == "NorthEast":
            BLOCKTOPFACING = "East"
            BLOCKROTATION = "North"

    def FlipXYVisual():
        global BLOCKTOPFACING
        global BLOCKROTATION
        BLOCKFULLINFO = BLOCKTOPFACING+BLOCKROTATION
        if BLOCKTOPFACING in ["North","South"]:
            if BLOCKROTATION == "West":
                BLOCKROTATION = "Top"
            elif BLOCKROTATION == "Top":
                BLOCKROTATION = "West"
            elif BLOCKROTATION == "East":
                BLOCKROTATION = "Bottom"
            elif BLOCKROTATION == "Bottom":
                BLOCKROTATION = "East"
            else:
                return
        elif BLOCKROTATION in ["North","South"]:
            if BLOCKTOPFACING == "West":
                BLOCKTOPFACING = "Top"
            elif BLOCKTOPFACING == "Top":
                BLOCKTOPFACING = "West"
            elif BLOCKTOPFACING == "East":
                BLOCKTOPFACING = "Bottom"
            elif BLOCKTOPFACING == "Bottom":
                BLOCKTOPFACING = "East"
            else:
                return
        elif BLOCKFULLINFO == "WestTop":
            BLOCKTOPFACING = "Top"
            BLOCKROTATION = "West"
        elif BLOCKFULLINFO == "TopWest":
            BLOCKTOPFACING = "West"
            BLOCKROTATION = "Top"
        elif BLOCKFULLINFO == "WestBottom":
            BLOCKTOPFACING = "Top"
            BLOCKROTATION = "East"
        elif BLOCKFULLINFO == "BottomWest":
            BLOCKTOPFACING = "East"
            BLOCKROTATION = "Top"
            
        elif BLOCKFULLINFO == "EastTop":
            BLOCKTOPFACING = "Bottom"
            BLOCKROTATION = "West"
        elif BLOCKFULLINFO == "TopEast":
            BLOCKTOPFACING = "West"
            BLOCKROTATION = "Bottom"
        elif BLOCKFULLINFO == "EastBottom":
            BLOCKTOPFACING = "Bottom"
            BLOCKROTATION = "East"
        elif BLOCKFULLINFO == "BottomEast":
            BLOCKTOPFACING = "East"
            BLOCKROTATION = "Bottom"
                

    
    VISUAL = os.path.join(FOLDER, "Visualizations\\"+BLOCKTOPFACING+BLOCKROTATION+".png")
    def ImageReload():
        global VisualImage, VisualImageBase, VisualImageLabel, VISUAL, BLOCKROTATION, BLOCKTOPFACING
        InfoButton["text"] = "Informations"
        VISUAL = os.path.join(FOLDER, "Visualizations\\"+BLOCKTOPFACING+BLOCKROTATION+".png")
        VisualImageBase = Image.open(VISUAL)
        VisualImageBase = VisualImageBase.resize((200,200),Image.LANCZOS)
        VisualImage = ImageTk.PhotoImage(VisualImageBase)
        VisualImageLabel["image"] = VisualImage
        VisualImageLabel.image = VisualImage
    def Reversing():
        global REVERSEDX, REVERSEDY, REVERSEDZ
        if REVERSEDX == True:
            ReversedXLabel["foreground"] = "#ffffff" 
        else:
            ReversedXLabel["foreground"] = "#606060"
        if REVERSEDY == True:
            ReversedYLabel["foreground"] = "#ffffff"
        else:
            ReversedYLabel["foreground"] = "#606060"
        if REVERSEDZ == True:
            ReversedZLabel["foreground"] = "#ffffff"
        else:
            ReversedZLabel["foreground"] = "#606060"
    def InformationsButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            InfoButton["text"] = "(Check Console)"
            print("""Informations :\n
The mirror buttons will mirror the cube on the specified axis.
Example for Mirror North-South:

         ██████                                      ......
   ...███      ██████                          ██████      ......
...      ██████      ███                    ███      ██████      ...
.  ......      ██████  █           ██       █  ██████      ███...  .
.        ..y...   █    █   Becomes ████     █        ██y███  █     .
.          ↑      █    █   ██████████████   █          ↑     █     .
.          .      █    █           ████     █          █     █     .
.          .      █    █           ██       █          █     █     .
x←.        .      █  █→z                    x←█        █     █   .→z
   ......  .   ...███                          ██████  █   ███...
         ......                                      ██████
         BEFORE                                      AFTER

This can be used to change, for example, facing North to facing South.


The flip buttons will swap 2 axis of the cube.
Example for Flip East-West and Top-Down axis (Axis X and Y):

         ██████                                      ██████
   ...███      ██████                          ██████      ███...
...      ██████      ███                    ███      ██████      ...
.  ......      ██████  █           ██       █  ██████      ......  .
.        ..y...   █    █   Becomes ████     █    █   ..y...        .
.          ↑      █    █   ██████████████   █    █     ↑           .
.          .      █    █           ████     █    █     .           .
.          .      █    █           ██       █    █     .           .
x←.        .      █  █→z                    x←█  █     .         .→z
   ......  .   ...███                          ███...  .   ......
         ......                                      ......
         BEFORE                                      AFTER

This can be use to change, for example, facing North to facing East.
""")
    def MirrorXButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            MirrorXVisual()
            MirrorX()
            Reversing()
            ImageReload()
    def MirrorYButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            MirrorYVisual()
            MirrorY()
            Reversing()
            ImageReload()
    def MirrorZButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            MirrorZVisual()
            MirrorZ()
            Reversing()
            ImageReload()
    def FlipXYButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            FlipXYVisual()
            FlipXY()
            Reversing()
            ImageReload()
    def FlipYZButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            FlipYZVisual()
            FlipYZ()
            Reversing()
            ImageReload()
    def FlipZXButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            FlipZXVisual()
            FlipZX()
            Reversing()
            ImageReload()
    def PresetButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            InfoButton["text"] = "Informations"
            print("Work in progress")
    def ResetButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            global BLOCKROTATION, BLOCKTOPFACING, REVERSEDX, REVERSEDY, REVERSEDZ, VISUAL, MODEL, FOLDER
            BLOCKTOPFACING = "Top"
            BLOCKROTATION = "North"
            REVERSEDX = False
            REVERSEDY = False
            REVERSEDZ = False
            VISUAL = os.path.join(FOLDER, "Visualizations\\"+BLOCKTOPFACING+BLOCKROTATION+".png")
            with open(BaseFile, "r") as file:
                MODEL = json.load(file)
                MODEL = MODEL["elements"]
            Reversing()
            ImageReload()
    def none():
        return
    def FinishButtonAction():
        global AlreadyInFinishMode
        if AlreadyInFinishMode == False:
            AlreadyInFinishMode = True
            ContinueFinish = False
            FinishError = False
            FinishErrorText = ""
            NAME = ""
            InfoButton["text"] = "Informations"
            FinishButton["font"] = ("Arial",-12,"bold")
            FinishButton["text"] = "(Check\nConsole)"
            FinishButton["command"] = none
            while ContinueFinish == False:
                if FinishError == True:
                    FinishErrorText = "Error: Name is too short.\nPlease try another name.\n"
                NAME = input("""Choose a name for the list of collisions.
IMPORTANT :
How the name should be ?
It should be written in (minimum) 4 letters.

The first letter can be :
  S for a Straight shaped block
  I for an Inner corner block
  O for an Outer corner block
  Anything else for a custom shaped block

The second letter will always be C for Collision boxes.

The third letter can be :
  T for a block placed on the top/upper half of the block (upside down)
  B for a block placed on the bottom/lower half of the block (right side up)
  N for a block placed on the North half of the block (top of the block facing North)
  S for a block placed on the South half of the block (top of the block facing South)
  E for a block placed on the East half of the block (top of the block facing East)
  W for a block placed on the West half of the block (top of the block facing West)
  Anything else for when the block is place on another non-existing half of the block, you sorcerer

The fourth letter can be :
  N for a block facing North
  S for a block facing South
  E for a block facing East
  W for a block facing West
  T for a block facing up/to the sky
  B for a block facing down/to the void
  Anything else for when the block is facing another direction from another dimension, you are really scary

The next letters (fifth and more) can be anything you want, these won't be took in consideration.
WARNING : The name must not contain any spaces, it should contain only characters that can be used in variable names.

What's your collisions list's name ?
"""+FinishErrorText)
                try:
                    TEST = NAME[0]
                    try:
                        TEST = NAME[1]
                        try:
                            TEST = NAME[2]
                            try:
                                TEST = NAME[3]
                                ContinueFinish = True
                            except:
                                FinishError=True
                        except:
                            FinishError=True
                    except:
                        FinishError=True
                except:
                    FinishError=True
            
            NAME = NAME[0] + "C" + NAME[2:]
            
            if NAME[0] == "S":
                SHAPE = "Straight block"
            elif NAME[0] == "I":
                SHAPE = "Inner corner block"
            elif NAME[0] == "O":
                SHAPE = "Outer corner block"
            else:
                SHAPE = "Custom shaped block"
                
            if NAME[2] == "T":
                HALF = ", upside down"
            elif NAME[2] == "B":
                HALF = ", right side up"
            elif NAME[2] == "N":
                FACING = ", top side facing North"
            elif NAME[2] == "S":
                FACING = ", top side facing facing South"
            elif NAME[2] == "E":
                FACING = ", top side facing facing East"
            elif NAME[2] == "W":
                FACING = ", top side facing facing West"
            else:
                HALF = ", on a non existing half of the block"

            if NAME[3] == "N":
                FACING = ", facing North"
            elif NAME[3] == "S":
                FACING = ", facing South"
            elif NAME[3] == "E":
                FACING = ", facing East"
            elif NAME[3] == "W":
                FACING = ", facing West"
            elif NAME[3] == "T":
                FACING = ", facing Up"
            elif NAME[3] == "B":
                FACING = ", facing Down"
            else:
                FACING = ", facing a direction from another dimension"
            
            if VERSION == "1.12":
                STRSTART = "Java code to create the collision parts :\nprotected static final class PartHolder {\n"+"    /** "+SHAPE+"\n    * "+NAME+" = "+SHAPE+" collision boxes"+HALF+FACING+"\n    * x1 y1 z1 x2 y2 z2 */\n    protected static final double[][] "+NAME+" = {"
                LISTSTR = str(LIST)
                LISTSTR = LISTSTR.replace("], ","},\n    "+" "*(38+len(NAME))).replace("[","{").replace("]","}").replace("{{","{").replace("}}","}")
                STREND = "}"
                STRADD = ""
                for i in range(len(LIST)):
                    STREND += "\n    protected static final AxisAlignedBB "+NAME+"Part"+str(i+1)+" = new AxisAlignedBB("+NAME+"["+str(i)+"][0], "+NAME+"["+str(i)+"][1], "+NAME+"["+str(i)+"][2], "+NAME+"["+str(i)+"][3], "+NAME+"["+str(i)+"][4], "+NAME+"["+str(i)+"][5]);"
                    STRADD += "    addCollisionBoxToList(pos, entityBox, collidingBoxes, holder."+NAME+"Part"+str(i+1)+");\n"
                print(STRSTART+LISTSTR+STREND+"""\n}

Java code to add the collision parts to the block :
public void addCollisionBoxToList(IBlockState state, World worldIn, BlockPos pos, AxisAlignedBB entityBox, List<AxisAlignedBB> collidingBoxes, @Nullable Entity entityIn, boolean isActualState) {
    PartHolder holder = new PartHolder();\n"""+STRADD+"}")

            elif VERSION == "1.14":
                STRSTART = "Java code to create the collision parts :\n"+"/** "+SHAPE+"\n* "+NAME+" = "+SHAPE+" collision boxes"+HALF+FACING+"\n* x1 y1 z1 x2 y2 z2 */\nprotected static final double[][] "+NAME+" = {"
                LISTSTR = str(LIST)
                LISTSTR = LISTSTR.replace("], ","},\n"+" "*(38+len(NAME))).replace("[","{").replace("]","}").replace("{{","{").replace("}}","}")
                STREND = ""
                STRADD = "\nprivate static final VoxelShape FULL_"+NAME+"_SHAPE = VoxelShapes.or("
                for i in range(len(LIST)):
                    STREND += "\nprotected static final VoxelShape "+NAME+"Part"+str(i+1)+" = Block.makeCuboidShape("+NAME+"["+str(i)+"][0], "+NAME+"["+str(i)+"][1], "+NAME+"["+str(i)+"][2], "+NAME+"["+str(i)+"][3], "+NAME+"["+str(i)+"][4], "+NAME+"["+str(i)+"][5]);"
                    if i != len(LIST)-1:
                        STRADD += NAME+"Part"+str(i+1)+", "
                    else:
                        STRADD += NAME+"Part"+str(i+1)+");"
                print(STRSTART+LISTSTR+STREND+STRADD+"""

@Override
public VoxelShape getShape(BlockState state, IBlockReader worldIn, BlockPos pos, ISelectionContext context) {
    return FULL_"""+NAME+"""_SHAPE;
}""")
            print("\n\n\nYou can continue working on the tool if you want, or close it if you want to stop.")
            AlreadyInFinishMode = False
            FinishButton["command"] = FinishButtonAction
            FinishButton["text"] = "Finish"
            FinishButton["font"] = ("Arial",-16,"bold")
    VisualImageBase = Image.open(VISUAL)
    VisualImageBase = VisualImageBase.resize((200,200),Image.LANCZOS)
    VisualImage = ImageTk.PhotoImage(VisualImageBase)
    
    QuestionLabel = Label(CollisionCalculatorWindow, text="What do you want to do ?",font=("Arial",-16,"bold") ,justify="center", background="#282c34", foreground="#ffffff")
    InvertedLabel = Label(CollisionCalculatorWindow, text="",font=("Arial",-16,"bold") ,justify="center", background="#282c34", foreground="#ffffff")
    VisualImageLabel = Label(image=VisualImage,background="#282c34")
    VisualImageLabel.image = VisualImage
    MirrorXButton = HoverButton(CollisionCalculatorWindow, text="Mirror X",font=("Arial",-16,"bold") , command=MirrorXButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    MirrorYButton = HoverButton(CollisionCalculatorWindow, text="Mirror Y",font=("Arial",-16,"bold") , command=MirrorYButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    MirrorZButton = HoverButton(CollisionCalculatorWindow, text="Mirror Z",font=("Arial",-16,"bold") , command=MirrorZButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    FlipXYButton = HoverButton(CollisionCalculatorWindow, text="Flip XY",font=("Arial",-16,"bold") , command=FlipXYButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    FlipYZButton = HoverButton(CollisionCalculatorWindow, text="Flip YZ",font=("Arial",-16,"bold") , command=FlipYZButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    FlipZXButton = HoverButton(CollisionCalculatorWindow, text="Flip ZX",font=("Arial",-16,"bold") , command=FlipZXButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    ReversedXLabel = Label(CollisionCalculatorWindow, text="West and East mirrored/exchanged",font=("Arial",-12,"bold") ,justify="center", background="#282c34", foreground="#606060")
    ReversedYLabel = Label(CollisionCalculatorWindow, text="Top and Bottom mirrored/exchanged",font=("Arial",-12,"bold") ,justify="center", background="#282c34", foreground="#606060")
    ReversedZLabel = Label(CollisionCalculatorWindow, text="North and South mirrored/exchanged",font=("Arial",-12,"bold") ,justify="center", background="#282c34", foreground="#606060")
    ResetButton = HoverButton(CollisionCalculatorWindow, text="Reset",font=("Arial",-16,"bold") , command=ResetButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    PresetButton = HoverButton(CollisionCalculatorWindow, text="Presets",font=("Arial",-16,"bold") , command=PresetButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    InfoButton = HoverButton(CollisionCalculatorWindow, text="Informations",font=("Arial",-16,"bold") , command=InformationsButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    FinishButton = HoverButton(CollisionCalculatorWindow, text="Finish",font=("Arial",-16,"bold") , command=FinishButtonAction, background="#20242c", foreground="#cacad4", relief="flat", overrelief="flat", activebackground="#282c34", activeforeground="#ffffff", borderwidth=0)
    
    TitleBarLabel.grid(row=0,column=0,columnspan=4,sticky="ew")
    QuestionLabel.grid(row=1,column=0,columnspan=4,sticky="ew")
    VisualImageLabel.grid(row=2,column=1,rowspan=3,columnspan=2)
    MirrorXButton.grid(row=2,column=0)
    MirrorYButton.grid(row=3,column=0)
    MirrorZButton.grid(row=4,column=0)
    FlipXYButton.grid(row=2,column=3)
    FlipYZButton.grid(row=3,column=3)
    FlipZXButton.grid(row=4,column=3)
    ReversedXLabel.grid(row=5,column=0,columnspan=4,sticky="ew")
    ReversedYLabel.grid(row=6,column=0,columnspan=4,sticky="ew")
    ReversedZLabel.grid(row=7,column=0,columnspan=4,sticky="ew")
    ResetButton.grid(row=8,column=0)
    PresetButton.grid(row=8,column=1)
    InfoButton.grid(row=8,column=2)
    FinishButton.grid(row=8,column=3)
    
    CollisionCalculatorWindow.mainloop()