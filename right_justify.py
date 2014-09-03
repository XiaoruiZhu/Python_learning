#!/usr/bin/python
# Filename:right_justify.py

def right_justify(s):
    l = len(s)
    n = 70 - l
    print ' '*n,s

s = raw_input('The word:')
right_justify(s)
