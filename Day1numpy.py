#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numpy stands for the numerical pyhthon it is the library used to calculate the highl
#high speed
#numpy is the back end of the another libraries like matplot lib and pandas
#their is only one type of data abstration in numpy numpy nd array and numpy n dimensional
#array


# In[5]:


import numpy as np
np.__version__
#numpy version greater than 2 are higly unstable they are high compactablity for other issue
#and functions


# In[18]:


arr1 = np.array(10)
arr2 = np.array([1,2,3,4,5,6,7,8,9])
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[9]:


print(arr1, type(arr1),arr1.shape,arr1.ndim,arr1.dtype,arr1.size)


# In[10]:


print(arr2,type(arr2),arr2.shape,arr2.ndim,arr2.dtype,arr2.size)


# In[11]:


print(arr3,type(arr3),arr3.size,arr3.shape,arr3.dtype,arr3.ndim)


# In[21]:


arr4 = ([[1,2,3],[1,8,3],[1,9,3]])
print(arr3)


# In[22]:


print(arr4)


# In[25]:


#creation of the numpy array for the set 
import numpy as np
arr1=({10,20,30,40})
print(arr1)


# In[28]:


import numpy as np
arr1=({10,20,30,40})
print(arr1),
print(type(arr1)),
print(arr1.size)
print(arr1.shape)
print(arr1.dtype)
print(arr1.ndim)


# In[29]:


import numpy as np

arr1 = np.array(list({10,20,30,40}))  # convert set → list → NumPy array
print(arr1)
print("Type:", type(arr1))
print("Size:", arr1.size)
print("Shape:", arr1.shape)
print("Dtype:", arr1.dtype)
print("Ndim:", arr1.ndim)


# In[32]:


import numpy as np
arr2 = np.array(list[{10,20,30},{22,44,55},{23,45,66}])
print(arr2)
print(type(arr2))
print(arr2.shape)
print(arr2.size)
print(arr2.dtype)
print(arr2.ndim)


# In[34]:


import numpy as np
dic1 = np.array(list[{10:3},{30:3},{40:4}])
print(dic1)


# In[35]:


print(dic1)


# In[36]:


print(type(dic1))
print(dic1.shape)
print(dic1.size)
print(dic1.dtype)
print(dic1.ndim)


# In[39]:


#Reshape function
arr2 = np.array([1,2,3,4,5,6,7,8])
arr4 = arr2.reshape(2,4)
print(arr4) 


# In[45]:


arr5 = arr2.reshape(4,2)
print(arr5)


# In[47]:


arr6 = arr2.reshape(8,1)
print(arr6)


# In[ ]:


#array can only reshape the activity if they are in sequence

