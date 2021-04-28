from tkinter import *
from tkinter import ttk
import periodictable

# Global variables
s_orbital = 2
p_orbital = 6
d_orbital = 10
f_orbital = 14

grid_col = 18

Be_index = 19
Mg_index = 37


class Element:
    def __init__(self, name, symbol, atomic_num, atomic_mass):
        self.name = name
        self.symbol = symbol
        self.atomic_num = atomic_num
        self.atomic_mass = atomic_mass

    def add_block(self, mainframe, block, grid_index):
        row_index = grid_index // grid_col
        col_index = grid_index % grid_col
        Label(mainframe, text="\n".join([str(e) for e in block]), height=8, width=8).grid(
              column=col_index, row=row_index, sticky="NESW")


# Setup Tkinter frame
root = Tk()
root.title("Periodic Table")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky="NESW")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add all elements from 'periodictable' library to an array
elements = []
for el in periodictable.elements:
    elements.append(el.name)

# Get elements' properties from library and display it on the table
grid_index = 0
elements_len = len(elements)
block = []
for i in range(1, elements_len):
    block.append(i)
    block.append(periodictable.elements[i])
    block.append("{:.3f}".format(periodictable.elements[i].mass))

    atom = Element(periodictable.elements[i].name, periodictable.elements[i], 
                    grid_index, periodictable.elements[i].mass)
    atom.add_block(mainframe, block, grid_index)

    block.clear()

    # Space out each element block appropriately by incrementing grid_index
    if (grid_index == 0):
        grid_index += p_orbital + d_orbital
    elif (grid_index == Be_index or grid_index == Mg_index):
        grid_index += d_orbital
    grid_index += 1

root.mainloop()