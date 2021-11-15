import random
import numpy as np
import time
start= time.perf_counter() #to check the running time so as to compare with the other generators

def myRandomnum(l):
    randkey= [] #here we define a list where the randomly genereated bits will be appended
    for i in range(l): #An iteration to perform an XOR operation for l times ie: 25 times --myRandomnum(25)
        randgen= (random.randint(0,1))
        randkey.append(randgen)
    print("the random number is",(randkey))
    print ("the encrypted number is:",XOR(randkey,msg)) #here our XOR function is called and it XOR's The randomly 
                                                        #generated bits and our plain message which is also binary bits.

def XOR(a,b):
    for i in msg:
        return np.array(a) ^ np.array(b)
msg= [0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0]

print ("the plain text is",msg)
myRandomnum(25)

end = time.perf_counter()
print("The running time is: %s Seconds"%(end-start))