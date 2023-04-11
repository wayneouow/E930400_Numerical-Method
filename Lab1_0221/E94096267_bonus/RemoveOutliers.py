#!/usr/bin/env python
# coding: utf-8

# In[5]:


def remove_outliers(n):

    data = []
    outliers = []

    while(True):
        cmd = input("Enter a value (q or Q to quit): ")
        if(cmd == "q" or cmd == "Q"):
            print("The original data: ",data)
            break
        else:
            cmd = int(cmd)
            data.append(cmd)
            #print(data)

    data_sorted = sorted(data)
    #print(data_sorted)

#     for i in range(n):
#         outliers.append(data_sorted.pop(0))
#     for i in range(n):
#         outliers.append(data_sorted.pop())
    #outliers.extend(data_sorted[:n])
    outliers += data_sorted[:n]
    #outliers.extend(data_sorted[-n:])
    outliers += data_sorted[-n:]
    
    data_sorted = data_sorted[n : -n]
    
    print("The data with the outliers removed: ", data_sorted)
    print("The outliers: ", outliers)


# In[4]:


n = int(input("Enter the number of smallest and largest values to remove: "))


# In[6]:


remove_outliers(n)

