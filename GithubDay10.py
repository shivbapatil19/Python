#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Create a list of 7 city names."""

# Add one new city at the end.

city = ["latur","pune","solapur","mumbai","nagpur","sona"]
city.append("jaipur")
city


# In[5]:


##Insert a city at the 3rd position.
city.insert(2,"nagar")
city


# In[7]:


#Replace the last city with "Mumbai" 
city[-1] = "mumbai"
city


# In[10]:


"""Take a list of numbers [12, 45, 23, 67, 45, 89, 23, 12]."""

#Find the index of 89.

list = [12, 45, 23, 67, 45, 89, 23, 12]
list.index(89)


# In[12]:


#Remove the first occurrence of 23.
list.remove(23)
list


# In[13]:


#pop out the last element and print it
list.pop()
list


# In[15]:


"""Make a list marks = [67, 45, 89, 90, 45, 56]."""

marks = [67, 45, 89, 90, 45, 56]
marks.sort()
marks


# In[17]:


#Sort it in descending order.
marks.sort(reverse=True)
marks


# In[20]:


"""Find the sum of all marks."""
total=sum(marks)
print(total)


# In[21]:


#Copy a list and clear the original
nums = [10, 20, 30, 40, 50]

# make a copy
copy_nums = nums.copy()

# clear the original list
nums.clear()

print("Original list after clear:", nums)
print("Copied list still exists:", copy_nums)


# In[ ]:




