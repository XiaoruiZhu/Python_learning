 #!/usr/bin/python
# Filename: func_return.py

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

a = int(raw_input('First Num:'))
b = int(raw_input('Second Num:'))
print 'The bigger one is:', maximum(a, b) 
