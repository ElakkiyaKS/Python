import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
train_df = pd.read_csv("Red Wine Quality.csv")
plt.figure(figsize=(15,15))
sns.heatmap(train_df.corr(),color = "k", annot=True)
plt.show()
