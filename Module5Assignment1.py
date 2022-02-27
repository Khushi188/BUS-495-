# The goal of this program is to build a temperature converter application using GUI that
# allows the user to input temperature in degrees Fahrenheit and push a button to convert that
# temperature to degrees Celsius.
#Source: realpython.com & learn.sparkfun.com
#Lines of code I added: 15,16,27,35,60 (indicated on the line as well)

import tkinter as tk

# Declare global variables:
temp_c = None
temp_f = None

# This function is called whenever the button is pressed:
def convert():
    global temp_c #code added by me (declared temperatures as global variables so they can be accessed from within the function)
    global temp_f #same as line 15

 # Convert Celsius to Fahrenheit and update label (through textvariable)
    try:
        val = temp_c.get()
        temp_f.set((val * 9.0 / 5) + 32)
    except:
        pass

# Create the main window:
root = tk.Tk()
root.title("Temperature Converter")
root.resizable(0,0) #Code added by me in order to prohibit resizing of the Tkinrer window


# Create the main container:
frame = tk.Frame(root)

# Lay out the main container, specify that we want it to grow with window size
frame.pack(fill=tk.BOTH, expand=True) #Code added by me (Created a frame within the window to control widgets)

# Allow middle cell of grid to grow when window is resized
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

# Variables for holding temperature data
temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()

# Create widgets
entry_celsius = tk.Entry(frame, width=20, textvariable=temp_c)
label_unitc = tk.Label(frame, text="°C")
label_equal = tk.Label(frame, text="is equal to")
label_fahrenheit = tk.Label(frame, textvariable=temp_f)
label_unitf = tk.Label(frame, text="°F")
button_convert = tk.Button(frame, text="Convert", command=convert)

# Lay out widgets
entry_celsius.grid(row=0, column=1, padx=5, pady=5)
label_unitc.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
label_equal.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
label_fahrenheit.grid(row=1, column=1, padx=5, pady=5)
label_unitf.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
button_convert.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.E)

# Place cursor in entry box by default (Code added by me)
entry_celsius.focus()

# Run forever!
root.mainloop()