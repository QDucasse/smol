# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:55:31 2022
@author: Quentin Ducasse
"""

from abc import ABC
import re


GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

class Node(ABC):
    '''
    Principal Node of the system, meta-defines the accept function for all others subnodes.
    It is defined as an abstract class so it should not be instanciated but rather herited from.
    '''

    def accept(self, visitor):
        '''
        Accepts the upcoming visitor with its arguments.

        Parameters
        ----------
        visitor: Visitor object.
            Visitor of the ast.

        args: objects
            Arguments that need to be passed to the visit method cast on the
            visitor.

        Note
        ----
        The accept function, as described in the Visitor pattern, allows the receiver
        (subnode) to cast the correct visitor visit method.
        '''
        # Formatting the name
        class_name_camel_case = self.__class__.__name__
        class_name_snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name_camel_case).lower()
        method_name = getattr(visitor, "visit_" + class_name_snake_case)
        # Casting the visit<class_name> method on the visitor
        method_name(visitor)


class ProgramNode(Node):
    '''
    AST Node for the Program, it consists of a root node and holds
    a list of assignments, i.e. leaves of AssignmentNodes.
    '''
    def __init__(self, assignments=None):
        self.assignments = assignments if assignments is not None else []

    def __str__(self):
        return "Program (\n" + "\n".join([str(assignment) for assignment in self.assignments]) + "\n)"

class AssignmentNode(Node):
    '''
    AST Node for an Assignment, consists of an identifier (lhs) and an expression (rhs).
    '''
    def __init__(self, identifier=None, expression=None):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return "Assignment ( {} = {} )".format(str(self.identifier), str(self.expression))

class ExpressionNode(Node):
    '''
    AST Node for an Expression, consists of an two unary expressions and an operator.
    '''
    OPERATOR_STR = {
        'ADDITION': '+',
        'SUBTRACTION': '-',
        'MULTIPLICATION': '*',
        'DIVISION': '/'
    }

    def __init__(self, lhs=None, rhs=None, operator=None):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator

    def __str__(self):
        if self.operator is None:
            return "Expression( {} )".format(str(self.lhs))
        return "Expression( {} {} {} )".format(str(self.lhs), RED + ExpressionNode.OPERATOR_STR[self.operator.tag] + ENDC, str(self.rhs))

class UnaryNode(Node):
    '''
    AST Node for an Unary expression, consists of an identifier or a number.
    '''
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return "Unary ( {} )".format(str(self.value))

class IdentifierNode(Node):
    '''
    AST Node for an Identifier, consists of a name.
    '''
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return "Identifier {}".format(GREEN + self.value + ENDC)

class NumberNode(Node):
    '''
    AST Node for a Number, it consists of the number itself.
    '''
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return "Number {}".format(GREEN + str(self.value) + ENDC)
