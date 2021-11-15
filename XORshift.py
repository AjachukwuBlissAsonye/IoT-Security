import time
start= time.perf_counter() #to check the running time so as to compare with the other generators

xorshift_seed = 23456  # The initial seed value

def xorshift():
  global xorshift_seed
  xorshift_seed ^= xorshift_seed << 13 #a
  xorshift_seed ^= xorshift_seed >> 17 #b
  xorshift_seed ^= xorshift_seed << 5 #c
  xorshift_seed %= int("ffffffff", 16) # The modulus limits it to a 32-bit number
  return xorshift_seed


for i in range(6):
    print(xorshift())

end = time.perf_counter()
print("The running time is: %s Seconds"%(end-start))