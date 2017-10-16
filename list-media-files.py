from Tkinter import Tk
import tkFileDialog
import os
root = Tk()

root.withdraw()

source_folder = tkFileDialog.askdirectory(parent=root)

fileName = input("Log file name (with "+'"quotes"'+"): ")
logFile = open(fileName,"w")
numFiles = 0
sizeFiles = 0
for root, dirs, files in os.walk(source_folder):
	for name in files:
		if name[-4:].lower() == ".flv" or name[-4:].lower() == ".mp4" or name[-4:].lower() == ".mov" or name[-4:].lower() == ".avi" or name[-4:].lower() == ".wmv":
			numFiles += 1
			path = os.path.join(root,name)
			size = os.stat(path).st_size
			sizeFiles += size
			logFile.write(path + "\n")
			print(path)
print(str(numFiles) + " Files")
logFile.write(str(numFiles) + " Files" + "\n")
totalSize = sizeFiles/1073741824.0
formatedSize = round(totalSize, 2)
print(str(formatedSize)+"GB")
logFile.write(str(formatedSize)+"GB")
logFile.close()
