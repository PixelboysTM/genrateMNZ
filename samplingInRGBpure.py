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