from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from tkinter import font as tkFont
import os
import tkinter as tk
import cv2
from PIL import Image,ImageTk
import PIL
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

###############################################################################

#Functions......................................................................
def showimage():
    global lbl,lab2,link1
    try:
        try:
            lab2.destroy()
            lbl.destroy()
            fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image files",filetypes=(("JPG File","*,jpg"),("PNG file","*.png"),("All files","*.*")))
            img = Image.open(fln)#open the image file
            img.thumbnail((500,500))
            img = ImageTk.PhotoImage(img)#photoimage class is used to display the image
            lbl=Label(root,bg="silver")
            lbl.place(x=80,y=125,height="300",width="500")
            lbl.configure(image=img)
            lbl.image =img
        except:
            lab2.destroy()
            fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image files",filetypes=(("JPG File","*,jpg"),("PNG file","*.png"),("All files","*.*")))
            img = Image.open(fln)#open the image file
            img.thumbnail((500,500))
            img = ImageTk.PhotoImage(img)#photoimage class is used to display the image
            lbl=Label(root,bg="silver")
            lbl.place(x=80,y=125,height="300",width="500")
            lbl.configure(image=img)
            lbl.image =img
    except:
        exceptProtection()
    link1=fln


#kill the first presentation................................................... 
def firstkill():
    goto.destroy()
    lab0.destroy()
    lab1.destroy()
    lab2.destroy()
    
#kill the second presentation................................................... 
def secondkill():
    global lab0,lab1,lab2,Browse,process,quits,R1,R2,R3,R4,R5
    lab0.destroy()
    lab1.destroy()
    lab2.destroy()
    Browse.destroy()
    process.destroy()
    quits.destroy()
    R1.destroy()
    R2.destroy()
    R3.destroy()
    R4.destroy()
    R5.destroy()
    
    

#kill the three presentation................................................... 
def thirdkill():
    global lab0,lab1,lab2,lab3,lab4,Back,quits,Save,pdf
    lab0.destroy()
    lab1.destroy()
    lab2.destroy()
    lab3.destroy()
    lab4.destroy()
    Back.destroy()
    quits.destroy()
    Save.destroy()
    pdf.destroy()

    
#build the second presentation.................................................    
def secondbuild():
    global lab0,lab1,lab2,Browse,process,quits,link1,R1,R2,R3,R4,R5
    lab0=Label(text="WWAQ Analysis Dashboard",bg="silver",fg="black")
    lab0.config(font=("segoe UI", 32))
    lab0.pack(pady=10)

    str1="Enter your satellite image to be processed"
    lab1=Label(text=str1,bg="silver",fg="black")
    lab1.config(font=("segoe UI", 12))
    lab1.place(x=35,y=90)

    global lab2
    img1 = Image.open("C:\\Users\\Lenovo\\Desktop\\Nordlys-1.jpg")#open the image file
    img1.thumbnail((500,500))
    img1 = ImageTk.PhotoImage(img1)#photoimage class is used to display the image
    lab2=Label(root,bg='silver')
    lab2.place(x=150,y=125)
    lab2.configure(image=img1)
    lab2.image =img1

    Browse =ttk.Button(text="Browse",command=showimage)
    Browse.place(x=280,y=440)

    process =ttk.Button(text="Process",command=lambda:[secondkill(),thirdbuild()])
    process.place(x=698,y=375)

    quits =ttk.Button(text="Quit",command=root.destroy)
    quits.place(x=480,y=440)

    var = IntVar()

    R1 = ttk.Radiobutton(root, text="O3",width="8", variable=var, value=1)
    R1.place(x=700,y=150)

    R2 = ttk.Radiobutton(root, text="SO2",width="8", variable=var, value=2)
    R2.place(x=700,y=175)

    R3 = ttk.Radiobutton(root, text="NH3",width="8", variable=var, value=3)
    R3.place(x=700,y=200)

    R4 = ttk.Radiobutton(root, text="CH4",width="8", variable=var, value=4)
    R4.place(x=700,y=225)

    R5 = ttk.Radiobutton(root, text="CO",width="8", variable=var, value=5)
    R5.place(x=700,y=250)

    R6 = ttk.Radiobutton(root, text="NO2",width="8", variable=var, value=6)
    R6.place(x=700,y=275)

    R7 = ttk.Radiobutton(root, text="Dust",width="8", variable=var, value=7)
    R7.place(x=700,y=300)

    R8 = ttk.Radiobutton(root, text="Aerosol \nRadius",width="8", variable=var, value=8)
    R8.place(x=700,y=325)

#build the third presentation.................................................    
def thirdbuild():
    global lab0,lab1,lab2,lab3,lab4,Back,quits,lbl,Save,pdf
    try:
        lbl.destroy()
        thirdbuild2()
        
    except:
        thirdbuild2()

#help function for the third build............................................
def thirdbuild2():
    global lab0,lab1,lab2,lab3,lab4,Back,quits,lbl,Save,link1,link2,pdf
    lab0=Label(text="WWAQ Analysis Dashboard\nPrediction Results",bg="silver",fg="black")
    lab0.config(font=("segoe UI", 20))
    lab0.pack(pady=10)

    img = Image.open(link1)
    img.thumbnail((260,260))
    img = ImageTk.PhotoImage(img)
    lab1=Label(root,bg="silver")
    lab1.place(x=0,y=80,height="300",width="390")
    lab1.configure(image=img)
    lab1.image =img
    
    

    list1=list(link1)

    list2=[]
    for i in range(len(list1)-1,-1,-1):
        if list1[i]=="/":
            break
        else:
            list2.append(list1.pop())
    list2.reverse()
    str2=""
    str2="".join(list2)
    link2="C:\\Users\\Lenovo\\Desktop\\Python\\Output Image\\"+str2

    img1 = Image.open(link2)
    img1.thumbnail((250,250))
    img1 = ImageTk.PhotoImage(img1)
    lab2=Label(root,bg="silver")
    lab2.place(x=405,y=80,height="300",width="390")
    lab2.configure(image=img1)
    lab2.image =img1

    lab3=Label(text="Input Image",bg="silver",fg="black",width=10)
    lab3.config(font=("segoe UI", 15))
    lab3.place(x=130,y=350)

    lab4=Label(text="Output Image",bg="silver",fg="black",width=12)
    lab4.config(font=("segoe UI", 15))
    lab4.place(x=530,y=350)
        
    Back =ttk.Button(text="Back",command=lambda:[thirdkill(),secondbuild()])
    Back.place(x=680,y=410)
        
    quits =ttk.Button(text="Quit",command=root.destroy)
    quits.place(x=680,y=450)

    Save =ttk.Button(text="       Save\nOutput Image",command=Savefile)
    Save.place(x=285,y=420)

    pdf =ttk.Button(text="    Prediction\nResults in PDF",command=PDF)
    pdf.place(x=425,y=420)
    
    
#protection for 2nd presentation................................................
def exceptProtection():
    global lab2
    img3 = Image.open("Nordlys-1.jpg")#open the image file
    img3.thumbnail((500,500))
    img3 = ImageTk.PhotoImage(img3)#photoimage class is used to display the image
    lab2=Label(root,bg='silver')
    lab2.place(x=150,y=125)
    lab2.configure(image=img3)
    lab2.image =img3


#Save file function

def Savefile():
    global link1,link2
    try:
        imagination=PIL.Image.open(link2)
        files = [('All Files', '*.*'),  
                 ('PNG Files', '*.png'), 
                 ('JPG Files', '*.jpg'),
                 ('PDF Files', '*.pdf')] 

        filem = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
        imagination.save(filem.name)
    except:
        pass

#PDF generation

def PDF():
    try:
        from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet
        global link1,link2
        files = [('All Files', '*.*'),  
                 ('PDF Files', '*.pdf')] 

        filemm = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
        str1=""
        for i in range(len(str(filemm.name))):
            if filemm.name[i]==".":
                break
            else:
                str1=str1+filemm.name[i]
        str1+=".pdf"
        pdf=SimpleDocTemplate(str1)
        flow_obj=[]
        styles=getSampleStyleSheet()
        im_data1=Image(link1,500,300)
        im_data2=Image(link2,500,300)

        text1='<font name="Times-Italic" color=red size="10">********************************************INPUT  IMAGE****************************************</font>'
        p_text1=Paragraph(text1,style=styles["Normal"])
        text2='<font name="Times-Italic" color=red size="10">********************************************OUTPUT IMAGE****************************************</font>'
        p_text2=Paragraph(text2,style=styles["Normal"])


        t=Table([[im_data1 for i in range(1,2)],
                 [p_text1 for i in range(1,2)],
                 [im_data2 for i in range(1,2)],
                 [p_text2 for i in range(1,2)]])
        t_style=TableStyle([("BOX",(0,0),(-1,-1),1,colors.black),
                            ("GRID",(0,0),(-10,-10),1,colors.black),
                            ("BACKGROUND",(0,0),(-1,-1),colors.white)])
        t.setStyle(t_style)
        flow_obj.append(t)
        pdf.build(flow_obj)
        
    except:
        pass
        
    
    
    
    

###############################################################################
from PIL import Image,ImageTk    
#window setup..................................................................
root =Tk()
root.title("WWAQ - TEAM PHANTOM")
root.geometry("800x500+100+100")
root.configure(bg='silver')

#for the first presentation.................................................... 

img1 = Image.open("yes.png")#open the image file
img1.thumbnail((1050,1050))
img1 = ImageTk.PhotoImage(img1)#photoimage class is used to display the image
lab2=Label(root,bg="black")
lab2.place(x=0,y=0)

lab2.configure(image=img1)
lab2.image =img1

goto=ttk.Button(text="Go to",command=lambda:[firstkill(),secondbuild()])
goto.place(x=360,y=275)

lab0=Label(text="TEAM PHANTOM",bg="black",fg="white")
lab0.config(font=("segoe UI", 40))
lab0.pack()

str1="For healthier lives with air quality"
lab1=Label(text=str1,bg="black",fg="white")
lab1.config(font=("segoe UI", 13))
lab1.pack()

