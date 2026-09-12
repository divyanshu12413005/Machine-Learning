import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')



# Strip plot  -> axes level function

# sns.stripplot(
#     data=tips,
#     x='day',
#     y='total_bill',
#     hue='sex',
#     jitter=True,
#     dodge=True
# )



# using catplot  -> figure level function

# sns.catplot(
#     data=tips,
#     x='day',
#     y='total_bill',
#     hue='sex',
#     kind='strip',
#     jitter=True,
#     dodge=True
# )
# plt.show()


# swarm plot  -> axes level function

sns.swarmplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='sex',
    dodge=True
)
plt.show()
