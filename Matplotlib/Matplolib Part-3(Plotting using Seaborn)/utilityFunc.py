import seaborn as sns


# get dataset names

print(sns.get_dataset_names())


# load dataset
penguins=sns.load_dataset('penguins')
print(penguins.head())