# General purpose register
class Register:
    def __init__(self):
        self.state = ''
    
    # Return the state of the register
    def read(self):
        return self.state
    
    # Overwrite the state of the register
    def write(self, data):
        self.state = data
    
    def __str__(self):
        return f"State: {self.state}"


# 8-bit register
class ByteRegister(Register):
    def __init__(self):
        self.state = '0'*8

    def __str__(self):
        return f"State: {self.state}"


# 4-bit register
class NibbleRegister(Register):
    def __init__(self):
        self.state = '0'*4
    
    def __str__(self):
        return f"State: {self.state}"


# IR: you can access the first and the second nibble
class InstructionRegister(ByteRegister):

    def readOpCode(self):
        # Get the first nibble (op-code)
        return self.read()[:4]
    
    def readOperand(self):
        # Get the second nibble (operand)
        return self.read()[4:]

    def __str__(self):
        return f"OpCode: {self.readOpCode()}\nOperand: {self.readOperand()}"


# 4-bits Program counter
class ProgramCounter(NibbleRegister):

    # Update the counter
    def advance(self):       
        # Get the decimal value
        value = int(self.state, 2)
        # Update the counter mod 2**4
        value = (value + 1)%2**4
        # Convert the new value into a 4-bits string
        string = bin(value)[2:].zfill(4)

        self.state = string

    def __str__(self):
        return f"Value: {int(self.state, 2)}"

