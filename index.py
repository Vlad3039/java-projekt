import tkinter as tk

def on_click():
    print("Button wurde gedrückt!")

# Fenster erstellen
root = tk.Tk()
root.title("Mein Fenster")

# Button erstellen
button = tk.Button(root, text="Klick mich", command=on_click)
button.pack(pady=20)

# Fenster starten
root.mainloop()
