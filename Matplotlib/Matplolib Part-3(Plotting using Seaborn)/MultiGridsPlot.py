import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset('tips')
iris=sns.load_dataset('iris')


# facetgrid  -> figure level function

# g=sns.FacetGrid(
#     data=tips,
#     col='day',
#     row='time'
# )
# g.map(
#     sns.boxplot,'sex','total_bill',
  
# )

# plt.show()


# pairplot  -> figure level function

# sns.pairplot(
#     data=iris,
#     hue='species'
# )
# plt.show()


# pairgrid  -> figure level function

# g=sns.PairGrid(
#     data=iris,
#     hue='species'
# )
# g.map_upper(sns.scatterplot)
# g.map_lower(sns.kdeplot)
# plt.show()


# jointplot  -> figure level function

# sns.jointplot(
#     data=tips,
#     x='total_bill',
#     y='tip'
# )
# plt.show()



# jointgrid  -> figure level function

g=sns.JointGrid(
    data=tips,
    x='total_bill',
    y='tip'
)
g.plot(sns.scatterplot,sns.violinplot)
plt.show()