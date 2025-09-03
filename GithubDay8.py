#!/usr/bin/env python
# coding: utf-8

# In[1]:


#printing 1 to 5 using the while
i = 1
while i <= 5:
    print(i)
    i += 1


# In[3]:


#5 to 1 reverse
n = 5
while n > 0:
    print(n)
    n -= 1


# In[4]:


#complex problems
password = ""
while password != "open123":
    password = input("Enter password: ")
print("Access Granted")


# In[5]:


#sum of first 10 inteegers
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)


# In[6]:


#multiplication tabler of 7
i = 1
while i <= 10:
    print("7 x", i, "=", 7 * i)
    i += 1

