# Python Program - List All Files in Directory

import glob, os

os.chdir("C://Users//vramlma//Documents")
for file in glob.glob("*.*"):
    print(file)