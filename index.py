# imports


import tkinter 
import qrcode


# windows settings
window = tkinter.Tk()
window.geometry("600x400")
window.resizable(height=False , width=False)

# text
top_text_label=tkinter.Label(window,text='Paste Link + Press Go').pack()


# functions
def qr_code():
    image = qrcode.make(entry.get())
    image.save("qrcode.jpg")
    tkinter.Label(window, text="Success").pack()


#variables
qr_var = tkinter.StringVar()

# entry form text
entry=tkinter.Entry(window, textvariable=qr_var)
entry.pack()


# button
qr_button = tkinter.Button(window,text='Go',command= qr_code).pack()

# mainloop
window.mainloop()