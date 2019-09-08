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

FOLDER = os.path.dirname(os.path.abspath(__file__))

CONFIG = open(os.path.join(FOLDER, "config.txt"),"r", encoding="utf8")

for line in CONFIG:
    if line.lower().startswith("#     rotationvisualization = "):
        value = line[30:].lower()
        if value.startswith("false"):
            RotationVisualization = False
        else:
            RotationVisualization = True
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

def clear_screen():
    input("\nPress enter to continue\n")
    command = "cls" if platform.system().lower()=="windows" else "clear"
    return subprocess.call(command,shell=True) == 0 

def clear_screen_no_enter():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    return subprocess.call(command,shell=True) == 0 

LIST = []

if VERSIONCHECK == True:
    VERSION = ""
    VERSION12 = ["1","1.12","1.12.0","1.12.1","1.12.2","1.12.x"]
    VERSION14 = ["2","1.14","1.14.0","1.14.1","1.14.2","1.14.3","1.14.4","1.14.x"]

    while VERSION not in ["1.12","1.14"]:
        clear_screen_no_enter()
        VERSION = input("""For which version of the game are you creating collisions ?
  1. 1.12.x
  2. 1.14.x
""")
        if VERSION.lower() in VERSION12:
            VERSION = "1.12"
        elif VERSION.lower() in VERSION14:
            VERSION = "1.14"
        else:
            print("Error: Invalid version. Please retry.")
            clear_screen()

if VERSION == "1.12":
    dm = 0.5
elif VERSION == "1.14":
    dm = 8


clear_screen_no_enter()
print("This program will allow you to get the collisions of a minecraft custom block model by reading its .json file.")
clear_screen()

GOODFILE = False

while GOODFILE == False:
    MODELPATH = input("""Please, write the path to the model you want to get the collisions from
    (This is not compatible with rotations, as the collisions have no rotation, the program will not care about cuboids' rotations):
    (You can drag and drop the file here and then press enter ! (except if you use a bad console emulator *Laughing out loud emoji*))
""")
    clear_screen_no_enter()
    
    if MODELPATH.startswith('"') and MODELPATH.endswith('"'):
        MODELPATH = MODELPATH[1:-1]
    
    try:
        with open(MODELPATH, "r") as file:
            MODEL = json.load(file)
            GOODFILE = True
    except:
        clear_screen_no_enter()
        print("Error: File not found. Please retry")
        clear_screen()

MODEL = MODEL["elements"]

for i in range(len(MODEL)):
    CUBOID = MODEL[i]
    POS = CUBOID["from"]+CUBOID["to"]
    if VERSION == "1.12":
        for i in range(6):
            POS[i] = POS[i] / 16
    LIST.append(POS)

print("List of collisions : \n"+str(LIST).replace("],","],\n"))
clear_screen()

action = ""

BLOCKTOPFACING = "Top"
BLOCKROTATION = "North"
REVERSEDX = False
REVERSEDY = False
REVERSEDZ = False


def MirrorX():
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

def MirrorY():
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
        
def MirrorZ():
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

def RotateX():
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

def RotateY():
    global BLOCKTOPFACING
    global BLOCKROTATION
    BLOCKFULLINFO = BLOCKTOPFACING+BLOCKROTATION
    if BLOCKTOPFACING in ["Top","Bottom"]:
        if BLOCKROTATION == "West":
            BLOCKROTATION = "South"
        elif BLOCKROTATION == "South":
            BLOCKROTATION = "West"
        elif BLOCKROTATION == "East":
            BLOCKROTATION = "North"
        elif BLOCKROTATION == "North":
            BLOCKROTATION = "East"
        else:
            return
    if BLOCKROTATION in ["Top","Bottom"]:
        if BLOCKTOPFACING == "West":
            BLOCKTOPFACING = "South"
        elif BLOCKTOPFACING == "South":
            BLOCKTOPFACING = "West"
        elif BLOCKTOPFACING == "East":
            BLOCKTOPFACING = "North"
        elif BLOCKTOPFACING == "North":
            BLOCKTOPFACING = "East"
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

def RotateZ():
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
            

while action != "exit":
    FILE = open(os.path.join(FOLDER, "Visualizations\\"+BLOCKTOPFACING+BLOCKROTATION+".txt"),"r", encoding="utf8")
    VISUAL = FILE.read()
    FILE.close()
    if REVERSEDX == True:
        VISUAL += "\nWest and East mirrored/exchanged.\n"
    if REVERSEDY == True:
        VISUAL += "\nTop and Bottom mirrored/exchanged.\n"
    if REVERSEDZ == True:
        VISUAL += "\nNorth and South mirrored/exchanged.\n"
    VISUAL += "\n"
    if RotationVisualization == False:
        VISUAL = ""
    print("""What do you want to do ?
  1a. Mirror West-East (Axis X)
  1b. Mirror Top-Down (Axis Y)
  1c. Mirror North-South (Axis Z)

  2a. Exchange East-West and Top-Down axis (Axis X and Y)
  2b. Exchange Top-Down and North-South axis (Axis Y and Z)
  2c. Exchange North-South and East-West axis (Axis Z and X)

  Write "finish" to get the final code.
  Write "info" to get informations about each commands.
  Write "exit" to quit the program.

"""+VISUAL)
    action = input()
    clear_screen_no_enter()
    if action == "info":
        print("""Informations :\n
The mirror commands will mirror the cube on the specified axis.
Example for Mirror West-East:

         ██████                                      ......
   ...███      ██████                          ██████      ......
...      ██████      ███                    ███      ██████      ...
.  ......      ██████  █           ██       █  ██████      ███...  .
.        ..y...   █    █   Becomes ████     █        ██y███  █     .
.          ↑      █    █   ██████████████   █          ↑     █     .
.          .      █    █           ████     █          █     █     .
.          .      █    █           ██       █          █     █     .
z←.        .      █  █→x                    z←█        █     █   .→x
   ......  .   ...███                          ██████  █   ███...
         ......                                      ██████
         BEFORE                                      AFTER

This can be used to change, for example, facing North to facing South.
""")
        clear_screen()
        print("""Informations :\n
The exchange commands will swap 2 axis of the cube.
Example for Exchange East-West and Top-Down axis (Axis X and Y):

         ██████                                      ██████
   ...███      ██████                          ██████      ███...
...      ██████      ███                    ███      ██████      ...
.  ......      ██████  █           ██       █  ██████      ......  .
.        ..y...   █    █   Becomes ████     █    █   ..y...        .
.          ↑      █    █   ██████████████   █    █     ↑           .
.          .      █    █           ████     █    █     .           .
.          .      █    █           ██       █    █     .           .
z←.        .      █  █→x                    z←█  █     .         .→x
   ......  .   ...███                          ███...  .   ......
         ......                                      ......
         BEFORE                                      AFTER

This can be use to change, for example, facing North to facing East.
""")
        clear_screen()
    elif action in ["1a","MirrorX"]:
        MirrorX()
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
    elif action in ["1b","MirrorY"]:
        MirrorY()
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
    elif action in ["1c","MirrorZ"]:
        MirrorZ()
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
    elif action in ["2a","RotateZ"]:
        RotateZ()
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
    elif action in ["2b","RotateX"]:
        RotateX()
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
    elif action in ["2c","RotateY"]:
        RotateY()
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
    elif action == "exit":
        break
    elif action == "finish":
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
""")
        clear_screen_no_enter()
        
        if NAME[0] == "S":
            SHAPE = "Straight block"
        elif NAME[0] == "I":
            SHAPE = "Inner corner block"
        elif NAME[0] == "O":
            SHAPE = "Outer corner block"
        else:
            SHAPE = "Custom shaped block"
        
        NAME = NAME[0] + "C" + NAME[2:]
            
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
        input("\nPress enter to quit\n")
        clear_screen_no_enter()
        break
    else:
        print("Error: Wrong value. Please retry.")
        clear_screen()