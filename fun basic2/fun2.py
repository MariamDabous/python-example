


def Countdown(a):
    for x in range(a,-1,-1):
        print(x)

Countdown(5)

def PrintandReturn(list):
    print(list[0])
    return[list[1]] 

PrintandReturn([1,2])

from tkinter import Y


def first_plus_length(list):
    return(list[0]+len(list))

y=first_plus_length([1,3,4,5])
print(y)



def Greater(list):
    if(len(list)<3):
        return False
    r=0
    newlist = []
    for x in range(0,len(list),1):
        if (list[x]>list[1]):
            newlist.append(list[x])
            r=r+1
        else:
            continue
    print(r)
    return(newlist)
    
Z=Greater([5,2,7,8,2,3,8])
print(Z)

def length_and_value(a,b):
    newlist =[]
    for m in range(0,a,1):
        newlist.append(b)
    return newlist
Q=length_and_value(4,7)
print(Q)


