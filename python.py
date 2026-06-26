import tkinter as tk
from tkinter import messagebox
import webbrowser
import os


APP_NAME = "Elemental"


def join_game():
    place_id = place_id_entry.get().strip()
    job_id = job_id_entry.get().strip()

    if not place_id:
        messagebox.showerror("Missing Place ID", "Please enter a Roblox Place ID.")
        return

    if not place_id.isdigit():
        messagebox.showerror("Invalid Place ID", "The Place ID should only contain numbers.")
        return

    if job_id:
        url = f"roblox://experiences/start?placeId={place_id}&gameInstanceId={job_id}"
    else:
        url = f"roblox://experiences/start?placeId={place_id}"

    webbrowser.open(url)
    status_label.config(text="Join request sent to Roblox.")


def clear_fields():
    place_id_entry.delete(0, tk.END)
    job_id_entry.delete(0, tk.END)
    status_label.config(text="Ready.")


root = tk.Tk()
root.title(APP_NAME)
root.geometry("460x540")
root.resizable(False, False)
root.configure(bg="#0f1117")


# Logo
logo_path = os.path.join(os.path.dirname(__file__), "ElementalLogo.png")

if os.path.exists(logo_path):
    try:
        logo_image = tk.PhotoImage(file=logo_path)

        # Higher number = smaller logo.
        small_logo = logo_image.subsample(5, 5)

        root.iconphoto(False, small_logo)

        logo_label = tk.Label(
            root,
            image=small_logo,
            bg="#0f1117"
        )
        logo_label.image = small_logo
        logo_label.pack(pady=(18, 6))

    except Exception as error:
        print("Could not load logo:", error)
else:
    print("Logo not found:", logo_path)


title_label = tk.Label(
    root,
    text="Elemental",
    font=("Arial", 28, "bold"),
    fg="#ffffff",
    bg="#0f1117"
)
title_label.pack(pady=(4, 4))


subtitle_label = tk.Label(
    root,
    text="Roblox Auto Join Launcher",
    font=("Arial", 12),
    fg="#9ca3af",
    bg="#0f1117"
)
subtitle_label.pack(pady=(0, 20))


form_frame = tk.Frame(root, bg="#0f1117")
form_frame.pack(padx=30, fill="x")


place_id_label = tk.Label(
    form_frame,
    text="Place ID",
    font=("Arial", 10, "bold"),
    fg="#ffffff",
    bg="#0f1117",
    anchor="w"
)
place_id_label.pack(fill="x")


place_id_entry = tk.Entry(
    form_frame,
    font=("Arial", 13),
    bg="#1f2430",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
place_id_entry.pack(fill="x", ipady=9, pady=(6, 16))


job_id_label = tk.Label(
    form_frame,
    text="Server Job ID / gameInstanceId, optional",
    font=("Arial", 10, "bold"),
    fg="#ffffff",
    bg="#0f1117",
    anchor="w"
)
job_id_label.pack(fill="x")


job_id_entry = tk.Entry(
    form_frame,
    font=("Arial", 13),
    bg="#1f2430",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
job_id_entry.pack(fill="x", ipady=9, pady=(6, 22))


button_frame = tk.Frame(root, bg="#0f1117")
button_frame.pack(pady=4)


join_button = tk.Button(
    button_frame,
    text="Auto Join",
    command=join_game,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="#ffffff",
    activebackground="#1d4ed8",
    activeforeground="#ffffff",
    relief="flat",
    width=14,
    height=2,
    cursor="hand2"
)
join_button.grid(row=0, column=0, padx=7)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 12, "bold"),
    bg="#374151",
    fg="#ffffff",
    activebackground="#4b5563",
    activeforeground="#ffffff",
    relief="flat",
    width=10,
    height=2,
    cursor="hand2"
)
clear_button.grid(row=0, column=1, padx=7)


status_label = tk.Label(
    root,
    text="Ready.",
    font=("Arial", 10),
    fg="#86efac",
    bg="#0f1117"
)
status_label.pack(pady=(22, 0))


footer_label = tk.Label(
    root,
    text="Enter a Roblox Place ID and press Auto Join.",
    font=("Arial", 9),
    fg="#6b7280",
    bg="#0f1117"
)
footer_label.pack(pady=(8, 0))


root.mainloop()
