import pandas as pd

marks = {
    'maths': 90,
    'science': 85,
    'english': 95,
    'history': 80,
    'geography': 88
}

series = pd.Series(marks)

# Update maths marks
# series["maths"] = 95

# slicing and updating multiple values
series.loc["english":"geography"] = [100, 90, 95]

print(series)