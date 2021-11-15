import time
start= time.perf_counter() #to check the running time so as to compare with the other generators

def LCG(VarNo,Startposition): #here we input how many variables we want and the starting position(Seed)

    #Here i choose my parameters for a,c & M
    a = 7**5
    M=2**31-1
    c=0

    def f(Startposition):
        return (a*Startposition+c)%M #given that c is 0 we have (a*startposition)%M
    
    U = [] #Here i define an empty list to store my O/P

    for i in range(VarNo):
        Startposition=f(Startposition)
        U += [Startposition/M] #Here i append the generated values to the list. 

    return U

print(LCG(6,254655454))

end = time.perf_counter()
print("The running time is: %s Seconds"%(end-start))