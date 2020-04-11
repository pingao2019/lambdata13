

class Calc:

​ 

    def __init__(self, a, b):
      ''' __init__ is called as a constructor. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.'''
        self.a = a

        self.b = b

​

    def add_me(self):

        return self.a + self.b

​

    def sub_me(self):

        return self.a - self.b

​

​

class MulDiv(Calc):

​

    def mul_me(self):

        return self.a * self.b

    

    def div_me(self):

        return self.a / self.b

​

​

if __name__ == "__main__":

    if MulDiv(1, 2).add_me() == 3:

        print('Addition looks good!')

    if MulDiv(1, 2).sub_me() == -1:

        print('Subtraction looks good!')

    if MulDiv(1, 2).mul_me() == 2:

        print('Multiplication looks good!')

    if MulDiv(1, 2).div_me() == 0.5:

        print('Division looks good!')





class calculation():
    def __init__():

