import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("finance.csv")

# Calculation
df["Profit"] = df["Revenue"] - df["Expense"]
df["Profit_Margin"] = (df["Profit"] / df["Revenue"]) * 100

# KPI
total_revenue = df["Revenue"].sum()
total_expense = df["Expense"].sum()
total_profit  = df["Profit" ].sum()

print("\n KEY MATRICS")
print("Total Revenue:",total_revenue)
print("Total Expense:",total_expense)
print("Total Profit: ", total_profit)

# Styling
sns.set_style("whitegrid")
sns.set_palette("Set2")

# 1. Revenue Trend (Line Plot)
plt.figure(figsize=(8,5))
sns.lineplot(x="Month",y="Revenue",data=df,marker='o',linewidth=3)
plt.title("Revenue Trend",fontsize=16)
plt.savefig("revenue_trend.png", dpi=600, bbox_inches="tight")
plt.clf()

# 2. Expense vs Profit (Bar Plor)
plt.figure(figsize=(8,5))
df.set_index("Month")[["Expense","Profit"]].plot(kind="bar")
plt.title("Expense vs Profit", fontsize=16)
plt.ylabel("Amount")
plt.savefig("profit_margin.png", dpi=600, bbox_inches="tight")
plt.clf()

# 3. Profit Margin (Line plot)

plt.figure(figsize=(8,5))
sns.lineplot(x="Month",y="Profit_Margin",data=df,marker='o')
plt.title("Profit Margin (%)",fontsize=16)
plt.savefig("expense_profit.png", dpi=600, bbox_inches="tight")
plt.clf()

# 4. Regression Plot (TREND)

plt.figure(figsize=(8,5))
sns.regplot(x=df.index,y="Revenue",data=df,scatter=True)
plt.title("Revenue Trend With Regression", fontsize=16)
plt.xlabel("Time Index")
plt.ylabel("Revenue")
plt.savefig("regression.png",dpi=600,bbox_inches="tight")
plt.clf()
print("\n All graph saved!")