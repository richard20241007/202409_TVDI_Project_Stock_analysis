import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageButton(ttk.Button):
    def __init__(self, master=None, **kwargs):
        self.icon_img = Image.open(r'D:\\Project_TVDI\\202409_TVDI_Project_Stock_analysis\\picture\\refresh16.png').resize((18,18),Image.LANCZOS)
        self.icon_phto = ImageTk.PhotoImage(self.icon_img)
        super().__init__(master=master,image=self.icon_phto,**kwargs)
        