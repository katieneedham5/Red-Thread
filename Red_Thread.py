import tkinter as tk
import customtkinter as ctk
import calendar
from datetime import datetime
import json

period_data = []

#load json as data
def load_data(file):
    try:
        with open (file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: The file was not found.")
        data = []
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON, or is corrupted.")
        data = []
    return data

def save_data(file, data):
    try:
        with open (file, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Could not save data to file. {e}")

def new_period():
    {

    }

def edit_period():
    {

    }

def calculate_cycle():
    {

    }

def calculate_phase():
    {

    }


root = tk.Tk()
root.resizable(False, False)
root.title("Red Thread")
root.geometry("600x800")

#Appearance
ctk.set_appearance_mode("dark")

#Date
current_date = datetime.now()
selected_date = None
logs = {} #stores logged periods {date_string: [logs]}

"""Labels and buttons"""
def init_ui():
    settings_button = tk.Button(
        root,
        text="* (useless)"
    ) 

    top_label = tk.Label(
        root,
        text="RED THREAD"
    ) 

    prediction_box = tk.Frame(
        root,
        bg="pink",
        bd=2,
        width=200,
        height=200
    ) 

    add_button = tk.Button(
        root,
        text="Add",
        command= new_period()
    ) 

    edit_button = tk.Button(
        root,
        text="Edit",
        command= edit_period()
    ) 

    average = tk.Label(
        root,
        text= "Average cycle length: "
    ) 
    predicted = tk.Label(
        root,
        text= "Predicted phase: "
    )

    settings_button.pack()
    top_label.pack()
    prediction_box.pack()

    add_button.pack()
    edit_button.pack()

    average.pack()
    predicted.pack()


"""Calendar"""

def cal_header():
    """Navigation and month/year display"""
    return

def cal_grid():
    """Main grid with days"""

    return


""""""


if __name__ == "__main__":
    period_data = load_data(".\data.json") #temp file path, stupid windows
    print(period_data)

    root.mainloop()
    init_ui()


"""GUI NOTES"""
'''
window = tk.Tk() #initializes window
#label- a widget that displays text or images
#button- a widget that can be clicked to perform an action
#entry- a widget that allows user input(single line of text)
#text- a widget that allows user input(multi-line text area)
#frame- a container widget to hold other widgets (provides padding)

name = entry.insert(tk.END, string="enter text here") #gets the text from the entry widget
#delete operation- removes text from the entry widget
#insert operation- adds text to the entry widget at a specific position
#large text boxes require .get("1.0", tk.END) to get all of the input

frame = tk.Frame(padx=10, pady=10, background="pink") #creates a frame with padding
frame_label = tk.Label(master=frame, text="Inside Frame")
frame_label.pack()
frame.pack()

#This goes last to open the window . ?
window.mainloop()
'''