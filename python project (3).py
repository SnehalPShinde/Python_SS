#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
page=requests.get("https://en.wikipedia.org/wiki/List_of_river_systems_by_length")


# In[2]:


soup=BeautifulSoup(page.content)
soup


# In[3]:


table1=soup.find_all("table",class_="wikitable")
table1


# In[4]:


all_data=[]
for i in table1:
    for j in i.find_all("td"):
        all_data.append(j.text.replace("\n",""))
all_data  


# In[5]:


river=all_data[0::7]
river


# In[6]:


lenghtKM=all_data[1::7]
lenghtKM


# In[7]:


lenghtM=all_data[2::7]
lenghtM


# In[8]:


area=all_data[3::7]
area


# In[9]:


avg=all_data[4::7]
avg


# In[10]:


outflow=all_data[5::7]
outflow


# In[11]:


countries=all_data[6::7]
countries


# In[12]:


import pandas as pd
Totalriver=pd.DataFrame({})
Totalriver["River"]=river
Totalriver["LenghtinKM"]=lenghtKM
Totalriver["Lenghtin Miles"]=lenghtM
Totalriver["Areaofriver"]=area
Totalriver["Average"]=avg
Totalriver["Outflow"]=outflow
Totalriver["Countries"]=countries
Totalriver


# In[13]:


Totalriver.to_csv("top river in world")


# In[14]:


get_ipython().system('pip install pymysql')
import pymysql as mycon


# In[15]:


con1=mycon.connect(host="localhost",user="root",database="python projectss",password="")
print("connected")


# In[16]:


mycursor=con1.cursor()
mycursor.execute("Create table if not exists river1(River varchar(50),LenghtinKM int,LenghtinMiles int,Areaofriver int,Average int,Outflow varchar(50),Countries varchar(50))")
print("SUCCESS")


# In[17]:


for i in range(len(river)):
    mycursor.execute("""insert into river1 values("%s","%s","%s","%s","%s","%s","%s")"""%(river[i],lenghtKM[i],lenghtM[i],area[i],avg[i],outflow[i],countries[i]))
    con1.commit()


# In[18]:


q="select * from river1"
mycursor.execute(q)


# In[19]:


al=mycursor.fetchall()


# In[20]:


al


# In[ ]:




