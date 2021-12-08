class Rectangle():
    def __init__(self,a,b):
      self.a = a
      self.b = b

    def get_perim(self):
        return (self.a + self.b)*2
    def get_param(self):
        return f'Parameters(length={self.a}, width={self.b})'

r=Rectangle(3,9)
print('Perim =',r.get_perim())
print(r.get_param())