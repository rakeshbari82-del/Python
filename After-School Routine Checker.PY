# ==========================================================
# 🚀 AFTER-SCHOOL MISSION CONTROL
# Python + Tkinter Event Handling Project
# ==========================================================

from tkinter import *
from tkinter import messagebox
import random


# ==========================================================
# PART 1: CREATE THE MAIN WINDOW
# ==========================================================

window = Tk()
window.title("🚀 After-School Mission Control")
window.geometry("520x600")
window.resizable(False, False)


# ==========================================================
# VARIABLES
# ==========================================================

completed_tasks = 0


# ==========================================================
# PART 2: HEADING
# ==========================================================

heading = Label(
    window,
    text="🚀 AFTER-SCHOOL MISSION CONTROL 🚀",
    font=("Arial", 18, "bold")
)
heading.pack(pady=15)

subtitle = Label(
    window,
    text="Plan your mission. Complete your tasks. Become a champion!",
    font=("Arial", 10)
)
subtitle.pack()


# ==========================================================
# PART 3: TASK ENTRY
# ==========================================================

instruction = Label(
    window,
    text="🎯 Enter your next after-school mission:",
    font=("Arial", 12, "bold")
)
instruction.pack(pady=(20, 5))

task_entry = Entry(
    window,
    width=42,
    font=("Arial", 12)
)
task_entry.pack(pady=5)


# ==========================================================
# PART 4: KEY PRESS EVENT
# ==========================================================

key_label = Label(
    window,
    text="⌨️ Last key pressed: None",
    font=("Arial", 10)
)
key_label.pack(pady=8)


def handle_keypress(event):
    """Show the character of the last key pressed."""

    if event.char:
        key_label.config(
            text="⌨️ Last key pressed: " + event.char
        )


task_entry.bind("<Key>", handle_keypress)


# ==========================================================
# PART 5: MISSION DISPLAY AREA
# ==========================================================

mission_message = Label(
    window,
    text="🖱️ Click this Mission Panel to activate it!",
    bg="#d0efff",
    width=45,
    height=4,
    font=("Arial", 11, "bold")
)
mission_message.pack(pady=15)


def handle_click(event):
    """Run when the Mission Panel is clicked."""

    mission_message.config(
        text="🔥 Mission Panel Activated!\n"
             "Your after-school mission is ready!"
    )


mission_message.bind("<Button-1>", handle_click)


# ==========================================================
# PART 6: CHECK ROUTINE FUNCTION
# ==========================================================

def check_routine():
    """Check the task entered by the user."""

    global completed_tasks

    task = task_entry.get().strip()

    # If no task was entered
    if task == "":
        messagebox.showwarning(
            "⚠️ Missing Mission",
            "Please enter an after-school task first!"
        )

    else:
        completed_tasks += 1

        mission_message.config(
            text="🎯 NEXT MISSION:\n" + task
        )

        progress_label.config(
            text="🏆 Missions Completed: " + str(completed_tasks)
        )

        encouragement = [
            "🔥 Great choice! Let's complete it!",
            "💪 You can do this!",
            "⭐ Excellent mission!",
            "🚀 Keep going, champion!",
            "🧠 Time to level up your skills!",
            "🏆 One more step toward success!"
        ]

        messagebox.showinfo(
            "🚀 Mission Accepted!",
            random.choice(encouragement)
            + "\n\nYour mission:\n"
            + task
        )


# ==========================================================
# PART 7: CHECK BUTTON
# ==========================================================

check_button = Button(
    window,
    text="🎯 CHECK MY MISSION",
    font=("Arial", 12, "bold"),
    command=check_routine,
    width=25
)
check_button.pack(pady=10)


# ==========================================================
# PART 8: QUICK TASK SUGGESTIONS
# ==========================================================

suggestion_label = Label(
    window,
    text="💡 Quick Mission Suggestions",
    font=("Arial", 12, "bold")
)
suggestion_label.pack(pady=(15, 5))


def add_homework():
    task_entry.delete(0, END)
    task_entry.insert(0, "Complete my homework")


def add_coding():
    task_entry.delete(0, END)
    task_entry.insert(0, "Practice Python coding")


def add_exercise():
    task_entry.delete(0, END)
    task_entry.insert(0, "Do 20 minutes of exercise")


suggestion_frame = Frame(window)
suggestion_frame.pack(pady=5)

homework_button = Button(
    suggestion_frame,
    text="📚 Homework",
    command=add_homework,
    width=13
)
homework_button.grid(row=0, column=0, padx=5)

coding_button = Button(
    suggestion_frame,
    text="💻 Coding",
    command=add_coding,
    width=13
)
coding_button.grid(row=0, column=1, padx=5)

exercise_button = Button(
    suggestion_frame,
    text="🏃 Exercise",
    command=add_exercise,
    width=13
)
exercise_button.grid(row=0, column=2, padx=5)


# ==========================================================
# PART 9: PROGRESS
# ==========================================================

progress_label = Label(
    window,
    text="🏆 Missions Completed: 0",
    font=("Arial", 11, "bold")
)
progress_label.pack(pady=15)


# ==========================================================
# PART 10: MOTIVATIONAL MESSAGE
# ==========================================================

motivation_label = Label(
    window,
    text="🌟 Small progress every day creates big success!",
    font=("Arial", 10, "italic")
)
motivation_label.pack(pady=5)


# ==========================================================
# PART 11: EXIT BUTTON
# ==========================================================

exit_button = Button(
    window,
    text="❌ Exit Mission Control",
    command=window.destroy,
    width=22
)
exit_button.pack(pady=10)


# ==========================================================
# START THE PROGRAM
# ==========================================================

window.mainloop()