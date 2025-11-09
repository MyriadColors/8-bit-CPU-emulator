from .registers import ByteRegister
from ..utils.conversions import binary_to_decimal, decimal_to_binary


# ALU: 8-bit temporary register
class ALU(ByteRegister):

    def __init__(self, aRegister, bRegister):
        self.a = aRegister
        self.b = bRegister
        self.state='0'*8
        self.last_mode = 'add'  # Track last operation mode

    # Possible operations: add, sub
    def update(self, mode='add'):
        value_a, value_b = binary_to_decimal(self.a.read()), binary_to_decimal(self.b.read())
        result = 0  # Initialize result to prevent unbound variable error
        
        if mode == 'add':
            result = value_a + value_b
        elif mode == 'sub':
            result = value_a - value_b
        else:
            raise ValueError(f"Invalid operation mode: {mode}. Supported modes: 'add', 'sub'")
        
        # Handle 8-bit overflow/underflow (wrap around)
        # For addition: if result > 255, wrap around to 0-255 range
        # For subtraction: if result < 0, wrap around to 0-255 range
        if result > 255:
            result = result % 256
        elif result < 0:
            result = (result + 256) % 256
        
        # Remove redundant slicing - decimal_to_binary already returns 8-bit result
        self.state = decimal_to_binary(result, 8)
        self.last_mode = mode

    def read(self):
        # Return the current state without re-updating
        return self.state
        
    def __str__(self):
        return self.state

