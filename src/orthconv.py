#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: April 16, 2023

def leftcont(word,oldchar,newchar,leftchar):
	'''replace oldchar by newchar in word if leftchar
	immediately occurs before oldchar'''
	j=0
	c=len(word)
	while(j<c):
		thischar=word[j]
		i=j-1
		if i >= 0:
			if thischar == oldchar and leftchar==word[i]:
				word=f"{word[:j]}{newchar}{word[j+1:]}"
		j+=1
	return word

def leftcont2(word,oldchar,newchar,leftchars):
	'''replace oldchar by newchar in word if leftchars immediately
	occur before oldchar'''
	j=0
	c=len(word)
	d=len(leftchars)
	while(j<c):
		thischar=word[j]
		i=j-d
		if i >= 0:
			if thischar == oldchar and leftchars==word[i:j]:
				word=f"{word[:j]}{newchar}{word[j+1:]}"
		j+=1
	return word

def leftcont3(word,oldchar,newchar,leftchars):
	'''replace oldchar by newchar in word if leftchars immediately
	occur before oldchar'''
	if newchar == '0':
		newchar=''
	if leftchars == '#' and word[0] == oldchar:
		return f"{newchar}{word[1:]}"
	j=0
	c=len(word)
	d=len(leftchars)
	print(word)
	while(j<c):
		print(j,word[j])
		thischar=word[j]
		i=j-d
		if i >= 0:
			if thischar == oldchar and leftchars==word[i:j]:
				word=f"{word[:j]}{newchar}{word[j+1:]}"
		j+=1
	return word

def leftcont4(word,oldchar,newchar,leftchars):
	'''replace oldchar by newchar in word if leftchars immediately
	occur before oldchar'''
	if newchar == '0':
		newchar=''
	if leftchars == '#' and word[0] == oldchar:
		return f"{newchar}{word[1:]}"
	j=0
	c=len(word)
	d=len(leftchars)
	new=word
	while(j<c):
		thischar=word[j]
		i=j-d
		if i >= 0:
			if thischar == oldchar and leftchars==word[i:j]:
				new=f"{word[:j]}{newchar}{word[j+1:]}"
				break
		j+=1
	return new

def leftcont5(word,oldchar,newchar,leftchars):
	'''replace oldchar by newchar in word if leftchars immediately
	occur before oldchar'''
	if newchar == '0':
		newchar=''
	if leftchars == '#' and word[0] == oldchar:
		return f"{newchar}{word[1:]}"
	j=0
	c=len(word)
	d=len(leftchars)
	new=word
	while(j<c):
		thischar=word[j]
		i=j-d
		if i >= 0:
			if thischar == oldchar and leftchars==word[i:j]:
				new=f"{word[:j]}{newchar}{word[j+1:]}"
				return new
		j+=1

def leftcont6(word,oldchar,newchar,leftchars):
	'''replace oldchar by newchar in word if leftchars immediately
	occur before oldchar'''
	if newchar == '0':
		newchar=''
	if leftchars == ['#'] and word[0] == oldchar:
		return f"{newchar}{word[1:]}"
	j=0
	c=len(word)
	new=word
	while(j<c):
		thischar=word[j]
		for string in leftchars:
			d=len(string)
			i=j-d
			if i >= 0:
				if thischar == oldchar and string==word[i:j]:
					new=f"{word[:j]}{newchar}{word[j+1:]}"
					return new
		j+=1


def leftcont7(word,oldchar,newchar,leftchars):
	'''replace oldchar by newchar in word if leftchars immediately
	occur before oldchar'''
	if newchar == '0':
		newchar=''
	if leftchars == ['#'] and word[0] == oldchar:
		return f"{newchar}{word[1:]}"
	j=0
	c=len(word)
	new=word
	while(j<c):
		thischar=word[j]
		if thischar == oldchar and hasLeftChars(leftchars,word,j):
			new=f"{word[:j]}{newchar}{word[j+1:]}"
			break
		j+=1
	return new

def rightcont(word,oldchar,newchar,rightchars):
	'''replace oldchar by newchar in word if rightchars immediately
	occur after oldchar'''
	if newchar == '0':
		newchar=''
	if rightchars == '#' and word[-1] == oldchar:
		return f"{newchar}{word[1:]}"
	i=0
	c=len(word)
	d=len(rightchars)
	new=word
	while(i<c):
		thischar=word[i]
		j=i+1
		if j < c:
			if thischar == oldchar and rightchars==word[j:j+d]:
				new=f"{word[:i]}{newchar}{word[j:]}"
				return new
		i+=1

def rightcont2(word,oldchar,newchar,rightchars):
	'''replace oldchar by newchar in word if rightchars immediately
	occur after oldchar'''
	if newchar == '0':
		newchar=''
	if rightchars == ['#'] and word[-1] == oldchar:
		return f"{newchar}{word[1:]}"
	i=0
	c=len(word)
	new=word
	while(i<c):
		thischar=word[i]
		if thischar == oldchar and hasRightChars(rightchars,word,i+1):
			new=f"{word[:i]}{newchar}{word[i+1:]}"
			break
		i+=1
	return new

def hasRightChars(chars,word,start):
	for c in chars:
		d=len(c)
		if c == word[start:start+d]:
			return True
	return False

def hasLeftChars(chars,word,end):
	for c in chars:
		d=len(c)
		if c == word[end-d:end]:
			return True
	return False

def rightleftcont(word,oldchar,newchar,leftchars,rightchars):
	'''replace oldchar by newchar in word if rightchars immediately
	occur after oldchar and leftchars immediately  occur before oldchar'''
	i=0
	c=len(word)
	new=word
	while(i<c):
		thischar=word[i]
		if thischar == oldchar:
			if  hasLeftChars(leftchars,word,i) and hasRightChars(rightchars,word,i+1):
				new=f"{word[:i]}{newchar}{word[i+1:]}"
				break
		i+=1
	return new
