import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)   
incomes = np.random.lognormal(mean=10, sigma=1, size=1000) 
scores = 100 - np.random.beta(a=2, b=5, size=1000) * 100   
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})
def analyze_distribution(data, title):
    mean_val = np.mean(data)
    median_val = np.median(data)
    plt.figure(figsize=(7,4))
    sns.histplot(data, kde=True, bins=30, color="skyblue")
    plt.axvline(mean_val, color="red", linestyle="--", label=f"Mean = {mean_val:.2f}")
    plt.axvline(median_val, color="green", linestyle="-.", label=f"Median = {median_val:.2f}")
    plt.title(title)
    plt.legend()
    plt.show()
    print(f"{title}: Mean = {mean_val:.2f}, Median = {median_val:.2f}")
    if mean_val > median_val:
        print("Observation: Right-Skewed (Mean > Median)\n")
    elif mean_val < median_val:
        print("Observation: Left-Skewed (Mean < Median)\n")
    else:
        print("Observation: Symmetric (Mean ≈ Median)\n")
analyze_distribution(df["Heights"], "Human Heights (Normal)")
analyze_distribution(df["Incomes"], "Household Incomes (Right-Skewed)")
analyze_distribution(df["Scores"], "Test Scores (Left-Skewed)")


import pandas as pd
import numpy as np
data = {
    "values": [10, 12, 11, 13, 12, 14, 15, 100, 11, 12, 13, 14, 12, 13]
}
df = pd.DataFrame(data)
mu = df["values"].mean()
sigma = df["values"].std()
print(f"Mean (μ): {mu:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
df["z_score"] = (df["values"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]
print("\nDataset with z-scores:")
print(df)
print("\nOutliers (|Z| > 3):")
print(outliers)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
data = np.random.lognormal(mean=2, sigma=1.5, size=10000)
sample_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=30, replace=True)
    sample_means.append(np.mean(sample))
df = pd.DataFrame(sample_means, columns=["sample_mean"])
plt.figure(figsize=(8,5))
sns.histplot(df["sample_mean"],
         kde=True, bins=30, color="skyblue")
plt.title("Distribution of Sample Means" 
          "(Central Limit Theorem)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()