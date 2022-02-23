# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:58:12 2022
@author: Quentin Ducasse
"""

class Visitor:
    '''
    An example of a visitor performing a pass over an AST.
    '''
    def visit(self, program):
        '''
        Launch the AST visit.
        '''
        program.accept(self)
        return program

    def visit_program_node(self, program):
        '''
        Visit a program node
        '''
        ...
