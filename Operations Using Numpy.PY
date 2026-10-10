import numpy as np

def run_classroom_project():
    print("=" * 60)
    print("Welcome to Roy's Classroom Data Management System (Class 8)")
    print("=" * 60)

    student_ids = np.linspace(0, 9, 10, dtype=int)
    print("\n[Task 1] Initializing Student Database...")
    print(f"Original Student IDs Array: {student_ids}")
    print(f"Array Dimension: {student_ids.ndim}D")

    attendance_status = np.where(student_ids % 2 != 0, -1, student_ids)
    print("\n[Task 2] Updating Attendance (Marking odd IDs with -1)...")
    print(f"Modified Attendance Array: {attendance_status}")
    print(f"Verifying Original Array remains unchanged: {student_ids}")

    classroom_seating = student_ids.reshape(2, 5)
    print("\n[Task 3] Rearranging Classroom Seating Chart (2 Rows)...")
    print("Seating Matrix:")
    print(classroom_seating)
    print(f"New Array Dimension: {classroom_seating.ndim}D (Shape: {classroom_seating.shape})")

    even_sum = 0
    for student_id in student_ids:
        if student_id % 2 == 0:
            even_sum += student_id

    print("\n[Task 4] Analyzing Performance Metrics...")
    print(f"Iterating and calculating the sum of all even IDs: {even_sum}")
    print("\n" + "=" * 60)
    print("Project successfully executed! Roy has updated the teacher's records.")
    print("=" * 60)

if __name__ == "__main__":
    run_classroom_project()