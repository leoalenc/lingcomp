#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: May 23, 2023

# BIRD, S.; KLEIN, E.; LOPER, E. Natural language processing with Python: analyzing text with the Natural Language Toolkit. Sebastopol, CA: O’Reilly, 2009.

def freqdist(words):
    for word in words:
    	if freqdist.get(word):
    		freqdist[word]+=1
    	else:
    		freqdist[word]=1
    return freqdist
