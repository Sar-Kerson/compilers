# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 23:06:40 2017

@author: Sar
"""

from grammar import Grammar

class lr_grammar(Grammar):

	def __init__(self, V=None, T=None, S=None, P=None):
		'''specific grammar for lr parser, comes with first and follow set'''
		Grammar.__init__(self, V, T, S, P)
		self.first = {}
		self.follow = {}

	def set_first(self, f_set):
		'''Sets the first set for the lr_grammar'''
		self.first = f_set

	def set_follow(self, f_set):
		'''Sets the follow set for the lr_grammar'''
		self.follow = f_set

	def __str__(self):
		'''returns grammar in printable format'''
		s = 'Grammar \n'
		s = s + 'Start Symbol \n' + str(self.start) + '\n'
		s = s + 'Terminals \n' + str(self.terminals) + '\n'
		s = s + 'Variables \n' + str(self.variables) + '\n'
		s = s + 'Productions \n' + str(self.productions) + '\n'
		s = s + 'First set \n' + str(self.first) + '\n'
		s = s + 'Follow set \n' + str(self.follow) + '\n'
		return s


		



