import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')


# box plot  -> axes level function


# plt.figure(figsize=(10, 6))
# sns.boxplot(x='sex', y='total_bill', data=tips)
# plt.title('Box Plot of Total Bill by Day')
# plt.show()


# using catplot  -> figure level function

# sns.catplot(
#     data=tips,
#     x='sex',
#     y='total_bill',
#     kind='box',
#     hue='day',
# )
# plt.show()


# single box plot  -> axes level function

sns.boxplot(
    data=tips,
    y='total_bill'
)
plt.title('Box Plot of Total Bill by Sex')
plt.show()