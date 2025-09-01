#!/usr/bin/env python
# coding: utf-8

# In[3]:


#program to reverse the number using the for loop
num=input("enter the number")
reverse=''
for char in num :
    reverse=char+reverse
print(f"the reverse of {num} is",reverse)
    


# In[12]:


#program to fing the prime number from 1 to 100
print("the prime number from 1 to 100 are")#bcz 1 is not an natural as it does not have +ve number from both side
for num in range(2,101):
    is_prime=True

    for i in range(2,int(num**0.5)+1):#to know whether the numbr has square root
        if num % i == 0:# to know wheater other number divisible by it
            is_prime=False
            break

    if is_prime:
        print(num,end=' ')




# In[14]:


#print the factorial of 9 usimg the for loop 1*2*3*4*5*6*7*8
num=9
fact=1

for i in range(1,num+1):
    fact *= i #starting from 1 it will stops at end 

print("the factorial of the number is",fact)


# In[16]:


#check wheather the number is prime or not
num=29
is_prime=True


for i in range(2,int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break

print(f"the number {num} is prime",is_prime)


# In[18]:


#check wheater 3 i prime or not
num = 3
is_prime=True

for i in range(2,int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break

print(f"the number {num} is prime",is_prime)


# In[20]:


#for loop program upto n number fibonasis series
n=int(input("enter the number"))

a,b=0,1 #single lineout to execute code
print("the fibonasis series")
for i in range(n):
    print(a,end=' ') #single lineout to execute code
    a, b = b , a+b
    


# In[21]:


#forloop program to find sum of the integer
num = 456
total = 0

for digit in str(num):
    total += int(digit)

print(f"Sum of digits in {num} is {total}")


# In[ ]:




