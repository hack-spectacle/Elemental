import tkinter as tk
from tkinter import messagebox
import webbrowser


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
root.geometry("440x330")
root.resizable(False, False)
root.configure(bg="#0f1117")

title_label = tk.Label(
    root,
    text="Elemental",
    font=("Arial", 26, "bold"),
    fg="#ffffff",
    bg="#0f1117"
)
title_label.pack(pady=(22, 4))

subtitle_label = tk.Label(
    root,
    font=("Arial", 11),
    fg="#9ca3af",
    bg="#0f1117"
)
subtitle_label.pack(pady=(0, 18))

form_frame = tk.Frame(root, bg="#0f1117")
form_frame.pack(padx=28, fill="x")

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
    font=("Arial", 12),
    bg="#1f2430",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
place_id_entry.pack(fill="x", ipady=8, pady=(5, 14))

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
    font=("Arial", 12),
    bg="#1f2430",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
job_id_entry.pack(fill="x", ipady=8, pady=(5, 18))

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
    height=2
)
join_button.grid(row=0, column=0, padx=6)

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
    height=2
)
clear_button.grid(row=0, column=1, padx=6)

status_label = tk.Label(
    root,
    text="Ready.",
    font=("Arial", 10),
    fg="#86efac",
    bg="#0f1117"
)
status_label.pack(pady=(18, 0))

root.mainloop()
text="Roblox Auto Join Launcher",
