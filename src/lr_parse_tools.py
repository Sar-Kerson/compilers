# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 23:12:21 2017

@author: Sar
"""

import lr_gramtools
import lr_parser
import re

I = []
look_up = []
look_up_red = []

'''E : E + T
E : T
T : T * F
T : F
F : ( E )
F : a
E : E - T
T : T / F'''
grammar = ['Z:E', 'E:E+T', 'E:T', 'T:T*F', 'T:F', 'F:(E)', 'F:a', 'E:E-T', 'T:T/F']

#def lr_table(lr_g):
#    '''
#    returns the lr_parsing table, given the lr_grammar as param
#    '''
#    table = {}
#    for i in range(12):
#        table[i] = {}
#    
#    table[0]['id'] = 's:5'
#    table[0]['+'] = ' '
#    table[0]['*'] = ' '
#    table[0]['('] = 's:4'
#    table[0][')'] = ' '
#    table[0]['$'] = ' '
#    table[0]['E'] = '1'
#    table[0]['T'] = '2'
#    table[0]['F'] = '3'
#    
#    table[1]['id'] = ' '
#    table[1]['+'] = 's:6'
#    table[1]['*'] = ' '
#    table[1]['('] = ' '
#    table[1][')'] = ' '
#    table[1]['$'] = 'acc'
#    table[1]['E'] = ' '
#    table[1]['T'] = ' '
#    table[1]['F'] = ' '
#    
#    table[2]['id'] = ' '
#    table[2]['+'] = 'r:2'
#    table[2]['*'] = 's:7'
#    table[2]['('] = ' '
#    table[2][')'] = 'r:2'
#    table[2]['$'] = 'r:2'
#    table[2]['E'] = ' '
#    table[2]['T'] = ' '
#    table[2]['F'] = ' '
#    
#    table[3]['id'] = ' '
#    table[3]['+'] = 'r:4'
#    table[3]['*'] = 'r:4'
#    table[3]['('] = ' '
#    table[3][')'] = 'r:4'
#    table[3]['$'] = 'r:4'
#    table[3]['E'] = ' '
#    table[3]['T'] = ' '
#    table[3]['F'] = ' '
#
#    table[4]['id'] = 's:5'
#    table[4]['+'] = ' '
#    table[4]['*'] = ' '
#    table[4]['('] = 's:4'
#    table[4][')'] = ' '
#    table[4]['$'] = ' '
#    table[4]['E'] = '8'
#    table[4]['T'] = '2'
#    table[4]['F'] = '3'
#    
#    table[5]['id'] = ' '
#    table[5]['+'] = 'r:6'
#    table[5]['*'] = 'r:6'
#    table[5]['('] = ' '
#    table[5][')'] = 'r:6'
#    table[5]['$'] = 'r:6'
#    table[5]['E'] = ' '
#    table[5]['T'] = ' '
#    table[5]['F'] = ' '
#    
#    table[6]['id'] = 's:5'
#    table[6]['+'] = ' '
#    table[6]['*'] = ' '
#    table[6]['('] = 's:4'
#    table[6][')'] = ' '
#    table[6]['$'] = ' '
#    table[6]['E'] = ' '
#    table[6]['T'] = '9'
#    table[6]['F'] = '3'
#    
#    table[7]['id'] = 's:5'
#    table[7]['+'] = ' '
#    table[7]['*'] = ' '
#    table[7]['('] = 's:4'
#    table[7][')'] = ' '
#    table[7]['$'] = ' '
#    table[7]['E'] = ' '
#    table[7]['T'] = ' '
#    table[7]['F'] = '10'
#    
#    table[8]['id'] = ' '
#    table[8]['+'] = 's:6'
#    table[8]['*'] = ' '
#    table[8]['('] = ' '
#    table[8][')'] = 's:11'
#    table[8]['$'] = ' '
#    table[8]['E'] = ' '
#    table[8]['T'] = ' '
#    table[8]['F'] = ' '
#    
#    table[9]['id'] = ' '
#    table[9]['+'] = 'r:1'
#    table[9]['*'] = 's:7'
#    table[9]['('] = ' '
#    table[9][')'] = 'r:1'
#    table[9]['$'] = 'r:1'
#    table[9]['E'] = ' '
#    table[9]['T'] = ' '
#    table[9]['F'] = ' '
#    
#    table[10]['id'] = ' '
#    table[10]['+'] = 'r:3'
#    table[10]['*'] = 'r:3'
#    table[10]['('] = ' '
#    table[10][')'] = 'r:3'
#    table[10]['$'] = 'r:3'
#    table[10]['E'] = ' '
#    table[10]['T'] = ' '
#    table[10]['F'] = ' '
#    
#    table[11]['id'] = ' '
#    table[11]['+'] = 'r:5'
#    table[11]['*'] = 'r:5'
#    table[11]['('] = ' '
#    table[11][')'] = 'r:5'
#    table[11]['$'] = 'r:5'
#    table[11]['E'] = ' '
#    table[11]['T'] = ' '
#    table[11]['F'] = ' '
#    
#
#    
#    return table

def closure(items_set, g):
    clo_set = []
    for i in items_set:
        if i not in clo_set:
            clo_set.append(i)
    for item in items_set:
        dot_pos = item.find('.')
        temp_set = []
        if dot_pos < len(item)-1 and item[dot_pos+1] in g.variables:
            for prods in g.productions:
                for prod in grammar:
                    if prod[0]==item[dot_pos+1]:
                        left = prod[0]
                        right = "." + prod[2:]
                        new_item = left + ":" + right
                        print str(len(prod)) + ":" + prod
                        if prod[2] is not left:
                            if new_item not in temp_set:
                                temp_set.append(new_item)
                        if new_item not in clo_set:
                            clo_set.append(new_item)
        if temp_set:
            c = closure(temp_set, g)
            for i in c:
                if i not in clo_set:
                    clo_set.append(i)
    return clo_set

def shift_dot(string):
    left,right = string.rsplit('.')
    next_val = right[0]
    left = left + next_val
    new_right = "." + right[1:] 
    string = left + new_right
    return string

def create_states_util(state, g):
    count = 0
    if len(I[state])==1 and I[state][0][len(I[state][0])-1]=='.':
        item = I[state][0]
        item = item[:len(item)-1]
        index = grammar.index(item)
        look_up_red.append((state, item[0], index))
        return
    for item in I[state]:
        dot_pos = item.find('.')
        if dot_pos < len(item)-1:
            val = item[dot_pos+1]
            new_item = shift_dot(item)
            temp_tup = (state, val)
            flag = 0
            for a_tuple in look_up:
                if a_tuple[:2] == temp_tup:
                    flag = 1
                    #print("Flag value changed")
                    _set = closure([new_item], g)
                    for i in _set:
                        if i not in I[a_tuple[2]]:
                            I[a_tuple[2]].append(i)
                    break
            if flag==0:
                if len(I)>1:
                    last_state = I[len(I)-1]
                    i = 0
                    while i < len(I)- 1:
                        if I[i] == last_state:
                            I.pop()
                            count-=1
                            old_val = look_up[len(look_up)-1][1]
                            old_state = look_up[len(look_up)-1][0]
                            look_up.pop()
                            #print("Old value: " + old_val)
                            look_up.append((old_state, old_val, i))
                            break;
                        i+=1
                new_state = closure([new_item], g)
                I.append(new_state)
                look_up.append((state, val, len(I)-1))
                count+=1
        else:
            item = item[:len(item)-1]
            index = grammar.index(item)
            if item[0] is not 'Z':
                look_up_red.append((state, item[0], index))
            
    return count

def create_states(g):
    create_states_util(0, g)
    curr = 0
    for a_tuple in look_up:
        i = a_tuple[2]
        if i>curr:
            create_states_util(i, g)
            curr = i
            
    
    lookup_len = len(look_up)-1
    waste = look_up[len(look_up)-1][0]
    i = 0
    while waste != look_up[i][2] and i<=lookup_len:
        i+=1
    if i == lookup_len:
        while True:
            if look_up[lookup_len][0]==waste:
                look_up.pop()
                lookup_len-=1
            else:
                break
    else:
        i = 0
        last_state = I[len(I)-1]
        while i < len(I)- 1:
            if I[i] == last_state:
                #I.pop()
                old_val = look_up[len(look_up)-1][1]
                old_state = look_up[len(look_up)-1][0]
                look_up.pop()
                #print("Old value: " + old_val)
                look_up.append((old_state, old_val, i))
                break;
            i+=1
    I.pop()

def create_full_table(g):
    full_table = {}
    for a_tuple in look_up:
        col = a_tuple[0]
        term = a_tuple[1]
        val = a_tuple[2]
        if col in full_table:
            if term in g.terminals:
                full_table[col][term] = 's:' + str(val)
            else:
                full_table[col][term] = str(val)
        else:
            full_table[col] = {}
            if term in g.terminals:
                full_table[col][term] = 's:' + str(val)
            else:
                full_table[col][term] = str(val)
    #tables.apppend(table)
    for a_tuple in look_up_red:
        col = a_tuple[0]
        nonterm = a_tuple[1]
        val = a_tuple[2]
        if col in full_table:
            for sym in g.follow[nonterm]:
                if sym in full_table[col]:
                    full_table[col][sym] = 'r:' + str(val)
                else:
                    full_table[col][sym] = 'r:' + str(val)
        else:
            full_table[col] = {}
            for sym in g.follow[nonterm]:
                if sym in full_table[col]:
                    full_table[col][sym] = 'r:' + str(val)
                else:
                    full_table[col][sym] = 'r:' + str(val)
    full_table[1]['$'] = 'acc'
    return full_table
   
    

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

def lr_table(g):
    I.append(closure(["Z:.E"], g))
    create_states(g)
#    print_states()
    return create_full_table(g)

if __name__ == '__main__':
    g = \
'''E : E + T
E : T
T : T * F
T : F
F : ( E )
F : a
E : E - T
T : T / F'''
    p = get_parser(g)
    input = 'a / a - ( a + a ) * a'
    input = input.split(" ")
    print '\n'+ str(p.table)+ '\n'
    p.parse(input)