# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:37:42 2017

@author: hauck
"""
firstline = ["Happy", "families", "are", "all", "alike;", "every", \
              "unhappy", "family", "is", "unhappy", "in", "its", "own", \
              "way.", "Leo Tolstoy", "Anna Karenina"]

print(firstline)
firstline = [element.lower() for element in firstline]
firstline.sort()
print(firstline)
