from tkinter import Label,Canvas,Frame,Tk


# created root of app
root = Tk()
root.title("My Digital Clock")
root.geometry("600x300")
root.rowconfigure(index=0,weight=1)
root.columnconfigure(index=0,weight=1)

root.config(bg="black")

# defined primary frame
primary_frm = Frame(root,bg="black")
primary_frm.rowconfigure(index=0,weight=1)
primary_frm.rowconfigure(index=0,weight=1)
primary_frm.grid(row=0,column=0)

# defining secondary 
secondary_frm = Frame(root,bg="black")
secondary_frm.rowconfigure(index=[0,1],weight=1)
secondary_frm.rowconfigure(index=[0,1],weight=1)
secondary_frm.grid(row=1,column=0)

# describing clock UI
time_lbl = Label(primary_frm,text="8 : 55PM",font=("consolas",30,"bold"),padx=130,pady=20)
time_lbl.grid(row=0,column=0,sticky="nsew")

date_lbl = Label(secondary_frm,text="08-05-2025",font=("consolas",22,"bold"),padx=70,pady=20)
date_lbl.grid(row=0,column=0,sticky="nsew")

# desgning circle of clock
canvas  = Canvas(secondary_frm,bg="black",border=0,height=100,width=100)
canvas.grid(row=0,column=1,sticky="nsew",padx=20)
canvas.create_oval(20,20,90,90,fill="purple")


# describing functionalities for clock
def update_clock_time():
    # added to get time module
    from datetime import datetime

    # to get current time and date
    time_data = datetime.now()

    # setting time here in time label
    time_lbl.config(text=time_data.strftime("%I:%M:%S%p"))

    # setting date here for date label
    date_lbl.config(text=time_data.strftime("%d-%M-%Y"))

    # setting color of the day/night
    if time_data.strftime("%p") == 'PM':
        canvas.create_oval(20,20,90,90,fill="purple")
    else:
        canvas.create_oval(20,20,90,90,fill="yellow")

    # setting it to call again and again to update time
    root.after(1000,update_clock_time)

update_clock_time()

# entery point of the loop
root.mainloop()