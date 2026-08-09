import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


tips=sns.load_dataset('tips')



# figure level -> displot
# axes level -> histplot,kdeplot,rugplot


# plotting univariate histogram
# sns.histplot(
#     data=tips,
#     x='total_bill'
# )
# plt.show()

# bins parameter

# sns.displot(
#     data=tips,
#     x='tip',
#     bins=20,
#     hue='sex',
# )
# plt.show()


titanic=sns.load_dataset('titanic')

# sns.displot(
#     data=titanic,
#     x='age',
#     element='step',
#     hue='sex',
# )
# plt.show()


# facetting using col and row -> not work on histplot, kdeplot, rugplot

# sns.displot(
#     data=titanic,
#     x='age',
#     col='sex'
# )
# plt.show()


# kdeplot -> kernel density estimation plot
# rather than discrete bins, kdeplot uses a continuous probability density curve to estimate the distribution of the data.

# sns.kdeplot(
#     data=tips,
#     x='total_bill',
#     hue='sex',
#     fill=True,
# )
# plt.show()



# rugplot -> rugplot is a simple visualization that displays individual data points along an axis. 
# It is often used in conjunction with other plots, such as histograms or kernel density estimation (KDE) plots, 
# to provide additional information about the distribution of the data.

# sns.rugplot(
#     data=tips,
#     x='total_bill'
# )
# sns.kdeplot(
#     data=tips,
#     x='tip'
# )
# plt.show()


# Bivariate histogram
# a bivariate histogram is a graphical representation of the joint distribution of two continuous variables.

# sns.histplot(
#     data=tips,
#     x='total_bill',
#     y='tip'
# )
# plt.show()


# Bivariate kdeplot
# in a bivariate KDE plot, the density is estimated in two dimensions, allowing us to visualize the joint distribution of the two variables.

sns.kdeplot(
    data=tips,
    x='total_bill',
    y='tip'
)
plt.show()