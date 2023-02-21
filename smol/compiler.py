# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:57:03 2022
@author: Quentin Ducasse
"""

from smol.ast import *
from smol.lexer import Lexer
from smol.parser import Parser
from smol.visitor import Visitor

class Compiler:
    '''
    The compiler is the main class that includes all components and performs the
    operation that goes from raw data to the final product
    '''
    def __init__(self, lexer=None, parser=None, visitor=None):
        self.lexer = Lexer()
        self.parser = Parser()
        self.visitor = Visitor()

    def compile(self, file_data=None):
        '''
        Launches all the passes one after the other
        '''
        # First pass: transformation from data to lexems
        lexems = self.lexer.lex(file_data)
        print("Lexer: analysis successful!")
        # Parsing phase and transformation to AST
        ast = self.parser.parse(lexems)
        print("Parser: parsing successful!")
        # Different visitor phases (no effect for now)
        ast_pass_1 = self.visitor.visit(ast)
        print("Visitor: visit successful!")

        return ast_pass_1
