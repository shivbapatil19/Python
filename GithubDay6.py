#!/usr/bin/env python
# coding: utf-8

# In[1]:


#different type of pattern using for loop
*
**
***
****
*****
n=5 
#enter the number how much rows you want
for i in range (1,n+1):#n+1 bcz if later we want to increase the size not to change in code it will run manually
    print("*"*i)#i will increse one by one by multiplying


# In[7]:


"""print inverted right angle traingle
*****
****
***
**
*"""
n=5
for i in range(n,0,-1):#n=number we have given 0 as we have to stop on one star and -1 that is step
    print("*"*i)


# In[9]:


#print right angle traingle with numbers
"""1
   12
   123
   1234
   12345"""
n = 5 #their are 5 rows
for i in range(1, n + 1):#here i range is given for rows 
    for j in range(1, i + 1):#her j range is given for column so that they can increse one by one
        print(j, end="")#end will avoid new line until full row is printed
    print()#this print is their to move the condition next line


# In[22]:


"""star with space
    *
   **
  ***
 ****
***** """
n = 5
for i in range(1, n + 1):#this condition is for row
    print(" " * (n - i) + "*" * i)#using this condition we can create space 


# In[13]:


"""
A
AB
ABC
ABCD
ABCDE"""
n = 5
for i in range(1, n + 1):
    for j in range(65, 65 + i):#65 stands for the alphabets
        print(chr(j), end="")#this line is for character as compared to row
    print()#used to change the line


# In[ ]:




