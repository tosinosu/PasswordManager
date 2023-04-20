import os
import platform
from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
# import pathlib module
import pathlib

"""
class GUIDesign():
    def __init__(self,root):
        self.initUI(root) 

    def initUI(self,root):
        print ("hello")"""

class Encrypt_Pass():
    def upload_file():
        NotImplementedError('Not implemented', 'Not yet available')
    def encrypt_file():
        NotImplementedError('Not implemented', 'Not yet available')
    def save_file(file_location):
        # To create a file
        pathlib.Path(file_location).touch()

def makemenu(win):
   # win = Toplevel(root)
    menubar = Menu(win)
    #win['menu'] = menubar
    win.config(menu=menubar)

    menu_encrypt = Menu(win, tearoff=False)
    menubar.add_cascade(menu=menu_encrypt, label='Encrpt', command=Enc, underline=0)

    menu_decrypt = Menu(win, tearoff=False) 
    menubar.add_cascade(menu=menu_decrypt, label='Decrypt', underline=0)

    menu_viewpass = Menu(win, tearoff=False)
    menubar.add_cascade(menu=menu_viewpass, label='ViewPass', underline=0)

    menu_setting = Menu(win, tearoff=False)
    menubar.add_cascade(menu=menu_setting, label='Settings', underline=0)

    menu_donate = Menu(win, tearoff=False)
    menubar.add_cascade(menu=menu_donate, label='Donate', underline=0)

    menu_help = Menu(win, tearoff=False)
    menubar.add_cascade(menu=menu_help, label='Help', underline=0)

   # gui_design=GUIDesign(root)

class UploadDrag():
    def uploadDnd():
        root_dnd = TkinterDnD.Tk()  # notice - use this instead of tk.Tk()

        lb = Listbox(root_dnd)
        lb.insert(1, "drag files to here")

        # register the listbox as a drop target
        lb.drop_target_register(DND_FILES)
        lb.dnd_bind('<<Drop>>', lambda e: lb.insert(END, e.data))

        lb.pack()

        return "The File"
    def upload_file():
        global img
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        b2 =Button(root, text='Browse File', command=submitForm) # using Button 
        b2.grid(row=3,column=1)

    def encrypt_file(file):
        if file == 0:
            return "No file attach: Please attach text file"
        else:
            
class Decrypt():
    def upload_file():
    
    def decrypt_button():'
    
class ViewPass():
    def listpass():
    
    def addPass():
    
    def deletePass

if __name__ == '__main__':
    root = Tk()
    root.title('Password Manager')
    msg = Label(root, text='Window menu basics') # add something below
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    makemenu(root)

    root.mainloop()
    
