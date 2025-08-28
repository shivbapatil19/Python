#!/usr/bin/env python
# coding: utf-8

# In[9]:


#print all the numbers divisible by 5 between 1 to 50
for i in range(1,51):
    if i % 5 == 0:
        print(i)


# In[11]:


#wheater the number are divisible by 7 between 1 to 140
for i in range(1,141):
    if i % 7 == 0:
        print(i)


# In[15]:


#count how many are even number between 1 to 20
count=0
for i in range(1,21):
    if i % 2 == 0:
        count+=1
print(count)


# In[21]:


#count how many number are divisible by 2 but not by 7 between 1 to 400
count=0
for i in range(1,401):
    if i % 2 == 0 and i % 7 != 0:
        count+=1
print(count)


# In[30]:


#print the sqaure of the numbers from 1 to 10
for i in range(1,11):
    print(i*i)


# In[57]:


evencount=0
oddcount=0
for i in range(1,21):
    if i % 2 == 0:
        evencount+=1
        print("even_number",i)
    else:
        oddcount+=1
        print("odd_number",i)
        
print("total number of even",evencount)
print("total number of odd",oddcount)


# In[52]:


# reverse number using for loop
num = input("enter the number you want to enter") #here the input will work like string
reverse='' #extra variable is created to store the value

for digit in num:#for every digit in taken num
    reverse = digit + reverse #it will store the value as like string
print("the reversed number is",reverse)



# In[62]:


#print the sum of all even number from 1 to 50
sum=0
for i in range(1,51):
    if i % 2 == 0:
        sum += i
print("total addition",sum)


# In[ ]:




