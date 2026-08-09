import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

gap=px.data.gapminder()


# Heatmap ->axes level function

# plot rectangular data as a color-encoded matrix

temp_df=gap_pivot=gap.pivot_table(
    index='continent',
    columns='year',
    values='lifeExp'
)

# sns.heatmap(
#     data=temp_df,
#     annot=True,
#     fmt='.0f',
#     cmap='YlGnBu',
#     linewidths=0.5,
    
# )
# plt.show()



# clustermap -> figure level function
# it performs hierarchical clustering on both rows and columns of the data matrix, 
# and then reorders the rows and columns based on the clustering results. 
# This can help to reveal patterns and relationships in the data that may not be immediately apparent from a standard heatmap.

sns.clustermap(
    data=temp_df,
    annot=True,
    fmt='.0f',
    cmap='YlGnBu',
    linewidths=0.5
)
plt.show()