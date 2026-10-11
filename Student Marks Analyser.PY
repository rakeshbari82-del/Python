
# ==========================================
# 🎓 STUDENT SUCCESS HUB
# A Pandas Data Analysis Project
# ==========================================

import pandas as pd
import os

FILE_NAME = "student_marks.csv"

print("=" * 45)
print("       🎓 STUDENT SUCCESS HUB")
print("      Smart Student Analytics System")
print("=" * 45)

# ------------------------------------------
# PART 1: LOAD OR CREATE STUDENT DATA
# ------------------------------------------

if os.path.exists(FILE_NAME):
    df = pd.read_csv(FILE_NAME)
    print("\n✅ Existing student records loaded!")
else:
    data = {
        "Student": ["Aarav", "Meera", "Kabir", "Anaya", "Rohan"],
        "Math": [88, 76, 92, 67, 85],
        "Science": [91, 80, 89, 72, 87],
        "English": [84, 78, 95, 70, 82],
        "Attendance": [96, 90, 98, 85, 92]
    }

    df = pd.DataFrame(data)
    df.to_csv(FILE_NAME, index=False)
    print("\n✅ Sample student records created!")

# ------------------------------------------
# PART 2: HELPER FUNCTIONS
# ------------------------------------------

def save_data():
    df.to_csv(FILE_NAME, index=False)
    print("💾 Records saved successfully!")


def show_students():
    if df.empty:
        print("\nNo student records available.")
        return

    print("\n📋 STUDENT RECORDS")
    print("-" * 65)
    print(df.to_string(index=False))


def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("⚠️ Marks must be between 0 and 100.")

        except ValueError:
            print("⚠️ Please enter a valid number.")


def get_attendance():
    while True:
        try:
            attendance = float(input("Enter attendance percentage (0-100): "))

            if 0 <= attendance <= 100:
                return attendance

            print("⚠️ Attendance must be between 0 and 100.")

        except ValueError:
            print("⚠️ Please enter a valid number.")


def calculate_results():
    global df

    subjects = ["Math", "Science", "English"]

    # Replace missing marks with zero for this analysis.
    df[subjects] = df[subjects].fillna(0)

    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = (df["Total"] / len(subjects)).round(2)

    df["Grade"] = df["Average"].apply(
        lambda avg:
        "A+" if avg >= 90 else
        "A" if avg >= 80 else
        "B" if avg >= 70 else
        "C" if avg >= 60 else
        "D" if avg >= 40 else
        "Needs Improvement"
    )

# ------------------------------------------
# PART 3: ADD A STUDENT
# ------------------------------------------

def add_student():
    global df

    name = input("\nEnter student name: ").strip()

    if not name:
        print("⚠️ Student name cannot be empty.")
        return

    if df["Student"].astype(str).str.casefold().eq(
        name.casefold()
    ).any():
        print("⚠️ This student already exists.")
        return

    print("\nEnter subject marks:")

    new_student = {
        "Student": name,
        "Math": get_marks("Math"),
        "Science": get_marks("Science"),
        "English": get_marks("English"),
        "Attendance": get_attendance()
    }

    df = pd.concat(
        [df, pd.DataFrame([new_student])],
        ignore_index=True
    )

    save_data()
    print(f"🎉 Welcome, {name}! Student added successfully.")


# ------------------------------------------
# PART 4: SEARCH FOR A STUDENT
# ------------------------------------------

def search_student():
    name = input("\nEnter student name to search: ").strip()

    result = df[
        df["Student"].astype(str).str.casefold()
        == name.casefold()
    ]

    if result.empty:
        print("❌ Student not found.")
    else:
        calculate_results()
        print("\n🔎 STUDENT REPORT")
        print(result.to_string(index=False))


# ------------------------------------------
# PART 5: PERFORMANCE ANALYSIS
# ------------------------------------------

def performance_analysis():
    if df.empty:
        print("\nNo records to analyse.")
        return

    calculate_results()

    print("\n📊 CLASS PERFORMANCE REPORT")
    print("-" * 45)

    print(f"Total students : {len(df)}")
    print(f"Class average  : {df['Average'].mean():.2f}")
    print(f"Highest average: {df['Average'].max():.2f}")
    print(f"Lowest average : {df['Average'].min():.2f}")

    print("\n📚 Subject-wise averages:")

    for subject in ["Math", "Science", "English"]:
        print(f"{subject:10}: {df[subject].mean():.2f}")

    print("\n🏅 Student results:")
    print(
        df[["Student", "Total", "Average", "Grade"]]
        .sort_values("Average", ascending=False)
        .to_string(index=False)
    )


# ------------------------------------------
# PART 6: FIND THE CLASS TOPPER
# ------------------------------------------

def find_topper():
    if df.empty:
        print("\nNo student records available.")
        return

    calculate_results()
    highest = df["Average"].max()

    toppers = df[df["Average"] == highest]

    print("\n🏆 CLASS TOPPER")
    print("-" * 35)

    for _, student in toppers.iterrows():
        print(f"Name    : {student['Student']}")
        print(f"Average : {student['Average']:.2f}%")
        print(f"Grade   : {student['Grade']}")
        print("-" * 35)


# ------------------------------------------
# PART 7: ATTENDANCE ANALYSIS
# ------------------------------------------

def attendance_analysis():
    if df.empty:
        print("\nNo student records available.")
        return

    print("\n📅 ATTENDANCE REPORT")
    print("-" * 45)

    for _, student in df.iterrows():
        attendance = student["Attendance"]

        if pd.isna(attendance):
            status = "Missing attendance"
        elif attendance >= 90:
            status = "Excellent"
        elif attendance >= 75:
            status = "Satisfactory"
        else:
            status = "Needs attention"

        print(
            f"{student['Student']}: "
            f"{attendance}% - {status}"
            if pd.notna(attendance)
            else f"{student['Student']}: {status}"
        )


# ------------------------------------------
# PART 8: CLEAN MISSING DATA
# ------------------------------------------

def clean_data():
    global df

    print("\n🧹 DATA CLEANING")

    missing_before = int(df.isna().sum().sum())
    print(f"Missing values before cleaning: {missing_before}")

    # Fill missing marks with zero.
    for subject in ["Math", "Science", "English"]:
        df[subject] = df[subject].fillna(0)

    # Fill missing attendance with the available class average.
    attendance_average = df["Attendance"].mean()

    if pd.isna(attendance_average):
        attendance_average = 0

    df["Attendance"] = df["Attendance"].fillna(
        attendance_average
    )

    # Remove duplicate student records, keeping the first.
    df = df.drop_duplicates(
        subset=["Student"],
        keep="first"
    ).reset_index(drop=True)

    missing_after = int(df.isna().sum().sum())

    print(f"Missing values after cleaning: {missing_after}")
    print("Duplicate student records removed.")
    print("✅ Data cleaning completed!")

    save_data()


# ------------------------------------------
# PART 9: MAIN MENU
# ------------------------------------------

while True:

    print("\n" + "=" * 45)
    print("             MAIN MENU")
    print("=" * 45)

    print("1. 📋 View All Students")
    print("2. ➕ Add a New Student")
    print("3. 🔎 Search for a Student")
    print("4. 📊 Class Performance Analysis")
    print("5. 🏆 Find Class Topper")
    print("6. 📅 Attendance Analysis")
    print("7. 🧹 Clean Missing Data")
    print("8. 💾 Save Student Records")
    print("9. 🚪 Exit")

    choice = input("\nChoose an option (1-9): ").strip()

    if choice == "1":
        show_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        performance_analysis()

    elif choice == "5":
        find_topper()

    elif choice == "6":
        attendance_analysis()

    elif choice == "7":
        clean_data()

    elif choice == "8":
        save_data()

    elif choice == "9":
        save_data()
        print("\n🌟 Thank you for using Student Success Hub!")
        print("Keep learning, keep growing! 🚀")
        break

    else:
        print("❌ Invalid choice. Please select 1-9.")