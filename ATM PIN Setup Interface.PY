# ============================================================
# 🏦 ATM SECURE PIN CENTER
# Tkinter Project
# ============================================================

from tkinter import *

# ------------------------------------------------------------
# 1. CREATE MAIN WINDOW
# ------------------------------------------------------------

root = Tk()
root.title("🏦 ATM Secure PIN Center")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#102A43")


# ------------------------------------------------------------
# 2. TITLE
# ------------------------------------------------------------

title_label = Label(
    root,
    text="🏦 ATM SECURE PIN CENTER",
    font=("Arial", 16, "bold"),
    bg="#102A43",
    fg="white"
)

title_label.place(x=65, y=8)


subtitle_label = Label(
    root,
    text="Create your secure ATM PIN",
    font=("Arial", 9),
    bg="#102A43",
    fg="#9AD7F5"
)

subtitle_label.place(x=110, y=37)


# ------------------------------------------------------------
# 3. ACCOUNT DETAILS FRAME
# ------------------------------------------------------------

details_frame = Frame(
    master=root,
    height=135,
    width=360,
    bg="#D0EFFF",
    relief=RAISED,
    borderwidth=2
)

details_frame.place(x=20, y=55)


# ------------------------------------------------------------
# 4. ACCOUNT NAME LABEL
# ------------------------------------------------------------

name_label = Label(
    details_frame,
    text="Account Name",
    bg="#3895D3",
    fg="white",
    width=14,
    font=("Arial", 9, "bold")
)

name_label.place(x=15, y=20)


# ------------------------------------------------------------
# 5. ACCOUNT NAME ENTRY
# ------------------------------------------------------------

name_entry = Entry(
    details_frame,
    width=21,
    font=("Arial", 10)
)

name_entry.place(x=145, y=20)


# ------------------------------------------------------------
# 6. PIN LABEL
# ------------------------------------------------------------

pin_label = Label(
    details_frame,
    text="Create PIN",
    bg="#3895D3",
    fg="white",
    width=14,
    font=("Arial", 9, "bold")
)

pin_label.place(x=15, y=70)


# ------------------------------------------------------------
# 7. PIN ENTRY
# ------------------------------------------------------------

pin_entry = Entry(
    details_frame,
    width=21,
    show="*",
    font=("Arial", 10)
)

pin_entry.place(x=145, y=70)


# ------------------------------------------------------------
# 8. FUNCTION TO HANDLE KEYPAD
# ------------------------------------------------------------

def keypad_press(value):

    if value == "Clear":
        pin_entry.delete(0, END)

    elif value == "Enter":
        confirm_pin()

    else:
        # Limit PIN to 4 digits
        if len(pin_entry.get()) < 4:
            pin_entry.insert(END, str(value))


# ------------------------------------------------------------
# 9. CONFIRM PIN FUNCTION
# ------------------------------------------------------------

def confirm_pin():

    # Read values
    account_name = name_entry.get()
    pin = pin_entry.get()

    # Clear old message
    message_box.delete(1.0, END)

    # Check account name
    if account_name == "":
        message_box.insert(
            END,
            "⚠️ Please enter your account name."
        )
        return

    # Check PIN
    if pin == "":
        message_box.insert(
            END,
            "⚠️ Please enter your PIN."
        )
        return

    # Check PIN length
    if len(pin) != 4:
        message_box.insert(
            END,
            "⚠️ PIN must contain exactly 4 digits."
        )
        return

    # Check whether PIN contains only numbers
    if not pin.isdigit():
        message_box.insert(
            END,
            "⚠️ PIN must contain numbers only."
        )
        return

    # Check PIN strength
    if len(set(pin)) == 1:
        security = "⚠️ Weak PIN - avoid repeated digits."

    elif pin in ["1234", "4321", "1111", "0000"]:
        security = "⚠️ Common PIN - choose a safer PIN."

    else:
        security = "🟢 Good PIN - security check passed!"

    # Final message
    message = (
        "✅ ATM PIN SETUP SUCCESSFUL!\n\n"
        "👤 Account: " + account_name +
        "\n🔐 PIN: ****\n\n"
        + security +
        "\n\n🏦 Your PIN is ready."
    )

    message_box.insert(END, message)


# ------------------------------------------------------------
# 10. KEYPAD FRAME
# ------------------------------------------------------------

keypad_frame = Frame(
    master=root,
    relief=SUNKEN,
    borderwidth=3,
    bg="#243B53"
)

keypad_frame.place(x=70, y=205)


# ------------------------------------------------------------
# 11. KEYPAD VALUES
# ------------------------------------------------------------

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["Clear", 0, "Enter"]
]


# ------------------------------------------------------------
# 12. BUILD KEYPAD
# ------------------------------------------------------------

for i in range(4):

    keypad_frame.rowconfigure(
        i,
        weight=1,
        minsize=45
    )

    for j in range(3):

        keypad_frame.columnconfigure(
            j,
            weight=1,
            minsize=75
        )

        # Create raised cell
        cell = Frame(
            master=keypad_frame,
            relief=RAISED,
            borderwidth=2,
            bg="#D0EFFF"
        )

        cell.grid(
            row=i,
            column=j,
            sticky="nsew"
        )

        # Get keypad value
        value = numbers[i][j]

        # Different button appearance
        if value == "Clear":
            button_bg = "#E74C3C"
            button_fg = "white"

        elif value == "Enter":
            button_bg = "#27AE60"
            button_fg = "white"

        else:
            button_bg = "#D0EFFF"
            button_fg = "#102A43"

        # Create keypad button
        keypad_button = Button(
            master=cell,
            text=value,
            font=("Arial", 10, "bold"),
            bg=button_bg,
            fg=button_fg,
            width=7,
            height=1,
            command=lambda v=value: keypad_press(v)
        )

        keypad_button.pack(
            padx=5,
            pady=5
        )


# ------------------------------------------------------------
# 13. SET ATM PIN BUTTON
# ------------------------------------------------------------

confirm_button = Button(
    root,
    text="🔒 SET ATM PIN",
    command=confirm_pin,
    bg="#FF5733",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18,
    relief=RAISED,
    borderwidth=3
)

confirm_button.place(x=105, y=400)


# ------------------------------------------------------------
# 14. MESSAGE BOX
# ------------------------------------------------------------

message_box = Text(
    root,
    height=4,
    width=42,
    bg="#E8F1F5",
    fg="#102A43",
    font=("Arial", 9),
    relief=SUNKEN,
    borderwidth=2
)

message_box.place(x=20, y=440)


# ------------------------------------------------------------
# 15. START GUI
# ------------------------------------------------------------

root.mainloop()