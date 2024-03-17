from tkinter import *
from tkinter import colorchooser

# ------- GLOBALS -----------------------------

# colors
BG = 'black'
BUTTON_COLOR = "#e1e1e1"

# track all selected colors in a list
c_list = []


# ------- END GLOBALS -------------------------

# -------------- METHODS --------------------------------------------------------
def show():
    """
    shows the hex value of the selected color.
    :return: None
    """

    copy_button.configure(text="copy")

    colors = colorchooser.askcolor()
    # print(colors) -> shows ((r, g, b),'hex_value')

    # (None,None) returned if we close the window without selecting a color.
    # so, inorder to handle that exception.
    if colors[1] is not None:
        # making text area un-disabled.
        color_text.config(state='normal', fg=str(colors[1]))
        color_text.insert("1.0", str(colors[1]))

        # making text area disabled again.
        color_text.config(state='disabled')
        c_list.append(colors[1])


def copy():
    """
    put the hex-value into your clipboard
    :return:
    """
    if len(c_list) > 0:
        hex_value = c_list[-1]  # last element in the list

        # print(c_list)
        # print(hex_value)

        window.clipboard_append(hex_value)  # copied to clipboard

        copy_button.configure(text="copied")


# -------------- END METHODS ----------------------------------------------------


# ============= MAIN WINDOW ====================================================

window = Tk()
window.title('Hex-Color Finder')
window.resizable(False, False)

frame = Frame(window, relief=RAISED, bd=10,
              bg=BG, padx=10, pady=5)
frame.pack()

color_text = Text(frame,
                  font=('Ink free', 40, 'bold'),
                  fg='#00FF00', state='disabled',
                  bg=BG, width=8, height=1)
color_text.pack()

Button(frame, text='Hex color', command=show, bg=BUTTON_COLOR, relief=RAISED,
       font=('Consoles', 11, 'bold')).pack(side=LEFT, padx=32, pady=5)
copy_button = Button(frame, text='copy', command=copy, bg=BUTTON_COLOR, relief=RAISED,
                     font=('Consoles', 11, 'bold italic'), width=8)
copy_button.pack(side=LEFT, pady=5)
window.mainloop()

# ============= END MAIN WINDOW ================================================
