# ============================================================
# 🚀 TECH WORKSHOP MISSION CHECK-IN
# Tkinter Project
# ============================================================

from tkinter import *
from datetime import date


# ============================================================
# PART 1: CREATE THE MAIN WINDOW
# ============================================================

root = Tk()

root.title("🚀 Tech Workshop Mission Check-In")
root.geometry("600x500")
root.configure(bg="#071A2B")


# ============================================================
# PART 2: CREATE THE HEADING
# ============================================================

heading = Label(
    root,
    text="🚀 TECH WORKSHOP",
    fg="white",
    bg="#0B3D5C",
    font=("Arial", 24, "bold"),
    height=2
)

heading.pack(fill=X)


# Subtitle

subtitle = Label(
    root,
    text="MISSION CHECK-IN DESK",
    fg="#7FDBFF",
    bg="#071A2B",
    font=("Arial", 14, "bold")
)

subtitle.pack(pady=10)


# ============================================================
# PART 3: PARTICIPANT NAME
# ============================================================

name_label = Label(
    root,
    text="👨‍💻 Enter Participant Name",
    fg="white",
    bg="#071A2B",
    font=("Arial", 12, "bold")
)

name_label.pack(pady=5)


name_entry = Entry(
    root,
    font=("Arial", 14),
    width=35,
    justify="center"
)

name_entry.pack(pady=5)


# ============================================================
# PART 4: DISPLAY FUNCTION
# ============================================================

def display_welcome():

    # Read the participant's name
    name = name_entry.get()

    # Clear previous message
    text_box.delete(1.0, END)

    # Check if name is empty
    if name == "":
        text_box.insert(
            END,
            "⚠️ Please enter your name first!\n\n"
            "Then click the CHECK IN button."
        )
        return

    # Get today's date
    workshop_date = str(date.today())

    # Create the welcome message
    greeting = "👋 Hello, " + name + "!\n\n"

    message = (
        "🎯 Welcome to the Tech Workshop!\n"
        "💻 Your learning mission starts now!\n\n"
    )

    details = (
        "📅 Date: " + workshop_date + "\n"
        "🟢 Status: CHECKED IN\n"
        "🚀 Mission: LEARN • CREATE • INNOVATE\n\n"
    )

    final_message = (
        "⭐ Have an amazing workshop, "
        + name
        + "!\n"
        "Keep Coding. Keep Creating. Keep Exploring! 🚀"
    )

    # Insert everything into the Text widget
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, details)
    text_box.insert(END, final_message)


# ============================================================
# PART 5: TEXT WIDGET
# ============================================================

text_box = Text(
    root,
    height=10,
    width=55,
    font=("Arial", 12),
    bg="#102A43",
    fg="white",
    insertbackground="white",
    wrap=WORD
)

text_box.pack(pady=15)


# ============================================================
# PART 6: CHECK-IN BUTTON
# ============================================================

welcome_button = Button(
    root,
    text="🚀 CHECK IN",
    command=display_welcome,
    font=("Arial", 13, "bold"),
    bg="#00A8E8",
    fg="white",
    activebackground="#0077B6",
    activeforeground="white",
    width=18,
    height=2,
    cursor="hand2"
)

welcome_button.pack(pady=5)


# ============================================================
# PART 7: FOOTER
# ============================================================

footer = Label(
    root,
    text="💡 Code • Learn • Create • Innovate",
    fg="#7FDBFF",
    bg="#071A2B",
    font=("Arial", 10, "italic")
)

footer.pack(pady=10)


# ============================================================
# PART 8: START THE PROGRAM
# ============================================================

root.mainloop()