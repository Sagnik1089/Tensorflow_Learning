import random
import pandas as pd
import os

a=[]
b=[]
c=[]
d=[]
e=[]

# Coefficients
coeff=[1,6,0,2]

r=100000 # No of samples
for i in range(r):
    a.append(random.randint(1,10))
    b.append(random.randint(1,15))
    c.append(random.randint(1,20))
    d.append(random.randint(1,25))
    e.append(((coeff[0]*a[i])-(coeff[1]*b[i])+(coeff[2]*c[i])-(coeff[3]*d[i])))
# print(a,b,c,d,sep=', ', end='\t')
# print(e)

dict={'a':a, 'b':b, 'c':c, 'd':d, 'e':e}
df=pd.DataFrame(dict)
df.to_csv(os.path.join(os.getcwd(), 'data{}.csv'.format(r)))