
import random
from math import pow


a=random.randint(2,10) #The value for a will be randomly generated

#Here we have to find the gcd of two numbers keeping in mind : gcd(a, b) = 1.
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)

#Now we wil compute the key generation (large random number)
def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key
def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c
        y=(y*y)%c
        b=int(b/2)
    return x%c

#And now we will perform the asymetric encryption using the generated key
def encryption(msg,q,h,g):
    ct=[]
    k=gen_key(q)
    s=power(h,k,q)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])
    print("g^k = ",p)
    print("g^ak = ",s)
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p

#As we know For decryption, Bob Uses Both the public key and private key to decrypt the message that has been sent my Alice. 
def decryption(ct,p,key,q):
    pt=[]
    h=power(p,key,q)
    for i in range(0,len(ct)):
        pt.append(chr(int(ct[i]/h)))
    return pt
msg=input("Enter your message.")
q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=gen_key(q)
h=power(g,key,q)
print("g =",g)
print("g^a =",h)
ct,p=encryption(msg,q,h,g)
print("Our Original Message is = ",msg)
print("The Encrypted Message is = ",ct)
pt=decryption(ct,p,key,q)
d_msg=''.join(pt)
print("The Decrypted Message is = ",d_msg)