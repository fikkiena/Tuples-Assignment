#!/usr/bin/env python
# coding: utf-8

# Ada Task
# 
# You are the facilitator in the ADA program for 3 tracks of your choice, here is the list of your students in those three tracks, "['Amaka disappoint', 'Nedu japan', 'Pretty cynthia', 'Nedu japan', 'Pretty cynthia', 'Pretty cynthia']", "('jon doe', 'john doe', 'john doe', 'jon bellion', 'jon bellion', 'john bellcat', 'jon doe')", "{'ada ada', 'pyhon ezege', 'dog catcher', 'bitrus beetroot', 'doja cat', 'beja rat'}",
# Your first task
# Create a nested dictionary students with your chosen tracks, a names key is required for each track and choose any sequence above as the value for that names key. Kindly note that each sequence in your names keys should have unique values (i.e no duplicates) and must be of type list and this must be done programatically.
# Your second task,
# Using your imaginative powers as a data superhero, create a scores key of type, list in each track where the first index in the names key, corresponds with the first index in the scores key.
# Your third task,
# Print this desired result. The top students are: [studentName] with score of [score] for [track] track, [studentName] with score 

# First task Create a nested dictionary students with your chosen tracks, a names key is required for each track and choose any sequence above as the value for that names key

# In[1]:


Ada = {'Data':{'Amaka disappoint', 'Nedu japan', 'Pretty cynthia', 'Nedu japan', 'Pretty cynthia', 'Pretty cynthia'}, 'ProDesign' : {'jon doe', 'john doe', 'john doe', 'jon bellion', 'jon bellion', 'john bellcat', 'jon doe'}, 
       'ProMgt':{'ada ada', 'pyhon ezege', 'dog catcher', 'bitrus beetroot', 'doja cat', 'beja rat'}}


# In[2]:


print(Ada)


# Second task, Using your imaginative powers as a data superhero, create a scores key of type, list in each track where the first index in the names key, corresponds with the first index in the scores key

# In[3]:


Ada = {'data' :{'Amaka disappoint' : 84, 'Nedu japan' : 97, 'Pretty cynthia' :100}, 'ProDesign': {'jon bellion' : 69, 'john bellcat' : 85, 'john doe' : 90, 'jon doe' : 55},
       
       'ProMgt': {'doja cat': 45, 'bitrus beetroot' : 78, 'pyhon ezege' : 95, 'beja rat': 49, 'ada ada': 60, 'dog catcher' : 100}}


# In[4]:


print(Ada)


# Third task, Print this desired result. The top students are: [studentName] with score of [score] for [track] track, [studentName] with score

# In[7]:



print(Ada ['data']['Pretty cynthia'])
print(Ada ['ProDesign']['john doe'])  
print(Ada ['ProMgt']['dog catcher'])


# In[ ]:




