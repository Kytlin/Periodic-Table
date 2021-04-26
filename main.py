from tkinter import *
from periodictable import elements

# Create & Configure window 
window = Tk()
window.geometry('800x600')

# Creating the square frame
square_frame = Frame(window, width=300, height=300)
square_frame.grid(column=0, row=0)
square_frame.grid_propagate(False)
square_frame.rowconfigure(0, weight=1)
square_frame.columnconfigure(0, weight=1)

# Setting Up Grid
Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)

# Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(5):
    Grid.rowconfigure(window, row_index, weight=1)
    for col_index in range(10):
        Grid.columnconfigure(window, col_index, weight=1)
        block = []
        
        block.append(elements[(row_index * 10) + col_index + 1].symbol)
        block.append(str((row_index * 10) + col_index + 1))

        atomic_number = Label(window, text="\n\n".join(block), height="70", width="70")
        atomic_number.grid(row=row_index, column=col_index, sticky="NESW")  

window.mainloop()