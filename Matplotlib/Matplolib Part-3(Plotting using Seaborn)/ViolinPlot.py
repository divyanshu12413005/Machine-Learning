import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')



# violin plot  -> axes level function

sns.violinplot(
    data=tips,
    x='sex',
    y='total_bill',
)
plt.title('Violin Plot of Total Bill by Sex')
plt.show()



# catplot  -> figure level function

# sns.catplot(
#     data=tips,
#     x='sex',
#     y='total_bill',
#     hue='day',
#     kind='violin'
# )
# plt.title('Violin Plot of Total Bill by Sex')
# plt.show()


