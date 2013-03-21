import os
from Tkinter import Tk
from tkFileDialog import *
from PIL import Image

sizes = [ 512, 256, 128, 32, 16 ]

filePath = os.path.realpath(__file__)
homeDir = os.path.dirname(filePath) + "/"

Tk().withdraw()
source = askopenfilename(title="Choose your PNG icon file.", initialdir="~/Desktop", filetypes=[("PNG files","*.png")])

sourceFile, sourceExt = os.path.splitext(os.path.basename(source))
destDir = os.path.dirname(source) + "/" + sourceFile + ".iconset"

os.makedirs(destDir)

img = Image.open(source)

for i in range(len(sizes)):
	newImg = img.resize((sizes[i], sizes[i]), Image.ANTIALIAS)
	newImg.save(destDir + "/icon_" + str(sizes[i]) + "x" + str(sizes[i]) + ".png")

os.system("iconutil -c icns %s;" % (destDir))
