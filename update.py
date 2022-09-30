#!/usr/bin/env 
import os
import subprocess
from termcolor import colored



print(colored("Update has begun! 3","yellow"))
cwd = os.getcwd()
print("the current dir is "+ cwd)
print("")

print(colored("Navigating to desktop file 'Liked'","yellow"))
path = "/mnt/c/Users/liam/Desktop/Liked"
print(path)
print("")

os.chdir(path)
print(colored("Downloading plalist 'Vehicular Manslaughter'","yellow"))
playlistID = "https://open.spotify.com/playlist/1aspn6wkVaDVrAR5KZ3g7t?si=cff9a34d548d4e5e"
subprocess.run(["spotdl", playlistID])
print("")

print(colored("Complete!","yellow"))

