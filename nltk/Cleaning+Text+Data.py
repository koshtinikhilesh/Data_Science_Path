
# coding: utf-8

# Inspired from the below blogs:-
# 
# https://www.theschool.ai/courses/data-lit/lessons/cleaning-text-data/
# 
# https://machinelearningmastery.com/clean-text-machine-learning-python/
# 
# 
# I will show you the use-case of nltk in the text processing along with the difference between the nltk processing and regex processing in Python.

# 
# Download the Datasets from the below link:--
# 
# http://www.gutenberg.org/cache/epub/5200/pg5200.txt
# 
# Remove the header and footer from the above text file and save it in your local computer as  "**metamorphosis_clean.txt**".
# 

# ## Read Content
# 

# Using the regex processing.

# In[1]:


filename = 'metamorphosis_clean.txt'


# In[2]:


textdata = open(filename, 'r')


# In[3]:


textdata


# In[4]:


text = textdata.read()


# In[5]:


text[:100]


# ## Splitting with spaces

# We will tokenize the above sentences in to the words using split.

# In[6]:


text_split = text.split()


# In[7]:


text_split[:100]


# ## Splitting with regex

# In[8]:


import re


# In[9]:


text_split_data = re.split(r'\W+',text)


# In[10]:


text_split_data[:100]


# ## Split using String module

# The above list contained the words like  'dream.'. SO, we will remove the puctuation from the above list.

# In[11]:


import string
string.punctuation


# In[12]:


text_update = [data.strip(string.punctuation) for data in text_split]


# In[13]:


text_update[:100]


# Also the above list contain the single character words, so we will replace those words.

# ## Remove the Capitalization

# In[14]:


filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words by white space
words = text.split()
# convert to lower case
words = [word.lower() for word in words]
print(words[:100])


# In[ ]:





# ## NLTK

# The Natural Language Toolkit, or NLTK for short, is a Python library written for working and modeling text.
# 
# It provides a high-level api to flexibly implement a variety of cleaning methods.

# ## Install nltk and its datasets
# 
# 

# In[15]:


# pip install -U nltk
# python -m  nltk.downloader all


# ## Tokenize

# In[16]:


import nltk


# In[17]:


# Read the datasets


# In[18]:


# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens[:100])


# 
# ## Tokenize based on word and sentences
# 

# In[19]:


from nltk.tokenize import word_tokenize


# In[20]:


word_tokenize(text)


# In[21]:


## Sentences tokenize


# In[22]:


from nltk import sent_tokenize


# In[23]:


sentences = sent_tokenize(text)


# ## Filter based on punctuation

# In[24]:


# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
print(words[:100])


# ## Filter based on stopwords

# In[25]:


from nltkl.corpus import stopwords
stop_words = stopwords.words('english')


# In[26]:


# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])


# ## FINISH

# In[ ]:




