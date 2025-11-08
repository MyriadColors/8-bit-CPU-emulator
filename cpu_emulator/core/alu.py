from .registers import ByteRegister
from ..utils.conversions import binary_to_decimal, decimal_to_binary


# ALU: 8-bit temporary register
class ALU(ByteRegister):

    def __init__(self, aRegister, bRegister):
        self.a = aRegister
        self.b = bRegister
        self.state='0'*8

    # Possible operation: add, sub
    def update(self, mode='add'):
        value_a, value_b=binary_to_decimal(self.a.read()), binary_to_decimal(self.b.read())
        
        if(mode=='add'):
            result=value_a+value_b
        
        elif(mode=='sub'):
            result=value_a-value_b
        self.state=decimal_to_binary(result)[0:8] 

    def read(self, mode='add'):
        # Update the state before the reading operation
        self.update(mode)
        return self.state
        
    def __str__(self):
        self.read()
        return self.state

