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
            for x in range(out.size()[0]):
                for y in range(out.size()[1]):
                    out.set(x,y, self.get(x,y) * p2)
            return out
        elif type(p2) is Matrix:
            pass#TODO: Make here
        else:
            raise Exception("Cant multiply")
            return None