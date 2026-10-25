import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic= sns.load_dataset("titanic")
tips= sns.load_dataset("tips")
flight= sns.load_dataset("flights")
iris= sns.load_dataset("iris")


# scatter plot numerical-numerical data [tips dataset]
sns.scatterplot(x=tips['total_bill'], y=tips['tip'],hue=tips['sex'])
plt.title("Scatter Plot of Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# bar plot categorical-numerical data  [titanic dataset]

sns.barplot(x=titanic['class'], y=titanic['fare'], hue=titanic['sex'])
plt.title("Bar Plot of Fare by Class and Sex")
plt.xlabel("Class")
plt.ylabel("Fare")
plt.show()

# box plot numerical-categorical data [tips dataset]
sns.boxplot(x=tips['day'], y=tips['total_bill'], hue=tips['sex'])
plt.title("Box Plot of Total Bill by Day and Sex")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# displot numerical-categorical data [titanic dataset]
sns.displot(data=titanic, x='age', hue='survived', multiple='dodge')
plt.title("Distribution of Age by Survival")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# heatmap categorical-categorical data [iris dataset]

# Correlation heatmap
sns.heatmap(
    iris.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Heatmap of Correlation Matrix for Iris Dataset")
plt.show()



# clustermap categorical-categorical data [flight dataset]
flight_pivot = flight.pivot(index="month", columns="year", values="passengers")

sns.clustermap(
    flight_pivot,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    figsize=(12, 8)
)

plt.show()


# pairplot numerical-numerical data [iris dataset]
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()


# lineplot numerical-numerical data [flight dataset]
sns.lineplot(data=flight, x="year", y="passengers", hue="month", marker="o")
plt.title("Line Plot of Passengers Over Years by Month")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
