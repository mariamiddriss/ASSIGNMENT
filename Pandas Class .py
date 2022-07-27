#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


np.array([1,2,3,4])


# In[9]:


import pandas as pd


# In[11]:


pd.Series([10,20,30,40,50])


# In[12]:


s=pd.Series([10,20,30,40,50])


# In[13]:


type(s)


# In[14]:


s.axes


# In[15]:


s.dtype


# In[16]:


s.size


# In[17]:


s.ndim


# In[18]:


s.values


# In[22]:


s.head()


# In[23]:


s.head(3)


# In[20]:


s.head(2)


# In[30]:


import numpy as np


# In[36]:


mytail=np.array([8,9,7,10,14,2,8])


# In[37]:


mytail


# In[40]:


mytail = pd.Series(mytail)


# In[41]:


mytail


# In[34]:


s.tail(3)


# In[42]:


mytail.values


# In[43]:


mytail.tail()


# In[48]:


mytail.tail(3)


# In[50]:


pd.Series([13,10,20,5,53])


# In[55]:


pd.Series([13,10,20,5,53],index = [4,6,7,3,87])


# In[60]:


s=pd.Series([13,10,20,5,53],index =["first","second","third","fourth","fifth"])
s


# In[61]:


s["third"]


# In[62]:


s['fifth']


# In[63]:


ages =  {"Jonh": 42, "Julia": 53, "Dan": 21}


# In[64]:


ages


# In[65]:


pd.Series(ages)


# In[66]:


s1 = pd.Series([2,3,55,2,6,44])
s2 = pd.Series([421,325,3426,2,1,4,42])


# In[67]:


pd.concat([s1,s2])  #this is merging the two together


# In[68]:


s = pd.Series([13,214,210,440,53],index=["first","second","third","fourth","fifth"])
s


# In[69]:


s["first"]


# In[72]:


s.index


# In[71]:


s.keys


# In[70]:


list(s.items())


# In[73]:


s1 = pd.Series([2,3,55,2,6,44])
s1


# In[74]:


3 in s1


# In[75]:


34 in s1


# In[76]:


s1[[2,4]]


# In[77]:


s1= pd.Series([2,3,55,2,6,44])


# In[78]:


s1


# In[80]:


s1[2]


# In[81]:


s1[4]=4


# In[82]:


s1[4]


# In[83]:


pd.DataFrame({'Name': ['Mellon','Josh','Mary'], 'Age': [17,34,45], 'Location': ['Suame','Ash','Tafo']})


# In[84]:


dic = pd.DataFrame({'Name': ['Mellon','Josh','Mary'], 'Age': [17,34,45], 'Location': ['Suame','Ash','Tafo']})
dataframe = pd.DataFrame(dic)
dataframe


# In[86]:


dataframe["Age"]


# In[87]:


dataframe[["Age"]] #this is if you want it in a data frame i.e tabular form


# In[88]:


dataframe.Age


# In[89]:


# above are diff ways of calling a data


# In[90]:


l = [23,35423,25235,325,235,75]
df = pd.DataFrame(l,columns=["variable"])


# In[91]:


df


# In[92]:


names = ["John","Mike","Julia","Anastacia"]
df = pd.DataFrame(names,columns=["Names"])
df


# In[93]:


arr = np.array([5,6,7,3,3,1,2,42,5]).reshape(3,3,)
arr


# In[94]:


df = pd.DataFrame(data=arr,columns=["Variable_1","Variable_2","Variable_3"])
df


# In[95]:


df.axes


# In[96]:


df.shape


# In[97]:


df.ndim


# In[98]:


df.size


# In[99]:


df.values


# In[100]:


df.columns


# In[101]:


df.index


# In[ ]:




