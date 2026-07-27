import numpy as np
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import expense


# simple example 

s=pd.Series(["2026-07-27", "2026-07-28", "2026-07-29"])
# print(s)

# print(pd.to_datetime(s))

# with error handling

t=pd.Series(["2026-07-27", "2026-07-28", "2026-70-290", "2026-07-30", "2026-07-31", "2026-08-01", "2026-08-02"])
# print(
#     pd.to_datetime(t, errors="coerce")
# )


expense["Date"]=pd.to_datetime(expense["Date"])
# print(expense["Date"])

# dt  accessor

# print(
#     expense["Date"].dt.year
# )


# plot graph

import matplotlib.pyplot as plt

# plt.plot(expense["Date"], expense["INR"])
# plt.show()


# day name wise bar chart/month wise bar chart

# plt.bar(expense["Date"].dt.day_name(), expense["INR"])
# plt.xlabel("Day of the Week")
# plt.ylabel("INR")
# plt.show()


plt.bar(expense["Date"].dt.month_name(), expense["INR"])
plt.xlabel("Month")
plt.ylabel("INR")
plt.show()