import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import random
import urllib.request


APP_NAME = "Elemental"

LOGO_FILE = "ElementalLogo.png"
LOGO_URL = "https://raw.githubusercontent.com/hack-spectacle/Elemental/main/ElementalLogo.png"

# Add/change Roblox game IDs here.
RANDOM_GAME_IDS = [
    "2788229376",      # Da Hood
    "286090429",       # Arsenal
    "3233893879",      # Bad Business
    "292439477",       # Phantom Forces
    "6872265039",      # BedWars
    "7991339063",      # Rainbow Friends
    "920587237",       # Adopt Me
    "2753915549",      # Blox Fruits
    "6284583030",      # Pet Simulator X
    "142823291",       # Murder Mystery 2
]


def get_file_path(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def download_logo_if_missing():
    logo_path = get_file_path(LOGO_FILE)

    if os.path.exists(logo_path):
        return logo_path

    try:
        urllib.request.urlretrieve(LOGO_URL, logo_path)
        print("Downloaded logo:", logo_path)
        return logo_path
    except Exception as error:
        print("Could not download logo:", error)
        return None


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
    status_label.config(text=f"Joining Roblox game: {place_id}")


def clear_fields():
    place_id_entry.delete(0, tk.END)
    job_id_entry.delete(0, tk.END)
    random_game_label.config(text="Random game: none selected")
    status_label.config(text="Ready.")


def insert_random_game():
    random_id = random.choice(RANDOM_GAME_IDS)

    place_id_entry.delete(0, tk.END)
    place_id_entry.insert(0, random_id)

    random_game_label.config(text=f"Random game inserted: {random_id}")
    status_label.config(text="Random Place ID ready. Press Auto Join.")


root = tk.Tk()
root.title(APP_NAME)
root.geometry("460x640")
root.resizable(False, False)
root.configure(bg="#0f1117")


# Logo
logo_path = download_logo_if_missing()

if logo_path and os.path.exists(logo_path):
    try:
        logo_image = tk.PhotoImage(file=logo_path)

        # Higher number = smaller logo.
        small_logo = logo_image.subsample(7, 7)

        root.iconphoto(False, small_logo)

        logo_label = tk.Label(
            root,
            image=small_logo,
            bg="#0f1117"
        )
        logo_label.image = small_logo
        logo_label.pack(pady=(16, 4))

    except Exception as error:
        print("Could not load logo:", error)
else:
    print("Logo not found and could not be downloaded.")


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
subtitle_label.pack(pady=(0, 18))


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
job_id_entry.pack(fill="x", ipady=9, pady=(6, 18))


random_frame = tk.Frame(root, bg="#171b24")
random_frame.pack(padx=30, pady=(0, 16), fill="x")


random_title = tk.Label(
    random_frame,
    text="Random Game Box",
    font=("Arial", 11, "bold"),
    fg="#ffffff",
    bg="#171b24",
    anchor="w"
)
random_title.pack(fill="x", padx=14, pady=(12, 2))


random_game_label = tk.Label(
    random_frame,
    text="Random game: none selected",
    font=("Arial", 10),
    fg="#9ca3af",
    bg="#171b24",
    anchor="w"
)
random_game_label.pack(fill="x", padx=14, pady=(0, 10))


random_button = tk.Button(
    random_frame,
    text="Insert Random Game ID",
    command=insert_random_game,
    font=("Arial", 11, "bold"),
    bg="#7c3aed",
    fg="#ffffff",
    activebackground="#6d28d9",
    activeforeground="#ffffff",
    relief="flat",
    height=2,
    cursor="hand2"
)
random_button.pack(fill="x", padx=14, pady=(0, 14))


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
status_label.pack(pady=(20, 0))


footer_label = tk.Label(
    root,
    text="Enter a Place ID or insert a random one.",
    font=("Arial", 9),
    fg="#6b7280",
    bg="#0f1117"
)
footer_label.pack(pady=(8, 0))


root.mainloop()
