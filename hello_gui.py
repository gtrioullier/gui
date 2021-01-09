import tkinter as tk

greeting_count = 1

# create the main window (entry point)
root = tk.Tk()

# create a label widget
label = tk.Label(root, text="")

# create a response to event click on button "Greet"
def set_message():
    global greeting_count
    label["text"] = f"Hello! ({greeting_count})"
    greeting_count += 1

# create button widget "Greet"
button = tk.Button(root, text="Greet", command=set_message)

# add widgets to the master
button.pack()
label.pack()

# start main window
root.mainloop()
