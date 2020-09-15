class Matrix(object):
    def __init__(self, xDim, yDim):
        self.m = [[0 for y in range(xDim) ] for i in range(yDim) ]
    
    def __str__(self):
        string = ""
        for x in self.m:
            string += str(x) + "\n"
        return string

    def set(self,x,y,value):
        self.m[y][x] = value
        return self
    
    def get(self,x,y):
        return self.m[y][x]
    
    def size(self):
        return ( self.m[0].__len__(),self.m.__len__())

    def __mul__(self,p2):
        if type(p2) is int:
            out = Matrix(self.size()[0], self.size()[1])
            
        elif type(p2) is Matrix:
            pass
        else:
            raise Exception("Cant multiply")
            return None