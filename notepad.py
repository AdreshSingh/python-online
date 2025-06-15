import tkinter as tk
from tkinter import messagebox,Menu,filedialog

# creating root of app
root = tk.Tk()
root.title("Notepad 2")
root.geometry("1200x620")

menubar = Menu(root)

# functionality of apps
#? about app ✅
def aboutApp(e=None):
    print(e)
    messagebox.showinfo("About","This App is property of All4One | Devank")


def createNotice(title,message):
    messagebox.showinfo(title=title,message=message)

alreadyOpenedFile = ""
def openFile(e=None):
    # open dialog
    location = filedialog.askopenfilename()
    
    if location:
        # load the file content in the text box
        with open(location,'r') as file:
            main_txt.insert("1.0",file.read())
    
        # change the root title
        root.title(f"{location.split('/')[-1]} Notepad-2")

        # updating global variable
        global alreadyOpenedFile 

        alreadyOpenedFile= location

def saveFile(e=None):
    if alreadyOpenedFile != "":
        with open(alreadyOpenedFile,'w') as file:
            file.write(main_txt.get("1.0","end-1c"))
            createNotice("File saved successfully!")
        return
    
    # if file not created
    saveAsFile()

def saveAsFile(e=None):
    newFileLocation = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[
            # our own app extension
            # ("Special Notepad 2 File","*.txt2"),
            ("Text File","*.txt"),
            ("All Files","*.*")
            ])
    if newFileLocation:
        newFileLocation.write(main_txt.get("1.0","end-1c"))
         # change the root title
        root.title(f"{newFileLocation.name.split('/')[-1]} Notepad-2")

        createNotice("file","New File saved")

def closeFile(e=None):
    global alreadyOpenedFile
    createNotice("INFO","Closing the file")
    if alreadyOpenedFile:
        with open(alreadyOpenedFile,'w') as file:
            file.write(main_txt.get("1.0","end-1c"))
            createNotice("INFO","file saved")
        alreadyOpenedFile = ""
        main_txt.delete("1.0",tk.END)


# creating menus inside menubar

#! FILE MENU
file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)

#! FILE MENU OPTION
# open menu
file.add_cascade(label="Open",command=openFile)

# save option
file.add_cascade(label="Save",command=saveFile)

# save as option
file.add_cascade(label="Save As",command=saveAsFile)

# close option
file.add_cascade(label="Close",command=closeFile)

#! HELP MENU
help = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)

help.add_cascade(label="Aout",command=aboutApp)


# defining UI of App
main_txt = tk.Text(root)
main_txt.pack(expand=1,fill=tk.BOTH)





# creating shortcuts using bind()
root.bind('<Control-h>',aboutApp)
root.bind('<Control-o>',openFile)
root.bind('<Control-s>',saveFile)
root.bind('<Control-C>',closeFile)
root.bind('<Control-S>',saveAsFile)




# setted menubar to root widget
root.config(menu=menubar)
# entry point of app
root.mainloop()