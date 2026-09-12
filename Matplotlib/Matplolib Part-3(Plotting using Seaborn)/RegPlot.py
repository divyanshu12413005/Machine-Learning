import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')


# regplot  -> axes level function

# sns.regplot(
#     data=tips,
#     x='total_bill',
#     y='tip'
# )
# plt.show()


# lmplot  -> figure level function

# sns.lmplot(
#     data=tips,
#     x='total_bill',
#     y='tip',
#     hue='sex',
# )
# plt.show()


# resid plot  -> axes level function

sns.residplot(
    data=tips,
    x='total_bill',
    y='tip'
)
plt.show()