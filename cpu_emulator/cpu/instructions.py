# Dictionaries to convert op-code in mnemonics and viceversa
mnemo_op_code = {
    "LDA": "0000",
    "ADD": "0001",
    "SUB": "0010",
    "OUT": "1110",
    "HLT": "1111",
    "STA": "1010",
    "LDI": "1011",
    "JMP": "0101",
    "JC" : "0111",
    "JZ" : "1001"
}

op_code_mnemo = {
    '0000' : 'LDA', 
    '0001' : 'ADD',
    '0010' : 'SUB',
    '1110' : 'OUT',
    '1111' : 'HLT',
    "1010" : "STA",
    "1011" : "LDI",
    "0101" : "JMP" ,
    "0111" : "JC" ,
    "1001" : "JZ"
}


# Helper function to get the op-code of a mnemonics
def convert_mnemo_op_code(instruction):
    op_code = mnemo_op_code.get(instruction, "N/A")
    return op_code

