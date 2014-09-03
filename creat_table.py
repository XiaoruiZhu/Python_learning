#!/usr/bin/python
# Filename: creat_table.py

def creat_te(fir,sec):
    print fir,
    print sec*4,

def creat_one(ncol,fir,sec):
    for i in range(1,ncol+1):
        creat_te(fir,sec)
    print fir
    
def creat_raw(ncol,nrow):
    print ''
    for i in range(1,nrow+1):
        creat_one(ncol,'+','-')
        creat_one(ncol,'|',' ')
        creat_one(ncol,'|',' ')
        creat_one(ncol,'|',' ')
        creat_one(ncol,'|',' ')
    creat_one(ncol,'+','-')

        

    
ncol = 5
nrow = 4
creat_raw(ncol,nrow)
