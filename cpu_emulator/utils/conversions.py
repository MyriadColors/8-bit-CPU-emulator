def binary_to_decimal(binary_string):
    # Check if the number is negative
    if binary_string[0] == '1':  
        # Calculate the two's complement by subtracting 2^n
        return int(binary_string, 2) - 2**len(binary_string)
    else:
        return int(binary_string, 2)


def decimal_to_binary(decimal_number, bit_width=8):
    if decimal_number < 0:
        # Calculate the two's complement by adding 2^n
        binary_string = bin(decimal_number + 2**bit_width)[2:]
    else:
        binary_string = bin(decimal_number)[2:]

    # Ensure the binary string has the correct length (bit_width)
    return binary_string.zfill(bit_width)


def hex_to_binary(hex_number, bit_width):
    # remove the 0x if present
    hex_number = hex_number.lstrip("0x")

    # Convert the number in binary and add zeros if necessary
    binary_number = bin(int(hex_number, 16))[2:].zfill(bit_width)[:bit_width]

    return binary_number

