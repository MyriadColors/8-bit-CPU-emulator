import argparse
import sys
from pathlib import Path
from datetime import datetime
from cpu_emulator import CPU


def main():
    parser = argparse.ArgumentParser(
        description='8-bit CPU Emulator - Run assembly programs on the CPU',
        epilog='''
Examples:
  python main.py fibonacci.txt
  python main.py count_from_5_to_1.txt
  python main.py fibonacci.txt --translate
  python main.py fibonacci.txt --verbose
  python main.py Programs/fibonacci.txt  (or use full path)

Supported Instructions:
  LDA <addr>  - Load value from memory address into register A
  ADD <addr>  - Add value from memory address to register A
  SUB <addr>  - Subtract value from memory address from register A
  STA <addr>  - Store value from register A to memory address
  LDI <value> - Load immediate value into register A
  JMP <addr>  - Jump to memory address
  JC <addr>   - Jump to memory address if carry flag is set
  JZ <addr>   - Jump to memory address if zero flag is set
  OUT         - Output the value in register A
  HLT         - Halt execution

File Format:
  Programs can be written in assembly format (e.g., "LDA 0x5") or as
  raw binary/hex values (e.g., "0x00"). Each line represents one
  instruction or data value to be loaded into memory.
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'file_path',
        type=str,
        help='Name of the program file (e.g., fibonacci.txt) or full path to the assembly program file'
    )
    parser.add_argument(
        '--translate',
        action='store_true',
        help='Translate binary output values to decimal representation'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging: generate log file in logs/ folder with CPU state after each micro-instruction'
    )
    parser.add_argument(
        '--threshold',
        type=int,
        default=1000,
        help='Maximum number of clock cycles to execute before aborting (default: 1000)'
    )
    
    args = parser.parse_args()
    
    # If the path doesn't contain directory separators, assume it's in the Programs directory
    file_path = Path(args.file_path)
    if not any(sep in str(file_path) for sep in ['/', '\\']):
        # It's just a filename, prepend Programs directory
        file_path = Path('Programs') / file_path
    
    # Check if file exists
    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    
    if not file_path.is_file():
        print(f"Error: '{file_path}' is not a file.", file=sys.stderr)
        sys.exit(1)
    
    # Generate log file path if verbose is enabled
    log_file_path = None
    if args.verbose:
        # Extract program name (without extension)
        program_name = file_path.stem
        
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create logs directory if it doesn't exist
        logs_dir = Path('logs')
        logs_dir.mkdir(exist_ok=True)
        
        # Generate log file path
        log_file_path = logs_dir / f"log_{program_name}_{timestamp}.txt"
    
    # Create CPU instance and run the program
    try:
        cpu = CPU(translate_output=args.translate, log_file_path=str(log_file_path) if log_file_path else None)
        cpu.load(str(file_path))
        cpu.run(threshold=args.threshold)
    except Exception as e:
        print(f"Error running program: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
