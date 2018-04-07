
# coding: utf-8

# In[31]:


import csv
with open('SanFran1.csv', 'w') as csvfile:
    writerobject = csv.writer(csvfile)
    with open('/Users/sreyamuppalla/Desktop/SanFran.csv', 'r', encoding = "ISO-8859-1") as csvfile2:
        spamreader = csv.reader(csvfile2)
        for row in spamreader:
            if row[11] != "":
                writerobject.writerow(row)


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords


# In[2]:


#reads the csv file
get_ipython().system('head -500 /Users/sreyamuppalla/Desktop/SanFran.csv ')


# In[10]:


df = pd.read_csv("/Users/sreyamuppalla/Desktop/SanFran.csv", engine='python')


# In[57]:


wordList = ['storage', 'equipment', 'utensil', 'floor', 'ceiling', 'license', 'handwashing', 'facilities', 'water', 
           'temperature', 'surface', 'food', 'contamination', 'cooling', 'hand', 'vermin', 'infestation']
def words(description):
    for word in description.split(' '):
        if word in wordList:
            ind = wordList.index(word)
            if ind <= 5:
                num = 0;
            elif ind >=11:
                num = 1;
            else:
                num = 2;
        '''
        for word1 in wordList:
            if(word == word1):
                if word1[n] <= 5:
                    num = 0;
                elif word1[n] >=11:
                    num = 1;
                else:
                    num = 2;
        '''
    return num

def clustering():
    dataset = []
    with open('SanFran1.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            feature_vector = []
            label = row[15]
            f1 = row[11]
            f2 = words(str(row[14]))
            feature_vector.append(label)
            feature_vector.append(f1)
            feature_vector.append(f2)
            
            dataset.append(feature_vector)  
            return dataset


# In[58]:


words("Inadequate and inaccessible handwashing facilities")


# In[61]:


from sklearn.cluster import KMeans
import numpy as np
X = np.array(clustering())
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
kmeans.labels_

kmeans.predict([90, ["Unclean Hands"]])

kmeans.cluster_centers_

