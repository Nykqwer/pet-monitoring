
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller1 as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_health():
    UpdateHealth()



class UpdateHealth(Frame):
     def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_r_id = self.parent.selected_rid
      
       
        self.data = {
            "id": StringVar(),
            "event": StringVar(),
            "w_event": StringVar(),
            "DT_heal": StringVar(),
            "meds": StringVar(),
        }
        
        self.initialize()
        
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 655,
            width = 1032,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            697.0,
            73.66262817382812,
            699.0,
            585.3191528320312,
            fill="#EFEFEF",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1032.0,
            655.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            371.0,
            75.0,
            anchor="nw",
            text="Update Health Events\n",
            fill="#0BBC8B",
            font=("RobotoRoman Bold", 30 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_update,
            relief="flat"
        )
        button_1.place(
            x=401.0,
            y=562.0,
            width=231.0,
            height=54.74924087524414
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            248.0,
            230.0,
            image=self.image_image_1
        )
        #ID

  

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            248.0,
            476.0,
            image=self.image_image_2
        )
        
        self.id_text =self.canvas.create_text(
            111.0,
            470.0,
            anchor="nw",
            text="01",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            252.0,
            245.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            self,
            textvariable=self.data["event"],
            bd=0,
            bg="#E6E6E6",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=111.0,
            y=230.0,
            width=282.0,
            height=28.0
        )

        self.canvas.create_text(
            111.0,
            232.0,
            anchor="nw",
            text="groom\n",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            248.0,
            360.0,
            image=self.image_image_3
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            246.5,
            375.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            self,
            textvariable=self.data["w_event"],
            bd=0,
            bg="#E6E6E6",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
        
            x=111.0,
            y=360.0,
            width=271.0,
            height=28.0
        )

        self.canvas.create_text(
            111.0,
            362.0,
            anchor="nw",
            text="Pet Groomer Shop",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            667.0,
            360.0,
            image=self.image_image_4
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            668.0,
            375.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            self,
            bd=0,
            textvariable=self.data["meds"],
            bg="#E6E6E6",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=524.0,
            y=360.0,
            width=288.0,
            height=28.0
        )

        self.canvas.create_text(
            576.0,
            362.0,
            anchor="nw",
            text="Ear Wax ",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            667.0,
            230.0,
            image=self.image_image_5
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            668.0,
            245.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            self,
            textvariable=self.data["DT_heal"],
            bd=0,
            bg="#E6E6E6",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
        
            x=524.0,
            y=230.0,
            width=288.0,
            height=28.0
        )

        self.canvas.create_text(
            576.0,
            232.0,
            anchor="nw",
            text="Oct 25 12 A.M",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate('view'),
            relief="flat"
        )
        button_2.place(
            x=79.0,
            y=38.0,
            width=81.0,
            height=73.0
        )

        self.canvas.create_rectangle(
            160.0,
            112.0,
            867.0,
            113.0,
            fill="#D9D9D9",
            outline="")
     
     def initialize(self):
        self.selected_r_id = self.parent.selected_rid
        self.rooms_data = self.parent.heal_data
        print("Debug: self.selected_r_id =", self.selected_r_id)
        print("Debug: self.rooms_data =", self.rooms_data)      

        # Filter out all reservations for selected id reservation
        if self.rooms_data is not None:
            self.selected_rooms_data = list(
                filter(lambda x: str(x[0]) == self.selected_r_id, self.rooms_data)
            )

            if self.selected_rooms_data:
                self.selected_rooms_data = self.selected_rooms_data[0]

                self.canvas.itemconfigure(self.id_text, text=self.selected_rooms_data[0])
                self.data["event"].set(self.selected_rooms_data[1])
                self.data["w_event"].set(self.selected_rooms_data[2])
                self.data["DT_heal"].set(self.selected_rooms_data[3])
                self.data["meds"].set(self.selected_rooms_data[4])

     def handle_update(self):
        result = db_controller.update_health(
            self.selected_r_id,
            event=self.data["event"].get(),
            w_event=self.data["w_event"].get(),
            DT_heal=self.data["DT_heal"].get(),
            medication=self.data["meds"].get(),    
        )

        if result:
            messagebox.showinfo("Successful", "Details updated successfully")
            self.parent.navigate("view")
            self.parent.windows.get("view").handle_refresh()
            # clear all fields
            for label in self.data.keys():
                self.data[label].set("")
            self.parent.windows['view'].handle_refresh()
        else:
            messagebox.showerror("Error", "Failed to update details")
 