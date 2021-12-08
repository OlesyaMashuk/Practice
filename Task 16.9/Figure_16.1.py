class AllFigures:
    def __init__(self, ftype, x, y, width=0, height=0, r=0, l=0):
        # 1 - круг, 2 - прямоугольник, 3 - квадрат
        if ftype == 1:
            self.x = x
            self.y = y
            self.r = r
        elif ftype == 2:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        elif ftype == 3:
            self.x = x
            self.y = y
            self.l = l
        self.ftype = ftype

    def __str__(self):
        if self.ftype == 1:
            return f'Circle (x={self.x}, y={self.y}, r={self.r})'
        elif self.ftype == 2:
            return f'Rectangl (x={self.x}, y={self.y}, width={self.width}, height={self.height})'
        elif self.ftype == 3:
            return f'Square (x={self.x}, y={self.y}, l={self.l})'


c = AllFigures(ftype = 1, x = 5, y = 6, r = 15)
r = AllFigures(ftype = 2, x=5, y=6, width=10, height=20)
s = AllFigures(ftype = 3, x=5, y=6, l=16)
print(c,r,s, sep='\n')











