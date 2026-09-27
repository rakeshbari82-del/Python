# ==========================================
#        SMART LETTER WRITING APP
# ==========================================

from tkinter import *
from tkinter import filedialog, messagebox


# ==========================================
# 1. MAIN WINDOW
# ==========================================

window = Tk()
window.title("📝 Smart Letter Writing Application")
window.geometry("800x600")
window.minsize(650, 450)

# Make the editor stretch
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)


# ==========================================
# 2. FUNCTIONS
# ==========================================

current_file = None


# ---------- NEW LETTER ----------
def new_letter():
    global current_file

    # Ask before removing existing text
    if txt_edit.get("1.0", END).strip():
        answer = messagebox.askyesno(
            "New Letter",
            "Do you want to create a new letter?\n\n"
            "Any unsaved text may be lost."
        )

        if not answer:
            return

    txt_edit.delete("1.0", END)

    current_file = None

    window.title("📝 Smart Letter Writing Application")
    status_label.config(text="New letter created")
    update_count()


# ---------- OPEN LETTER ----------
def open_letter():
    global current_file

    filepath = filedialog.askopenfilename(
        title="Open Letter",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filepath:
        return

    try:
        with open(filepath, "r", encoding="utf-8") as input_file:
            letter_text = input_file.read()

        txt_edit.delete("1.0", END)
        txt_edit.insert(END, letter_text)

        current_file = filepath

        window.title(
            "📝 Smart Letter Writing Application - "
            + filepath
        )

        status_label.config(text="Letter opened successfully")
        update_count()

    except Exception as error:
        messagebox.showerror(
            "Error",
            "Could not open the file.\n\n" + str(error)
        )


# ---------- SAVE LETTER ----------
def save_letter():
    global current_file

    filepath = filedialog.asksaveasfilename(
        title="Save Letter",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not filepath:
        return

    try:
        letter_text = txt_edit.get("1.0", END)

        with open(filepath, "w", encoding="utf-8") as output_file:
            output_file.write(letter_text)

        current_file = filepath

        window.title(
            "📝 Smart Letter Writing Application - "
            + filepath
        )

        status_label.config(text="Letter saved successfully")

        messagebox.showinfo(
            "Saved",
            "Your letter has been saved successfully! 💾"
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            "Could not save the file.\n\n" + str(error)
        )


# ---------- CLEAR LETTER ----------
def clear_letter():
    answer = messagebox.askyesno(
        "Clear Letter",
        "Are you sure you want to clear the entire letter?"
    )

    if answer:
        txt_edit.delete("1.0", END)
        status_label.config(text="Editor cleared")
        update_count()


# ---------- WORD AND CHARACTER COUNT ----------
def update_count(event=None):
    text = txt_edit.get("1.0", END)

    # Remove the extra newline added by Tkinter
    clean_text = text.strip()

    characters = len(clean_text)

    if clean_text:
        words = len(clean_text.split())
    else:
        words = 0

    count_label.config(
        text=f"Words: {words}   |   Characters: {characters}"
    )


# ---------- EXIT ----------
def exit_app():
    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit the Letter Writing Application?"
    )

    if answer:
        window.destroy()


# ==========================================
# 3. TOP TITLE
# ==========================================

title_frame = Frame(
    window,
    bg="#1e3a5f",
    height=60
)

title_frame.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew"
)

title_frame.columnconfigure(0, weight=1)

title_label = Label(
    title_frame,
    text="📝 SMART LETTER WRITING APP",
    font=("Arial", 20, "bold"),
    bg="#1e3a5f",
    fg="white"
)

title_label.grid(
    row=0,
    column=0,
    pady=12
)


# ==========================================
# 4. BUTTON FRAME
# ==========================================

fr_buttons = Frame(
    window,
    relief=RAISED,
    bd=2,
    padx=8,
    pady=8
)

fr_buttons.grid(
    row=1,
    column=0,
    sticky="ns"
)


# ---------- BUTTONS ----------

btn_new = Button(
    fr_buttons,
    text="🆕 New Letter",
    width=15,
    command=new_letter
)

btn_open = Button(
    fr_buttons,
    text="📂 Open Letter",
    width=15,
    command=open_letter
)

btn_save = Button(
    fr_buttons,
    text="💾 Save Letter",
    width=15,
    command=save_letter
)

btn_clear = Button(
    fr_buttons,
    text="🗑️ Clear",
    width=15,
    command=clear_letter
)

btn_exit = Button(
    fr_buttons,
    text="❌ Exit",
    width=15,
    command=exit_app
)


# ---------- BUTTON LAYOUT ----------

btn_new.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
)

btn_open.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
)

btn_save.grid(
    row=2,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
)

btn_clear.grid(
    row=3,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
)

btn_exit.grid(
    row=4,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
)


# ==========================================
# 5. EDITOR AREA
# ==========================================

editor_frame = Frame(
    window,
    bg="white"
)

editor_frame.grid(
    row=1,
    column=1,
    sticky="nsew",
    padx=5,
    pady=5
)

editor_frame.rowconfigure(0, weight=1)
editor_frame.columnconfigure(0, weight=1)


# ---------- TEXT EDITOR ----------

txt_edit = Text(
    editor_frame,
    font=("Arial", 13),
    wrap="word",
    undo=True
)

txt_edit.grid(
    row=0,
    column=0,
    sticky="nsew"
)


# ---------- SCROLLBAR ----------

scrollbar = Scrollbar(
    editor_frame,
    command=txt_edit.yview
)

scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)

txt_edit.config(
    yscrollcommand=scrollbar.set
)


# ==========================================
# 6. STATUS BAR
# ==========================================

bottom_frame = Frame(
    window,
    relief=SUNKEN,
    bd=1
)

bottom_frame.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="ew"
)

bottom_frame.columnconfigure(0, weight=1)

status_label = Label(
    bottom_frame,
    text="Ready to write your letter ✍️",
    anchor="w",
    padx=10
)

status_label.grid(
    row=0,
    column=0,
    sticky="ew"
)

count_label = Label(
    bottom_frame,
    text="Words: 0   |   Characters: 0",
    padx=10
)

count_label.grid(
    row=0,
    column=1
)


# ==========================================
# 7. KEYBOARD SHORTCUTS
# ==========================================

window.bind(
    "<Control-o>",
    lambda event: open_letter()
)

window.bind(
    "<Control-s>",
    lambda event: save_letter()
)

window.bind(
    "<Control-n>",
    lambda event: new_letter()
)


# ==========================================
# 8. UPDATE WORD COUNT WHEN TYPING
# ==========================================

txt_edit.bind(
    "<KeyRelease>",
    update_count
)


# ==========================================
# 9. START PROGRAM
# ==========================================

window.mainloop()