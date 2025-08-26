n = int(input())

def thaphanoi(n,A,C,B):
    if(n==1): print(f"{A} -> {C}")
    else :
        thaphanoi(n-1,A,B,C)
        thaphanoi(1,A,C,B) #hoac print luon cx ddc
        thaphanoi(n-1,B,C,A)

thaphanoi(n,'A','C','B')
    