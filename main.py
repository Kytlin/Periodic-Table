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

def more_info(blocks, i):
    top = Toplevel()
    top.title("More Info")

    print(i)
    print(blocks[i]["name"])

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)

    labelExample = Label(top, text="{} ({})".format(blocks[i]["name"], blocks[i]["symbol"]), height=3, width=30).grid(column=0, row=0)

def add_block(mainframe, blocks, block, grid_index, atomic_num):
    row_index = grid_index // grid_col
    col_index = grid_index % grid_col
    element = Button(mainframe, text="\n".join([str(e) for e in block]), height=8, width=8, command=lambda: more_info(blocks, atomic_num)).grid(
            column=col_index, row=row_index, sticky=(N, W, E, S))


# Setup Tkinter frame
root = Tk()
root.title("Periodic Table")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
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
blocks = []
for i in range(1, elements_len):
    block.append(i)
    block.append(periodictable.elements[i])
    block.append("{:.3f}".format(periodictable.elements[i].mass))

    properties = {"atomic_num": i, "name": periodictable.elements[i - 1].name, 
             "symbol": periodictable.elements[i - 1], "mass": "{:.3f}".format(periodictable.elements[i - 1].mass)}
    blocks.append(properties)

    # atom = Element(periodictable.elements[i].name, periodictable.elements[i], 
    #                grid_index, periodictable.elements[i].mass)
    add_block(mainframe, blocks, block, grid_index, i)

    block.clear()

    # Space out each element block appropriately by incrementing grid_index
    if (grid_index == 0):
        grid_index += p_orbital + d_orbital
    elif (grid_index == Be_index or grid_index == Mg_index):
        grid_index += d_orbital
    grid_index += 1

root.mainloop()