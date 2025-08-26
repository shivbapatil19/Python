#!/usr/bin/env python
# coding: utf-8

# In[5]:


#finding number is even or odd through if_else statement
num=int(input("enter the number"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")


# In[7]:


#check the number is +ve or -ve
num=int(input("enter number"))
if num>0:
    print("the number is +ve")
else:
    print("the number is -ve")


# In[14]:


#to find the greater number from the following #note :- '&' wrong 'and' right
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>=b and a>=c:
    print(f"the {a} is greater")
elif b>=a and b>=c:
    print(f"the {b} is greater")
else:
    print(f"the {c} is greater")


# In[18]:


#find wheater the year is leaf or not
year=int(input("enter the year"))
if year % 400==0:
    print(f"the {year} is leaf")
else:
    print(f"the {year} is normal year")
    


# In[19]:


#convrsion of celcius to fehrenait
celcius = float(input("enter the tem in celcius"))
fahrenait = (celcius*9/5)+32
print(f"concersion of {celcius} in fahrenait {fahrenait}")


# In[21]:


#swaping of number using 3rd variable
a=input("enter number")
b=input("enter number")

temp = a
a = b
b = temp

print(f"after swapping a={a},b={b}")
#the value of a and b have change but we have done formating 


# In[24]:


# swaping of number using the pythonic method
a=input("enter number")
b=input("enter number")

a,b=b,a #pythonic way to swap

print(f"after swapping:a={a},b={b}")


# In[25]:


# classifying the traingle

a = int(input("Enter side A"))
b = int(input("Enter side B"))
c = int(input("Enter side C"))


if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("This is an Equilateral triangle.")
    elif a == b or b == c or a == c:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")
else:
    print("Invalid triangle: The sides do not form a triangle.")

