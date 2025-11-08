from ..utils.conversions import binary_to_decimal


# Generic Flag
class Flag:
    def __init__(self, reg):
        self.state = 0
        self.reg=reg
    
    def update(self):
        self.state=self.state
    
    def __str__(self):
        return f"State: {self.state}"


# Flag minus: sign of the accumulator
class FlagMinus(Flag):

    def update(self):
        if(binary_to_decimal(self.reg.read())<0):
            self.state=1
        else:
            self.state=0

    def read(self):
        self.update()
        return self.state


# Flag Carry: carry of the operation
class FlagCarry(Flag): 

    def update(self):
        if binary_to_decimal(self.reg.a.read())+binary_to_decimal(self.reg.b.read()) > pow(2,7)-1:
            self.state=1
        else:
            self.state=0

    def read(self):
        return self.state


# Flag Zero: check if the accumulator is zero
class FlagZero(Flag): 

    def update(self):
        if(binary_to_decimal(self.reg.read())==0):
            self.state=1
        else:
            self.state=0
    def read(self):
        self.update()
        return self.state

