import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from function import df

gender = df.gender.value_counts()
gender.rename(index={0:'Female', 1:'Male'}, inplace=True)
colors = sns.color_palette("bright")
plt.pie(gender, labels=gender.index, colors=colors, autopct="%0.0f%%")
plt.show()