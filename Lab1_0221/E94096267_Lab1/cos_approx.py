#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


rad = input("Enter rad: ")
rad = float(rad)
cos_val = 0.0
for n in range(0, 25, 2):
    if(n%4 == 0):
        cos_val += (rad**n) / math.factorial(n)
    else:
        cos_val -= (rad**n) / math.factorial(n)
print("cos(",rad,") approximation is ",cos_val)

