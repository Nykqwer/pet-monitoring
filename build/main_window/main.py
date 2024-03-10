
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8

from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from main_window.profile.main import Profile
from main_window.activity.main import Activity
from main_window.health.main import Health
from controller import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





def mainWindow():
    MainWindow()

class MainWindow(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        
        self.geometry("1298x655")
        self.configure(bg = "#0BBC8B")
        
        self.current_window = None
        self.current_window_label = StringVar()
    
        self.canvas = Canvas(
            self,
            bg = "#0BBC8B",
            height = 655,
            width = 1298,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            266.0,
            0.0,
            1298.0,
            655.0,
            fill="#FFFFFF",
            outline="")
        
          # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=60, width=7)

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.act_btn = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.act_btn, "act"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.act_btn.place(
            x=0.0,
            y=216.0,
            width=266.0,
            height=71.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.health_btn = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.health_btn, "heal"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.health_btn.place(
            x=0.0,
            y=287.0,
            width=266.0,
            height=71.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.pet_btn = Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.pet_btn, "prof"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat"
        )
        self.pet_btn.place(
            x=0.0,
            y=145.0,
            width=266.0,
            height=71.0
        )
        
      

        self.canvas.create_text(
            27.0,
            39.0,
            anchor="nw",
            text="Fur & Feather",
            fill="#FFFFFF",
            font=("RobotoRoman Bold", 34 * -1)
        )
        
        self.windows = {
            "prof": Profile(self),
            "act": Activity(self),
            "heal": Health(self)
               
         }
        self.handle_btn_press(self.pet_btn, "prof")
        self.sidebar_indicator.place(x=0, y=133)
        
        self.current_window.place(x=270, y=-3, width=1032.0, height=658.0)
        self.current_window.tkraise()
    
     
    def place_sidebar_indicator(self):
        pass     
     
    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=270, y=-3, width=1032.0, height=658.0)
     

    def handle_dashboard_refresh(self):
        # Recreate the dash window
        self.windows["prof"] = Profile(self)



# Create an instance of MainWindow


#if __name__ == "__main__":
#   main_window = MainWindow()
 #  main_window.mainloop()
    