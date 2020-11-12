import pytube
from tkinter import filedialog
from tkinter import *
import os
from os import remove
from moviepy.editor import *
import time

url_des = ""

def carpeta():
    directorio=filedialog.askdirectory()
    global url_des
    if directorio!="":
        os.chdir(directorio)
        url_des = directorio
        print(url_des)
      
def enviarDatos():
    tex = texto.get()
    yt = pytube.YouTube(tex)
    t = yt.title.split(" ")
    titulo = '-'.join(t)
    titulo = normalize(titulo)
    print("normal: "+titulo)
    yt.streams.first().download(output_path=url_des,filename=titulo)
    print("mamalona ff "+url_des)
    inputVideo = titulo+'.mp4'
    outPutmusic = titulo+'.mp3'
    
    video = VideoFileClip(url_des+'/'+inputVideo)
    video.audio.write_audiofile(url_des+'/'+outPutmusic)
    video.close()
    #remove(url_des+'/'+inputVideo)
    Button(text="Listo.",bg="blue", fg='white',command=ventana.destroy).place(x=160,y=70)
    
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("'",""),
        ("´",""),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s   
    
ventana = Tk()
ventana.geometry("350x100")
ventana.title("Descargar video de youtube.")

Button(text="Seleccionar directorio.",bg="salmon",command=carpeta).place(x=5,y=35)

Label(ventana,text ="Link Youtube:",fg="gray").grid(row=3,column=0,sticky="w",padx=5,pady=1)

texto = Entry(ventana)
texto.place(x=90, y=5)

Button(ventana,text="Enviar Datos.",bg="salmon",command=enviarDatos).place(x=5,y=70)
ventana.mainloop()
