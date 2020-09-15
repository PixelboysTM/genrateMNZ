from PIL import Image
from threading import Thread
import time
from samplingInRGBpure import GetRGBpure

imageName = "color.png"
startTime = time.time()
sizes = int(input("Thread Dichte (min 1) (größer weniger Threads)"))
im = Image.open(imageName)
im = im.convert(mode="RGB")

def GetColors(x, sto):
    global colors
    for xw in range(x, xto):
        print("Row:" + str(xw))
        for y in range(im.size[1]):
            colors.append(im.getpixel((xw,y)))


# im.save("sky.png", "png")
colors = []
# for x in range(im.size[0]):
#     t = Thread(target=GetColors,args=(x))
#     t.start()
trs = []
x = 0
while x < im.size[0]:
    xto = x
    for xw in range(sizes):
        if xto < im.size[0]:
            xto +=1
    t = Thread(target=GetColors,args=(x,xto))
    t.start()
    trs.append(t)
    x = xto

afterThreadTime = time.time()
running = True
while running:
    running = False
    for t in trs:
        if t.isAlive():
            running = True

endTime = time.time()

s_colors = list(dict.fromkeys(colors))
print(s_colors)
print("Insgesamt " + str(s_colors.__len__()) + " farben")
print("Aus " + str(colors.__len__()) + " einträgen")
print("Zeit: " + str(endTime - startTime) + "s" )
print("Thread Start Zeit: " + str(afterThreadTime - startTime) + "s")
print("Zeit nach Thread: " + str(endTime - afterThreadTime) + "s")
input("Press any key to continue")

colorDict = {}
for c in s_colors:
    colorDict[c] = GetRGBpure(c)

print("Dictionary:")
print(colorDict)

new = Image.open(imageName)
new = new.convert("RGB")
for x in range(new.size[0]):
    for y in range(new.size[1]):
        new.putpixel((x,y), GetRGBpure(new.getpixel((x,y))))
        print("Done Pixel:" + str((x,y)) + " | " + str(x*y + y))

finalTime = time.time()
print("Finished")
print("Time all togehter: " + str((finalTime - startTime)))
print("Time for constructing: " + str((finalTime - endTime)))
new.save("f_" + imageName)
new.show()