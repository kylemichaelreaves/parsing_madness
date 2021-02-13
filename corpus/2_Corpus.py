#!/usr/bin/env python
# coding: utf-8

# # Corpus

# In[34]:


import nltk
import pandas as pd
import os
import numpy as np
import re
import string


# In[43]:


from string import punctuation


# In[89]:


os.getcwd()


# In[13]:


os.listdir('/Users/kylereaves/Documents/GitHub/parsing_madness')


# In[4]:


path = '/Users/kylereaves/Documents/GitHub/parsing_madness/corpus'


# In[5]:


os.chdir(path)


# In[14]:


os.listdir()


# In[7]:


os.getcwd()


# In[8]:


from protocols import protocols


# In[18]:


from nation_and_race import nation_and_race


# In[105]:


temp_corpus = [protocols, nation_and_race]


# In[31]:


sent_tokens = nltk.sent_tokenize(nation_and_race)


# In[38]:


word_tokens = [nltk.word_tokenize(tokens.lower()) for tokens in sent_tokens if tokens]


# In[81]:


cleaned_nation_sents = [re.sub(r'[^a-zA-Z\s]', '', sent.lower()) for sent in sent_tokens]


# In[93]:


protocols_sents = nltk.sent_tokenize(protocols)


# In[67]:


cleaned_protocols = [re.sub(r'[^a-zA-Z\s]', '', sent) for sent in protocols_sents]


# In[79]:


protocols_words = [nltk.word_tokenize(protocol) for protocol in cleaned_protocols]


# In[103]:


cleaned2x_protocols = [' '.join(clean.split()) for clean in cleaned_protocols]


# In[108]:


corpus = [cleaned2x_protocols, cleaned_nation_sents]


# In[132]:


corpus_df = pd.DataFrame(corpus).T


# In[143]:


corpus_df.rename(columns={'0': 'protocols', '1': 'nation_and_race'})


# In[147]:


corpus_df.rename(columns={0: 'protocols', 1: 'nation_and_race'})


# In[148]:


corpus_df.to_pickle('corpus.pickle')


# In[149]:


os.getcwd()


# In[83]:


[nltk.word_tokenize(sent) for sent in cleaned_nation_sents]


# In[ ]:




