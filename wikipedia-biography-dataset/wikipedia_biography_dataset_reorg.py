
# coding: utf-8

# # Generate Train txt file for thunlp/TensorFlow-NRE from wikipedia-biography dataset

# In[1]:


# Checking Python Version 3+ 
import sys
print(sys.version)


# ## Link files
# 
# train.title -1-1-> train.box -1-1-> train.nb -[number]-1-> train.sent
# 
# 
# ## Resule Schema:
# title, non_na_box, accumulated_sent_context
# 
# ## Sample Training Data from thunlp/TensorFlow-NRE:
# #### Format: (fb_mid_e1, fb_mid_e2, e1_name, e2_name, relation, sentence)   
# 
# ### Sample:    
# 
# fb_mid_e1 - m.0ccvx   
# fb_mid_e2 - m.05gf08   
# e1_name   - queens   
# e2_name   - belle_harbor   
# relation  - /location/location/contains   
# sentence  - sen. charles e. schumer called on federal safety officials yesterday to reopen their investigation into the fatal crash of a passenger jet in belle_harbor , queens , because equipment failure , not pilot error , might have been the cause . ###END###   
# 

# In[1]:


# wikipedia biography training files
# substitute test and validate files
data_type = 'train' # test, valid
train_title_file = data_type + '/' + data_type + ".title"
train_nb_file    = data_type + '/' + data_type + ".nb"
train_sent_file  = data_type + '/' + data_type + ".sent"
train_box_file   = data_type + '/' + data_type + ".box"


# In[2]:


# add line indexer for the sent file
nbs_dict = {}
with open(train_sent_file) as sent:
    for line, content in enumerate(sent):
        nbs_dict[line] = content
    
nbs_dict.get(0)


# In[3]:


# remove words from a context string, i.e., -lrb-
useless_words_to_remove = ['-lrb-', '-rrb-', '.\n', '']

def cleanUpSentence(input_sent):
    keywords_to_remove = useless_words_to_remove
    querywords = input_sent.split()
    resultwords  = [word for word in querywords if word.lower() not in keywords_to_remove]
    result = ' '.join(resultwords)
    return result


# In[4]:


send_index = 0

sent_dict = {}

with open(train_nb_file) as nbs:
    accumulated_lines = 0
    for nb in nbs:
        current_lines_to_read = int(nb)
        
        current_accumulated_sent_context = ''
        
        for i in range(current_lines_to_read):
            line_to_read = accumulated_lines + i
            current_accumulated_sent_context += cleanUpSentence(nbs_dict.get(line_to_read))
        
        accumulated_lines += current_lines_to_read

        sent_dict[send_index] = current_accumulated_sent_context
        send_index += 1      


# In[5]:


sent_dict[1]


# ## Get top 100 most shown relationships

# In[6]:


import re
from collections import defaultdict


# In[7]:


relations_stat_dict = defaultdict(int)

with open(train_box_file) as boxes:
    for one_entry in boxes:
        
        all_target_attributes = re.split(r'\t+', one_entry)
        
        filtered_attrs = [attr for attr in all_target_attributes if '<none>' not in attr]
        
        for attr in filtered_attrs:
            if '_1:' in attr:
                attr_label = attr.split(':')[0][:-2]
                relations_stat_dict[attr_label] += 1


# In[9]:


sumVal = 0
for i in relations_stat_dict:
    value = relations_stat_dict[i]
    


# In[9]:


top_100_most_shown_relations = {} # relation_label, number_of_times_it_shown
sortedValues = sorted(relations_stat_dict.values(), reverse=True)
max_value = sortedValues[0]
onehundredth_value = sortedValues[99]
for attr_label in relations_stat_dict:
    attr_rep = relations_stat_dict[attr_label]
    if attr_rep >= onehundredth_value:
        top_100_most_shown_relations[attr_label] = attr_rep


# In[10]:


print(top_100_most_shown_relations)


# ## Generate the relation2id.txt file

# In[11]:


#### Remove the following relation labels for speeding up:
del top_100_most_shown_relations['clubs']
del top_100_most_shown_relations['years']
del top_100_most_shown_relations['image']
del top_100_most_shown_relations['name']


# In[12]:


if data_type == 'train':
    relation2idFile = open(data_type+'/relation2id.generate.txt', "w") 
    relation2idFile.write('NA 0\n')
    relationid = 1
    for relation in top_100_most_shown_relations:
        relation2idFile.write(relation+' '+str(relationid)+'\n')
        relationid += 1
    relation2idFile.close()


# ## Get the Concatenated Relation Labels:
# Current, the relation labels are splitted in the wikipedia biography dataset.  
# In order to adapt to NRE code, we have to concatenate all splitted labels into one single string with underscore in between.  

# In[13]:


real_relation_label_and_value_list = []

counter = 0

with open(train_box_file) as boxes:
    for one_entry in boxes:
        
        all_target_attributes = re.split(r'\t+', one_entry)
        filtered_attrs = [attr for attr in all_target_attributes if '<none>' not in attr]
        
        current_box_dict = {}
        for oneLabel in filtered_attrs:
            labelStringOnly = oneLabel.split(':')[0].split('_')[0]
            if labelStringOnly in top_100_most_shown_relations:
                currentValue = cleanUpSentence(oneLabel.split(':')[1])
                if labelStringOnly in current_box_dict:
                    current_box_dict[labelStringOnly] = current_box_dict[labelStringOnly] + '_' + currentValue
                else:
                    current_box_dict[labelStringOnly] = currentValue
               
        real_relation_label_and_value_list.append(current_box_dict)


# In[14]:


print(len(real_relation_label_and_value_list))
print(len(real_relation_label_and_value_list) == len(sent_dict))


# ## Generate the training data txt file:

# #### Read the titles into a list, in original order:

# In[15]:


title_list = []
with open(train_title_file) as titles:
    for title in titles:
        title_list.append(title[:-1])


# #### Verify that the three lists (title_list, sent_dict, and real_relation_label_and_value_list) start with index 0:

# In[16]:


title_list[0]


# In[17]:


sent_dict[0]


# In[18]:


for i in real_relation_label_and_value_list[0]:
    print(real_relation_label_and_value_list[0][i])


# #### Join three list by the biography title and write to text file:
# This is going to generate a 1+ GB large file

# In[19]:


resultFile = open(data_type+'/'+data_type+".generate.txt", "w") 

index = 0

for relationAndValueEntry in real_relation_label_and_value_list:
    for relationName in relationAndValueEntry:
        resultFile.write(title_list[index])
        resultFile.write('\t')
        resultFile.write(relationAndValueEntry[relationName])
        resultFile.write('\t')
        resultFile.write(relationName)
        resultFile.write('\t')
        resultFile.write(sent_dict[index])
        resultFile.write(' ###END###\n')
    index += 1

resultFile.close()


# ## Generate the relation2id.txt file

# In[ ]:





# In[ ]:




