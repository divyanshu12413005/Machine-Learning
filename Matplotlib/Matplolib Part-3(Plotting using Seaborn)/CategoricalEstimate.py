import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')


# bar plot  -> axes level function

# sns.barplot(
#     data=tips,
#     x='sex',
#     y='total_bill',
#     hue='day',
#     estimator=np.mean,
# )
# plt.title('Bar Plot of Total Bill by Sex')
# plt.show()



# pointplot  -> axes level function

# sns.pointplot(
#     data=tips,
#     x='sex',
#     y='total_bill',
#     hue='smoker',
# )
# plt.title('Point Plot of Total Bill by Sex')
# plt.show()



# countplot  -> axes level function

# sns.countplot(
#     data=tips,
#     x='sex',
#     hue='smoker',
# )
# plt.title('Count Plot of Total Bill by Sex')
# plt.show()


# faceting using catplot  -> figure level function

sns.catplot(
    data=tips,
    x='sex',
    y='total_bill',
    col='smoker',
    kind='bar',
    ci=None
)   
plt.title('Bar Plot of Total Bill by Sex')
plt.show()