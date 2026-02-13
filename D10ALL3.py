OrderID,CustomerName,Product,Quantity,Price
101,John Doe,Laptop,1,1200
102,Jane Smith,Phone,2,800
,Michael Lee,Tablet,1,600
104,Sarah Kim,Laptop,1,1200
105,David Park,Phone,3,800
102,Jane Smith,Phone,2,800
,Michael Lee,Tablet,1,600
106,Alice Wong,Headphones,2,200
107,Bob Brown,Monitor,1,300
104,Sarah Kim,Laptop,1,1200
import pandas as pd
df = pd.read_csv("customer_ordersD10T1.csv")
print("Initial shape:", df.shape)
print("\nMissing values report:\n", df.isna().sum())
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)   
df = df.drop_duplicates()
print("\nFinal shape after cleaning:", df.shape)


import pandas as pd
data = {
    "Price": ["$120", "$250", "$180", "$300"],
    "Date": ["2026-01-01", "2026-01-05", "2026-01-10", "2026-01-15"]
}
df = pd.DataFrame(data)
print(df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
print(df.dtypes)
print(df["Price"].mean())
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)


import pandas as pd
df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles "]
})
df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()
print("Unique values after cleaning:\n", df["Location"].unique())