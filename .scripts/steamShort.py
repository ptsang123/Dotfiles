#!/usr/bin/env python3

import os
import subprocess
import sys

# ask user for name of game using rofi
name = os.popen('rofi -font "dejavu sans mono 20" -width 30 -lines 1 -dmenu -p "Name"')
FullName = name.read()

# ask user for ID of game using rofi
sID = os.popen('rofi -font "dejavu sans mono 20" -width 30 -lines 1 -dmenu -p "ID"')
SteamID = sID.read()

# get home directory of user
path = os.popen('echo $HOME')
Parent = path.read()

# get to the applications directory
Directory = Parent.strip()+"/.local/share/applications/"

# create the file name for desktop shortcut
Filename = FullName.strip()+".desktop"

# combine the directory with the filename
FullPath = Directory+Filename

# contents of file
Contents = "[Desktop Entry]\nName="+FullName.strip()+"\nComment=Play this game on Steam\nExec=steam steam://rungameid/"+SteamID.strip()+"\nIcon=steam_icon_"+SteamID.strip()+"\nTerminal=false\nType=Application\nCategories=Game" 

# create file
TheFile = open(FullPath, "w+")
# write contents into file
TheFile.write(Contents)
TheFile.close()
