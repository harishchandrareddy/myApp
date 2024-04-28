import tkinter as tk

def display_message():
    name = name_entry.get()
    age = age_entry.get()
    message_label.config(text=f"Hello, {name}! You are {age} years old.")

root = tk.Tk()
root.title("Experience Calculator")

# Create input fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Create button to display message
submit_button = tk.Button(root, text="Submit", command=display_message)
submit_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Create label to display message
message_label = tk.Label(root, text="")
message_label.grid(row=3, columnspan=2, padx=10, pady=5)

root.mainloop()
