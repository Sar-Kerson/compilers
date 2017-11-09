# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 23:13:09 2017

@author: Sar
"""

import lr_gramtools               #!!!!!!!!!

value={'id':5}

class parser:
    
    def __init__(self, grammar=None, table=None):
        if table:
            self.table = table
        else:
            self.table = {}

        self.grammar = grammar
        self.stack = []


    def set_table(self, table):
        self.table = table

    def set_grammar(self, grammar):
        self.grammar = grammar
    
    def action(self, s, a):           #s: int, a: string       ex:    action(0, 'id')
        cont = self.table[s][a]
        if cont.isdigit():
            return cont
        elif cont == ' ':
            return ' '
        else:
            cont = cont.split(':')
        return cont
        
    def goto(self, s, a):               #s: int, a: string       ex:    goto(0, 'id')
#        print "goto:" + str(s) + "," + str(a)
        cont = self.table[s][a]
#        cont = cont.split(':')
        return int(cont)

    def parse(self, input, verbose=False):
        self.stack = []
        stack = self.stack
        
        num_stack = []
        
        grammar = self.grammar
        table = self.table
        
        stack.append(0)
        num_stack.append(0)
        input.append('$')
#        next = input.pop(0)
        
        prod = ['', '']
        
        while True:
            print stack
            print "##" + str(num_stack)
            s = stack[-1]
            act = self.action(s, input[0])
            if act[0] == 'acc': 
                print "accept!\n"
                print "result:" + str(num_stack[-2])
                break
            elif len(act) == 2:
                
                if act[0] == 's':
                    top = input.pop(0)
                    stack.append(top)
                    stack.append(int(act[1]))
                    num_stack.append(top)
                    num_stack.append(int(act[1]))
                if act[0] == 'r':
                    num = int(act[1])
                    if num == 1:
                        prod[0] = 'E'
                        prod[1] = 'E + T'
                        num_stack[-6] = num_stack[-2] + num_stack[-6]
                    elif num == 2:
                        prod[0] = 'E'
                        prod[1] = 'T'
                        num_stack[-2] = num_stack[-2]
                    elif num == 3:
                        prod[0] = 'T'
                        prod[1] = 'T * F'
                        num_stack[-6] = num_stack[-2] * num_stack[-6]
                    elif num == 4:
                        prod[0] = 'T'
                        prod[1] = 'F'
                        num_stack[-2] = num_stack[-2]
                    elif num == 5:
                        prod[0] = 'F'
                        prod[1] = '( E )'
                        num_stack[-6] = num_stack[-4]
                    elif num == 6:
                        prod[0] = 'F'
                        prod[1] = 'id'
                        num_stack[-2] = 10
                    prod[1] = filter(lambda x: x != ' ', prod[1])
                    if prod[1] == 'id':                 #!!!!!need to change if case like: F->F + id
                        for i in range(2):
                            stack.pop(-1)
                        for i in range(1):
                            num_stack.pop(-1)
                    else:
                        for i in range(2 * len(prod[1])):
                            stack.pop(-1)
                        for i in range(2 * len(prod[1]) - 1):
                            num_stack.pop(-1)
                            
                    stack.append(prod[0])
                    s = self.goto(stack[-2], stack[-1])
                    stack.append(s)
                    num_stack.append(s)
                    print prod[0] + "->" + prod[1]
            else:
                print "error!"
                break



