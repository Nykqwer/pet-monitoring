
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


import base64
from io import BytesIO
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk,ImageFile,ImageDraw
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




#window.geometry("1032x655")
#window.configure(bg = "#FFFFFF")

def add_profile():
    AddProfile()
    

import base64
ImageFile.LOAD_TRUNCATED_IMAGES = True

def decode_base64(encoded_str):
    try:
        # Ensure encoded_str is of type bytes
        if isinstance(encoded_str, str):
            encoded_str = encoded_str.encode('utf-8')

        # Add padding to the base64 bytes if needed
        padding = b'=' * (4 - (len(encoded_str) % 4))
        encoded_str += padding

        # Decode the base64 bytes
        decoded_data = base64.b64decode(encoded_str)

        return decoded_data
    except base64.binascii.Error as e:
        print(f"Error decoding base64: {e}")
        return None


class AddProfile(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.configure(bg="#FFFFFF")
        self.retrieve_data_fromDb()
        self.image_retrieve()
        self.recommendation()
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

        canvas.create_rectangle(
            19.9998779296875,
            425.000244140625,
            647.9998404979706,
            427.0002440214157,
            fill="#D9D9D9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("edit"),
            relief="flat"
        )
        button_1.place(
            x=727.0,
            y=425.0,
            width=284.0,
            height=72.66717529296875
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("edit"),
            relief="flat"
        )
        button_2.place(
            x=727.0,
            y=504.0,
            width=284.0,
            height=72.66717529296875
        )

        #self.image_image_1 = PhotoImage(
         #   file=relative_to_assets("image_1.png"))
       # image_1 = canvas.create_image(
         #   870.0,
         #   161.0,
          #  image= self.image_image_1
        #)
        
     
       


        canvas.create_text(
            217.0,
            35.0,
            anchor="nw",
            text="Pet’s Information",
            fill="#0BBC8B",
            font=("RobotoRoman Bold", 34 * -1)
        )

        canvas.create_text(
            252.0,
            446.0,
            anchor="nw",
            text="Recommendation",
            fill="#0BBC8B",
            font=("RobotoRoman SemiBold", 26 * -1)
        )

        canvas.create_rectangle(
            697.0,
            73.66256713867188,
            699.0,
            585.319091796875,
            fill="#EFEFEF",
            outline="")

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            175.0,
            146.0,
            image= self.image_image_2
        )
        
        


        self.image_image_3 = PhotoImage(
            file=relative_to_assets("type_pet.png"))
        image_3 = canvas.create_image(
            508.0,
            146.0,
            image= self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            508.0,
            254.0,
            image=self.image_image_4
        )

    

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            176.0,
            254.0,
            image=self.image_image_5
        )

  
        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            175.0,
            357.0,
            image=self.image_image_6
        )
        
     
     
        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            334.0,
            564.0,
            image=self.image_image_7
        )

        canvas.create_text(
            100.0,
            543.0,
            anchor="nw",
            text=self.recommend,
            fill="#000000",
            font=("RobotoRoman SemiBold", 16 * -1)
        )
        
        canvas.create_text(
            118.0,
            140.0,
            anchor="nw",
            text= self.pet_info_dict['name'],
            fill="#030303",
            font=("RobotoRoman SemiBold", 20 * -1)
        )
        canvas.create_text(
                451.0,
                140.0,
                anchor="nw",
                text= self.pet_info_dict['breed'],
                fill="#030303",
                font=("RobotoRoman SemiBold", 20 * -1)
            )
        
        pet_weight =self.pet_info_dict['weight']
        pet_age = self.pet_info_dict['age']
        pet_text_weight = ''
        pet_text_age = ''
        
        if pet_weight.lower() == 'no info yet' and pet_age.lower() == 'no info yet':
             pet_text_weight = pet_weight
             pet_text_age = pet_age
        else:
            pet_text_weight = pet_weight + ' KG'
            pet_text_age1 =float(pet_age)
            
            if pet_text_age1 <= 1:
                pet_text_age = pet_age + ' Year old'
            else:
                pet_text_age = pet_age + ' Years old' 
        
        canvas.create_text(
                451.0,
                248.0,
                anchor="nw",
                #text="60 KG",
                text=pet_text_weight,
                fill="#030303",
                font=("RobotoRoman SemiBold", 20 * -1)
            )
        canvas.create_text(
                119.0,
                248.0,
                anchor="nw",
            # text="4 years old",
                text= pet_text_age,
                fill="#030303",
                font=("RobotoRoman SemiBold", 20 * -1)
            )
        
        canvas.create_text(
            118.0,
            351.0,
            anchor="nw",
            #text="Skin issues",
            text=self.pet_info_dict['heal_con'],
            fill="#030303",
            font=("RobotoRoman SemiBold", 20 * -1)
        )
        
                  
        # Create the label only if it doesn't exist
        if not hasattr(self, 'image_label'):
            self.image_label = Label(self)

        # Configure the label with the default image
        self.image_label.configure(image=  self.photo)
        self.image_label.image = self.photo # To keep a reference

        # Place the label on your Tkinter window
        self.image_label.place(x=775, y=110)
        
        
    def image_retrieve(self):
        encoded_image=self.pet_info_dict['image']
        decoded_image = decode_base64(encoded_image)
        
        if encoded_image != '':
            
            # Use BytesIO to create a binary stream from the bytes
            image_stream = BytesIO(decoded_image)

            try:
                # Open the image directly from the binary stream
                original_image = Image.open(image_stream)
                resized_image = original_image.resize((200, 200))

                # Create a circular mask
                mask = Image.new('L', (200, 200), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 200, 200), fill=255)

                # Apply the circular mask to the image
                circular_image = Image.new('RGBA', (200, 200), 0)
                circular_image.paste(resized_image, mask=mask)

                # Convert to PhotoImage for displaying in tkinter
                self.photo = ImageTk.PhotoImage(circular_image)
                

            except Exception as e:
                print(f"Error processing image: {e}")
        else:
            # Use the default image
            #r'D:\pet-monitoring\build\main_window\profile\view_pet\assets\def_img.png'
            self.photo =  PhotoImage(
            file=relative_to_assets("def_img.png"))
        
        return self.photo
         
            
          
  
    def recommendation(self):
        
     pet_weight_text = self.pet_info_dict['weight']
     pet_age_text = self.pet_info_dict['age'] 
     pet_type = self.pet_info_dict['breed']       
     recommend = ''
                
     if pet_weight_text == 'No Info yet' and pet_age_text == 'No Info yet': 
        recommend = "there's no Info just yet"
        self.recommend = recommend
        self.recommend
     else:
        pet_weight = float(pet_weight_text)
        pet_age = float(pet_age_text)
          
          
        if(pet_type.lower() == 'dog'):
            if(pet_age <= 1):
                if(pet_weight<=10):
                    recommend = 'Adjust meal portions based on weight to ensure healthy growth.'
                elif(pet_weight == 10 or pet_weight<=25):
                    recommend = 'Adjust meal portions based on weight to support steady growth'
                elif(pet_weight >25):
                    recommend = 'Adjust meal portions based on weight to support proper development'
            if(pet_age>1):
                if(pet_weight<=10):
                    recommend = 'Monitor weight and adjust portions to prevent obesity'
                elif(pet_weight == 10 or pet_weight<=25):
                    recommend = 'Monitor weight and adjust portions to maintain a healthy body condition.'
                elif(pet_weight >25):
                    recommend = 'Monitor weight and adjust portions to prevent excessive strain on joints'    
            if(pet_age>7):
                if(pet_weight<=10):
                    recommend = 'Monitor weight and adjust portions to prevent obesity and maintain a healthy weight'
                elif(pet_weight == 10 or pet_weight<=25):
                    recommend = 'Regular veterinary check-ups become crucial for early detection of\n\n age-related health issues'
                elif(pet_weight >25):
                    recommend = 'Regular veterinary check-ups are essential for monitoring weight\n\n and addressing age-related concerns'   
                    
        elif pet_type.lower() == 'cat':
         if pet_age <= 1:
            if pet_weight <= 3:
                recommend = 'Adjust meal portions based on weight to ensure healthy growth.'
            elif 3 < pet_weight <= 5:
                recommend = 'Adjust meal portions based on weight to support steady growth.'
            elif pet_weight > 5:
                recommend = 'Adjust meal portions based on weight to support proper development.'
         elif pet_age > 1:
            if pet_weight <= 3:
                recommend = 'Monitor weight and adjust portions to prevent obesity.'
            elif 3 < pet_weight <= 5:
                recommend = 'Monitor weight and adjust portions to maintain a healthy body condition.'
            elif pet_weight > 5:
                recommend = 'Monitor weight and adjust portions to prevent excessive strain on joints.'
         elif pet_age > 7:
            if pet_weight <= 3:
                recommend = 'Monitor weight and adjust portions to prevent obesity and maintain a healthy weight.'
            elif 3 < pet_weight <= 5:
                recommend = 'Regular veterinary check-ups become crucial for early detection of\n\n age-related health issues.'
            elif pet_weight > 5:
                recommend = 'Regular veterinary check-ups are essential for monitoring weight\n\n and addressing age-related concerns.'

        elif pet_type.lower() == 'bird':
        # Bird recommendations
          if pet_age <= 1:
            if pet_weight <= 0.1:
                recommend = 'Provide a balanced diet with seeds, nuts, and fresh produce to support healthy growth.'
            elif 0.1 < pet_weight <= 0.5:
                recommend = 'Ensure a diverse diet with pellets, seeds, and fresh fruits to support steady growth.'
            elif pet_weight > 0.5:
                recommend = 'Offer a variety of foods, including pellets, seeds, nuts,\n\n and fresh vegetables, for proper development.'
          elif pet_age > 1:
            if pet_weight <= 0.1:
                recommend = 'Monitor weight and adjust diet to maintain a healthy body condition.'
            elif 0.1 < pet_weight <= 0.5:
                recommend = 'Maintain a balanced diet with a mix of pellets, seeds,\n\n and fresh produce to support overall health.'
            elif pet_weight > 0.5:
                recommend = 'Regularly assess weight and adjust the diet as needed.\n\n Provide a variety of foods for optimal nutrition.'
          else:
                recommend = "unknown type of age"   
        else:
            recommend = "unknown type of pet"

        self.recommend = recommend
        
        print(self.recommend)
        return self.recommend
    
    
    
    
    
    def retrieve_data_fromDb(self):
        # Execute the database query to get the latest pet information
        self.display_pet_info = db_controller.get_petInfo()

        # Check if any data is retrieved
        if self.display_pet_info:
            # Define column names for reference
            column_names = ['name', 'breed', 'age', 'weight', 'heal_con', 'image']
            pet_info_dict = dict(zip(column_names, self.display_pet_info))

            self.pet_info_dict = pet_info_dict
        else:
            # No pet information retrieved from the database, use default values
            self.pet_info_dict = {'name': 'No Info yet', 'breed': 'No Info yet', 'age': 'No Info yet',
                                'weight': 'No Info yet', 'heal_con': 'No Info yet', 'image': ''}

        return self.pet_info_dict