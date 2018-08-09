import timeit
import random

#2

def speed_type():
    num=1
    type(num)==type(0)
    
def speed_type_is():
    num=1
    type(num) is type(0)
def speed_isinstance():
    num=1
    isinstance(num,(int))
    
    
#2

def speed_len_in_loop():
    a=[1,2,3]#Each loop needs to re-execute len(a)
    i=0
    
    while i < len(a):
        b=1+1
        i+=1
        
def speed_len_out_of_loop():
    a=[1,2,3]#Each loop needs to re-execute len(a)
    i=0
    m=len(a)
    while i < m:
        b=1+1
        i+=1


#3
def speed_cond():
    a=random.choice([1,2,3,4])
    
    if a==1:
        b=a
    if a==2:
        b=a
    if a==3:
        b=a
    if a==4:
        b=a

def speed_dict():
    d={1:1,2:2,3:3,4:4}
    a=random.choice([1,2,3,4])
    b=d[a]
    
def speed_iter():
    a=[1,2,3]
    for el in a:
        b=a
        

def speed_iter_range():
    a=[1,2,3]
    for i in range(len(a)):
        b=a
    
        
def speed_list_comp():
    #Calculate the number of non-null characters in file f
    #List analysis
    f="Hello there!\n General Kenobi!"
    l = sum([len(word) for line in f for word in line.split()])
    
def speed_gen():
    f="Hello there!\n General Kenobi!"
    l = sum(len(word) for line in f for word in line.split())
    
if __name__=="__main__":
    
    num=10000
    
    #1 no code provided
    
    #2.1
    print(2.1)
    r=timeit.timeit("speed_type()",number=num,setup="from __main__ import speed_type")
    print(r)
    r=timeit.timeit("speed_type_is()",number=num,setup="from __main__ import speed_type_is")
    print(r)
    r=timeit.timeit("speed_isinstance()",number=num,setup="from __main__ import speed_isinstance")
    print(r)
    
    #2.2
    print(2.2)
    r=timeit.timeit("speed_len_in_loop()",number=num,setup="from __main__ import speed_len_in_loop")
    print(r)
    r=timeit.timeit("speed_len_out_of_loop()",number=num,setup="from __main__ import speed_len_out_of_loop")
    print(r)
    
    #3
    print(3)
    r=timeit.timeit("speed_cond()",number=num,setup="from __main__ import speed_cond")
    print(r)
    r=timeit.timeit("speed_dict()",number=num,setup="from __main__ import speed_dict")
    print(r)
    
    #4
    print(4)
    r=timeit.timeit("speed_iter()",number=num,setup="from __main__ import speed_iter")
    print(r)
    r=timeit.timeit("speed_iter_range()",number=num,setup="from __main__ import speed_iter_range")
    print(r)
    
    #5
    print(5)
    r=timeit.timeit("speed_list_comp()",number=num,setup="from __main__ import speed_list_comp")
    print(r)
    r=timeit.timeit("speed_gen()",number=num,setup="from __main__ import speed_gen")
    print(r)
    
    #6
    #no code provided
    #also you probably shouldn't really do it if you have any other choice at all.
    
    
    #7
    #not related to performance
    
    
