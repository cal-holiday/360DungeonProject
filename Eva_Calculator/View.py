import tkinter as tk
from tkinter import ttk #slightly more improved/updated than tk

#(tk.TK) means inherit from tk object
#we know have access to all of tk methods
class View(tk.Tk):

    #class variable/constant can be used throughout
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4

    #button array
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title('PyCalc1.0') #title of window

        self.value_var = tk.StringVar()
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()

    def main(self):
        #infinite loop til you click the x button
        #this generates GUI screen! (empty)
        self.mainloop()


    #creates main frame to add textfields, buttons, etc
    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady= self.PAD)


    #single underscore indicates this method is only used by this class
    #not the same as private in java
    def _make_entry(self):
        #add textfield
        # puts cursor on right side, user cannot interact with textfield
        entry = ttk.Entry(self.main_frame, justify='right', textvariable=self.value_var,state='disabled')
        entry.pack(fill='x') #.pack adds to frame

    def _make_buttons(self):
            outer_frame = ttk.Frame(self.main_frame) #add button frame to main frame
            outer_frame.pack()

            frame = ttk.Frame(outer_frame)
            frame.pack()

            buttons_in_row = 0

            #for loop!
            for caption in self.button_captions:
                if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                    frame = ttk.Frame(outer_frame)
                    frame.pack()
                    buttons_in_row = 0

                #tell controller when button is clicked
                button = ttk.Button(frame, text=caption,
                                    command=(lambda button=caption: self.controller.on_button_click(button)))
                button.pack(side='left')
                buttons_in_row += 1


    #so that no matter how you expand the window the calculator frame will be in the center all the time
    def _center_window(self):
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )

