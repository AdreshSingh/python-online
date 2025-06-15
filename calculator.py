import tkinter
from tkinter import Label,Button,Frame

# create a root of app
root = tkinter.Tk()
root.title("Calculator")

# create frames
outer_frame = Frame(root,bg="black",padx=10,pady=10)
outer_frame.grid(row=0,column=0,sticky="nsew")

# create calculator components
header_frame = Frame(outer_frame)
header_frame.columnconfigure(index=0,weight=1)
header_frame.rowconfigure(index=0,weight=1)
header_frame.grid(row=0,column=0,sticky="nsew")

button_frame = Frame(outer_frame,bg="black",padx=10,pady=10)
button_frame.rowconfigure(index=[0,1,2,3],minsize=60)
button_frame.columnconfigure(index=[0,1,2,3],minsize=50)
button_frame.grid(row=1,column=0)

# create display
display_lbl = Label(
    header_frame,
    text="",
    bg="gray",
    fg="white",
    padx=15,
    pady=15,
    font=("Areil",20,"bold")
    )
display_lbl.grid(row=0,column=0,sticky="nsew")


# create a list of buttons
button_list = [
    ['1','2','3','C'],
    ['4','5','6','/'],
    ['7','8','9','X'],
    ['-','0','+','=']
]

# create functionality for calculator
def calculate(click_btn): # checks which button clicked
    if click_btn == '=':
        display_lbl['text'] = f"{eval(display_lbl['text'])}"
    elif click_btn == 'C':
        display_lbl['text'] = ""
    elif click_btn == 'X':
        display_lbl['text'] = display_lbl['text'] + '*'
    else:
        display_lbl['text'] += click_btn

# attach buttons to the button frame
for row in range(4):
    for col in range(4):
        Button(
            button_frame,
            text=button_list[row][col],
            padx=15,pady=15,
            command=lambda val=button_list[row][col]:calculate(val) #calls for every button
            ).grid(row=row,column=col)    

# start the app main loop
root.mainloop()