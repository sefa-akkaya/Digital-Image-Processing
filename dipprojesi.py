import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk  
import filter   
import file
import dosyaacma 
global a   
program = tkinter.Tk()
photo = Image.open("C:/Users/SEFA/Desktop/bg.png")#open image
resize = photo.resize((1920,1080),Image.ANTIALIAS)
bgimg = ImageTk.PhotoImage(resize)
bglabel = tkinter.Label(program,image=bgimg,anchor="center")
bglabel.pack()
program.title("Digital Image Processing")
program.geometry("1920x1080")
def name_of_filter():
    name = clicked.get()
    return name 
clicked = tkinter.StringVar(program)
clicked.set("Select an option:")
drop = tkinter.OptionMenu(program,clicked,"Negative","Blur","Contour","Detail","Edge","Find Edge","Emboss","Sharp","Smooth","Minimum","Median","Maximum","Gauss")
drop.config(bg="#4A4242", fg="WHITE",width=18,height=2,font= ("Arial", 10))
def filtre_adi():#açılır pencereden filtre adı verecek.
    return clicked.get()
def get_name():
    file = dosyaacma.foto_yukle()
    return file
def filtreliyi_goster():#programa fotoğrafı yerleştirecek.
    filtre_adi = clicked.get()
    if(filtre_adi == "Gauss"):
        filtreli_foto = filter.gauss(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Blur"):
        filtreli_foto = filter.blur(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Contour"):
        filtreli_foto = filter.contour(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Detail"):
        filtreli_foto = filter.detail(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Edge"):
        filtreli_foto = filter.image_edge(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Find Edge"):
        filtreli_foto = filter.find_edge(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Emboss"):
        filtreli_foto = filter.emboss(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Sharp"):
        filtreli_foto = filter.sharp(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Smooth"):
        filtreli_foto = filter.smooth(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Minimum"):
        filtreli_foto = filter.min(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Median"):
        filtreli_foto = filter.median(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Maximum"):
        filtreli_foto = filter.max(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()
    elif(filtre_adi == "Negative"):
        filtreli_foto = filter.negative(a)
        photo = Image.open(filtreli_foto)#open image
        resize = photo.resize((300,400),Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(resize)
        label2 = tkinter.Label(program,image=new_pic,anchor="center")
        label2.place(relx = 0.53, rely = 0.8, anchor = "center")
        program.mainloop()


def goster():
    global a 
    a = dosyaacma.foto_yukle()
    photo = Image.open(a)#open image
    resize = photo.resize((300,400),Image.ANTIALIAS)
    original = ImageTk.PhotoImage(resize)
    label1 = tkinter.Label(program,image = original)
    label1.place(relx = 0.45, rely = 0.1)
    #filtreliyi_goster(a,filtre_adi())#filtreli halini bastiracak.
    program.mainloop()
def goster_foto():
    global a
    a = file.foto()
    photo = Image.open(a)#open image
    resize = photo.resize((300,400),Image.ANTIALIAS)
    original = ImageTk.PhotoImage(resize)
    label1 = tkinter.Label(program,image = original) 
    label1.place(relx = 0.45, rely = 0.1)
    #filtreliyi_goster(a,filtre_adi())#filtreli halini bastiracak.
    program.mainloop()
original = tkinter.Label(program,text = "Original Photo",bg = '#6c3030',fg='white',font= ("Arial", 25))
filtered = tkinter.Label(program,text = "Filtered Photo",bg = '#6c3030',fg='white',font= ("Arial", 25))
original.place(relx = 0.475,rely=0.05)
filtered.place(relx = 0.475,rely=0.55)
button_dosya = tkinter.Button(program,text = 'Select Folder',command=goster,height=5,width=20,bg = '#4A4242',fg = 'white',font= ("Arial", 10))
submit_button = tkinter.Button(program, text='Submit',command = filtreliyi_goster,bg = '#4A4242',fg='white',width=20,height=2,font= ("Arial", 10)) 
button_foto =tkinter.Button(program,text = "Take a Photo",command=goster_foto,bg = '#4A4242',fg='white',width=20,height=2,font= ("Arial", 10))
button_dosya.place(relx = 0.1,rely = 0.150,anchor="w")
button_foto.place(relx = 0.1,rely = 0.3,anchor="w")
drop.place(relx = 0.1,rely = 0.45,anchor="w")
submit_button.place(relx = 0.1,rely = 0.6,anchor="w",)
 

program.mainloop()
