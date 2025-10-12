# ### How to add modules in python:--

# Approach 1:--
import fact as f
f.fact1()

# Approach 2:--
from fact import fact1
fact1()

# Approach 3:-- 
from fact import fact1 as dogs
from fact2 import fact1 as cats
dogs()
cats()

