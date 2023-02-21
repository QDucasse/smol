# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:55:57 2022
@author: Quentin Ducasse
"""

import sys

from smol.ast import *


class Parser():
    '''
    Toy language parser.
    '''

    # ==========================
    #      Helper Functions
    # ==========================

    def error(self, message):
        '''
        Error template.
        '''
        print(f'ERROR at {str(self.peek().position)}: {message}')
        sys.exit(1)

    def peek(self, n=1):
        '''
        Returns the next token in the list WITHOUT popping it.
        '''

        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error('No more lexems left.')
    

    def expect(self, tag):
        '''
        Pops the next token from the lexems list and tests its type through the tag.
        '''
        next_lexem = self.peek()
        if next_lexem.tag == tag:
            return self.accept()
        else:
            self.error('Expected {}, got {} instead'.format(tag, next_lexem.tag))


    def accept(self):
        '''
        Pops the lexem out of the lexems list and log its tag/value combination.
        '''
        lexem = self.peek()
        return self.lexems.pop(0)


    def remove_comments(self):
        '''
        Removes the comments from the token list by testing their tags.
        '''
        self.lexems = [lexem for lexem in self.lexems if lexem.tag!="COMMENT"]


    # ==========================
    #      Parse Functions
    # ==========================

    def parse(self, lexems):
        '''
        Main function: launches the parsing operation given a lexem list.
        '''
        self.lexems = lexems
        self.remove_comments()
        ast = self.parse_program()
        return ast


    def parse_program(self):
        '''
        Parses a program which is a succession of assignments.
        '''
        program_node = ProgramNode()
        while(len(self.lexems) > 0):
            assignment = self.parse_assignment()
            program_node.assignments.append(assignment)
        return program_node


    def parse_assignment(self):
        '''
        Parses an assignment that looks like:
            Identifier, '=', Expression ';'
        '''
        assignment_node = AssignmentNode()
        assignment_node.identifier = self.parse_identifier()
        self.expect('ASSIGN')
        assignment_node.expression = self.parse_expression()
        self.expect('TERMINATOR')
        return assignment_node


    def parse_expression(self):
        '''
        Parses an expression that looks like:
            Unary, {[ "/" | "+" | "-" | "*" ], Expression}
        '''
        expression_node = ExpressionNode()
        expression_node.lhs = self.parse_unary()
        # To check the type of the expression, we look for a ';' after the first identifier or number
        if not self.peek().tag == 'TERMINATOR':
            # Binary operation so operator and another expression
            if self.peek().tag in ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION']:
                expression_node.operator = self.accept()
            else:
                self.error("Missing operator in expression.")
            expression_node.rhs = self.parse_expression()
        return expression_node


    def parse_unary(self):
        '''
        Parses an unary that looks like:
            Identifier | Number
        '''
        unary_node = UnaryNode()
        if self.peek().tag == 'IDENTIFIER':
            unary_node.value = self.parse_identifier()
        elif self.peek().tag == 'NUMBER':
            unary_node.value = self.parse_number()
        else:
            self.error("Unary should be an identifier or a number")
        return unary_node


    def parse_identifier(self):
        '''
        Parses an identifier that looks like:
            Character, {Character | Digit}

        Note that the 'parsing' is done through the associated regex in the lexer
        '''
        identifier_node = IdentifierNode()
        token = self.expect('IDENTIFIER')
        identifier_node.value = token.value
        return identifier_node


    def parse_number(self):
        '''
        Parses a number that looks like:
            Digit, {Digit}

        Note that the 'parsing' is done through the associated regex in the lexer
        '''
        number_node = NumberNode()
        token = self.expect('NUMBER')
        number_node.value = token.value
        return number_node
