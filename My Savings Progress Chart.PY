
# ============================================================
# PROJECT: SMART SAVINGS TRACKER
# Topic: Introduction to Matplotlib
# ============================================================

import matplotlib.pyplot as plt

# PART 1: PROJECT DATA
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

# Total savings accumulated by the end of each week (in rupees)
savings = [20, 45, 70, 110, 150]

# Savings target
goal = 200

# PART 2: CALCULATE IMPORTANT INFORMATION
total_savings = savings[-1]
average_savings = total_savings / len(weeks)
remaining = max(0, goal - total_savings)
progress = (total_savings / goal) * 100
best_week_index = savings.index(max(savings))
best_week = weeks[best_week_index]
best_amount = savings[best_week_index]

print("=" * 45)
print("       SMART SAVINGS TRACKER")
print("=" * 45)
print(f"Total savings       : Rs. {total_savings}")
print(f"Savings target      : Rs. {goal}")
print(f"Average per week    : Rs. {average_savings:.2f}")
print(f"Amount remaining    : Rs. {remaining}")
print(f"Goal completed     : {progress:.1f}%")
print(f"Highest total       : {best_week} - Rs. {best_amount}")

if total_savings >= goal:
    print("Status              : GOAL ACHIEVED!")
else:
    print("Status              : KEEP SAVING!")

print("=" * 45)

# PART 3: CREATE A DASHBOARD
fig, axes = plt.subplots(1, 2, figsize=(13, 6))

fig.suptitle(
    "SMART SAVINGS TRACKER",
    fontsize=18,
    fontweight="bold"
)

# PART 4: LINE GRAPH
ax1 = axes[0]

ax1.plot(
    weeks,
    savings,
    color="blue",
    marker="o",
    linestyle="solid",
    linewidth=3,
    markersize=8,
    label="Total Savings"
)

# Add a horizontal target line
ax1.axhline(
    y=goal,
    color="red",
    linestyle="dashed",
    linewidth=2,
    label=f"Savings Goal: Rs. {goal}"
)

# Show the amount at every point
for i, amount in enumerate(savings):
    ax1.annotate(
        f"Rs. {amount}",
        (weeks[i], amount),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center"
    )

ax1.set_title("Weekly Savings Progress")
ax1.set_xlabel("Week")
ax1.set_ylabel("Total Savings (Rs.)")
ax1.set_ylim(0, goal + 40)
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend()
ax1.tick_params(axis="x", rotation=20)

# PART 5: BAR CHART
ax2 = axes[1]

bars = ax2.bar(
    weeks,
    savings,
    color=["skyblue", "orange", "mediumseagreen",
           "mediumpurple", "gold"],
    label="Total Savings"
)

# Display values above each bar
ax2.bar_label(bars, fmt="Rs. %d", padding=4)

# Add the target line
ax2.axhline(
    y=goal,
    color="red",
    linestyle="dashed",
    linewidth=2,
    label=f"Savings Goal: Rs. {goal}"
)

ax2.set_title("Savings Comparison")
ax2.set_xlabel("Week")
ax2.set_ylabel("Total Savings (Rs.)")
ax2.set_ylim(0, goal + 40)
ax2.grid(axis="y", linestyle="--", alpha=0.5)
ax2.legend()
ax2.tick_params(axis="x", rotation=20)

# PART 6: ADD A SUMMARY BELOW THE CHARTS
summary = (
    f"Total: Rs. {total_savings}  |  "
    f"Average: Rs. {average_savings:.2f}  |  "
    f"Goal Progress: {progress:.1f}%  |  "
    f"Remaining: Rs. {remaining}"
)

fig.text(
    0.5,
    0.035,
    summary,
    ha="center",
    fontsize=10,
    fontweight="bold"
)

# Adjust spacing so everything fits
plt.tight_layout(rect=[0, 0.10, 1, 0.92])

# PART 7: SAVE AND DISPLAY THE DASHBOARD
plt.savefig(
    "Smart_Savings_Dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard saved as Smart_Savings_Dashboard.png")

plt.show()