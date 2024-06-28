import tkinter as tk
from tkinter import Label,Text,StringVar
from tkinter import filedialog
from tkinter import font as tkFont
from PIL import Image, ImageTk
import tensorflow as tf


def image_recognise(image_path):
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    input_image = tf.keras.preprocessing.image.img_to_array(image)
    input_image = tf.keras.applications.mobilenet_v2.preprocess_input(input_image)
    input_image = tf.expand_dims(input_image, axis=0)
    predictions = model.predict(input_image)
    predicted_classes = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]
    result_text.set(f"AI:Of course! Its a {predicted_classes[0][1].replace('_', ' ')}!!")
    # print(predicted_classes[0][1])
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    image_path = tk.filedialog.askopenfilename(filetypes=fileTypes)
    
    if len(image_path):
        image_recognise(image_path)
        img = Image.open(image_path)
        img = img.resize((400, 400))
        pic = ImageTk.PhotoImage(img)
        label.config(image=pic)
        label.image = pic
    else:
        print("No file is Choosen !! Please choose a file.")
 
 

if __name__ == "__main__":
 
    app = tk.Tk()
    app.title("Image Recognition AI")
    app.geometry("700x700")
 
    
    app.option_add("*Button*Background", "gray")
    header_text = StringVar()
    header_text.set("Me:Can you recognize what this is?")
    header = Label(app, textvariable=header_text,font=('Arial', 25))
    header.pack()
    label = tk.Label(app)
    label.pack(pady=10)
    
    font = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
    uploadButton = tk.Button(app, text="Input Image",font=font, command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM, pady=20)
    
    result_text = StringVar()
    result_text.set("")
    result = Label(app, textvariable=result_text,font=('Arial', 25))
    result.pack()
    app.mainloop()