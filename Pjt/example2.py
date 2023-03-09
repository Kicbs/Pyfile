# Import tkinter and ttk modules
import tkinter as tk
from tkinter import ttk

# Create a root window
root = tk.Tk()
root.title("GUI Example")

def update_entry(event):
    # Get the selected value from combobox
    selected = combo.get()
    # Get the corresponding information from data dictionary
    info = ip_dict.get(selected, "No information available")
    # Set the text of entry widget to info
    entry.delete(0, tk.END)
    entry.insert(0, info)


# Open log file for reading
with open("access.log", "r") as f:
    # Initialize an empty dictionary
    ip_dict = {}
    # Loop through each line
    for line in f:
        ip, data1, data2 = line.partition(" - ")
        # Check if IP address is already in dictionary
        if ip in ip_dict:
            # Append timestamp to existing list
            ip_dict[ip].append(data2)
        else:
            # Create a new list with timestamp
            ip_dict[ip] = [data2]
#print(ip_dict)
# Open new file for writing
#with open("data345.txt", "w") as g:
    # Loop through dictionary items
 #   for key, value in ip_dict.items():
        # Write IP address, count, first time and last time to file
#        g.write(f"{key} {len(value)} {value[0][3:29]} {value[-1][3:29]}\n")
        

combo = ttk.Combobox(root, values=list(ip_dict.keys()))
combo.pack()

# Bind an event handler function to combobox selection change
combo.bind("<<ComboboxSelected>>", update_entry)

# Create an entry widget to display information
entry = tk.Entry(root)
entry.pack()

# Start the main loop of root window
root.mainloop()
