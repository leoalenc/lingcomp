#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: April 16, 2023

TEST =['abcde', 'abc de', 'abc de fg', 'abc de fg gh']

def split(s):
	parts=[]
	i=0
	init=0
	end=0
	while(i<len(s)):
		if s[i] == ' ':
			end=i
			parts.append(s[init:end])
			init=end+1
		i+=1
	parts.append(s[init:])
	return parts
