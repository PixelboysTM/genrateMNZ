from PIL import Image
from threading import Thread
#from Matrix import Matrix
import numpy as np

def GetColors(x, xto):
    for xw in range(x, xto):
        for y in range(i.size[1]):
            availableColors.append(i.getpixel((xw,y)))

###
# i = Image.open("c_wh.png")

# availableColors = []

# allThreads = []
# x = 0
# while x < i.size[0]:
#     xto = x
#     for xw in range(1):
#         if xto < i.size[0]:
#             xto +=1
#     t = Thread(target=GetColors,args=(x,xto))
#     t.start()
#     allThreads.append(t)
#     x = xto

# running = True
# while running:
#     running = False
#     for t in allThreads:
#         if t.is_alive():
#             running = True

# s_colors = list(dict.fromkeys(availableColors))

# a = Matrix(3,3)
# a.set(0,0, -1).set(0,1, -2).set(0,2, -1)
# a.set(2,0, 1).set(2,1, 2).set(2,2,1)
# b = Matrix(1,3)
# b.set(0,0, 1).set(0,1,1).set(0,2,2)
# print(str(a.size()) + "*" + str(b.size()))
# print(a)
# print(b)
# print(a * b)
# print(b.size())

a = np.mat(np.array([[1],[2],[1]]))
b = np.mat(np.array([[1],[1],[2]]))
print(np.sqrt(a*a + b*b))