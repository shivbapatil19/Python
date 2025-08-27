#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for loop basic program
for i in range(1,6):
    #here i the variable created in the loop and 1 to 6-1 is the range
    print(i)


# In[5]:


#Program to print hello world for 3 times
for i in range(1,4):
    # it will range from 1 to 3 and at the end the msg will be texted
    print(i,"hello world")


# In[12]:


#program to print table of 2
for i in range(2,11,2):
    #here the range is added of 2 that exactly is step
    print(i)


# In[16]:


#program to print 1 to 5 in reverse
for i in range (5,0,-1):
    #the program will start from 5 and it will be end 1 so 0 is taken and -1 for minimizing the step
    print(i)


# In[19]:


#program to square of the number from 1 to 5
for i in range(1,6):
    print(f"the square of {i} is {i*i}")
    here the formating is done as it will automatically pick the values of i


# In[20]:


#program to print the cube of number from 5 to 1 in the reverse order
for i in range(5,0,-1):
    print(f"the square of {i} is {i*i*i}")


# In[32]:


#program to print the sum of the first 5 naturall number'
#we have to create the extra one variable to keep addition of the number
total=0
for i in range(1,6,1):
    total+=i
    #formula will work as total = total + i
print(total)#removing print outside the loop will help to gives totall


# In[30]:


#program to calculate the sum of the number which are in the reverse starting 6
total=0
for i in range(6,0,-1):
    total+=i
    print(total) #want to show steps i wrote print in the loop


# In[ ]:


"""the difference between both the program is that
 in 1st program print will  run one time
 in seconf program print will run step by as it is inside the loop"""


# In[35]:


#print the multiplication table of the 3
for i in range(3,31,3):
    print(f"{i}")


# In[39]:


#printing the table of 3 in the classical method
for i in range(1,11):
    print(f" 3 * {i} = {3*i}")
    #3 * {i} step is created {3*i} formula is created


# In[ ]:




