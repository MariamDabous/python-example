# Biggie Size 
def biggie_size(list):
    for i in range(0,len(list),1):
        if(list[i]>0):
            list[i]="big"
        else:
            continue
    return(list)

Z=biggie_size([1,0,-5,12])
print(Z)

# Count Positives
def count_positives(list):
    c=0
    for a in range(0,len(list),1):
        if(list[a]>0):
            c=c+1
        else:
            continue
    list[len(list)-1]=c
    return list

R=count_positives([-1,1,1,1])
print(R)

def sum_total(list):
    sum=0
    for a in range(0,len(list),1):
        sum=sum+list[a]
    print(sum)
    return(sum)
sum_total([1,2,3,4])

def average(list):
    sum=0
    for a in range(0,len(list),1):
        sum=sum+list[a]
    print(sum/len(list))
    return(sum/len(list))
average([1,2,3,4])

def length(list):
    print(len(list))
    return(len(list))
    
length([37,2,1,-9])

def Minimum(list):
    if(len(list)==0):
        return(False)
    else:
        min=list[0]
        for a in range(0,len(list),1):
            if(list[a]<min):
                min=list[a]
            else:
                continue
        return(min)
X=Minimum([])
print(X)

def Maximum(list):
    if(len(list)==0):
        return(False)
    else:
        max=list[0]
        for a in range(0,len(list),1):
            if(list[a]>max):
                max=list[a]
            else:
                continue
        return(max)
X=Maximum([1,-5,10,30,4])
print(X)

def ultimate_analysis(list):
    mydictionary ={'sumTotal': 0, 'average': 0, 'minimum': 0, 'maximum': 0, 'length': 0 }
    mydictionary['sumTotal']= sum_total(list)
    mydictionary['average']= average(list)
    mydictionary['minimum']=Minimum(list)
    mydictionary['maximum']=Maximum(list)
    mydictionary['length']=length(list)
    return(mydictionary)

ultimate_analysis([37,2,1,-9])
H=ultimate_analysis([37,2,1,-9])
print(H)

def reverse_list(list):
    for p in range(0,int(len(list)/2),1):
        temp= list[p]
        list[p]=list[len(list)-1-p]
        list[len(list)-1-p]=temp
    return(list)

k=reverse_list([37,2,1,-9,10,12])
print(k)