#%% 
import re


#%%
r = r"[^a-z]*([y]o|[h']?ello)?"
re_greeting = re.compile(r,flags=re.IGNORECASE)
re_match = re_greeting.match(input())
print(re_match)
# %%

# %%
