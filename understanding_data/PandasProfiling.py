import seaborn as sns
from ydata_profiling import ProfileReport

df = sns.load_dataset("titanic")

profile = ProfileReport(df, title="Titanic Report")

profile.to_file("titanic_report.html")

print("Report generated!")