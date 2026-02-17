import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Price": [100000,120000,130000,150000,180000,
              200000,220000,250000,300000,500000],
    "City": ["Delhi","Mumbai","Delhi","Chennai","Mumbai",
             "Delhi","Chennai","Delhi","Mumbai","Delhi"]
}
df = pd.DataFrame(data)
plt.figure(figsize=(7,4))
sns.histplot(df["Price"], kde=True, bins=6)
plt.title("Price Distribution (Histogram + KDE)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
print("Skewness :", df["Price"].skew())
print("Kurtosis :", df["Price"].kurt())
plt.figure(figsize=(6,4))
sns.countplot(x="City", data=df)
plt.title("City Frequency Count")
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [800, 1000, 1200, 1500, 
                      1800, 2000, 2200, 2500],
    "Price": [120000, 150000, 170000, 210000,
               250000, 280000, 310000, 350000],
    "Location": ["City","City","Suburb","Suburb",
                 "City","Suburb","City","Suburb"]
}
df = pd.DataFrame(data)
plt.figure(figsize=(6,4))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("SquareFootage vs Price")
plt.show()
plt.figure(figsize=(6,4))
sns.boxplot(x="Location", y="Price", data=df)
plt.title("Location vs Price")
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [800, 1000, 1200, 1500,
                       1800, 2000, 2200, 2500],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 4, 5],
    "Bathrooms": [1, 2, 2, 2, 3, 3, 3, 4],
    "Price": [200000, 250000, 300000, 360000, 
              400000, 450000, 480000, 550000]
}
df = pd.DataFrame(data)
corr_matrix = df.corr()
print(corr_matrix)
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price")
plt.show()