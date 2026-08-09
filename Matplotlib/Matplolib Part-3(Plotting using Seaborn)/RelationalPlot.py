import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips=sns.load_dataset('tips')

# scatter plot -> axes level function
# sns.scatterplot(
#     data=tips,
#     x='total_bill',
#     y='tip'
# )
# plt.show()


# relpot -> figure level function
# kind,hue,style,size
# sns.relplot(
#     data=tips,
#     x='total_bill',
#     y='tip',
#     kind='scatter',
#     hue='sex',
#     style='time',
#     size='size'
# )
# plt.show()    

# line plot

gap=px.data.gapminder()

# print(gap.head())


temp_df=gap[gap['country']=='India']

# axes level function
# sns.lineplot(
#     data=temp_df,
#     x='year',
#     y='lifeExp'
# )
# plt.show()

# using relplot
# sns.relplot(
#     data=temp_df,
#     x='year',
#     y='lifeExp',
#     kind='line'
# )
# plt.show()


# hue,style,size

temp_df=gap[gap['country'].isin(['India','China','Pakistan','United States','United Kingdom'])]

# sns.relplot(
#     data=temp_df,
#     x='year',
#     y='lifeExp',
#     kind='line',
#     hue='country',
#     style='continent'
# )
# plt.show()


# facet plot -> it will create multiple plots based on the column value
# sns.relplot(
#     data=temp_df,
#     x='year',
#     y='lifeExp',
#     kind='line',
#     hue='country',
#     style='continent',
#     col='continent'
# )
# plt.show()


# col_wrap -> it will create multiple plots based on the column value and wrap them into multiple rows
sns.relplot(
    data=temp_df,
    x='year',
    y='lifeExp',
    kind='line',
    hue='country',
    style='continent',
    col='continent',
    col_wrap=2
)
plt.show()
