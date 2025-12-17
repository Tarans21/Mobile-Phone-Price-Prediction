import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pickle as pk
import pandas as pd
import numpy as np

# Load the model and encoders
mobile_model = pk.load(open('Mobile_Service_Model.pk2', 'rb'))
brand_encoder = pk.load(open('Brand_Encodre.pk2', 'rb'))
data = pd.read_csv("https://github.com/sukhioo7/dataset/blob/main/Flipkart_Mobiles.csv?raw=True")
def fxn1():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == 'Admin' and password == '12345':
        window2 = tk.Toplevel(window)
        window2.geometry("1700x800")
        window2.title("MOBILE PRICE PREDICTION")

        image = Image.open("photob.png").resize((1700, 800))
        image = ImageTk.PhotoImage(image)
        image_label = tk.Label(window2, image=image)
        image_label.image = image  
        image_label.pack()

        border_frame = tk.Frame(window2, width=400, height=500, bg="black")
        border_frame.place(x=200, y=150)
            
        image_frame = tk.Frame(border_frame, width=400, height=500, bg="#010208")
        image_frame.pack_propagate(False)
        image_frame.pack()

        img = ImageTk.PhotoImage(Image.open("w2back.png").resize((400, 500)))
        image_label = tk.Label(image_frame, image=img)
        image_label.image = img 
        image_label.pack()

        tk.Label(image_frame, text="MOBILE PRICE PREDICTION", font=("Playfair Display", 20), bg="#1D3F6E", fg="white").place(x=13, y=25)
        
        
        tk.Label(image_frame, text="BRAND:", bg="#163866", fg="white", font=("arial", 15)).place(x=5, y=110)
        brand_entry = tk.Entry(image_frame, width=15, bg="#163866", fg="white", font=("arial", 18), border=3)
        brand_entry.place(x=120, y=110)

        tk.Label(image_frame, text="Memory:", bg="#163866", fg="white", font=("arial", 15)).place(x=5, y=170)
        memory_entry = tk.Entry(image_frame, width=15, bg="#163866", fg="white", font=("arial", 18), border=3)
        memory_entry.place(x=120, y=170)

        tk.Label(image_frame, text="Storage:", bg="#163866", fg="white", font=("arial", 15)).place(x=5, y=230)
        storage_entry = tk.Entry(image_frame, width=15, bg="#163866", fg="white", font=("arial", 18), border=3)
        storage_entry.place(x=120, y=230)

        tk.Label(image_frame, text="Org Price:", bg="#163866", fg="white", font=("arial", 15)).place(x=5, y=290)
        original_price_entry = tk.Entry(image_frame, width=15, bg="#163866", fg="white", font=("arial", 18), border=3)
        original_price_entry.place(x=120, y=290)

        tk.Label(image_frame, text="Rating:", bg="#163866", fg="white", font=("arial", 15)).place(x=5, y=350)
        rating_entry = tk.Entry(image_frame, width=15, bg="#163866", fg="white", font=("arial", 18), border=3)
        rating_entry.place(x=120, y=350)

        def save_and_predict():
            try:
                brand = brand_entry.get()
                memory = memory_entry.get()
                storage = storage_entry.get()
                original_price = original_price_entry.get()
                rating = rating_entry.get()

                            
                columns=['Brand','Memory','Storage','Rating','Original Price']
                row=[[brand,memory,storage,rating,original_price]]
                data=pd.DataFrame(row,columns=columns)

                arr=brand_encoder.transform(data[['Brand']]).toarray()

                temp_data=pd.DataFrame(arr,columns=['ASUS', 'Apple', 'GIONEE', 'Google Pixel', 'HTC', 'IQOO',
                        'Infinix', 'LG', 'Lenovo', 'Motorola', 'Nokia', 'OPPO', 'POCO',
                        'SAMSUNG', 'Xiaomi', 'realme', 'vivo'],dtype='int')

                data=pd.concat([data,temp_data],axis=1)

                data.drop(['Brand'],axis=1,inplace=True)

                predicted_price=mobile_model.predict(data)

                messagebox.showinfo("PRICE", f"THE PREDICTED VALUE IS {round(predicted_price[0])}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        predict_button = tk.Button(image_frame, text="PREDICT", bg="#156CAF", fg="white", font=("arial", 10), border=0, width=10, pady=10, command=save_and_predict)
        predict_button.place(x=150, y=420)

        window2.mainloop()
    elif username != 'Admin' and password != '12345':
        messagebox.showerror("Invalid", "Invalid username and password")
    elif password != '12345':
        messagebox.showerror("Invalid", "Invalid password")
    elif username != 'Admin':
        messagebox.showerror("Invalid", "Invalid username")

window = tk.Tk()
window.geometry("1700x800")
window.title("MOBILE PRICE PREDICTION")

# Image display
image = Image.open("photo.png").resize((1700, 800))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image)
image_label.image = image  
image_label.pack()

border_frame = tk.Frame(window, width=320, height=320, bg="black")
border_frame.place(x=610, y=250)

image_frame = tk.Frame(border_frame, width=300, height=300, bg="#010208")
image_frame.pack_propagate(False)
image_frame.pack()

img = ImageTk.PhotoImage(Image.open("backg.png").resize((320, 320)))
image_label = tk.Label(image_frame, image=img)
image_label.image = img  
image_label.pack()

username_label = tk.Label(image_frame, text="USERNAME:", bg="#010208", fg="white")
username_label.place(x=20, y=100)
username_entry = tk.Entry(image_frame, width=20, bg="black", border=1, fg="white")
username_entry.place(x=100, y=100)

password_label = tk.Label(image_frame, text="PASSWORD:", bg="#010208", fg="white")
password_label.place(x=20, y=150)
password_entry = tk.Entry(image_frame, show="*", width=20, bg="black", border=1, fg="white")
password_entry.place(x=100, y=150)

signin_button = tk.Button(image_frame, text="Sign In", bg="black", fg="white", command=fxn1)
signin_button.place(x=125, y=200)

window.mainloop()

