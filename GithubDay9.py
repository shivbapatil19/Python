#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Inverted Right-Aligned Triangle (Stars)
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)



# In[2]:


#Hollow Right-Angled Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()




# In[3]:


#hollow square in the form of the pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# In[4]:


#making the traingle using 01
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


# In[5]:


#make the trainglle using the increasing order for alphabets
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


# In[ ]:




