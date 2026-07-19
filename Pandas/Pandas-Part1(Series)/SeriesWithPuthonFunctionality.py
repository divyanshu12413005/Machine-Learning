import pandas as pd
import numpy as np  

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import subs, kohli, bollywood

# len/type/dir/sorted/max/min

# print(len(kohli))  
# print(type(kohli))
# print(dir(kohli))
# print(sorted(subs))
# print(max(kohli))
# print(min(kohli))

# type conversion
# print(list(kohli))
# print(dict(kohli))


# membership operators
# print("Why Cheat India" in bollywood)     #it search for index 

# print("Alia Bhatt" in bollywood.values)  # it search for values
# print(bollywood)

# looping

# for movie in bollywood.head(10):
#     print(movie)


# /Arithmatic operators   (Broadcasting)

print(kohli)

# print(kohli + 10)  # add 10 to each value

# Relational operators

# print(kohli > 50)  # returns boolean series
# print(kohli[kohli > 50])  # returns series with values greater than 50






