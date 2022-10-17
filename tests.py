# import arabic_reshaper

# reshaper = arabic_reshaper.ArabicReshaper({
#    "delete_harakat": True
# })

# print(reshaper.reshape("الفَاتِحة") == reshaper.reshape("الفاتحة"))

import os
from os.path import join
from time import sleep
import pyautogui as ag

n = 50

path = "src/data/quran"

files = os.listdir(path)
files.sort(key=lambda e:int(e.split(".")[0]))
files = [files[i:i+n] for i in range(0, len(files), n)]

sleep(5)

full_command = ""
for Files in files:
   full_command += "git add "
   for file in Files:
      full_command += f"{join(path, file)} "

   full_command += "\n"
   full_command += 'git commit -m "adding quran files"\n'
   full_command += "git push\n"
   full_command += "\n"

print(full_command)