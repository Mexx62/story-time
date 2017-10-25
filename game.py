from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
import os
import random
from resizeimage import resizeimage

nalready = []
i = 0
path = ''
files = os.listdir('images/')
minpic = [None]*len(files)
minipic = [None]*len(files)

def nextturn():
    global i, path, files
    if len(nalready) == len(files):
        showerror('Partie terminée', 'La partie est terminée, arrête d\'appuyer sur suivant.')
        return()
    minimage(i)
    i = i + 1
    index = random.randrange(0, len(files))
    while index in nalready:
        index = random.randrange(0, len(files))
    path = 'images/' + files[index]
    image = Image.open(path)
    image = resizeimage.resize_contain(image, [canvas.winfo_width()-10, canvas.winfo_height()-10])
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image=photo)
    canvas.img = photo
    nalready.append(index)

def nouvellepartie():
    global i, nalready, minpic, minipic
    if askyesno('Confirmation', 'Etes-vous sûr de vouloir recommencer à zéro ?'):
        canvas.delete('all')
        mincanvas.delete('all')
        i = 0
        nalready = []
        minpic = [None]*len(files)
        minipic = [None]*len(files)

def minimage(i):
    if i == 0:
        return()
    minpic[i] = Image.open(path)
    minpic[i] = resizeimage.resize_contain(minpic[i], [100, 100])
    minipic[i] = ImageTk.PhotoImage(minpic[i])
    if i-1 == 0:
        mincanvas.create_image(50, 55, image=minipic[i])
    else:
        mincanvas.create_image(50+100*(i-1), 55, image=minipic[i])



window = Tk()
window.wm_title('Story Time')
canvas = Canvas(window, width=500, height=500)
canvas.pack(side=TOP, expand=True, fill=BOTH)
mincanvas = Canvas(window, width=100*len(files), height=110, bg="#c6c6c6")
mincanvas.pack(fill=X)
scrollbar = Scrollbar(window, orient=HORIZONTAL, command=mincanvas.xview)
scrollbar.pack(fill=X)
mincanvas.config(xscrollcommand=scrollbar.set, scrollregion=(0, 0, 100*(len(files)-1), 110))
Button(window, text='Tour suivant', command=nextturn).pack(side=LEFT, padx=15, pady=15)
Button(window, text='Nouvelle Partie', command=nouvellepartie).pack(side=RIGHT, padx=15, pady=15)
window.mainloop()