#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: May 23, 2023

# ZELLE, J. M. Python programming: an introduction to computer science. Wilsonville: Franklin, Beedle & Associates, 2004.

def maxnum(*nums):
	if nums:
		maxnum=nums[0]
		for num in nums:
			if num > maxnum:
				maxnum=num
		return maxnum
