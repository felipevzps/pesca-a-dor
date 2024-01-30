from tkinter.ttk import Label, Button, Style
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

root = ThemedTk(theme="arc", themebg=True)
root.iconbitmap(default="images/1024x768/fishing_rod.ico")

root.title("pesca-a-dor")
root.geometry("500x500+250+250")
root.resizable(False, False)
style = Style()
style.configure("TButton", font=("Roboto", 10))

def load_image():
    image = Image.open("images/1024x768/trash.png")
    resized = image.resize((20,20))
    return ImageTk.PhotoImage(resized)

def widget(widget, row, column, sticky="NSEW", **kwargs):
    new_widget = widget(**kwargs)
    new_widget.grid(row=row, column=column, padx=5, pady=5, sticky=sticky)
    return new_widget

trash = load_image()

button_fishing_position = widget(Button, row=0, column=0, text="Fishing Position")
label_fishing_position = widget(Label, row=0, column=1, text="Empty", font=("Roboto", 10), sticky="W")
button_fishing_position_trash = widget(Button, row=0, column=2, image=trash, sticky="E")




root.mainloop()