# ============================================================
# 📚 READING SCHEDULE PLANNER
# ============================================================

from tkinter import *
from tkinter import messagebox

# ------------------------------------------------------------
# PART 1: MAIN WINDOW
# ------------------------------------------------------------

root = Tk()
root.title("📚 Reading Schedule Planner")
root.geometry("600x400")
root.configure(bg="#EAF4FF")


# ------------------------------------------------------------
# MAIN WINDOW DESIGN
# ------------------------------------------------------------

heading = Label(
    root,
    text="📚 READING SCHEDULE PLANNER",
    font=("Arial", 22, "bold"),
    bg="#EAF4FF",
    fg="#123B5D"
)
heading.pack(pady=(45, 15))

subtitle = Label(
    root,
    text="Plan your reading journey and finish your book on time! 🚀",
    font=("Arial", 12),
    bg="#EAF4FF",
    fg="#456"
)
subtitle.pack(pady=5)

info = Label(
    root,
    text="Enter your book details and discover your reading schedule.",
    font=("Arial", 10),
    bg="#EAF4FF",
    fg="#555"
)
info.pack(pady=10)


# ------------------------------------------------------------
# PART 2: TOPLEVEL WINDOW
# ------------------------------------------------------------

def topwin():

    # Create second window
    top = Toplevel(root)
    top.title("📖 Create My Reading Plan")
    top.geometry("600x500")
    top.configure(bg="#FFF8E7")

    # --------------------------------------------------------
    # TOPLEVEL HEADING
    # --------------------------------------------------------

    title = Label(
        top,
        text="📖 CREATE YOUR READING PLAN",
        font=("Arial", 20, "bold"),
        bg="#FFF8E7",
        fg="#7A4E00"
    )
    title.pack(pady=(25, 10))

    instruction = Label(
        top,
        text="Let's calculate how many days you need to finish your book!",
        font=("Arial", 10),
        bg="#FFF8E7",
        fg="#555"
    )
    instruction.pack(pady=(0, 20))

    # --------------------------------------------------------
    # INPUT LABELS AND ENTRIES
    # --------------------------------------------------------

    pages_label = Label(
        top,
        text="📚 Total pages in book:",
        font=("Arial", 11, "bold"),
        bg="#FFF8E7"
    )
    pages_label.place(x=80, y=110)

    pages_entry = Entry(
        top,
        font=("Arial", 11),
        width=20
    )
    pages_entry.place(x=310, y=110)

    daily_label = Label(
        top,
        text="📅 Pages to read each day:",
        font=("Arial", 11, "bold"),
        bg="#FFF8E7"
    )
    daily_label.place(x=80, y=160)

    daily_entry = Entry(
        top,
        font=("Arial", 11),
        width=20
    )
    daily_entry.place(x=310, y=160)

    # --------------------------------------------------------
    # RESULT LABELS AND ENTRIES
    # --------------------------------------------------------

    result_title = Label(
        top,
        text="✨ YOUR READING PLAN ✨",
        font=("Arial", 15, "bold"),
        bg="#FFF8E7",
        fg="#7A4E00"
    )
    result_title.place(x=190, y=260)

    days_label = Label(
        top,
        text="Complete reading days:",
        font=("Arial", 11, "bold"),
        bg="#FFF8E7"
    )
    days_label.place(x=80, y=310)

    days_entry = Entry(
        top,
        font=("Arial", 11),
        width=20
    )
    days_entry.place(x=310, y=310)

    remaining_label = Label(
        top,
        text="Pages remaining:",
        font=("Arial", 11, "bold"),
        bg="#FFF8E7"
    )
    remaining_label.place(x=80, y=355)

    remaining_entry = Entry(
        top,
        font=("Arial", 11),
        width=20
    )
    remaining_entry.place(x=310, y=355)

    # --------------------------------------------------------
    # PART 3: NESTED CALCULATION FUNCTION
    # --------------------------------------------------------

    def calculate_plan():

        try:
            # Get values from Entry widgets
            total_pages = int(pages_entry.get())
            pages_per_day = int(daily_entry.get())

            # Check for positive numbers
            if total_pages <= 0 or pages_per_day <= 0:

                messagebox.showerror(
                    "❌ Invalid Input",
                    "Please enter numbers greater than zero."
                )

                return

            # ------------------------------------------------
            # PART 4: FLOOR DIVISION AND MODULO
            # ------------------------------------------------

            complete_days = total_pages // pages_per_day

            remaining_pages = total_pages % pages_per_day

            # ------------------------------------------------
            # PART 5: CLEAR OLD RESULTS
            # ------------------------------------------------

            days_entry.delete(0, END)
            remaining_entry.delete(0, END)

            # ------------------------------------------------
            # PART 6: DISPLAY RESULTS
            # ------------------------------------------------

            days_entry.insert(END, str(complete_days))
            remaining_entry.insert(END, str(remaining_pages))

            # ------------------------------------------------
            # EXTRA MESSAGE
            # ------------------------------------------------

            if remaining_pages == 0:

                messagebox.showinfo(
                    "🎉 Perfect Plan!",
                    f"Excellent!\n\n"
                    f"You can finish the book in {complete_days} complete days! 📚\n"
                    f"Keep reading and keep learning! 🌟"
                )

            else:

                total_days = complete_days + 1

                messagebox.showinfo(
                    "📖 Reading Plan Ready!",
                    f"You need {complete_days} complete days "
                    f"plus one final day.\n\n"
                    f"Total reading days: {total_days} 📅\n"
                    f"Pages left after complete days: {remaining_pages} 📄"
                )

        # ----------------------------------------------------
        # PART 7: HANDLE INVALID INPUT
        # ----------------------------------------------------

        except ValueError:

            messagebox.showerror(
                "❌ Invalid Input",
                "Please enter valid whole numbers only.\n\n"
                "Example: 300 and 25"
            )

    # --------------------------------------------------------
    # CALCULATE BUTTON
    # --------------------------------------------------------

    calculate_button = Button(
        top,
        text="✨ CREATE MY PLAN ✨",
        font=("Arial", 11, "bold"),
        command=calculate_plan,
        bg="#FF9F1C",
        fg="white",
        activebackground="#F77F00",
        width=22,
        height=1
    )
    calculate_button.place(x=190, y=205)


# ------------------------------------------------------------
# MAIN WINDOW BUTTON
# ------------------------------------------------------------

start_button = Button(
    root,
    text="📖 CREATE MY READING PLAN",
    font=("Arial", 12, "bold"),
    command=topwin,
    bg="#1261A0",
    fg="white",
    activebackground="#0B4F71",
    width=25,
    height=2
)
start_button.pack(pady=30)


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

footer = Label(
    root,
    text="💡 Read • Learn • Grow • Achieve",
    font=("Arial", 11, "italic"),
    bg="#EAF4FF",
    fg="#1261A0"
)
footer.pack(pady=5)


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

root.mainloop()