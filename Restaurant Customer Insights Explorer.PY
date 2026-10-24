# ============================================================
# 🍽️ RESTAURANT CUSTOMER INSIGHTS EXPLORER
# Advanced Visualizations in Python using Seaborn & Matplotlib
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------------------------------------------
# PART 1: LOAD AND EXPLORE THE DATA
# ------------------------------------------------------------

sns.set_theme(style="darkgrid", palette="viridis")

df = sns.load_dataset("tips")
df = df.dropna()

print("=" * 60)
print("🍽️ RESTAURANT CUSTOMER INSIGHTS EXPLORER")
print("=" * 60)

print("\n📋 First 5 Customer Records:")
print(df.head())

print("\n📊 Dataset Information:")
df.info()

print("\n💰 Restaurant Statistics:")
print(f"Total Customers/Transactions: {len(df)}")
print(f"Total Sales: ${df['total_bill'].sum():.2f}")
print(f"Average Bill: ${df['total_bill'].mean():.2f}")
print(f"Average Tip: ${df['tip'].mean():.2f}")
print(f"Largest Bill: ${df['total_bill'].max():.2f}")
print(f"Average Party Size: {df['size'].mean():.2f}")

print("\n📅 Busiest Day:")
print(df["day"].value_counts().idxmax())

print("\n💳 Best Average Tip Day:")
print(df.groupby("day")["tip"].mean().idxmax())

# ------------------------------------------------------------
# PART 2: DAILY SALES DASHBOARD
# ------------------------------------------------------------

daily_sales = df.groupby("day", observed=False)["total_bill"].sum()

plt.figure(figsize=(10, 5))
sns.barplot(x=daily_sales.index, y=daily_sales.values)

plt.title("💰 Total Restaurant Sales by Day", fontsize=16)
plt.xlabel("Day of the Week")
plt.ylabel("Total Sales ($)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 3: CUSTOMER COUNT BY DAY AND GENDER
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="day", hue="sex")

plt.title("👥 Customer Distribution by Day and Gender", fontsize=16)
plt.xlabel("Day of the Week")
plt.ylabel("Number of Records")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 4: BILL DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))
sns.histplot(
    data=df,
    x="total_bill",
    bins=20,
    kde=True,
    color="teal"
)

plt.title("🧾 Distribution of Restaurant Bills", fontsize=16)
plt.xlabel("Total Bill ($)")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 5: BILL VS TIP — SCATTER PLOT
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="day",
    size="size",
    sizes=(40, 250),
    alpha=0.8
)

plt.title("💵 How Bills Relate to Tips", fontsize=16)
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 6: WEEKEND VS WEEKDAY SALES
# ------------------------------------------------------------

df["day_type"] = df["day"].apply(
    lambda day: "Weekend" if day in ["Sat", "Sun"] else "Weekday"
)

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="day_type", y="total_bill")

plt.title("📦 Weekday vs Weekend Bill Comparison", fontsize=16)
plt.xlabel("Day Type")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 7: TIP PERCENTAGE ANALYSIS
# ------------------------------------------------------------

df["tip_percentage"] = (df["tip"] / df["total_bill"]) * 100

plt.figure(figsize=(10, 5))
sns.histplot(
    data=df,
    x="tip_percentage",
    bins=20,
    kde=True,
    color="orange"
)

plt.title("⭐ Customer Tip Percentage Distribution", fontsize=16)
plt.xlabel("Tip as Percentage of Bill (%)")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 8: PARTY SIZE ANALYSIS
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))
sns.barplot(
    data=df,
    x="size",
    y="total_bill",
    errorbar=None
)

plt.title("👨‍👩‍👧‍👦 Average Bill by Party Size", fontsize=16)
plt.xlabel("Number of People")
plt.ylabel("Average Bill ($)")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 9: CORRELATION HEATMAP
# ------------------------------------------------------------

numeric_df = df[
    ["total_bill", "tip", "size", "tip_percentage"]
]

plt.figure(figsize=(9, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("🔥 Customer Data Correlation Heatmap", fontsize=16)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# PART 10: PAIR PLOT
# ------------------------------------------------------------

sns.pairplot(
    df[["total_bill", "tip", "size", "tip_percentage"]],
    diag_kind="hist"
)

plt.suptitle(
    "🔍 Customer Behaviour — Pair Plot",
    y=1.02,
    fontsize=16
)
plt.show()

# ------------------------------------------------------------
# PART 11: BILL VS TIP WITH TREND LINE
# ------------------------------------------------------------

sns.lmplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    height=6,
    aspect=1.3
)

plt.title("📈 Bill and Tip Relationship by Gender")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# ------------------------------------------------------------
# PART 12: CUSTOMER INSIGHTS REPORT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("🏆 RESTAURANT CUSTOMER INSIGHTS REPORT")
print("=" * 60)

print(f"\n1. Total Sales: ${df['total_bill'].sum():.2f}")

print(
    f"2. Average Customer Bill: "
    f"${df['total_bill'].mean():.2f}"
)

print(
    f"3. Average Tip: "
    f"${df['tip'].mean():.2f}"
)

print(
    f"4. Most Frequently Recorded Day: "
    f"{df['day'].value_counts().idxmax()}"
)

print(
    f"5. Highest Average Bill Day: "
    f"{df.groupby('day', observed=False)['total_bill'].mean().idxmax()}"
)

print(
    f"6. Highest Average Tip Day: "
    f"{df.groupby('day', observed=False)['tip'].mean().idxmax()}"
)

print(
    f"7. Average Tip Percentage: "
    f"{df['tip_percentage'].mean():.2f}%"
)

print(
    f"8. Most Common Party Size: "
    f"{df['size'].mode().iloc[0]} people"
)

print(
    f"9. Largest Recorded Bill: "
    f"${df['total_bill'].max():.2f}"
)

print(
    f"10. Average Party Size: "
    f"{df['size'].mean():.2f} people"
)

print("\n✅ Analysis completed successfully!")
print("📊 All visualizations have been generated.")
print("=" * 60)