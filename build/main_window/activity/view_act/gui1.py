
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller1 as db_controller
from tkinter.ttk import Treeview

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def view_activity():
    ViewActivity()


class ViewActivity(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 655,
            width = 1032,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1032.0,
            655.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            160.0,
            95.56231689453125,
            anchor="nw",
            text="View Activity History",
            fill="#0BBC8B",
            font=("RobotoRoman Bold", 32 * -1)
        )

        canvas.create_rectangle(
            83.0,
            153.29786682128906,
            948.0,
            508.6702117919922,
            fill="#D9D9D9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate('add'),
            relief="flat"
        )
        button_1.place(
            x=89.0,
            y=78.63981628417969,
            width=59.0,
            height=65.69908905029297
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            888.0,
            102.71733093261719,
            image=self.image_image_1
        )

        #canvas.create_rectangle(
         #   36.831298828125,
          #  948.0,
          #  38.82218027114868,
          #  fill="#EFEFEF",
          #  outline="")
          
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.delete_btn = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
           command=self.handle_delete,
            relief="flat"
        )
        self.delete_btn.place(
            x=717.0,
            y=528.5790405273438,
            width=231.0,
            height=54.74924087524414
        )
        
        
        self.columns = {
            "id": ["ID", 100],
            "act1": ["Activity", 130],
            "dur": ["Duration",130],
            "d_t": ["Date & Time", 130],
            "note": ["Notes",150]
        }
        
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.edit_btn = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_edit,
            relief="flat"
        )
        self.edit_btn.place(
            x=470.0,
            y=528.5800170898438,
            width=231.0,
            height=54.74924087524414
        )
                

        
        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )
        
        # Show the headings
        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.treeview.column(idx, width=txt[1])

        self.treeview.place(x=83, y=153.3, width=865, height=355.37)
        
        # Insert data
        self.handle_refresh()
     
         # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)
        
    def filter_treeview_records(self, query):
        self.treeview.delete(*self.treeview.get_children())
        # run for loop from original data
        for row in self.act_data1:
            # Check if query exists in any value from data
            if query.lower() in str(row).lower():
                # Insert the data into the treeview
                self.treeview.insert("", "end", values=row)
        self.on_treeview_select()

    def on_treeview_select(self, event=None):
        try:
            self.treeview.selection()[0]
        except:
            self.parent.selected_rid = None
            return
        # Get the selected item
        item = self.treeview.selection()[0]
        # Get the room id
        self.parent.selected_rid = self.treeview.item(item, "values")[0]
        # Enable the buttons
        self.delete_btn.config(state="normal")
        self.edit_btn.config(state="normal")
        
    def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        self.act_data1 = db_controller.get_activity()
        print("gui1",self.act_data1)
        for row in self.act_data1:
                self.treeview.insert("", "end", values=row)
            
    def handle_delete(self):
        if db_controller.delete_activity(self.parent.selected_rid):
            messagebox.showinfo("Success", "Successfully Deleted the activity")
        else:
            messagebox.showerror("Error" ,"Unable to delete activity")

        self.handle_refresh()
        
    def handle_navigate_back(self):
        self.parent.navigate("add")
        
    def handle_edit(self):
        self.parent.navigate("add")
        self.parent.windows["add"].initialize()

