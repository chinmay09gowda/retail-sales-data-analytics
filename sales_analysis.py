import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("superstore.csv", encoding="latin1")

data = data.dropna()
data = data.drop_duplicates()

data["Order Date"] = pd.to_datetime(data["Order Date"])

total_sales = data["Sales"].sum()

region_data = data.groupby("Region")["Sales"].sum()

plt.figure()
region_data.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

category_data = data.groupby("Category")["Sales"].sum()

plt.figure()
category_data.plot(kind="bar")
plt.title("Sales by Category")
plt.show()

data["Month"] = data["Order Date"].dt.month
month_data = data.groupby("Month")["Sales"].sum()

plt.figure()
month_data.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.show()