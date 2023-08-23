import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.attributes("-topmost", True)  # Keep the window on top

# Set transparency (0.0 is fully transparent, 1.0 is opaque)
transparency = 0.3
root.attributes("-alpha", transparency)

# Function to update the time
def update_time():
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create a label to display the time
label = tk.Label(root, font=('calibri', 100, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()  # Start the time update loop

# Run the main event loop
root.mainloop()
