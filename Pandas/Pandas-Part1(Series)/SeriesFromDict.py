import pandas as pd
import numpy as np




marks={
    'Maths':90,
    'Physics':80,
    'Chemistry':70,
    'Hindi':60,
    'English':50
}

print(marks)


print(pd.Series(marks,name='Student Marks'))        