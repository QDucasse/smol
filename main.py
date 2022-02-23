# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:55:21 2022
@author: Quentin Ducasse
"""

import sys
from pprint import pprint

from compiler import Compiler

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Erro: Please provide a file to process.")
    file_name = sys.argv[1]
    try:
      with open(file_name, 'r') as file:
          file_data = file.readlines()
    except FileNotFoundError:
      print('Error: test file {} does not exist'.format(file_name))
      sys.exit()

     # The compiler will:
     #  - lex the raw data through the lexer and generate lexems
     #  - parse the lexems through the parser and generate an AST
     #  - visit the AST through a visitor and generate an output

    compiler = Compiler()
    ast = compiler.compile(file_data)

    # Pretty print the instance vars from the program node but as it
    # is not recursive it would be more interesting to inspect it
    # through a debugger
    pprint(vars(ast))
