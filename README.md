# 8-bit CPU emulator
### The context
The final project for the 'Management and Analysis of Physics Dataset (MOD. A)' course in the 'Physics of Data' master program, University of Padua. <br>
Authors: <a href=https://github.com/paololapo> Paolo Lapo Cerni </a>, <a href=https://github.com/emanuele-quaglio> Emanuele Quaglio </a>, <a href=https://github.com/LorenzoVigorelli> Lorenzo Vigorelli </a>
### The project
A Python object-oriented high-level emulator for a simple 8-bit CPU, inspired by the <a href=https://eater.net/8bit/> project of Ben Eater </a>. <br>
The code is organized into a modular package structure:

#### Package Structure
```
cpu_emulator/
├── core/                    # Core hardware components
│   ├── registers.py         # Register, ByteRegister, NibbleRegister, InstructionRegister, ProgramCounter
│   ├── memory.py            # RAM class
│   ├── flags.py             # Flag, FlagMinus, FlagCarry, FlagZero
│   ├── alu.py               # ALU (Arithmetic Logic Unit)
│   └── clock.py             # Clock and RingCounter
├── cpu/                      # CPU logic and instructions
│   ├── cpu.py               # Main CPU class with microinstructions and execution logic
│   └── instructions.py      # Instruction definitions and opcode mappings
└── utils/                    # Utility functions
    └── conversions.py       # Binary/decimal/hexadecimal conversion functions

main.py                       # Entry point to load and run programs
Code_examples/                # Example assembly programs
```

#### Main Components
* <code> cpu_emulator/core/ </code>: Contains all hardware component classes (registers, memory, flags, ALU, clock)
* <code> cpu_emulator/cpu/ </code>: Contains the main CPU class with microinstruction logic, and instruction definitions. The CPU class includes <code> load() </code> to read assembly code from a .txt file, and <code> run() </code> to execute programs. By default, the state of the CPU after every micro-instruction will be saved into a log file.
* <code> cpu_emulator/utils/ </code>: Contains utility functions for number conversions
* <code> main.py </code>: Entry point to load the RAM and start the emulator
  
At the moment, our instruction set is composed of *LDA*, *ADD*, *SUB*, *STA*, *LDI*, *JMP*, *JC*, *JZ*, *OUT*, *HLT*. Thus, this CPU is slightly more complicated than a SAP 1. <br>
As a reference, here are the high-level schematics of the Ben Eater CPU:
<p align="center">
<img src="https://eater.net/schematics/high-level.png" alt="schematics" width="70%" height="70%">
</p>
