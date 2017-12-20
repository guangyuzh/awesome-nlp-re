# Relation Extraction for Knowledge Graph
Ongoing Paper Writing: Overleaf link: https://www.overleaf.com/read/jtbgxkxckwbt


### - Distant Supervision
**Paper Name:** [Distant Supervision for Relation Extraction beyond the Sentence Boundary](https://arxiv.org/pdf/1609.04873.pdf)  

### - PCNN with Selective Attention
**Paper Name:** Neural Reltaion Extraction with Selective Attention over Instances    

### - Reinforcement Learning
**Paper Name:** DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning       
**Source Code:** https://github.com/xwhan/DeepPath   

### Graphical Model Approach:
**Paper Name:** Jointly Identifying Entities and Extracting Relations in Encyclopedia Text via A Graphical Model Approach   
**Link:**   
**Source Code:**    
We extract relationships between principal entity and secondary entities in the format of <Article, Principal_E, Secondary_E, UnaryPotential>.   
The relationships which has the same Principal_E groups as a cluster of relationships of a person's biography; for example, Donald J. Trump. All relationships between Donald J. Trump will be used to train in a graphical model for one run. For example: The graphical model needs to build up recognition on a global constraint between relationships of <isPresidentOfUSA>, <assumedOfficeDate>, <precededBy>, <politicalParty>, <netWorth>, etc. The graphical model should understand that any biased relationship such as <isAFemale> is very unlikely to be part of this relationship appearance (because there has been no woman in US president-ship). The model should be trained to correct the label or eliminate bias.    

### Other Notes and Materials:
https://zhuanlan.zhihu.com/p/22683996  

### - Word Embedding
- [GloVe](https://nlp.stanford.edu/projects/glove/)
    
    Pretrained: Wikipedia 2014 + Gigaword 5 (6B tokens, 400K vocab, uncased, 50d)
    
- https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/  

### Dataset:
**Wikipedia Biography Dataset:** https://github.com/DavidGrangier/wikipedia-biography-dataset

### Addressed Open Improvement:
1. Current attention mechanism uses the relative positions of the two entities in a sentence. If an entity is not or partially not appeared in the sentence, then current attention mechanism excludes such data entry. 
2. Current attention mechanism looks at the word itself along with relative position index in a sentence, all based on word embedding of the entities and the sentence. However, it does not consider the Part-Of-Speech Tag. **In addition to the current available vector representations, we can add POS Tag to each entity and sentence.**
