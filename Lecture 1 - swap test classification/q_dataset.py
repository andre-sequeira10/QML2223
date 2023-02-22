### Quantum dataset generator ###
import numpy as np 

theta_0 = 0
theta_1 = np.pi/2
phi = 0

epsilon = 0.2
epsilon_new = 2

N=20
d = []
d_bloch=[]

d_= []
d__bloch = []
for i in range(N):

    l = np.random.randint(0,2)
    if l:
        t = theta_1 + np.random.uniform(0,epsilon)
    else:
        t = theta_0 + np.random.uniform(-epsilon,epsilon)
  
    phi = np.random.uniform(0,2*np.pi)

    b = complex(np.cos(phi),np.sin(phi))
    b *= complex(np.sin(t))
    a = complex(np.cos(t))
    vector = [a,b]

    x = np.sin(2*t)*np.cos(phi)
    y = np.sin(2*t)*np.sin(phi)
    z = np.cos(2*t)

    d.append((vector, l))
    d_bloch.append(([x,y,z],l))

for i in range(int(N/2)):

    t = np.random.uniform(theta_0,theta_1)
    
    phi = np.random.uniform(0,2*np.pi)
    
    b = complex(np.cos(phi),np.sin(phi))
    b *= complex(np.sin(t))
    a = complex(np.cos(t))
    vector = [a,b]

    x = np.sin(2*t)*np.cos(phi)
    y = np.sin(2*t)*np.sin(phi)
    z = np.cos(2*t)

    d_.append(vector)
    d__bloch.append([x,y,z])

with open('q_dataset.npy', 'wb') as f:
    np.save(f, np.array(d, dtype=object)  ,allow_pickle = True) 
    np.save(f, np.array(d_bloch,dtype=object)  ,allow_pickle = True) 
    np.save(f, np.array(d_,dtype=object) ,allow_pickle = True)  
    np.save(f, np.array(d__bloch,dtype=object)  ,allow_pickle = True) 

