#%%
import numpy as np
import pandas as pd

def return_values(r):
    wn= 1e5
    zeta= r/2
    Q= 1/(2*zeta)
    p1= wn*(complex(-zeta) - np.sqrt( complex(zeta**2 -1) ) )
    p2= wn*(-zeta + np.sqrt( complex(zeta**2 -1) ) )
    wp1= abs(p1)
    wp2= abs(p2)
    return [r,zeta,Q,p1,p2,wp1,wp2]

R= [0.02,0.10,0.40,1.00,1.40,2.00,5.00,10.00,20.00,100.00]
R= np.array(R)

value=[]

for i in R:
    value.append(return_values(i))
value= pd.DataFrame(value)
value.columns= ['R','Zeta','Q','p1','p2','wp1','wp2']
value
#%%
gm1= 0.1*1e-3
gm2= 0.1*1e-3
Ro1= 1e6
Ro2= 1e6
    

#%%