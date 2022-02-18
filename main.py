# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:55:21 2022
@author: Quentin Ducasse
"""

import sys
import os

from pprint import pprint

from ast import *
from lexer import *
from parser import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Erro: Please provide a file to process.")
    file_name = sys.argv[1]
    try:
      with open(file_name, 'r') as file:
          file_data = file.readlines()
    except FileNotFoundError:
      print('Error: test file {} does not exist'.format(testFileName))
      sys.exit()


    # Lex the contents
    lexer = Lexer()
    lexems = lexer.lex(file_data)

    # Parse the lexems
    parser = Parser()
    ast = parser.parse(lexems)

    # Print the nodes
    pprint(vars(ast))
    pprint(vars(ast.assignments[2]))
