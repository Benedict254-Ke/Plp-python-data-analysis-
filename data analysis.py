# Data Analysis and Visualization with Pandas & Matplotlib
# Author: Lulu B (Benedict Wambua)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------
# Task 1: Load and Explore the Dataset
# -------------------------
iris = load_iris(as_frame=True)
df = iris.frame
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

print("✅ Dataset loaded successfully!\n")

# Show first few rows
print("First 5 rows of the dataset:\n", df.head(), "\n")

# Dataset info
print("Dataset Info:")
print(df.info(), "\n")

# Missing values
print("Missing Values:\n", df.isnull().sum(), "\n")

# Clean dataset
df = df.dropna()

# -------------------------
# Task 2: Basic Data Analysis
# -------------------------
print("Basic Statistics:\n", df.describe(), "\n")

# Group by species
grouped = df.groupby("species").mean()
print("Mean values per species:\n", grouped, "\n")

print("Observation: Iris-setosa has smaller petal length than others.\n")

# -------------------------
# Task 3: Data Visualization
# -------------------------
sns.set(style="whitegrid")

# 1. Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Line Chart: Sepal Length over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="Set2")
plt.title("Bar Chart: Avg Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

print("✅ Analysis complete!")