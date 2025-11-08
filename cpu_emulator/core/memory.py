from .registers import ByteRegister


# RAM: store both the program and the data: 16 adresses of 8 bits each
class RAM:
    def __init__(self):
        # List of 8-bits registers
        self.state = [ByteRegister() for _ in range(16)]

    # Write on the address of the RAM
    def write(self, data, address):
        
        # Data validation
        assert type(data) is str, 'data type error'
        assert len(data) == 8, 'size error'

        self.state[address].write(data)
    
    # Read the address of the RAM
    def read(self, address):
        return self.state[address].read()
    
    def __str__(self):
        return "\n".join([f"Address {i}: {register}" for i, register in enumerate(self.state)])

