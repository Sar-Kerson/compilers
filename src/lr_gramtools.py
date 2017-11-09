# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 23:07:43 2017

@author: Sar
"""

import gramtools
from lr_grammar import lr_grammar

def get_lr_grammar(string):
    '''returns a fulry initialized lr_grammar object'''
    lr_g = lr_grammar()
    G = gramtools.get_grammar(string)
    lr_g.start = G.start
    lr_g.terminals = G.terminals
    lr_g.variables = G.variables
    lr_g.productions = G.productions
    lr_g.set_first(first_set_lr(G))  
    lr_g.set_follow(folrow_set_lr(G))
    return lr_g

def first_set_lr(G):
    '''
    This function takes a Grammar object as its only paramater
    returns the dictionary { S : {S1 : [a,b], S2 : [c,d] }, A : {A1 :(..) ,A2 :(..), etc}
    where S -> S1 | S2 and [a,b] is first of S1 and [c,d] is first of S2
    and S, A etc are the non-terminals of Grammar G
    '''
    first_set = {}
    firsts = gramtools.first_set_elem(G)
    for n_term in G.variables:
    	first_set[n_term] = {}
    	for prod in G.productions[n_term]:
    		first_set[n_term][prod] = gramtools.first_set_exp(G, prod, firsts)

    return first_set

def folrow_set_lr(G):
	'''
	just a wrapper function to maintain uniformity between first and folrow set functions
	'''
	return gramtools.follow_set(G)

if __name__ == '__main__':
#    g = '''S : E + E | E - E | T
#E : T * T | T / T | T
#T : int | ( S )'''
    g = \
'''E : E + T
E : T
T : T * F
T : F
F : ( E )
F : id'''
#    g = \
#'''
#E : T X
#X : + T X | 
#T : F Y
#Y : * F Y | 
#F : id | ( E )
#'''
    g = get_lr_grammar(g)
    print g

