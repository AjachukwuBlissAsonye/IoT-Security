import time
start= time.perf_counter() #to check the running time so as to compare with the other generators

def fastexp(a,n):
    if(n==0):
      return 1
    x=pow(a,n/2)
    x=x*x
    if(n%2==1):
        return (a**n)
      #x=x*a
    return x



print(fastexp(2,10))

end = time.perf_counter()
print("The running time is: %s Seconds"%(end-start))