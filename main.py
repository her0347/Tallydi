import tkinter as tk
from tkinter import filedialog, messagebox
from mido import MidiFile

def count_notes():
    file_path = filedialog.askopenfilename(filetypes=[("MIDI Files", "*.mid *.midi")])
    if not file_path:
        return

    try:
        mid = MidiFile(file_path)
        note_count = 0
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    note_count += 1
        
        result_label.config(text=f"Total Notes: {note_count}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file: {e}")

# Create main window
root = tk.Tk()
root.title("Tallydi GUI")
root.geometry("300x200")
image = tk.PhotoImage(file="icon.png")
# Display image
label = tk.Label(image=image)
label.pack()
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(False, icon)



# GUI Elements
btn = tk.Button(root, text="Select MIDI File", command=count_notes)
btn.pack(pady=20)

result_label = tk.Label(root, text="Total Notes: 0", font=("Arial", 12))
result_label.pack()

root.mainloop()