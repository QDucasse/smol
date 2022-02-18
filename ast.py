# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:55:31 2022
@author: Quentin Ducasse
"""

from pprint import pformat

from abc import ABC


class Node(ABC):
    '''
    Principal Node of the system, meta-defines the accept function for all others subnodes.
    It is defined as an abstract class so it should not be instanciated but rather herited from.
    '''

    def accept(self, visitor, args):
        '''
        Accepts the upcoming visitor with its arguments.

        Parameters
        ----------
        visitor: Visitor object.
            Visitor of the ast.

        args: objects
            Arguments that need to be passed to the visit___ method cast on the
            visitor.

        Note
        ----
        The accept function, as described in the Visitor pattern, allows the receiver
        (subnode) to cast the correct visitor visit method.
        '''
        # Formatting the name
        className  = self.__class__.__name__
        methodName = getattr(visitor, "visit" + className)
        # Casting the visit<className> method on the visitor
        methodName(args)
        

class ProgramNode(Node):
    '''
    AST Node for the Program, it consists of a root node and holds
    a list of assignments, i.e. leaves of AssignmentNodes.
    '''
    def __init__(self):
        self.assignments = []

class AssignmentNode(Node):
    '''
    AST Node for an Assignment, consists of a variable (lhs) and an expression (rhs).
    '''
    def __init__(self):
        self.variable = None
        self.expression = None

class ExpressionNode(Node):
    '''
    AST Node for an Expression, consists of an two unary expressions and an operator.
    '''
    def __init__(self):
        self.lhs = None
        self.rhs = None
        self.operator = None

class UnaryNode(Node):
    '''
    AST Node for an Unary expression, consists of a variable or a number.
    '''
    def __init__(self):
        self.value = None

class VariableNode(Node):
    '''
    AST Node for a Variable, consists of a name.
    '''
    def __init__(self):
        self.name = None

class NumberNode(Node):
    '''
    AST Node for a Number, it consists of the number itself.
    '''
    def __init__(self):
        self.number = None
