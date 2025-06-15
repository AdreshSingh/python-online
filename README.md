# Mini Python Projects <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="Python Logo" width="100" height="100"/>

This repository contains three beginner-friendly Python GUI projects built using Tkinter:

- **Calculator**
- **Digital Clock**
- **Notepad**

Each project is self-contained and demonstrates the use of Tkinter for building desktop applications.

---

## 1. Calculator

**File:** [`calculator.py`](calculator.py)

A simple calculator with a GUI for basic arithmetic operations.

### Functions in Caculator

- **`calculate(click_btn)`**  
  Handles button clicks:
  - If `=` is pressed, evaluates the expression in the display.
  - If `C` is pressed, clears the display.
  - If `X` is pressed, adds a multiplication operator (`*`).
  - Otherwise, appends the pressed button's value to the display.

---

## 2. Digital Clock

**File:** [`digital-clock.py`](digital-clock.py)

A simple digital clock that displays the current time and date, with a colored circle indicating AM/PM.

### Functions in Digital Clock

- **`update_clock_time()`**  
  Updates the time and date labels every second using the current system time.  
  - Sets the time label (`time_lbl`) with the current time in `HH:MM:SSAM/PM` format.
  - Sets the date label (`date_lbl`) with the current date.
  - Changes the color of the circle to purple for PM and yellow for AM.
  - Uses `root.after(1000, update_clock_time)` to refresh every second.

---

## 3. Notepad

**File:** [`notepad.py`](notepad.py)

A basic text editor that allows you to open, edit, and save text files. Includes menu options and keyboard shortcuts.

### Functions in Notepad

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

## How to Run

Each project can be run individually:

```sh
python [calculator.py](calculator.py)
python [digital-clock.py](digital-clock.py)
python [notepad.py](notepad.py)
```
