#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: April 16, 2023

def leftcont(word,oldchar,newchar,leftchar):
	'''replace oldchar by newchar in word if leftchar occurs immediately before oldchar'''
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
	'''replace oldchar by newchar in word if leftchars occur immediately before oldchar'''
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
	'''replace oldchar by newchar in word if leftchars occur immediately before oldchar'''
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
	'''replace oldchar by newchar in word if leftchars occur immediately before oldchar'''
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
	'''replace oldchar by newchar in word if leftchars occur immediately before oldchar'''
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

def rightcont(word,oldchar,newchar,rightchars):
	'''replace oldchar by newchar in word if rightchars occur immediately after oldchar'''
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
