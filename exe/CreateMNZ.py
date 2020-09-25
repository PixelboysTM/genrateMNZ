from PIL import Image, ImageFilter
from threading import Thread
import time
import numpy as np

# █
# Methods
def GetRGBpure(color):
    if color[0] > color[1] and color[0] > color[2]:
        return (255,0,0)
    if color[1] > color[0] and color[1] > color[2]:
        return (0,255,0)
    if color[2] > color[0] and color[2] > color[1]:
        return (0,0,255)
    if color[0] == color[1] == color[2]:
        if color[0] <= 127:
            return (0,0,0)
        else:
            return (255,255,255)

    if color[0] == color[1]:
        if color[0] > color[2]:
            return (255,0,0)
        else:
            return (0,0,255)
    if color[0] == color[2]:
        if color[0] > color[1]:
            return (255,0,0)
        else:
            return (0,255,0)
    if color[1] == color[2]:
        if color[1] > color[0]:
            return (0,255,0)
        else:
            return (255,0,0)
    input("Falsche Farbe " + str(color) ) 

def GetColors(x, xto):
    for xw in range(x, xto):
        for y in range(originalImage.size[1]):
            availableColors.append(originalImage.getpixel((xw,y)))

def SortBucket(bucket):
    rangeR = max([o[0] for o in bucket]) - min([o[0] for o in bucket])
    rangeG = max([o[1] for o in bucket]) - min([o[1] for o in bucket])
    rangeB = max([o[2] for o in bucket]) - min([o[2] for o in bucket])
    if rangeR > rangeG and rangeR > rangeB:
        return sorted(bucket, key=lambda x: x[0], reverse=True)
    elif rangeG > rangeR and rangeG > rangeB:
        return sorted(bucket, key=lambda x: x[1], reverse=True)
    elif rangeB > rangeR and rangeB > rangeG:
        return sorted(bucket, key=lambda x: x[2], reverse=True)
    elif rangeR == rangeB > rangeG:
        return sorted(bucket, key=lambda x: x[0], reverse=True)
    elif rangeR == rangeG > rangeB:
        return sorted(bucket, key=lambda x: x[0], reverse=True)
    elif rangeG == rangeB > rangeR:
        return sorted(bucket, key=lambda x: x[1], reverse=True)
    elif rangeB == rangeR == rangeG:
        return sorted(bucket, key=lambda x: x[0], reverse=True)
    else:
        raise Exception("Mit deiner Mathematik stimm was nicht!!!")

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def PerformMedianCut():
    colorBuckets = [[(c[0], c[1], c[2]) for c in s_colors]]
    for iterable in range(iterationCount):
        print("Iteration " + str(iterable))
        newBuckets = []
        for bucket in colorBuckets:
            sortedBucket = SortBucket(bucket)
            newBuckets.append(split_list(sortedBucket)[0])
            newBuckets.append(split_list(sortedBucket)[1])
        colorBuckets = newBuckets
    return MakeAverageColors(colorBuckets)

def MakeAverageColors(bucktes):
    colorDict = {}
    for mainColorList in bucktes:
        color = (GetAverage([o[0] for o in mainColorList]), GetAverage([o[1] for o in mainColorList]), GetAverage([o[2] for o in mainColorList]))
        for c in mainColorList:
            colorDict[c] = color
    return colorDict

def GetAverage(list):
    allNumbers = 0
    for n in list:
        allNumbers += n
    return int(allNumbers / list.__len__())

def GetPixelAtPos(image,x,y):
    if image.size[0] < x and image.size[1] < y:
        return image.getpixel((x,y))
    else:
        return None

def PerformX(x,y, image):
    a = np.mat(np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))
    p00 = image.getpixel((x - 1,y - 1))
    p01 = image.getpixel((x - 1,y    ))
    p02 = image.getpixel((x - 1,y + 1))

    p00 = image.getpixel((x    ,y - 1))
    p01 = image.getpixel((x    ,y    ))
    p02 = image.getpixel((x    ,y + 1))

    p00 = image.getpixel((x + 1,y - 1))
    p01 = image.getpixel((x + 1,y    ))
    p02 = image.getpixel((x + 1,y + 1))


    b = np.mat(np.array([
        [p[0]],
        [p[1]],
        [p[2]]
    ]))
    r = a * b
    return (r.item((0,0)), r.item((1,0)), r.item((2,0)))

def PerformY(x,y, image):
    a = np.mat(np.array([[-1,-2,-1],[0,0,0],[1,2,1]]))
    p = image.getpixel((x,y))
    b = np.mat(np.array([[p[0]],[p[1]],[p[2]]]))
    r = a * b
    return (r.item((0,0)), r.item((1,0)), r.item((2,0)))

def PerformPythagoras(x,y,a,b):
    ca = a.getpixel((x,y))
    cb = b.getpixel((x,y))
# ENd methods
imageName = input("Image to be processed: ")
print("Analysing...")
startTime = time.time()
sizes = 1
originalImage = Image.open(imageName)
originalImage.convert(mode="RGB")

availableColors = []

allThreads = []
# Get All pixels in Threads
x = 0
while x < originalImage.size[0]:
    xto = x
    for xw in range(sizes):
        if xto < originalImage.size[0]:
            xto +=1
    t = Thread(target=GetColors,args=(x,xto))
    t.start()
    allThreads.append(t)
    x = xto


afterThreadTime = time.time()
running = True
while running:
    running = False
    for t in allThreads:
        if t.is_alive():
            running = True

catchedColorsEndTime = time.time()
s_colors = list(dict.fromkeys(availableColors))


# Print Stats
print("")
print("Image Statistiks")
print("Image: " + imageName + " " + str(originalImage.size))
print("Insgesamt " + str(s_colors.__len__()) + " farben")
print("Aus " + str(availableColors.__len__()) + " pixeln")
print("Zum Analysieren benötigte Zeit: " + str(afterThreadTime - startTime) + "s" )
print("Thread Start Zeit: " + str(afterThreadTime - startTime) + "s")
print("Zeit nach Thread: " + str(afterThreadTime - afterThreadTime) + "s")
input("Press any key to continue")
print("\n--------------------------")
print("Color precessing:")
method = input("Please select a processing method out of the following: PureRGB(p), MedianCutAlgorythm(m)")
newImage = Image.open(imageName)
newImage = newImage.convert("RGB")
if method == "p" or method == "P":
    colorDict = {}
    for c in s_colors:
        colorDict[c] = GetRGBpure(c)

    for x in range(newImage.size[0]):
        for y in range(newImage.size[1]):
            newImage.putpixel((x,y), GetRGBpure(newImage.getpixel((x,y))))
        print("Done Pixelrow:" + str(x) + " / " + str(newImage.size[0] - 1) )

elif method == "m" or method == "M":
    iterationCount = int(input("Number of Iterations (Results in colors = 2^i):"))
    colorPalette = PerformMedianCut()
    
    for x in range(newImage.size[0]):
        for y in range(newImage.size[1]):
            oldPixel = newImage.getpixel((x,y))
            newPixel = colorPalette[oldPixel] 
            newImage.putpixel((x,y), newPixel )
        print("Done Pixelrow:" + str(x) + " / " + str(newImage.size[0] - 1) )



finalTime = time.time()
print("color processing finished")
print("Saved result as c_" + imageName)
print("Time since start: " + str((finalTime - startTime)))
print("Time for color processing: " + str((finalTime - catchedColorsEndTime)))
if imageName.endswith("jpeg") or imageName.endswith("jpg"):
    name = imageName.replace("jpeg", "png",-1 ).replace("jpg", "png", -1)
    newImage.save("c_" + name)
else:
    newImage.save("c_" + imageName)

print("-------------------------------------------------")
print("Noise reduction:")
name = imageName
grayA = newImage.filter(ImageFilter.FIND_EDGES)
if imageName.endswith("jpeg") or imageName.endswith("jpg"):
    name = imageName.replace("jpeg", "png",-1 ).replace("jpg", "png", -1)
    grayA.save("f_" + name)
else:
    grayA.save("f_" + imageName)

print("######################### Finished #########################")
print("Saved final Image as f_" + name)
