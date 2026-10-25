import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# categorical data

# countplot for survived column


# df['survived'].value_counts().sort_index().plot(kind='bar')
# print(df['survived'].value_counts().sort_index())

# plt.title("Titanic Survival Count")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.ylabel("Number of Passengers")
plt.show()




# pie chart for pclass column


# df['pclass'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()



# numerical data


# histogram for age column


# df['age'].plot(kind='hist', bins=20, edgecolor='black')
# plt.title("Age Distribution of Titanic Passengers")
# plt.xlabel("Age")
# plt.ylabel("Number of Passengers")
plt.show()


# distplot for fare column

# sns.distplot(df['fare'], kde=True, bins=20)
# plt.title("Fare Distribution of Titanic Passengers")
# plt.xlabel("Fare")
# plt.ylabel("Density")
plt.show()



# boxplot for fare column

sns.boxplot(x=df['fare'])
plt.title("Boxplot of Fare Distribution")
plt.xlabel("Fare")
plt.show()
