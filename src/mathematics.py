#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: April 16, 2023

def factorial(n):
	'''computes the factorial of n'''
	i=1
	k=1
	while(i<=n):
		k=k*i
		i+=1
	return k

def add(n,m):
	return n+m

def subtract(n,m):
	return n-m
