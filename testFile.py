import numpy as np


fid1=open('C://Users/Albert GB/Documents/fILES/Sent.txt','r+')

Tot=fid1.readlines()
TotOrdenat=sorted(Tot)
print(TotOrdenat)

fid1.close()
