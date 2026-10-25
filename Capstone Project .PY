# ================================================================
# 🎬 IMDB MOVIE DATA EXPLORER — CAPSTONE PROJECT
# Libraries: NumPy, Pandas, Seaborn, Matplotlib
# ================================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================== PROJECT SETTINGS ========================

sns.set_theme(style="darkgrid", palette="husl")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titleweight"] = "bold"

print("=" * 75)
print("🎬 WELCOME TO THE IMDB MOVIE DATA EXPLORER 🎬".center(75))
print("=" * 75)

# ======================== 1. IMPORT DATASET ========================

print("\n📂 STEP 1: IMPORTING IMDB DATASET")

# Place your CSV file in the same folder as this Python program.
# If the filename differs, update the candidates below.
possible_files = [
    "IMDB Dataset.CSV",
    "IMDB_Rows_41_to_75.CSV",
]

df = None

for filename in possible_files:
    if os.path.exists(filename):
        try:
            df = pd.read_csv(filename, encoding="utf-8")
            print(f"✅ Dataset loaded successfully: {filename}")
            break
        except UnicodeDecodeError:
            df = pd.read_csv(filename, encoding="latin1")
            print(f"✅ Dataset loaded successfully: {filename}")
            break

if df is None:
    print("\n❌ CSV file not found!")
    print("Put your IMDB CSV file in this program's folder.")
    print("Supported filenames:")
    for filename in possible_files:
        print(" -", filename)
    raise FileNotFoundError("Please add your IMDB dataset CSV file.")

# Clean column names for easier use.
df.columns = df.columns.str.strip()

print(f"\n📊 Total Movies/Records: {df.shape[0]:,}")
print(f"🧾 Total Features/Columns: {df.shape[1]}")

# ======================== 2. FIRST AND LAST ROWS ========================

print("\n" + "=" * 75)
print("🔍 STEP 2: FIRST THREE ROWS")
print("=" * 75)
print(df.head(3).to_string())

print("\n🔍 LAST THREE ROWS")
print(df.tail(3).to_string())

# ======================== 3. DATASET INFORMATION ========================

print("\n" + "=" * 75)
print("📋 STEP 3: DATASET INFORMATION")
print("=" * 75)

print("\nDataset structure:")
df.info()

print("\nStatistical summary:")
print(df.describe(include="all").to_string())

print("\nColumn data types:")
print(df.dtypes)

# ======================== 4. CHECK MISSING VALUES ========================

print("\n" + "=" * 75)
print("🧹 STEP 4: MISSING VALUE ANALYSIS")
print("=" * 75)

missing_values = df.isnull().sum()

print("\nMissing values in each column:")
print(missing_values.to_string())

print("\nTotal missing values:", int(missing_values.sum()))

if missing_values.sum() == 0:
    print("✅ Great! No missing values found.")
else:
    print("⚠️ Some columns contain missing values.")

# ======================== FIND IMPORTANT COLUMNS ========================

def find_column(possible_names):
    """Find a column using common alternative names."""
    for name in possible_names:
        for column in df.columns:
            if column.strip().lower() == name.lower():
                return column

    for name in possible_names:
        for column in df.columns:
            if name.lower() in column.strip().lower():
                return column

    return None


rating_col = find_column([
    "IMDB Rating", "IMDb Rating", "Rating",
    "imdb_rating", "rating", "averageRating"
])

runtime_col = find_column([
    "Runtime", "Run Time", "Duration",
    "runtime", "runtimeMinutes"
])

votes_col = find_column([
    "Votes", "Vote Count", "No. of Votes",
    "Number of Votes", "imdbVotes", "numVotes"
])

movie_col = find_column([
    "Movie Name", "Movie Title", "Series Title",
    "Title", "Name", "Series_Title", "movie"
])

genre_col = find_column(["Genre", "Genres"])
year_col = find_column(["Year", "Release Year", "Released_Year"])
gross_col = find_column(["Gross", "Box Office", "Revenue"])
certificate_col = find_column(["Certificate", "Rating Category"])

print("\n🔎 Detected columns:")
print("Movie title:", movie_col)
print("IMDb rating:", rating_col)
print("Runtime:", runtime_col)
print("Votes:", votes_col)
print("Genre:", genre_col)

# Convert numerical columns safely.
def convert_numeric(column):
    if column is not None:
        cleaned = (
            df[column]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace(r"[^\d.\-]", "", regex=True)
        )
        df[column] = pd.to_numeric(cleaned, errors="coerce")


convert_numeric(rating_col)
convert_numeric(runtime_col)
convert_numeric(votes_col)

if year_col is not None:
    df[year_col] = pd.to_numeric(
        df[year_col].astype(str).str.extract(r"(\d{4})")[0],
        errors="coerce"
    )

# ======================== 5. CREATE A SUBSET ========================

print("\n" + "=" * 75)
print("✂️ STEP 5: ROWS 41 TO 75")
print("=" * 75)

# Interpreting row numbers as ordinary 1-based row positions.
subset = df.iloc[40:75].copy()

print(f"Subset contains {len(subset)} rows.")
print(subset.to_string(index=False))

subset.to_csv("IMDB_Rows_41_to_75.csv", index=False)
print("\n💾 Subset saved as IMDB_Rows_41_to_75.csv")

# ======================== 6. MOVIE WITH MOST VOTES ========================

print("\n" + "=" * 75)
print("🏆 STEP 6: MOST VOTED MOVIE")
print("=" * 75)

if votes_col is not None and df[votes_col].notna().any():
    most_voted_index = df[votes_col].idxmax()
    most_voted_movie = df.loc[most_voted_index]

    print("\n🎖️ MOVIE WITH THE HIGHEST NUMBER OF VOTES")
    print(most_voted_movie.to_string())
else:
    print("⚠️ A usable votes column was not found in the dataset.")

# ======================== 7. BOXPLOTS ========================

print("\n" + "=" * 75)
print("📦 STEP 7: BOXPLOTS — RATING AND RUNTIME")
print("=" * 75)

box_columns = [
    col for col in [rating_col, runtime_col]
    if col is not None and df[col].notna().any()
]

if box_columns:
    fig, axes = plt.subplots(1, len(box_columns), figsize=(7 * len(box_columns), 6))
    axes = np.atleast_1d(axes)

    for ax, column in zip(axes, box_columns):
        sns.boxplot(y=df[column], ax=ax, color="skyblue")
        ax.set_title(f"Distribution of {column}")
        ax.set_ylabel(column)

    plt.suptitle("📦 IMDb Movie Statistics — Boxplot Analysis", fontsize=16)
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ No usable rating or runtime column found.")

# ======================== 8. RATING VS RUNTIME ========================

print("\n" + "=" * 75)
print("📈 STEP 8: RELATIONSHIP BETWEEN RATING AND RUNTIME")
print("=" * 75)

if rating_col is not None and runtime_col is not None:
    relationship_data = df[[rating_col, runtime_col]].dropna()

    if len(relationship_data) > 0:
        plt.figure(figsize=(11, 7))

        sns.scatterplot(
            data=relationship_data,
            x=runtime_col,
            y=rating_col,
            alpha=0.65,
            s=65
        )

        if len(relationship_data) >= 2:
            sns.regplot(
                data=relationship_data,
                x=runtime_col,
                y=rating_col,
                scatter=False,
                color="red",
                line_kws={"linewidth": 2}
            )

        plt.title("🎥 Do Longer Movies Receive Higher IMDb Ratings?")
        plt.xlabel("Runtime")
        plt.ylabel("IMDb Rating")
        plt.tight_layout()
        plt.show()

        if len(relationship_data) >= 2:
            correlation = relationship_data[rating_col].corr(
                relationship_data[runtime_col]
            )
            print(f"Pearson correlation: {correlation:.3f}")

            if pd.notna(correlation):
                if correlation > 0.5:
                    print("Interpretation: Strong positive linear relationship.")
                elif correlation > 0.2:
                    print("Interpretation: Moderate positive linear relationship.")
                elif correlation < -0.5:
                    print("Interpretation: Strong negative linear relationship.")
                elif correlation < -0.2:
                    print("Interpretation: Moderate negative linear relationship.")
                else:
                    print("Interpretation: Weak linear relationship.")
    else:
        print("⚠️ No complete rating/runtime records available.")
else:
    print("⚠️ Rating or runtime column not found.")

# ======================== 9. DISTRIBUTION ANALYSIS ========================

print("\n" + "=" * 75)
print("📊 STEP 9: DISTRIBUTION OF RATINGS AND RUNTIME")
print("=" * 75)

distribution_columns = [
    col for col in [rating_col, runtime_col]
    if col is not None and df[col].notna().any()
]

if distribution_columns:
    fig, axes = plt.subplots(
        1, len(distribution_columns),
        figsize=(7 * len(distribution_columns), 5)
    )
    axes = np.atleast_1d(axes)

    for ax, column in zip(axes, distribution_columns):
        values = df[column].dropna()

        sns.histplot(
            values,
            bins=20,
            kde=len(values) >= 2,
            ax=ax,
            color="mediumseagreen"
        )

        ax.axvline(
            values.mean(),
            color="red",
            linestyle="--",
            label=f"Mean: {values.mean():.2f}"
        )

        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Number of Movies")
        ax.legend()

    plt.suptitle("📊 IMDb Rating and Runtime Distributions", fontsize=16)
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ No usable numerical columns found.")

# ======================== 10. COUNT PLOT OF RATINGS ========================

print("\n" + "=" * 75)
print("🎭 STEP 10: COUNT PLOT OF MOVIE RATINGS")
print("=" * 75)

# Use the explicit Rating Category column if available.
# Otherwise, group numerical IMDb scores into rating bands.
if certificate_col is not None:
    count_col = certificate_col
    count_data = df.dropna(subset=[count_col]).copy()
elif rating_col is not None:
    count_col = "Rating Category"
    count_data = df.dropna(subset=[rating_col]).copy()

    count_data[count_col] = pd.cut(
        count_data[rating_col],
        bins=[-np.inf, 2, 4, 6, 8, 10, np.inf],
        labels=[
            "0–2", "2–4", "4–6", "6–8", "8–10", "Above 10"
        ],
        right=False
    )

    count_data = count_data.dropna(subset=[count_col])
else:
    count_col = None
    count_data = pd.DataFrame()

if count_col is not None and not count_data.empty:
    plt.figure(figsize=(12, 6))

    order = count_data[count_col].value_counts().index

    sns.countplot(
        data=count_data,
        x=count_col,
        order=order,
        hue=count_col,
        legend=False
    )

    plt.title("🎭 Number of Movies by Rating Category")
    plt.xlabel(count_col)
    plt.ylabel("Number of Movies")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ No usable rating category or IMDb rating column found.")

# ======================== EXTRA 1: CORRELATION HEATMAP ========================

print("\n" + "=" * 75)
print("🔥 BONUS: NUMERICAL CORRELATION HEATMAP")
print("=" * 75)

numeric_df = df.select_dtypes(include=[np.number])
numeric_df = numeric_df.dropna(axis=1, how="all")

if numeric_df.shape[1] >= 2:
    correlation_matrix = numeric_df.corr()

    plt.figure(figsize=(
        max(9, len(correlation_matrix.columns) * 1.1),
        max(7, len(correlation_matrix.columns) * 0.8)
    ))

    sns.heatmap(
        correlation_matrix,
        annot=len(correlation_matrix.columns) <= 10,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("🔥 Correlation Between Numerical Movie Features")
    plt.tight_layout()
    plt.show()

    print(correlation_matrix.round(3).to_string())
else:
    print("Not enough numerical columns for a correlation heatmap.")

# ======================== EXTRA 2: TOP 10 MOVIES ========================

print("\n" + "=" * 75)
print("🌟 BONUS: TOP 10 HIGHEST-RATED MOVIES")
print("=" * 75)

if rating_col is not None:
    ranked_movies = df.dropna(subset=[rating_col]).copy()

    if not ranked_movies.empty:
        ranked_movies = ranked_movies.sort_values(
            by=rating_col, ascending=False
        ).head(10)

        display_columns = [
            col for col in [movie_col, rating_col, votes_col, year_col, genre_col]
            if col is not None
        ]

        print(ranked_movies[display_columns].to_string(index=False))

        if movie_col is not None:
            chart_data = ranked_movies.dropna(subset=[movie_col])

            if not chart_data.empty:
                plt.figure(figsize=(12, 7))

                sns.barplot(
                    data=chart_data,
                    x=rating_col,
                    y=movie_col,
                    hue=rating_col,
                    legend=False
                )

                plt.title("🌟 Top 10 Highest-Rated Movies")
                plt.xlabel("IMDb Rating")
                plt.ylabel("Movie")
                plt.tight_layout()
                plt.show()
else:
    print("⚠️ IMDb rating column not found.")

# ======================== EXTRA 3: GENRE INSIGHTS ========================

print("\n" + "=" * 75)
print("🎞️ BONUS: MOST COMMON MOVIE GENRES")
print("=" * 75)

if genre_col is not None:
    genres = (
        df[genre_col]
        .dropna()
        .astype(str)
        .str.split(r",\s*")
        .explode()
        .str.strip()
    )

    genre_counts = genres.value_counts().head(10)

    print(genre_counts.to_string())

    if not genre_counts.empty:
        plt.figure(figsize=(11, 6))

        sns.barplot(
            x=genre_counts.values,
            y=genre_counts.index,
            hue=genre_counts.index,
            legend=False
        )

        plt.title("🎞️ Top 10 Most Common Genres")
        plt.xlabel("Number of Movies")
        plt.ylabel("Genre")
        plt.tight_layout()
        plt.show()
else:
    print("No genre column found; skipping genre analysis.")


# ======================== FINAL PROJECT SUMMARY ========================

print("\n" + "=" * 75)
print("🏁 IMDB MOVIE DATA EXPLORER — PROJECT COMPLETED!")
print("=" * 75)

print(f"🎬 Total records analysed: {len(df):,}")
print(f"🧾 Total columns analysed: {len(df.columns)}")
print(f"🕳️ Total missing cells: {int(df.isnull().sum().sum()):,}")
print(f"✂️ Rows in saved subset: {len(subset)}")
print("\n📁 Output file: IMDB_Rows_41_to_75.csv")
print("📊 All available analyses and visualizations are complete!")
print("🚀 Thank you for exploring movie data with Python!")
print("=" * 75)