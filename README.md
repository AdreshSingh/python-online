# Mini Python Projects

This repository contains three beginner-friendly Python GUI projects built using Tkinter:

- **Digital Clock**
- **Notepad**
- **Calculator**

Each project is self-contained and demonstrates the use of Tkinter for building desktop applications.

---

## 1. Digital Clock

**File:** [`digital-clock.py`](digital-clock.py)

A simple digital clock that displays the current time and date, with a colored circle indicating AM/PM.

### Main Functions

- **`update_clock_time()`**  
  Updates the time and date labels every second using the current system time.  
  - Sets the time label (`time_lbl`) with the current time in `HH:MM:SSAM/PM` format.
  - Sets the date label (`date_lbl`) with the current date.
  - Changes the color of the circle to purple for PM and yellow for AM.
  - Uses `root.after(1000, update_clock_time)` to refresh every second.

---

## 2. Notepad

**File:** [`notepad.py`](notepad.py)

A basic text editor that allows you to open, edit, and save text files. Includes menu options and keyboard shortcuts.

### Main Functions

- **`aboutApp(e=None)`**  
  Shows an "About" dialog with app information.

- **`createNotice(title, message)`**  
  Displays a message box with a custom title and message.

- **`openFile(e=None)`**  
  Opens a file dialog to select a file, loads its content into the text area, and updates the window title.

- **`saveFile(e=None)`**  
  Saves the current content to the already opened file, or calls `saveAsFile()` if no file is open.

- **`saveAsFile(e=None)`**  
  Opens a "Save As" dialog to save the current content as a new file and updates the window title.

- **`closeFile(e=None)`**  
  Saves the current file (if any), clears the text area, and resets the open file state.

---

## 3. Calculator

**File:** [`calculator.py`](calculator.py)

A simple calculator with a GUI for basic arithmetic operations.

### Main Functions

- **`calculate(click_btn)`**  
  Handles button clicks:
  - If `=` is pressed, evaluates the expression in the display.
  - If `C` is pressed, clears the display.
  - If `X` is pressed, adds a multiplication operator (`*`).
  - Otherwise, appends the pressed button's value to the display.

---

## How to Run

Each project can be run individually:

```sh
python [digital-clock.py](http://_vscodecontentref_/0)
python [notepad.py](http://_vscodecontentref_/1)
python [calculator.py](http://_vscodecontentref_/2)
```
