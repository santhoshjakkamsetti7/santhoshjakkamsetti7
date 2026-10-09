
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a sample sales dataset
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone",
                "Headphones", "Tablet", "Laptop", "Phone", "Headphones"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics",
                 "Electronics", "Accessories", "Electronics", "Electronics",
                 "Electronics", "Accessories"],
    "Quantity": [2, 5, 3, 1, 4, 6, 2, 3, 2, 5],
    "Unit_Price": [50000, 15000, 20000, 50000, 15000,
                   2000, 20000, 50000, 15000, 2000]
}

df = pd.DataFrame(data)

# 2. Explore the original dataset
print("SALES DATASET")
print(df)

print("\nDataset Information:")
print(df.info())

# 3. Clean the dataset
df = df.drop_duplicates()
df = df.dropna()

# 4. Calculate revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# 5. Analyze sales
print("\nTOTAL REVENUE:")
print(df["Revenue"].sum())

print("\nTOTAL QUANTITY SOLD:")
print(df["Quantity"].sum())

print("\nREVENUE BY PRODUCT:")
product_sales = df.groupby("Product")["Revenue"].sum()
print(product_sales.sort_values(ascending=False))

print("\nREVENUE BY CATEGORY:")
category_sales = df.groupby("Category")["Revenue"].sum()
print(category_sales.sort_values(ascending=False))

# 6. Create a chart
product_sales.sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Product",
    xlabel="Product",
    ylabel="Revenue"
)

plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()
