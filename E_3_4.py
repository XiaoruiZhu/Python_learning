#!/usr/bin/python
# Filename:E_3_4.py

def print_twice(num):
    print num
    print num

def do_twice(f,num):
    f(num)
    f(num)

num = raw_input('The word:')
do_twice(print_twice,num)
