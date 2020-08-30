#%%
from itertools import permutations, product



# %%
A =['a','b']
Z = ['x','z']

[p for p in product('ab', range(3))]
[p for p in product(A,Z)]
[p for p in product(A, repeat=3)]
# %%
msg = 'Good Morning Rosa!'
msgList = msg.split()
[' '.join(p) for p in permutations(msgList,3)]
# %%
# complex phrase
s = """Find textbooks with titles containing 'NLP',
    or 'natural' and 'language', or 
    'computational' and 'linguistics'."""

s_length  = len(set(s.split()))
import numpy as np
np.arange(1,s_length+1).prod()
# %%
