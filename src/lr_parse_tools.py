# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 23:12:21 2017

@author: Sar
"""

import lr_gramtools
import lr_parser
import re

def lr_table(lr_g):
    '''
    returns the lr_parsing table, given the lr_grammar as param
    '''
    table = {}
    for i in range(12):
        table[i] = {}
    
    table[0]['id'] = 's:5'
    table[0]['+'] = ' '
    table[0]['*'] = ' '
    table[0]['('] = 's:4'
    table[0][')'] = ' '
    table[0]['$'] = ' '
    table[0]['E'] = '1'
    table[0]['T'] = '2'
    table[0]['F'] = '3'
    
    table[1]['id'] = ' '
    table[1]['+'] = 's:6'
    table[1]['*'] = ' '
    table[1]['('] = ' '
    table[1][')'] = ' '
    table[1]['$'] = 'acc'
    table[1]['E'] = ' '
    table[1]['T'] = ' '
    table[1]['F'] = ' '
    
    table[2]['id'] = ' '
    table[2]['+'] = 'r:2'
    table[2]['*'] = 's:7'
    table[2]['('] = ' '
    table[2][')'] = 'r:2'
    table[2]['$'] = 'r:2'
    table[2]['E'] = ' '
    table[2]['T'] = ' '
    table[2]['F'] = ' '
    
    table[3]['id'] = ' '
    table[3]['+'] = 'r:4'
    table[3]['*'] = 'r:4'
    table[3]['('] = ' '
    table[3][')'] = 'r:4'
    table[3]['$'] = 'r:4'
    table[3]['E'] = ' '
    table[3]['T'] = ' '
    table[3]['F'] = ' '

    table[4]['id'] = 's:5'
    table[4]['+'] = ' '
    table[4]['*'] = ' '
    table[4]['('] = 's:4'
    table[4][')'] = ' '
    table[4]['$'] = ' '
    table[4]['E'] = '8'
    table[4]['T'] = '2'
    table[4]['F'] = '3'
    
    table[5]['id'] = ' '
    table[5]['+'] = 'r:6'
    table[5]['*'] = 'r:6'
    table[5]['('] = ' '
    table[5][')'] = 'r:6'
    table[5]['$'] = 'r:6'
    table[5]['E'] = ' '
    table[5]['T'] = ' '
    table[5]['F'] = ' '
    
    table[6]['id'] = 's:5'
    table[6]['+'] = ' '
    table[6]['*'] = ' '
    table[6]['('] = 's:4'
    table[6][')'] = ' '
    table[6]['$'] = ' '
    table[6]['E'] = ' '
    table[6]['T'] = '9'
    table[6]['F'] = '3'
    
    table[7]['id'] = 's:5'
    table[7]['+'] = ' '
    table[7]['*'] = ' '
    table[7]['('] = 's:4'
    table[7][')'] = ' '
    table[7]['$'] = ' '
    table[7]['E'] = ' '
    table[7]['T'] = ' '
    table[7]['F'] = '10'
    
    table[8]['id'] = ' '
    table[8]['+'] = 's:6'
    table[8]['*'] = ' '
    table[8]['('] = ' '
    table[8][')'] = 's:11'
    table[8]['$'] = ' '
    table[8]['E'] = ' '
    table[8]['T'] = ' '
    table[8]['F'] = ' '
    
    table[9]['id'] = ' '
    table[9]['+'] = 'r:1'
    table[9]['*'] = 's:7'
    table[9]['('] = ' '
    table[9][')'] = 'r:1'
    table[9]['$'] = 'r:1'
    table[9]['E'] = ' '
    table[9]['T'] = ' '
    table[9]['F'] = ' '
    
    table[10]['id'] = ' '
    table[10]['+'] = 'r:3'
    table[10]['*'] = 'r:3'
    table[10]['('] = ' '
    table[10][')'] = 'r:3'
    table[10]['$'] = 'r:3'
    table[10]['E'] = ' '
    table[10]['T'] = ' '
    table[10]['F'] = ' '
    
    table[11]['id'] = ' '
    table[11]['+'] = 'r:5'
    table[11]['*'] = 'r:5'
    table[11]['('] = ' '
    table[11][')'] = 'r:5'
    table[11]['$'] = 'r:5'
    table[11]['E'] = ' '
    table[11]['T'] = ' '
    table[11]['F'] = ' '
    

    
    return table
    

def get_parser(rules):              # make a table in this method and put it in the parser
    '''r:ules is the string that contains all grammar rules'''
    g = lr_gramtools.get_lr_grammar(rules)
    par = lr_parser.parser(g)
    par.set_table(lr_table(g))
    return par


def get_input(scanner, text):
	'''
	puts input in acceptable form for the parser
	'''
	tokens, remainder = scanner.scan(text)
	return tokens


if __name__ == '__main__':
    g = \
'''E : E + T
E : T
T : T * F
T : F
F : ( E )
F : id'''
    p = get_parser(g)
    input = 'id * id + id'
    input = input.split(" ")
    print '\n'+ str(p.table)+ '\n'
    p.parse(input)