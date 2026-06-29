import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print(pd.options.display.max_rows) 
# PROBLEM 1
# Task 1
df = sns.load_dataset("iris")
print(df.head(5))
print(df.shape)
print(df.dtypes)

# Task 2

mean  = df.mean(axis=0, numeric_only=True)
print(f"Mean:\n{mean}\nMean.shape: {mean.shape}\n")

median = df.median(axis=0, numeric_only=True)
print(f"Median:\n{median}\nMedian.shape: {median.shape}\n")

mode = df.mode(axis=0, numeric_only=True)
print(f"Mode:\n{mode}\nMode.shape: {mode.shape}\n")

var = df.var(axis=0, numeric_only=True)
print(f"Variance:\n{var}\nVariance.shape: {var.shape}\n")

std = df.std(axis=0, numeric_only=True)
print(f"Standard Deviation:\n{std}\nStandard Deviation.shape: {std.shape}\n")

min  = df.min(axis=0, numeric_only=True)
print(f"Minimum:\n{min}\nMinimum.shape: {min.shape}\n")

max = df.max(axis=0, numeric_only=True)
print(f"Maximum:\n{max}\nMaximum.shape: {max.shape}\n")

q1 = df.quantile(0.25, axis=0, numeric_only=True)
q3 = df.quantile(0.75, axis=0, numeric_only=True)
iqr = q3 - q1
print("Quantile: ")
print(f"Q1:\n{q1}\nQ1.shape: {q1.shape}\n")
print(f"Q3:\n{q3}\nQ3.shape: {q3.shape}\n")
print(f"IQR:\n{iqr}\nIQR.shape: {iqr.shape}\n")

mean_species = df.groupby(["species"]).mean()
std_species = df.groupby(["species"]).std()
print(f"Median_species:\n{mean_species}\nMedian_species.shape: {mean_species.shape}\n")
print(f"Standard Deviation_species:\n{std_species}\nStandard Deviation.shape: {std_species.shape}\n")


# # PROBLEM 2:
# # Task 1
# fig, ax = plt.subplots(1, 4, figsize=(12, 6))
# label = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
# for i in range(4):
#     sns.histplot(data=df, x=label[i], kde=True, bins=22, ax=ax[i]) 
#     ax[i].set_title(f"{label[i]} distribution")
#     ax[i].set_xlabel(f"{label[i]} (cm)")

# fig, ax = plt.subplots(1, 2, figsize=(12, 6))
# for i in range(2):
#     sns.histplot(data=df, x=label[i+2], hue="species", kde=True, bins=22, ax=ax[i]) 
#     ax[i].set_title(f"{label[i+2]} distribution")
#     ax[i].set_xlabel(f"{label[i+2]} (cm)")

# #Task 2
# fig, ax = plt.subplots(1, 4, figsize=(12,6))
# for i in range(4):
#     sns.boxplot(data=df, y=label[i], hue="species", ax=ax[i])
#     ax[i].set_title(f"{label[i]} distribution")
#     ax[i].set_xlabel(f"{label[i]} (cm)")

# #Task 3
# mean_sepal_length = mean["sepal_width"]
# std_sepal_length = std["sepal_width"]
# x = np.linspace(
#     df["sepal_width"].min(),
#     df["sepal_width"].max(),
#     200
# )
# pdf = (
#     1 / (std_sepal_length * np.sqrt(2*np.pi))
#     * np.exp(-0.5 * ((x - mean_sepal_length) / std_sepal_length) ** 2)
# )
# fig = plt.figure(figsize=(10,5))
# sns.histplot(data=df, x="sepal_width", stat="density", bins=22)
# plt.plot(x, pdf, color="red", linewidth=2)

# # plt.tight_layout()
# # plt.show()


#PROBLEM 3
#Task 1
numeric_col = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
cov = df[numeric_col].cov()
corr = df[numeric_col].corr()
cov_matrix = cov.to_numpy()
corr_matrix = corr.to_numpy()
print(f"Covariance:\n{cov_matrix}\n")
print(f"Correlation:\n{corr_matrix}\n")

#Task 2
fig, ax = plt.subplots(figsize=(6, 4.8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues", vmin=-1, vmax=1, ax=ax)
ax.set_title("Numeric feature correlation")

#Task 3
sns.pairplot(
    df,
    vars=numeric_col,
    hue="species"
)
plt.show()