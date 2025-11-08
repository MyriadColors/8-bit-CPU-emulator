"""
CPU module containing the main CPU class and instruction definitions.
"""

from .cpu import CPU
from .instructions import (
    mnemo_op_code,
    op_code_mnemo,
    convert_mnemo_op_code
)

__all__ = [
    'CPU',
    'mnemo_op_code',
    'op_code_mnemo',
    'convert_mnemo_op_code'
]

