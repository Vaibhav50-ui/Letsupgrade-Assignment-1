#!/usr/bin/env python
# coding: utf-8

# # Basic Assignment
# Data types

# ## List

# In[8]:


lst=[1,2,3,4,5,6,7,8,80.25,45.63,45.52,"python","letsupgrade","jupyter","github","python","python"]
print(lst)


# In[42]:


lst.count("python")


# In[43]:


lst=[1,2,3,4,5,6,7,8,80.25,45.63,45.52,"python","letsupgrade","jupyter","github","python","python"]
lst.remove(7)
print(lst)


# In[44]:


lst=[1,2,3,4,5,6,7,8,80.25,45.63,45.52,"python","letsupgrade","jupyter","github","python","python"]
lst.append("HTML")
print(lst)


# In[47]:


lst=[1,2,3,4,5,6,7,8,80.25,45.63,45.52,"python","letsupgrade","jupyter","github","python","python"]
lst.reverse()
print(lst)


# In[31]:


lst=[1,2,3,4,5,6,7,8,80.25,45.63,45.52,"python","letsupgrade","jupyter","github","python","python"]
lst.index("jupyter")


# In[ ]:





# # Dictionary

# In[48]:


dct={"one":"python",2: "java", 3:"HTML","four":"c++",5:"css"}
print(dct)


# In[49]:


dct.items()


# In[50]:


dct.get(3)


# In[58]:


dct={"one":"python",2: "java", 3:"HTML","four":"c++",5:"css"}
dct.pop("one")
print(dct)


# In[62]:


dct.update({"six":"hacking"})
print(dct)


# In[63]:


dct.keys()


# In[ ]:





# # Tuple

# In[64]:


tup=("goat","cow","cat","dog","cow","cow",2,3,6,4,8,9)
print(tup)


# In[68]:


tup.count("cow")


# In[70]:


tup.index(2)


# In[ ]:





# # Sets

# In[75]:


st={1,2,3,4,5,6,7,8,8,4,5,6,3,45.52,"python","letsupgrade","jupyter","github","python","python"}
print(st)


# In[76]:


st.add("monkey")
print(st)


# In[88]:


st.difference()


# In[90]:


st.union()


# In[89]:


st.clear()
print(st)


# In[ ]:





# # String

# In[107]:


name="Pranal"

print(name[2])
print(len(name))
print(name.upper())
print(name.split())
print(name.find("a"))
print(name[::2])
print(name.partition("a"))


# In[ ]:





# In[ ]:




