#!/usr/bin/env python
# coding: utf-8

# In[3]:


# list of n numbers
my_list = [1,6,9,3,0,4,5,3,2,7,3,8,4]


# In[8]:


#the oracle

def the_oracle(my_input):
    winner = 8
    if my_input is winner:
        response = True
    else:
        response = False
    return response


# In[9]:


for index,trial_number in enumerate(my_list):
    if the_oracle(trial_number)is True:
        print('The correct number was found at index %i'%index)
        print('%i calls to the Oracle functtion were used'%(index +1))
        break


# In[12]:


from qiskit import*
import matplotlib.pyplot as plt
import numpy as np


# In[15]:


#define the oracle circuit
oracle = QuantumCircuit(2,name='oracle')
oracle.cz(0,1)
oracle.to_gate()
oracle.draw()


# In[17]:


backend = Aer.get_backend('statevector_simulator')
grover_circ = QuantumCircuit(2,2)
grover_circ.h([0,1])
grover_circ.append(oracle,[0,1])
grover_circ.draw()


# In[18]:


job = execute(grover_circ,backend)
result = job.result()


# In[20]:


sv = result.get_statevector()
np.round(sv)


# In[22]:


reflection = QuantumCircuit(2,name='reflection')
reflection.h([0,1])
reflection.z([0,1])
reflection.cz(0,1)
reflection.to_gate()


# In[34]:


reflection.draw()


# In[35]:


backend = Aer.get_backend('qasm_simulator')
grover_circ = QuantumCircuit(2,2)
grover_circ.h([0,1])
grover_circ.append(oracle,[0,1])
grover_circ.append(reflection,[0,1])
grover_circ.measure([0,1],[0,1])


# In[36]:


grover_circ.draw()


# In[37]:


job = execute(grover_circ,backend,shots=1)
result = job.result()
result.get_counts()


# In[ ]:




