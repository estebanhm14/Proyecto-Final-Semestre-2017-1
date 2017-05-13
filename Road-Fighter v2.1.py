import tkinter
import time
import random 
import threading

#Creando la Ventana Principal 
v = tkinter.Tk()
v.geometry("1350x730")
v.title("Menú Road Fighter")

#poniendo imagen de fondo
imagen = tkinter.PhotoImage(file="fondoMenu.png")
fondo = tkinter.Label(v,image=imagen).place(x=0,y=0)


#Funciones que mueven el fondo

#Nivel 1
mov1 = 0
def movnvl1():
    global canvas, fondon1,mov1, pruebaf
    if(mov1 < 4000):
        canvas.move(pruebaf,0,10)
        mov1 = mov1 + 1
        canvas.after(40,movnvl1)
        


        
        




         ##### FUNCIONES SINGLE-PLAYER #####

#Esta funcion mueve el miniBan en el nivel 1 singleplayer
b = 0
def movimientoBan():
    """
    """
    global canvas,b, ban
   
    if(b<100):
        canvas.move(ban,0,15)
        b = b+1
        canvas.after(30,movimientoBan)

    else:
        b=0
        canvas.delete(ban)
        ban = canvas.create_image(random.randrange(450,800),50,image=imagen3)
        movimientoBan()




#funcion que mueve el runner
r=0
def movimientoRunner():
    global canvas,runner,r
    if (r<260):
        if(canvas.coords(runner)[0]<800):
            canvas.move(runner,5,3)
            r = r+1
            canvas.after(20,movimientoRunner)
        else:
            mri()            
    if(r == 250):
        r = 0
        runner = canvas.create_image(690,50,image=imagen4)
            
def mri():    
    global canvas,runner,r
    if (r<250):
        if(canvas.coords(runner)[0]>450):
            canvas.move(runner,-5,3)
            r = r+1           
            canvas.after(20,mri)
        else:
            movimientoRunner()

    
        
#Funciones las cuales hacen que movamos nuestro carro principal
presiono = False
x = None
i = 0
j = 0

def key(event):
    """
    """
    global x,i,j,carro,carrom,canvas,fondon1,n1
    
    tecla = repr(event.char)
    if(tecla == "'d'" or tecla == "'D'"):
        if(i < 195):
            canvas.delete(carro)
            i = i + 15
            carro = canvas.create_image(600+i,600+j,image=imagen2)
      
    if(tecla == "'a'" or tecla == "'A'"):
        if(i > -150):
            canvas.delete(carro)
            i = i - 15
            carro = canvas.create_image(600+i,600+j,image=imagen2)
    
    
    """if(tecla == "'w'"):
        if(j < 730):
            canvas.delete(x)
            j = j - 15
            x = canvas.create_image(600+i,600+j,image=imagen2)
                    
    if(tecla == "'s'"):
        if(j < 730):
            canvas.delete(x)
            j = j + 15
            x = canvas.create_image(600+i,600+j,image=imagen2)"""


    
#Funciones que ayudan a iniciar el juego con una letra para el nivel 1
def keypausa(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):
        movimientoBan()
        movnvl1()
        canvas.bind("<Key>", key)
        #movimientoBanN2()



#####                                                               #####








          ##### FUNCIONES MULTIPLAYER #####

#Esta funcion mueve el miniBan para el player 1
bm1 = 0
def movimientoBanM1():
    """
    """
    global canvas,bm1, banm
    if(bm1<200):
        canvas.move(banm,0,5)
        bm1 = bm1+1
        canvas.after(50,movimientoBanM1)
    else:
        bm1=0
        canvas.delete(banm)
        banm = canvas.create_image(random.randrange(140,400),30,image=imagebanm) 
        movimientoBanM1()

#Funcion que mueve el miniBan en el lado del player 2
bm2 = 0
def movimientoBanM2():
    """
    """
    global canvas,bm2, banm2
    if(bm2<200):
        canvas.move(banm2,0,5)
        bm2 = bm2+1
        canvas.after(50,movimientoBanM2)
    else:
        bm2=0
        canvas.delete(banm2)
        banm2 = canvas.create_image(random.randrange(970,1230),30,image=imagebanm2) 
        movimientoBanM2()




        
#funcion que mueve el runner para el player 1
def mri2m():    
    global canvas,runnerm,rm1
    if (rm1<210):
        if(canvas.coords(runnerm)[0]>140):
            canvas.move(runnerm,-5,3)
            rm1 = rm1+1           
            canvas.after(30,mri2m)
        else:
            movimientoRunnerM1()
            
rm1=0
def movimientoRunnerM1():
    global canvas,runnerm,rm1
    if (rm1<210):
        if(canvas.coords(runnerm)[0]<400):
            canvas.move(runnerm,5,3)
            rm1 = rm1+1
            canvas.after(30,movimientoRunnerM1)
        else:
            mri2m()


        
            
    else:
        rm1 = 0
        canvas.delete(runnerm)
        runnerm = canvas.create_image(random.randrange(140,400),30,image=imagerunnerm)
        movimientoRunnerM1()
            
#funcion que mueve el Runner en el lado del jugador 2
def mri2m2():    
    global canvas,runnerm2,rm2
    if (rm2<210):
        if(canvas.coords(runnerm2)[0]>960):
            canvas.move(runnerm2,-5,3)
            rm2 = rm2+1           
            canvas.after(30,mri2m2)
        else:
            movimientoRunnerM2()
            
rm2=0
def movimientoRunnerM2():
    global canvas,runnerm2,rm2
    if (rm2<210):
        if(canvas.coords(runnerm2)[0]<1220):
            canvas.move(runnerm2,5,3)
            rm2 = rm2+1
            canvas.after(30,movimientoRunnerM2)
        else:
            mri2m2()


        
            
    else:
        rm2 = 0
        canvas.delete(runnerm2)
        runnerm2 = canvas.create_image(random.randrange(965,1220),30,image=imagerunnerm2)
        movimientoRunnerM2()





#Funcion que mueve el carro del player 1
def key2(event):
    """
    """
    global x,i,j,carrom,canvas
    
    tecla = repr(event.char)
    if(tecla == "'d'" or tecla == "'D'"):
        if(i < 90):
            canvas.delete(carrom)
            i = i + 15
            carrom = canvas.create_image(300+i,600+j,image=imagecarrom)        
    if(tecla == "'a'"or tecla == "'A'"):
        if(i > -150):
            canvas.delete(carrom)
            i = i - 15
            carrom = canvas.create_image(300+i,600+j,image=imagecarrom)
            


p = 0
q = 0
#Funcion que mueve el carro del player 2
def keym2(event):
    """
    """
    global x,p,j,carrom2,canvas
    
    tecla = repr(event.char)
    if(tecla == "'ñ'" or tecla == "'Ñ'"):
        if(p < 160):
            canvas.delete(carrom2)
            p = p + 15
            carrom2 = canvas.create_image(1050+p,600+q,image=imagecarrom2)        
    if(tecla == "'k'"or tecla == "'K'"):
        if(p > -75):
            canvas.delete(carrom2)
            p = p - 15
            carrom2 = canvas.create_image(1050+p,600+q,image=imagecarrom2)

#Funcion que mueve la parte izquierda del mapa
fm1 = 0
def mov1m1():
    global canvas,fm1,fondon1m1
    if(fm1 < 4000):
        canvas.move(fondon1m1,0,10)
        fm1 = fm1 + 1
        canvas.after(40,mov1m1)

#funcion que mueve la parte derecha del mapa
fm12 = 0
def mov1m2():
    global canvas,fm12,fondon1m2
    if(fm12 < 4000):
        canvas.move(fondon1m2,0,10)
        fm12 = fm12 + 1
        canvas.after(40,mov1m2)


#Funciones que ayudan a iniciar el juego con una letra para el nivel 1 MULTIPLAYER
def keypausam1(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):
        
        movimientoBanM1()
        movimientoBanM2()
        
        movimientoRunnerM1()
        movimientoRunnerM2()
        
        mov1m1()
        mov1m2()
        canvas.bind("<KeyPress>", key2)
        canvas.bind("<KeyRelease>", keym2)



#####                                                                  #####







        

#Funcion que mueve el fighter
def movimientoFighter():
    global canvas,fighter,i
    if(canvas.coords(fighter)[1]<700)and(i <= 195):
        if(canvas.coords(carro)[0]<canvas.coords(fighter)[0]):
            canvas.move(fighter,-10,10)             
        elif(canvas.coords(carro)[0]>canvas.coords(fighter)[0]):
            canvas.move(fighter,10,10)            
        else:
            canvas.move(fighter,0,10)           
    else:
        canvas.move(fighter,0,-900)
    canvas.after(100,movimientoFighter)



    
#Imagenes niveles single player
imagen2 = tkinter.PhotoImage(file="carro.png")
imagen3 = tkinter.PhotoImage(file="ban.png")
imagen4 = tkinter.PhotoImage(file="runner.png")
imagen5 = tkinter.PhotoImage(file="fighter.png")
imagen1 = tkinter.PhotoImage(file="nivel1.png")
fondonv3 = tkinter.PhotoImage(file="nivel2.png")
fondon3 = tkinter.PhotoImage(file="nivel3.png")
fondon4 = tkinter.PhotoImage(file="nivel4.png")
fondon5 = tkinter.PhotoImage(file="nivel5.png")

#Imagenes niveles multiplayer
imagecarrom = tkinter.PhotoImage(file="carroM.png")
imagecarrom2 = tkinter.PhotoImage(file="Carrom2.png")
imagebanm = tkinter.PhotoImage(file="banM.png")
imagebanm2 = tkinter.PhotoImage(file="banM2.png")
imagerunnerm = tkinter.PhotoImage(file="runnerM.png")
imagerunnerm2 = tkinter.PhotoImage(file="runnerM2.png")

fondo1m1 = tkinter.PhotoImage(file="fondo1m1.png")
fondo1m2 = tkinter.PhotoImage(file="fondo1m2.png")
fondonm1 = tkinter.PhotoImage(file="nivelm1.png")
fondonm2 = tkinter.PhotoImage(file="nivelm2.png")
fondonm3 = tkinter.PhotoImage(file="nivelm3.png")
fondonm4 = tkinter.PhotoImage(file="nivelm4.png")
fondonm5 = tkinter.PhotoImage(file="nivelm5.png")


fondop = tkinter.PhotoImage(file="fondo1prueba.png")


#Funcion para el boton back (volver al menu)
def volverMenu():
    global v,n1,n2,n3,n4,n5,n1m,n2m,n3m,n4m,n5m
    if(niveless.get() == 1)and(players.get()==1):
        n1.destroy()
        v.deiconify()
    elif(niveless.get() == 2)and(players.get()==1):
        n2.destroy()
        v.deiconify()
    elif(niveless.get() == 3)and(players.get()==1):
        n3.destroy()
        v.deiconify()
    elif(niveless.get() == 4)and(players.get()==1):
        n4.destroy()
        v.deiconify()
    elif(niveless.get() == 5)and(players.get()==1):
        n5.destroy()
        v.deiconify()
        
    if(niveless.get() == 1)and(players.get()==2):
        n1m.destroy()
        v.deiconify()
    elif(niveless.get() == 2)and(players.get()==2):
        n2m.destroy()
        v.deiconify()
    elif(niveless.get() == 3)and(players.get()==2):
        n3m.destroy()
        v.deiconify()
    elif(niveless.get() == 4)and(players.get()==2):
        n4m.destroy()
        v.deiconify()
    elif(niveless.get() == 5)and(players.get()==2):
        n5m.destroy()
        v.deiconify()
    

#Funcion para guardar... si tuviera una


#Con esta funcion abro los niveles desde la seleccion de los radioButton    
def niveles():
    """
    """
    global imagen1,fondonv3,imagen2,imagen3,imagen4,presiono,x,i,j,b,canvas,ban,runner,carro,banm,carrom,runnerm,fighterm,n1,n2,n3,n4,n5,fighter,n1m,n2m,n3m,n4m,n5m,fondon1 
    global pruebaf,fondon1m1,fondon1m2,carrom2,banm2,runnerm2
    #Abriendo Nivel 1 
    if(niveless.get() == 1)and(players.get()==1):      
        n1=tkinter.Toplevel()
        v.iconify()
        n1.title("Nivel 1 - Road Fighter")
        canvas = tkinter.Canvas(n1,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()

        #poniendo los botones de guardar y volver al menú
        back = tkinter.Button(n1,text="Back",fg="black",command = volverMenu).place(x=1280,y=350)
        save = tkinter.Button(n1,text="Save",fg="black").place(x=1200,y=350)##falta la funcion para el command

        #nombres de jugadores
        p1 = tkinter.Label(n1,text="Player1:" + "\n" +nombre1.get()).place(x=1230,y=200)
        
        #cargando imagene de fondo   
        fondon1 = canvas.create_image(675,365,image=imagen1)
        ######
        pruebaf = canvas.create_image(675,-5000,image=fondop)

        #Este es nuestro carro principal
        carro = canvas.create_image(600,600,image=imagen2)
        
        #Esta es la mini ban        
        ban = canvas.create_image(random.randrange(450,800),100,image=imagen3)

        
        
        #Este es el runner        
        #runner = canvas.create_image(690,100,image=imagen4)

        #Este es mi fighter
        #fighter = canvas.create_image(650,100,image=imagen5)

        #llamando funciones de los carros           
        
        canvas.bind("<Key>", keypausa)

        
        n1.mainloop()

    #Abriendo Nivel 2    
    elif(niveless.get() == 2)and(players.get()==1):
               
        n2=tkinter.Toplevel()
        v.iconify()
        n2.title("Nivel 2 - Road Fighter")
        canvas = tkinter.Canvas(n2,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n2,text="Back",fg="black",command = volverMenu).place(x=1280,y=350)
        save = tkinter.Button(n2,text="Save",fg="black").place(x=1200,y=350)##falta la funcion para el command

        p1 = tkinter.Label(n2,text="Player1:" + "\n" +nombre1.get()).place(x=1230,y=200)

        fondon2 = canvas.create_image(675,365,image=fondonv3)
        ban = canvas.create_image(random.randrange(450,800),100,image=imagen3)
        carro = canvas.create_image(600,600,image=imagen2)
        runner = canvas.create_image(690,100,image=imagen4)
        fighter = canvas.create_image(650,100,image=imagen5)
                     
        canvas.bind("<Key>", key)
        movimientoBan()
        movimientoRunner()
        movimientoFighter()
         

        
        n2.mainloop()










    ### ABRIENDO LOS NIVELES MULTIPLAYER ###

        
    #Abriendo nivel 1   
    elif(niveless.get() == 1)and(players.get()==2):
               
        n1m=tkinter.Toplevel()
        v.iconify()
        n1m.title("Nivel 2 Multiplayer - Road Fighter")
        canvas = tkinter.Canvas(n1m,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n1m,text="Back",fg="black",command = volverMenu).place(x=678,y=350)
        save = tkinter.Button(n1m,text="Save",fg="black").place(x=640,y=350)##falta la funcion para el command

        p1 = tkinter.Label(n1m,text="Player1:" + "\n" + "\n" +nombre1.get()).place(x=580,y=200)
        p2 = tkinter.Label(n1m,text="Player2:" + "\n" + "\n" +nombre2.get()).place(x=710,y=200)
        #mire a ver si elimina el fondo estatico
        fondon1m = canvas.create_image(675,365,image=fondonm1)
        #fondos separados
        fondon1m1 = canvas.create_image(339,-8000,image=fondo1m1)
        fondon1m2 = canvas.create_image(1013,-8000,image=fondo1m2)

        carrom = canvas.create_image(300,600,image=imagecarrom)
        carrom2 = canvas.create_image(1050,600,image=imagecarrom2)
        banm = canvas.create_image(random.randrange(140,400),30,image=imagebanm)
        banm2 = canvas.create_image(random.randrange(965,1220),30,image=imagebanm2)
        
        runnerm = canvas.create_image(random.randrange(140,400),30,image=imagerunnerm)
        runnerm2 = canvas.create_image(random.randrange(970,1230),30,image=imagerunnerm2)


        canvas.bind("<Key>", keypausam1)
        


         

        
        n1m.mainloop()






















#poniendo todas las varras
niveless = tkinter.IntVar()
players = tkinter.IntVar()
nombre1 = tkinter.StringVar()
nombre2 = tkinter.StringVar()



#definiendo funciones para los botones del menú
def onePlayer():
    p = tkinter.Label(v,text="Player:").place(x=600,y=360)
    player = tkinter.Entry(v,textvariable=nombre1 ).place(x=650,y=360)

def twoPlayers():
    p1 = tkinter.Label(v,text="Player1:\n").place(x=600,y=420)
    player1 = tkinter.Entry(v,textvariable = nombre1).place(x=650,y=420)
    p2 = tkinter.Label(v,text="Player2:").place(x=600,y=450)
    player2 = tkinter.Entry(v,textvariable = nombre2).place(x=650,y=450)

  
def select():
    global radioboton1, radioboton2
    radioboton1 = tkinter.Radiobutton(v,text="One Player",value=1,variable=players,command=onePlayer).place(x=640,y=330)
    radioboton2 = tkinter.Radiobutton(v,text="Two PLayers",value=2,variable=players,command=twoPlayers).place(x=637,y=390)


def Exit():
    exit()
        

#Crea los radio buttons
def radioButtons():
    rb1 = tkinter.Radiobutton(v,text="Lvl 1",value=1,variable = niveless).place(x=600,y=510)
    rb2 = tkinter.Radiobutton(v,text="Lvl 2",value=2,variable = niveless).place(x=660,y=510)
    rb3 = tkinter.Radiobutton(v,text="Lvl 3",value=3,variable = niveless).place(x=720,y=510)
    rb4 = tkinter.Radiobutton(v,text="Lvl 4",value=4,variable = niveless).place(x=600,y=540)
    rb5 = tkinter.Radiobutton(v,text="Lvl 5",value=5,variable = niveless).place(x=660,y=540)





#poniendo botones y cajas de texto
selectPlayer = tkinter.Button(v,text="Select PLayers",fg="red",command=select).place(x=640, y=300)
bExit = tkinter.Button(v,text="Exit",fg="red",command = Exit).place(x=650,y=600)
bPlay = tkinter.Button(v,text="Play",fg="red",command = niveles).place(x=690,y=600)
selectLvl = tkinter.Button(v,text="Select your level:",fg="red",command=radioButtons).place(x=635,y=480)



    
#Funcion que abre una ventana con las instrucciones
def instrucciones():
    vi = tkinter.Toplevel()    
    vi.geometry("1000x500")
    vi.title("Instructions")
    vi.config(bg="black")
    inst = tkinter.Label(vi,text="""El objetivo es superar los 5 diferentes niveles los cuales contaran con un mapa ambientado
en las diferentes condiciones climáticas y una dificultad creciente (del nivel 1 al 5)para acabar el juego.
Estos niveles se pasan esquivando los carros enemigos de derecha a izquierda o izquierda a derecha
y cuidando de que no se agote la gasolina. Los coches enemigos van apareciendo por la parte superior de la pantalla.
Se puede obtener un poco de combustible pasando por encima de un ítem con forma de galón de gasolina que aparece
un par de veces en cada nivel. Adicional a esto, en la carretera puede salir manchas de aceite que desestabilizan
él carro del jugador al igual que los choques con los carros enemigos.
La única forma de que el carro del jugador explote, será tocando los bordes de la carretera.""").place(x=200,y=50)
    
    comojug = tkinter.Label(vi,text="""Para jugar se utilizan las siguientes teclas del teclado: """ ).place(x=375,y=250)
    
    imagenTeclas = tkinter.PhotoImage(file="teclas.png")
    teclas = tkinter.Label(vi,image=imagenTeclas).place(x=350,y=300)
    
    vi.mainloop()
    
    



#Creando menú instrucciones
barraMenu = tkinter.Menu(v)
menuInstrucciones = tkinter.Menu(barraMenu)
menuInstrucciones.add_command(label="How To Play",command=instrucciones)
menuInstrucciones.add_command(label="Exit",command=Exit)
barraMenu.add_cascade(label="Instructions",menu=menuInstrucciones)
v.config(menu=barraMenu)#Nos pone nuestro menú en la ventana 



v.mainloop
