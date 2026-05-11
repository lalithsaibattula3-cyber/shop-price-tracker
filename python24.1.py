'''
try:
  x = 10/0
except ZeroDivisionError:
    print('cannot divide by zero ')    
'''
'''
try:
    x = '10'+ 5
except TypeError:
    print('mismatched')
    '''
'''
try:
    r = [0,1,2,3]
    print(r[5])
except IndexError:
    print('indexnotfound')
    '''  
'''
try:
    d ={'a':1}
    print(d[b])
except KeyError:
    print('key is not found')
'''
'''
try:
    int('abc')
except ValueError:
    print('invalidError')  
'''
'''
try:
    open('file.txt')
except FileNotFoundError:
    print('filenotfound')
'''