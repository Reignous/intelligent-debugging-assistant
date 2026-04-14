import customtkinter as ctk
from tkinter import filedialog
from main import run_user_code
import threading

# Appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

selected_file = ""

def choose_file():
    global selected_file
    selected_file = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py")]
    )
    if selected_file:
        file_label.configure(text=selected_file)

def run_debugger_thread():
    run_btn.configure(state="disabled", text="⏳ Analyzing...")
    output_box.delete("1.0", "end")
    output_box.insert("end", "🔍 Running your code...\n")
    result = run_user_code(selected_file)
    output_box.delete("1.0", "end")
    output_box.insert("end", result)
    run_btn.configure(state="normal", text="▶  Run Debugger")

def run_debugger():
    if selected_file:
        thread = threading.Thread(target=run_debugger_thread)
        thread.start()
    else:
        output_box.delete("1.0", "end")
        output_box.insert("end", "⚠️  Please select a Python file first.")

# Main window
root = ctk.CTk()
root.title("Intelligent Debugging Assistant")
root.geometry("900x620")
root.resizable(True, True)

# Title bar
title_frame = ctk.CTkFrame(root, fg_color="transparent")
title_frame.pack(pady=(24, 4), padx=30, fill="x")

title_label = ctk.CTkLabel(
    title_frame,
    text="🐛  Intelligent Debugging Assistant",
    font=ctk.CTkFont(size=24, weight="bold")
)
title_label.pack(side="left")

subtitle_label = ctk.CTkLabel(
    title_frame,
    text="Powered by Gemini AI",
    font=ctk.CTkFont(size=13),
    text_color="gray"
)
subtitle_label.pack(side="left", padx=(12, 0), pady=(6, 0))

# Divider
divider = ctk.CTkFrame(root, height=2, fg_color="#2a2a2a")
divider.pack(fill="x", padx=30, pady=(0, 16))

# File selection area
file_frame = ctk.CTkFrame(root)
file_frame.pack(padx=30, pady=(0, 16), fill="x")

file_inner = ctk.CTkFrame(file_frame, fg_color="transparent")
file_inner.pack(padx=16, pady=12, fill="x")

select_btn = ctk.CTkButton(
    file_inner,
    text="📂  Select Python File",
    width=180,
    height=38,
    corner_radius=8,
    command=choose_file
)
select_btn.pack(side="left")

file_label = ctk.CTkLabel(
    file_inner,
    text="No file selected",
    font=ctk.CTkFont(size=12),
    text_color="gray"
)
file_label.pack(side="left", padx=(16, 0))

# Run button
run_btn = ctk.CTkButton(
    root,
    text="▶  Run Debugger",
    width=200,
    height=44,
    corner_radius=10,
    font=ctk.CTkFont(size=15, weight="bold"),
    fg_color="#1f6aa5",
    hover_color="#1a5a8f",
    command=run_debugger
)
run_btn.pack(pady=(0, 16))

# Output label
output_label = ctk.CTkLabel(
    root,
    text="Output",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color="gray"
)
output_label.pack(anchor="w", padx=30)

# Output box
output_box = ctk.CTkTextbox(
    root,
    font=ctk.CTkFont(family="Courier", size=13),
    corner_radius=10,
    wrap="word"
)
output_box.pack(padx=30, pady=(4, 20), fill="both", expand=True)

# Bottom bar
bottom_frame = ctk.CTkFrame(root, fg_color="transparent")
bottom_frame.pack(pady=(0, 12))

appearance_label = ctk.CTkLabel(
    bottom_frame,
    text="Theme:",
    font=ctk.CTkFont(size=12),
    text_color="gray"
)
appearance_label.pack(side="left", padx=(0, 8))

appearance_menu = ctk.CTkOptionMenu(
    bottom_frame,
    values=["Dark", "Light", "System"],
    width=100,
    command=lambda mode: ctk.set_appearance_mode(mode.lower())
)
appearance_menu.pack(side="left")

root.mainloop()