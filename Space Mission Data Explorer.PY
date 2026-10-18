
# ============================================================
# 🚀 SPACE MISSION DATA EXPLORER
# Python + Pandas + Seaborn + Matplotlib
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ------------------------------------------------------------
# PART 1: PROJECT SETTINGS
# ------------------------------------------------------------

print("=" * 60)
print("       SPACE MISSION DATA EXPLORER 🚀")
print("=" * 60)

print("\nLoading planetary discovery data...")

# Load the built-in planets dataset
df = sns.load_dataset("planets")

# Keep rows containing the information needed for our analysis
df = df.dropna(
    subset=["orbital_period", "distance", "method"]
).copy()

# Remove invalid values for logarithmic visualizations
df = df[
    (df["orbital_period"] > 0) &
    (df["distance"] > 0)
].copy()

print("Dataset loaded successfully!")
print("Number of usable records:", len(df))
print("Number of columns:", len(df.columns))

# ------------------------------------------------------------
# PART 2: MAIN MENU
# ------------------------------------------------------------

while True:

    print("\n" + "=" * 60)
    print("             MISSION CONTROL")
    print("=" * 60)

    print("1. View dataset information")
    print("2. Explore planetary statistics")
    print("3. Analyse discovery methods")
    print("4. View orbital period histogram")
    print("5. View planet distance KDE plot")
    print("6. View distance vs orbital period")
    print("7. View correlation heatmap")
    print("8. Open complete visual dashboard")
    print("9. Save analysis report")
    print("0. Exit Mission Control")

    choice = input("\nEnter your choice: ").strip()

    # --------------------------------------------------------
    # OPTION 1: DATASET INFORMATION
    # --------------------------------------------------------

    if choice == "1":

        print("\nFIRST FIVE RECORDS")
        print(df.head().to_string(index=False))

        print("\nDATASET INFORMATION")
        df.info()

        print("\nNUMERICAL SUMMARY")
        print(df.describe().round(2))

    # --------------------------------------------------------
    # OPTION 2: PLANETARY STATISTICS
    # --------------------------------------------------------

    elif choice == "2":

        shortest = df.loc[df["orbital_period"].idxmin()]
        longest = df.loc[df["orbital_period"].idxmax()]

        print("\nPLANETARY STATISTICS")
        print("-" * 40)

        print("Usable records:", len(df))
        print(
            "Different discovery methods:",
            df["method"].nunique()
        )

        print(
            "Shortest orbital period:",
            round(shortest["orbital_period"], 3),
            "days"
        )

        print(
            "Associated discovery method:",
            shortest["method"]
        )

        print(
            "Longest orbital period:",
            round(longest["orbital_period"], 3),
            "days"
        )

        print(
            "Associated discovery method:",
            longest["method"]
        )

        print(
            "Median orbital period:",
            round(df["orbital_period"].median(), 3),
            "days"
        )

        print(
            "Median distance:",
            round(df["distance"].median(), 3),
            "parsecs"
        )

        print(
            "\nNote: The dataset may contain multiple planets "
            "from the same system."
        )

    # --------------------------------------------------------
    # OPTION 3: DISCOVERY METHODS
    # --------------------------------------------------------

    elif choice == "3":

        methods = df["method"].value_counts()

        print("\nDISCOVERY METHOD STATISTICS")
        print(methods.to_string())

        plt.figure(figsize=(11, 6))

        sns.countplot(
            data=df,
            y="method",
            order=methods.index,
            color="steelblue"
        )

        plt.title("Planet Discoveries by Method")
        plt.xlabel("Number of Records")
        plt.ylabel("Discovery Method")
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # OPTION 4: ORBITAL PERIOD HISTOGRAM
    # --------------------------------------------------------

    elif choice == "4":

        plt.figure(figsize=(10, 6))

        sns.histplot(
            data=df,
            x="orbital_period",
            bins=30,
            color="deepskyblue"
        )

        plt.xscale("log")
        plt.title("Distribution of Planet Orbital Periods")
        plt.xlabel("Orbital Period (Days, Log Scale)")
        plt.ylabel("Number of Records")
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # OPTION 5: DISTANCE KDE PLOT
    # --------------------------------------------------------

    elif choice == "5":

        plt.figure(figsize=(10, 6))

        sns.kdeplot(
            data=df,
            x="distance",
            fill=True,
            color="purple"
        )

        plt.title("Distribution of Planet Discovery Distances")
        plt.xlabel("Distance (Parsecs)")
        plt.ylabel("Estimated Density")
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # OPTION 6: SCATTER PLOT
    # --------------------------------------------------------

    elif choice == "6":

        # Show the five most common methods separately.
        # Group remaining methods under "Other".

        top_methods = df["method"].value_counts().head(5).index

        plot_df = df.copy()

        plot_df["method_group"] = plot_df["method"].where(
            plot_df["method"].isin(top_methods),
            "Other"
        )

        plt.figure(figsize=(11, 7))

        sns.scatterplot(
            data=plot_df,
            x="distance",
            y="orbital_period",
            hue="method_group",
            alpha=0.75
        )

        plt.xscale("log")
        plt.yscale("log")

        plt.title("Discovery Distance vs Orbital Period")
        plt.xlabel("Distance (Parsecs, Log Scale)")
        plt.ylabel("Orbital Period (Days, Log Scale)")
        plt.legend(title="Discovery Method")
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # OPTION 7: CORRELATION HEATMAP
    # --------------------------------------------------------

    elif choice == "7":

        corr = df.corr(numeric_only=True)

        print("\nCORRELATION TABLE")
        print(corr.round(2).to_string())

        plt.figure(figsize=(10, 7))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            center=0
        )

        plt.title("Planet Dataset Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # OPTION 8: COMPLETE VISUAL DASHBOARD
    # --------------------------------------------------------

    elif choice == "8":

        fig, axes = plt.subplots(2, 2, figsize=(15, 10))

        # Graph 1: Orbital period distribution
        sns.histplot(
            data=df,
            x="orbital_period",
            bins=25,
            color="steelblue",
            ax=axes[0, 0]
        )
        axes[0, 0].set_xscale("log")
        axes[0, 0].set_title("Orbital Period Distribution")

        # Graph 2: Distance distribution
        sns.histplot(
            data=df,
            x="distance",
            bins=25,
            kde=True,
            color="coral",
            ax=axes[0, 1]
        )
        axes[0, 1].set_title("Discovery Distance Distribution")

        # Graph 3: Discovery method counts
        method_counts = df["method"].value_counts().head(8)

        sns.barplot(
            x=method_counts.values,
            y=method_counts.index,
            color="mediumseagreen",
            ax=axes[1, 0]
        )
        axes[1, 0].set_title("Top Discovery Methods")
        axes[1, 0].set_xlabel("Number of Records")

        # Graph 4: Correlation heatmap
        corr = df.corr(numeric_only=True)

        sns.heatmap(
            corr,
            cmap="coolwarm",
            center=0,
            ax=axes[1, 1]
        )
        axes[1, 1].set_title("Correlation Heatmap")

        fig.suptitle(
            "SPACE MISSION DATA EXPLORER",
            fontsize=17
        )

        plt.tight_layout()
        plt.show()

    # --------------------------------------------------------
    # OPTION 9: SAVE ANALYSIS REPORT
    # --------------------------------------------------------

    elif choice == "9":

        methods = df["method"].value_counts()
        shortest = df.loc[df["orbital_period"].idxmin()]
        longest = df.loc[df["orbital_period"].idxmax()]

        with open(
            "space_mission_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("SPACE MISSION DATA EXPLORER\n")
            file.write("=" * 40 + "\n\n")

            file.write(
                f"Usable records: {len(df)}\n"
            )

            file.write(
                f"Number of columns: {len(df.columns)}\n"
            )

            file.write(
                f"Discovery methods: {df['method'].nunique()}\n\n"
            )

            file.write("NUMERICAL SUMMARY\n")
            file.write(df.describe().round(3).to_string())
            file.write("\n\nDISCOVERY METHODS\n")
            file.write(methods.to_string())

            file.write(
                "\n\nShortest orbital period: "
                f"{shortest['orbital_period']:.3f} days\n"
            )

            file.write(
                "Longest orbital period: "
                f"{longest['orbital_period']:.3f} days\n"
            )

            file.write(
                "\nThis report describes the cleaned Seaborn "
                "planets dataset. It is not a live NASA feed.\n"
            )

        print("\nReport saved as space_mission_report.txt")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    elif choice == "0":

        print("\nMission complete, Space Scientist! 🚀")
        print("Thank you for exploring planetary data.")
        break

    else:

        print("\nInvalid choice. Please enter a number from 0 to 9.")