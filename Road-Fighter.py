import tkinter

#Creando la Ventana Principal 
v = tkinter.Tk()
v.geometry("1350x730")
v.title("Menú Road Fighter")

#poniendo imagen de fondo
imagen = tkinter.PhotoImage(file="fondoMenu.png")
fondo = tkinter.Label(v,image=imagen).place(x=0,y=0)


#Esta funcion mueve el miniBan
b = 0
def movimientoBan():
    """
    """
    global canvas,b,n1, ban
    if(b<200):
        canvas.move(ban,0,5)
        b = b+1
        canvas.after(18,movimientoBan)
    if(b==200):
        b=0
        ban = canvas.create_image(750,50,image=imagen3)




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

def derecha():
    """
    """
    
    global presiono,x,i,j, carro
    canvas.delete(carro)
    canvas.delete(x)
    i = i + 15
    x = canvas.create_image(600+i,600+j,image=imagen2)

def izquierda():
    """
    """
    global presiono,x,i,j, carro
    canvas.delete(carro)
    canvas.delete(x)
    i = i - 15
    x = canvas.create_image(600+i,600+j,image=imagen2)

"""def arriba():
    canvas.delete(x)
    j = j + 15
    x = canvas.create_image(600+i,600+j,image=imagen2)

def abajo():
    canvas.delete(x)
    j = j - 15
    y = canvas.create_image(600+i,600+j,image=imagen2)"""

def key(event):
    """
    """
    global x,i,j,carro,canvas
    canvas.delete(carro)
    
    tecla = repr(event.char)
    print(tecla)
    if(tecla == "'d'"):
        if(i < 195):
            canvas.delete(x)
            i = i + 15
            x = canvas.create_image(600+i,600+j,image=imagen2)
                    
    if(tecla == "'a'"):
        if(i > -150):
            canvas.delete(x)
            i = i - 15
            x = canvas.create_image(600+i,600+j,image=imagen2)

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

#cargando imagenes para el nivel 1 single player
imagen1 = tkinter.PhotoImage(file="nivel1.png")
imagen2 = tkinter.PhotoImage(file="carro.png")
imagen3 = tkinter.PhotoImage(file="ban.png")
imagen4 = tkinter.PhotoImage(file="runner.png")
fondonv3 = tkinter.PhotoImage(file="nivel2.png")


#Funcion para el boton back (volver al menu)
def volverMenu():
    global v,n1,n2,n3,n4,n5
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
        n1.destroy()
        v.deiconify()
    elif(niveless.get() == 2)and(players.get()==2):
        n2.destroy()
        v.deiconify()
    elif(niveless.get() == 3)and(players.get()==2):
        n3.destroy()
        v.deiconify()
    elif(niveless.get() == 4)and(players.get()==2):
        n4.destroy()
        v.deiconify()
    elif(niveless.get() == 5)and(players.get()==2):
        n5.destroy()
        v.deiconify()
    

#Funcion para guardar... si tuviera una


#Con esta funcion abro los niveles desde la seleccion de los radioButton    
def niveles():
    """
    """
    global imagen1,fondonv3,imagen2,imagen3,imagen4,presiono,x,i,j,b,canvas,ban,runner,carro,n1,n2,n3,n4,n5
    
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
        fondo = canvas.create_image(675,365,image=imagen1)

        #Este es nuestro carro principal
        carro = canvas.create_image(600,600,image=imagen2)
        
        #Esta es la mini ban        
        ban = canvas.create_image(600,100,image=imagen3)
        
        #Este es el runner        
        runner = canvas.create_image(690,100,image=imagen4)

        #Este es mi fighter si tuviera uno...

        #llamando funciones de los carros           
        canvas.bind("<Key>", key)
        movimientoBan()
        movimientoRunner()
        
        n1.mainloop()

        
    elif(niveless.get() == 2)and(players.get()==1):
        #Abriendo Nivel 1       
        n2=tkinter.Toplevel()
        v.iconify()
        n2.title("Nivel 1 - Road Fighter")
        canvas = tkinter.Canvas(n2,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n2,text="Back",fg="black",command = volverMenu).place(x=1280,y=350)
        save = tkinter.Button(n2,text="Save",fg="black").place(x=1200,y=350)##falta la funcion para el command

        p1 = tkinter.Label(n2,text="Player1:" + "\n" +nombre1.get()).place(x=1230,y=200)

        fondo = canvas.create_image(675,365,image=fondonv3)
        carro = canvas.create_image(600,600,image=imagen2)
        ban = canvas.create_image(600,100,image=imagen3)     
        runner = canvas.create_image(690,100,image=imagen4)
        #Este es mi fighter si tuviera uno...
         
        canvas.bind("<Key>", key)
        movimientoBan()
        movimientoRunner()
        
        n2.mainloop()








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
