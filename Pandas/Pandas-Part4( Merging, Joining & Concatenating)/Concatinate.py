import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import courses, students,nov,dec,deliveries,ipl


print(courses)
# print(students)
# print(nov)
# print(dec)
# print(deliveries)
# print(ipl.shape)


#pd.concat
regs=pd.concat([nov,dec],axis=0,ignore_index=True)
# print(regs)

# multiIndex Datafarme
multi=pd.concat([nov,dec],keys=["Nov","Dec"])

# print(multi.loc["Nov",4])


