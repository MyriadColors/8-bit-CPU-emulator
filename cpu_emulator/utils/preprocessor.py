"""
Preprocessor for assembly programs.

This module handles preprocessing of assembly source code before execution,
such as comment stripping and other transformations.
"""


def preprocess_line(line):
    """
    Preprocess a single line of assembly code.
    
    Currently strips comments (everything after ';') and trims whitespace.
    
    Args:
        line (str): A line of assembly code
        
    Returns:
        str: The preprocessed line, or empty string if line is empty/comment-only
    """
    # Strip comments (everything after ';')
    if ';' in line:
        line = line.split(';')[0]
    
    # Strip whitespace
    line = line.strip()
    
    return line


def preprocess_file(file_path):
    """
    Preprocess an entire assembly file.
    
    Reads the file, preprocesses each line, and returns a list of
    non-empty preprocessed lines.
    
    Args:
        file_path (str): Path to the assembly file
        
    Returns:
        list: List of preprocessed lines (empty lines and comment-only lines are removed)
    """
    preprocessed_lines = []
    
    with open(file_path, "r") as file:
        for line in file:
            processed_line = preprocess_line(line)
            # Skip empty lines (including comment-only lines)
            if processed_line:
                preprocessed_lines.append(processed_line)
    
    return preprocessed_lines

