import tkinter
import random
from tkinter import messagebox

print("Tiempo de espera aproximado: 20 Segundos.\nSe recomienda paciencia...")


#Creando la Ventana Principal 
v = tkinter.Tk()
v.geometry("1350x730")
v.title("Menú Road Fighter")

#poniendo imagen de fondo
imagen = tkinter.PhotoImage(file="fondoMenu.png")
fondo = tkinter.Label(v,image=imagen).place(x=0,y=0)




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
        if(choqueCrt()):
            return 0 
        canvas.after(30,movimientoBan)

    else:
        b=0
        canvas.delete(ban)
        ban = canvas.create_image(random.randrange(450,800),50,image=imagen3)
        movimientoBan()




#funcion que mueve el runner
                
r=0
def mri():    
    global canvas,runner,r
    if (r<260):
        if(canvas.coords(runner)[0]>450):
            canvas.move(runner,-5,3)
            r = r+1
            if(choqueCrt()):
                return 0 
            canvas.after(20,mri)

        else:
            movimientoRunner()
            
def movimientoRunner():
    global canvas,runner,r
    if (r<260):
        if(canvas.coords(runner)[0]<800):
            canvas.move(runner,5,3)
            r = r+1
            if(choqueCrt()):
                return 0 
            canvas.after(20,movimientoRunner)
        else:
            mri()            

    else:
        r = 0
        canvas.delete(runner)
        runner = canvas.create_image(690,50,image=imagen4)
        movimientoRunner()
        


    
        
#Funciones las cuales hacen que movamos nuestro carro principal
i = 0
j = 0

def key(event):
    """
    """
    global i,j,carro,canvas
    
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



    
#Funciones que ayudan a iniciar el juego con una letra para el nivel 1
def keypausa(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):
        movimientoBan()
        movnvl1()
        movimientoRunner()
        movimientoFighter()
        canvas.bind("<Key>", key)



#Funcion que mueve el fondo del nivel 1
mov1 = 0
def movnvl1():
    global canvas,mov1, pruebaf
    if(canvas.coords(pruebaf)[1] < 9800):
        if(mov1 < 4000):
            canvas.move(pruebaf,0,10)
            mov1 = mov1 + 1
            if(choqueCrt()):
                return 0 
            canvas.after(40,movnvl1)


#Funcion de choque contra los bordes single player    
def choqueCrt():
    global esplosion, canvas, carro
    x = canvas.coords(carro)[0]
    y = canvas.coords(carro)[1]
    
    if(x == 795)or(x == 450):
        explosion  = canvas.create_image(x,y,image=esplosion)
        return True

    

#Funcion que mueve el fighter
def movimientoFighter():
    
    global canvas,fighter,i
    if(canvas.coords(fighter)[1]<700)and(i <= 195):
        if(choqueCrt()):
            return 0 
        elif(canvas.coords(carro)[0]<canvas.coords(fighter)[0]):
            canvas.move(fighter,-10,10)             
        elif(canvas.coords(carro)[0]>canvas.coords(fighter)[0]):
            canvas.move(fighter,10,10)            
        else:
            canvas.move(fighter,0,10)           
    else:
        canvas.move(fighter,0,-900)
    canvas.after(100,movimientoFighter)

    
        

#######                                                        ########















####################################################################

           ###### FUNCIONES MULTIPLAYER ######
    
####################################################################

    

#FUNCIONES QUE MUEVEN LAS MINI VAN DE TODOS LOS NIVELES



#Funcion Extra ban
def movimientoBanE():
    global canvas,banE,carrom,g,g2,g3,g4,g5,vel,vel3,vel4,vel5

    #Ban jugador 1 NIVEL 1
    if(niveless.get() == 1)and(players.get()==2):
  
        if(canvas.coords(banE)[1] < 800):
            canvas.move(banE,0,5)
            
            xb = canvas.coords(banE)[0]
            yb = canvas.coords(banE)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banE,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g -= 1
                g3 -= 1
                g4 -= 1
                g5 -= 1
                vel -= 1
                vel3 -= 1
                vel4 -= 1
                vel5 -= 1
                
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banE,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g -= 1
                g3 -= 1
                g4 -= 1
                g5 -= 1
                vel -= 1
                vel3 -= 1
                vel4 -= 1
                vel5 -= 1
                
            if(choqueCarretera1m()):
                return 0

            canvas.after(30,movimientoBanE)

        else:
            canvas.delete(banE)
            banE = canvas.create_image(random.randrange(140,400),-200,image=imagebanE) 
            movimientoBanE()


def movimientoBanE2():
    global canvas,banE2,carrom2,gM,gM2,g3M,g4M,g5M,velM,vel2M,vel3M,vel4M,vel5M
    #Ban jugador 2 NIVEL 1
    if(niveless.get() == 1)and(players.get()==2):
  
        if(canvas.coords(banE2)[1]<800):
            canvas.move(banE2,0,5)

            xb = canvas.coords(banE2)[0]
            yb = canvas.coords(banE2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banE2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                gM -= 1
                g3M -= 1
                g4M -= 1
                g5M -= 1
                velM -= 1
                vel3M -= 1
                vel4M -= 1
                vel5M -= 1
                
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banE2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                gM -= 1
                g3M -= 1
                g4M -= 1
                g5M -= 1
                velM -= 1
                vel3M -= 1
                vel4M -= 1
                vel5M -= 1


            if(choqueCarretera1m2()):
                return 0

            canvas.after(30,movimientoBanE2)

        else:
            canvas.delete(banE2)
            banE2 = canvas.create_image(random.randrange(970,1230),-200,image=imagebanE2) 
            movimientoBanE2()




    
####################### Player 1 ##############################

def movimientoBanM1():
    global canvas, banm,g,g2,g3,g4,g5,vel,vel2,vel3,vel4,vel5
    #Ban jugador 1 NIVEL 1
    if(niveless.get() == 1)and(players.get()==2):
  
        if(canvas.coords(banm)[1] < 800):
            
            canvas.move(banm,0,5)

            xb = canvas.coords(banm)[0]
            yb = canvas.coords(banm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g -= 1
                vel -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g -= 1
                vel -=1

            if(choqueCarretera1m()):
                return 0

            canvas.after(60,movimientoBanM1)

        else:
            canvas.delete(banm)
            banm = canvas.create_image(random.randrange(140,400),-30,image=imagebanm) 
            movimientoBanM1()

    #Ban jugador 1 NIVEL 2
    elif(niveless.get() == 2)and(players.get()==2):

        if(canvas.coords(banm)[1] < 800):
            
            canvas.move(banm,0,5)

            xb = canvas.coords(banm)[0]
            yb = canvas.coords(banm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g2 -= 1
                vel2 -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g2 -= 1
                vel2 -=1

            if(choqueCarretera1m()):
                return 0

            canvas.after(40,movimientoBanM1)

        else:
            bm1=0
            canvas.delete(banm)
            banm = canvas.create_image(random.randrange(140,400),-30,image=imagebanm) 
            movimientoBanM1()

    #Ban jugador 1 NIVEL 3
    elif(niveless.get() == 3)and(players.get()==2):

        if(canvas.coords(banm)[1] < 800):
            
            canvas.move(banm,0,5)

            xb = canvas.coords(banm)[0]
            yb = canvas.coords(banm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g3 -= 1
                vel3 -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g3 -= 1
                vel3 -=1

            if(choqueCarretera1m()):
                return 0

            canvas.after(30,movimientoBanM1)

        else:
            bm1=0
            canvas.delete(banm)
            banm = canvas.create_image(random.randrange(140,400),-30,image=imagebanm) 
            movimientoBanM1()

    #Ban jugador 1 NIVEL 4
    elif(niveless.get() == 4)and(players.get()==2):

        if(canvas.coords(banm)[1] < 800):
            
            canvas.move(banm,0,5)
  
            xb = canvas.coords(banm)[0]
            yb = canvas.coords(banm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g4 -= 1
                vel4 -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g4 -= 1
                vel4 -=1

            if(choqueCarretera1m()):
                return 0

            canvas.after(20,movimientoBanM1)

        else:
            canvas.delete(banm)
            banm = canvas.create_image(random.randrange(140,400),-30,image=imagebanm) 
            movimientoBanM1()

    #Ban jugador 1 NIVEL 5
    elif(niveless.get() == 5)and(players.get()==2):

        if(canvas.coords(banm)[1] < 800):
            
            canvas.move(banm,0,5)

            xb = canvas.coords(banm)[0]
            yb = canvas.coords(banm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g5 -= 1
                vel5 -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g5 -= 1
                vel5 -=1

            if(choqueCarretera1m()):
                return 0

            canvas.after(10,movimientoBanM1)

        else:
            bm1=0
            canvas.delete(banm)
            banm = canvas.create_image(random.randrange(140,400),-50,image=imagebanm) 
            movimientoBanM1()


  

####################### Player 2 ##############################
#Funcion que mueve el miniBan en el lado del player 2

def movimientoBanM2():
    global canvas, banm2,gM,g2M,g3M,g4M,g5M,velM,vel2M,vel3M,vel4M,vel5M
    #Ban jugador 2 NIVEL 1
    if(niveless.get() == 1)and(players.get()==2):
        
        if(canvas.coords(banm2)[1] < 800):
            
            canvas.move(banm2,0,5)

            xb = canvas.coords(banm2)[0]
            yb = canvas.coords(banm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm2,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                gM -= 1
                velM -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                gM -= 1
                velM -=1

            if(choqueCarretera1m2()):
                return 0
            
            canvas.after(60,movimientoBanM2)
        else:
            
            canvas.delete(banm2)
            banm2 = canvas.create_image(random.randrange(970,1220),-30,image=imagebanm2) 
            movimientoBanM2()



    #Ban jugador 2 NIVEL 2
    elif(niveless.get() == 2)and(players.get()==2):
        
        if(canvas.coords(banm2)[1] < 800):
            
            canvas.move(banm2,0,5)

            xb = canvas.coords(banm2)[0]
            yb = canvas.coords(banm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm2,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g2M -= 1
                vel2M -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g2M -= 1
                vel2M -=1
            canvas.after(40,movimientoBanM2)
            
        else:

            canvas.delete(banm2)
            banm2 = canvas.create_image(random.randrange(970,1220),-30,image=imagebanm2) 
            movimientoBanM2()

    #Ban jugador 2 NIVEL 3
    elif(niveless.get() == 3)and(players.get()==2):
        
        if(canvas.coords(banm2)[1] < 800):
            
            canvas.move(banm2,0,5)

            xb = canvas.coords(banm2)[0]
            yb = canvas.coords(banm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm2,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g3M -= 1
                vel3M -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g3M -= 1
                vel3M -=1

            if(choqueCarretera1m2()):
                return 0
            
            canvas.after(30,movimientoBanM2)
            
        else:

            canvas.delete(banm2)
            banm2 = canvas.create_image(random.randrange(970,1220),-30,image=imagebanm2) 
            movimientoBanM2()
            

    #Ban jugador 2 NIVEL 4
    elif(niveless.get() == 4)and(players.get()==2):
        
        if(canvas.coords(banm2)[1] < 800):
            
            canvas.move(banm2,0,5)

            xb = canvas.coords(banm2)[0]
            yb = canvas.coords(banm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm2,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g4M -= 1
                vel4M -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g4M -= 1
                vel4M -=1

            if(choqueCarretera1m2()):
                return 0
            
            canvas.after(20,movimientoBanM2)
            
        else:

            canvas.delete(banm2)
            banm2 = canvas.create_image(random.randrange(970,1220),-40,image=imagebanm2) 
            movimientoBanM2()

    #Ban jugador 2 NIVEL 5
    elif(niveless.get() == 5)and(players.get()==2):
        
        if(canvas.coords(banm2)[1] < 800):
            
            canvas.move(banm2,0,5)

            xb = canvas.coords(banm2)[0]
            yb = canvas.coords(banm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xb and xc<=xb +30) and (yc>=yb and yc<=yb+60)) :
                canvas.move(banm2,0,300)
                print("K-BUM!"+"*Choque contra el ban*")
                g5M -= 1
                vel5M -=1
            if((xc <= xb and xc+30 >= xb) and (yc <= yb and yc+60 >= yb)) :
                canvas.move(banm2,0,350)
                print("K-BUM!"+"*Choque contra el ban*")
                g5M -= 1
                vel5M -=1

            if(choqueCarretera1m2()):
                return 0
            
            canvas.after(10,movimientoBanM2)
            
        else:

            canvas.delete(banm2)
            banm2 = canvas.create_image(random.randrange(970,1220),-40,image=imagebanm2) 
            movimientoBanM2()




#######################################################################################################################################################################



        
#FUNCIONES QUE MUEVEN LOS RUNNER DE TODOS LOS NIVELES

            
####################### Player 1 ##############################
#Funcion que mueve los runner del player 1 en todos los niveles
#Movimiento hacia la izquierda
def mri2m():    
    global canvas,runnerm,rm1,carrom,carroE,g,g2,g3,g4,g5,vel,vel2,vel3,vel4,vel5

    #If del NIVEL 2  Player 1
    if(niveless.get() == 2)and(players.get()==2):
        
        if (rm1<400):
            if(canvas.coords(runnerm)[0]>140):
                canvas.move(runnerm,-4,2)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2 -= 2
                    vel2 -=1
                    
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2 -= 2
                    vel2 -=1
                    

                if(choqueCarretera1m()):
                    return 0
                
                canvas.after(70,mri2m)
            else:
                movimientoRunnerM1()

    #If del NIVEL 3 Player1
    if(niveless.get() == 3)and(players.get()==2):

        if (rm1<400):
            if(canvas.coords(runnerm)[0]>140):
                canvas.move(runnerm,-5,3)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3 -= 3
                    vel3 -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3 -= 3
                    vel3 -=1

                if(choqueCarretera1m()):
                    return 0
                
                canvas.after(50,mri2m)
            else:
                movimientoRunnerM1()

    #If del NIVEL 4 Player1
    if(niveless.get() == 4)and(players.get()==2):

        if (rm1<350):
            if(canvas.coords(runnerm)[0]>140):
                canvas.move(runnerm,-6,4)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4 -= 4
                    vel4 -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4 -= 4
                    vel4 -=1

                if(choqueCarretera1m()):
                    return 0
                
                canvas.after(35,mri2m)
            else:
                movimientoRunnerM1()


    #If del NIVEL 5 Player1
    if(niveless.get() == 5)and(players.get()==2):

        if (rm1<300):
            if(canvas.coords(runnerm)[0]>140):
                canvas.move(runnerm,-7,4)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5 -= 5
                    vel5 -=2
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5 -= 5
                    vel5 -=2

                if(choqueCarretera1m()):
                    return 0
                
                canvas.after(20,mri2m)
            else:
                movimientoRunnerM1()




#Movimiento hacia la derecha            
rm1=0
def movimientoRunnerM1():
    global canvas,runnerm,rm1,carrom,g,g2,g3,g4,g5,vel,vel2,vel3,vel4,vel5

    #If del NIVEL 2  Player 1
    if(niveless.get() == 2)and(players.get()==2):

        if (rm1<400):
            if(canvas.coords(runnerm)[0]<400):
                canvas.move(runnerm,4,2)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2 -= 2
                    vel2 -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2 -= 2
                    vel2 -=1


                if(choqueCarretera1m()):
                    return 0

                canvas.after(70,movimientoRunnerM1)

            else:
                mri2m()
               
        else:
            rm1 = 0
            canvas.delete(runnerm)
            runnerm = canvas.create_image(random.randrange(140,400),-30,image=imagerunnerm)
            movimientoRunnerM1()
            

    #If del NIVEL 3 Player1
    if(niveless.get() == 3)and(players.get()==2):

        if (rm1<400):
            if(canvas.coords(runnerm)[0]<400):
                canvas.move(runnerm,5,3)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3 -= 3
                    vel3 -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3 -= 3
                    vel3 -=1


                if(choqueCarretera1m()):
                    return 0

                canvas.after(50,movimientoRunnerM1)

            else:
                mri2m()
                
        else:
            rm1 = 0
            canvas.delete(runnerm)
            runnerm = canvas.create_image(random.randrange(140,400),-30,image=imagerunnerm)
            movimientoRunnerM1()


    #If del NIVEL 4 Player1
    if(niveless.get() == 4)and(players.get()==2):

        if (rm1<350):
            if(canvas.coords(runnerm)[0]<400):
                canvas.move(runnerm,6,4)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4 -= 4
                    vel4 -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4 -= 4
                    vel4 -=1


                if(choqueCarretera1m()):
                    return 0

                canvas.after(35,movimientoRunnerM1)

            else:
                mri2m()
                
        else:
            rm1 = 0
            canvas.delete(runnerm)
            runnerm = canvas.create_image(random.randrange(140,400),-30,image=imagerunnerm)
            movimientoRunnerM1()


    #If del NIVEL 5 Player1
    if(niveless.get() == 5)and(players.get()==2):

        if (rm1<300):
            if(canvas.coords(runnerm)[0]<400):
                canvas.move(runnerm,7,4)
                rm1 = rm1+1

                xr = canvas.coords(runnerm)[0]
                yr = canvas.coords(runnerm)[1]
                xc = canvas.coords(carrom)[0]
                yc = canvas.coords(carrom)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5 -= 5
                    vel5 -=2
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5 -= 5
                    vel5 -=2


                if(choqueCarretera1m()):
                    return 0

                canvas.after(20,movimientoRunnerM1)

            else:
                mri2m()
                
        else:
            rm1 = 0
            canvas.delete(runnerm)
            runnerm = canvas.create_image(random.randrange(140,400),-30,image=imagerunnerm)
            movimientoRunnerM1()






####################### Player 2 ##############################

            

#funcion que mueve el Runner del player 2 en todos los niveles
#Movimiento hacia la izquierda
def mri2m2():    
    global canvas,runnerm2,rm2,carrom2,gM,g2M,g3M,g4M,g5M,velM,vel2M,vel3M,vel4M,vel5M

    #If del NIVEL 2 Player 2
    if(niveless.get() == 2)and(players.get()==2):
        if (rm2<400):
            if(canvas.coords(runnerm2)[0]>960):
                canvas.move(runnerm2,-4,2)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2M -= 2
                    vel2M -=1

                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2M -= 2
                    vel2M -=1

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(70,mri2m2)

            else:
                movimientoRunnerM2()
                
    #If del NIVEL 3 Player 2
    if(niveless.get() == 3)and(players.get()==2):
        if (rm2<400):
            if(canvas.coords(runnerm2)[0]>960):
                canvas.move(runnerm2,-5,3)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3M -= 3
                    vel3M -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3M -= 3
                    vel3M -=1

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(50,mri2m2)

            else:
                movimientoRunnerM2()

    #If del NIVEL 4 Player 2       
    if(niveless.get() == 4)and(players.get()==2):
        if (rm2<350):
            if(canvas.coords(runnerm2)[0]>960):
                canvas.move(runnerm2,-6,4)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4M -= 4
                    vel4M -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4M -= 4
                    vel4M -=1

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(35,mri2m2)

            else:
                movimientoRunnerM2()

    #If del NIVEL 5 Player 2       
    if(niveless.get() == 5)and(players.get()==2):
        if (rm2<300):
            if(canvas.coords(runnerm2)[0]>960):
                canvas.move(runnerm2,-7,4)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5M -= 5
                    vel5M -=2
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5M -= 5
                    vel5M -=2

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(20,mri2m2)

            else:
                movimientoRunnerM2()



#Movimiento hacia la Derecha        
rm2=0
def movimientoRunnerM2():
    global canvas,runnerm2,rm2,carrom2,gM,gM2,g3M,g4M,g5M,velM,vel2M,vel3M,vel4M,vel5M

    #If del NIVEL 2 Player 2
    if(niveless.get() == 2)and(players.get()==2):
        if (rm2<400):
            if(canvas.coords(runnerm2)[0]<1220):
                canvas.move(runnerm2,4,2)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2M -= 2
                    vel2M -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g2M -= 1
                    vel2M -=1

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(70,movimientoRunnerM2)
    

            else:
                mri2m2()

        else:
            rm2 = 0
            canvas.delete(runnerm2)
            runnerm2 = canvas.create_image(random.randrange(965,1220),-30,image=imagerunnerm2)
            movimientoRunnerM2()

    #If del NIVEL 3 Player 2
    if(niveless.get() == 3)and(players.get()==2):
        if (rm2<400):
            if(canvas.coords(runnerm2)[0]<1220):
                canvas.move(runnerm2,5,3)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3M -= 3
                    vel3M -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g3M -= 3
                    vel3M -=1

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(50,movimientoRunnerM2)

            else:
                mri2m2()

        else:
            rm2 = 0
            canvas.delete(runnerm2)
            runnerm2 = canvas.create_image(random.randrange(965,1220),-30,image=imagerunnerm2)
            movimientoRunnerM2()

    #If del NIVEL 4 Player 2
    if(niveless.get() == 4)and(players.get()==2):
        if (rm2<350):
            if(canvas.coords(runnerm2)[0]<1220):
                canvas.move(runnerm2,6,4)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4M -= 4
                    vel4M -=1
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g4M -= 4
                    vel4M -=1

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(35,movimientoRunnerM2)

            else:
                mri2m2()

        else:
            rm2 = 0
            canvas.delete(runnerm2)
            runnerm2 = canvas.create_image(random.randrange(965,1220),-30,image=imagerunnerm2)
            movimientoRunnerM2()

    #If del NIVEL 5 Player 2
    if(niveless.get() == 5)and(players.get()==2):
        if (rm2<300):
            if(canvas.coords(runnerm2)[0]<1220):
                canvas.move(runnerm2,7,4)
                rm2 = rm2+1

                xr = canvas.coords(runnerm2)[0]
                yr = canvas.coords(runnerm2)[1]
                xc = canvas.coords(carrom2)[0]
                yc = canvas.coords(carrom2)[1]
                if((xc>=xr and xc<=xr +30) and (yc>=yr and yc<=yr+60)) :
                    canvas.move(runnerm2,0,300)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5M -= 5
                    vel5M -=2
                if((xc <= xr and xc+30 >= xr) and (yc <= yr and yc+60 >= yr)) :
                    canvas.move(runnerm2,0,350)
                    print("K-BUM!"+"*Choque contra el Runner*")
                    g5M -= 5
                    vel5M -=2

                if(choqueCarretera1m2()):
                    return 0

                canvas.after(20,movimientoRunnerM2)

            else:
                mri2m2()

        else:
            rm2 = 0
            canvas.delete(runnerm2)
            runnerm2 = canvas.create_image(random.randrange(965,1220),-30,image=imagerunnerm2)
            movimientoRunnerM2()







#######################################################################################################################################################################







###   FUNCIONES QUE MUEVEN LOS FIGHTERS DE TODOS LOS NIVELES   ###

####################### Player 1 ##############################
            

def movimientoFighterM1():
    global canvas,fighterm,i,carrom,g3,g4,g5,vel3,vel4,vel5
    
    # Fighter nivel 3 Player 1
    if(niveless.get() == 3)and(players.get()==2):
            
        if(canvas.coords(fighterm)[1]<700)and(i < 400):

            xf = canvas.coords(fighterm)[0]
            yf = canvas.coords(fighterm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xf and xc<=xf +30) and (yc>=yf and yc<=yf+60)) :
                canvas.move(fighterm,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g3 -= 3
                vel3 -= 1
            if((xc <= xf and xc+30 >= xf) and (yc <= yf and yc+60 >= yf)) :
                canvas.move(fighterm,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g3 -= 3
                vel3 -= 1

            if(choqueCarretera1m()):
                return 0

            elif(canvas.coords(carrom)[0]<canvas.coords(fighterm)[0]):
                canvas.move(fighterm,-2,10)             
            elif(canvas.coords(carrom)[0]>canvas.coords(fighterm)[0]):
                canvas.move(fighterm,2,10)            
            else:
                canvas.move(fighterm,0,10)           
        else:
            canvas.move(fighterm,0,-900)
        canvas.after(100,movimientoFighterM1)

    # Fighter nivel 4 Player 1
    if(niveless.get() == 4)and(players.get()==2): 
        if(canvas.coords(fighterm)[1]<700)and(i < 400):

            xf = canvas.coords(fighterm)[0]
            yf = canvas.coords(fighterm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xf and xc<=xf +30) and (yc>=yf and yc<=yf+60)) :
                canvas.move(fighterm,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g4 -= 4
                vel4 -= 1
            if((xc <= xf and xc+30 >= xf) and (yc <= yf and yc+60 >= yf)) :
                canvas.move(fighterm,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g4 -= 4
                vel4 -= 1


            if(choqueCarretera1m()):
                return 0

            elif(canvas.coords(carrom)[0]<canvas.coords(fighterm)[0]):
                canvas.move(fighterm,-4,15)             
            elif(canvas.coords(carrom)[0]>canvas.coords(fighterm)[0]):
                canvas.move(fighterm,4,15)            
            else:
                canvas.move(fighterm,0,15)           
        else:
            canvas.move(fighterm,0,-900)
        canvas.after(100,movimientoFighterM1)

    # Fighter nivel 5 Player 1
    if(niveless.get() == 5)and(players.get()==2): 
        if(canvas.coords(fighterm)[1]<700)and(i < 400):

            xf = canvas.coords(fighterm)[0]
            yf = canvas.coords(fighterm)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xf and xc<=xf +30) and (yc>=yf and yc<=yf+60)) :
                canvas.move(fighterm,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g35 -= 5
                vel5 -= 2
            if((xc <= xf and xc+30 >= xf) and (yc <= yf and yc+60 >= yf)) :
                canvas.move(fighterm,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g5 -= 5
                vel5 -= 2


            if(choqueCarretera1m()):
                return 0

            elif(canvas.coords(carrom)[0]<canvas.coords(fighterm)[0]):
                canvas.move(fighterm,-6,20)             
            elif(canvas.coords(carrom)[0]>canvas.coords(fighterm)[0]):
                canvas.move(fighterm,6,20)            
            else:
                canvas.move(fighterm,0,20)           
        else:
            canvas.move(fighterm,0,-900)
        canvas.after(100,movimientoFighterM1)




####################### Player 2 ##############################


def movimientoFighterM2():
    global canvas,fighterm2,i,carrom2,g3M,g4M,g5M,vel3M,vel4M,vel5M
    
    # Fighter nivel 3 Player 2
    if(niveless.get() == 3)and(players.get()==2): 
        if(canvas.coords(fighterm2)[1]<700)and(i < 400):

            xf = canvas.coords(fighterm2)[0]
            yf = canvas.coords(fighterm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xf and xc<=xf +30) and (yc>=yf and yc<=yf+60)) :
                canvas.move(fighterm2,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g3M -= 3
                vel3M -= 1
            if((xc <= xf and xc+30 >= xf) and (yc <= yf and yc+60 >= yf)) :
                canvas.move(fighterm2,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g3M -= 3
                vel3M -= 1


            if(choqueCarretera1m2()):
                return 0

            elif(canvas.coords(carrom2)[0]<canvas.coords(fighterm2)[0]):
                canvas.move(fighterm2,-2,10)             
            elif(canvas.coords(carrom2)[0]>canvas.coords(fighterm2)[0]):
                canvas.move(fighterm2,2,10)            
            else:
                canvas.move(fighterm2,0,10)           
        else:
            canvas.move(fighterm2,0,-900)
        canvas.after(100,movimientoFighterM2)

    # Fighter nivel 4 Player 2
    if(niveless.get() == 4)and(players.get()==2): 
        if(canvas.coords(fighterm2)[1]<700)and(i < 400):

            xf = canvas.coords(fighterm2)[0]
            yf = canvas.coords(fighterm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xf and xc<=xf +30) and (yc>=yf and yc<=yf+60)) :
                canvas.move(fighterm2,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g4M -= 4
                vel4M -= 1
            if((xc <= xf and xc+30 >= xf) and (yc <= yf and yc+60 >= yf)) :
                canvas.move(fighterm2,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g4M -= 4
                vel4M -= 1

            if(choqueCarretera1m2()):
                return 0

            elif(canvas.coords(carrom2)[0]<canvas.coords(fighterm2)[0]):
                canvas.move(fighterm2,-4,10)             
            elif(canvas.coords(carrom2)[0]>canvas.coords(fighterm2)[0]):
                canvas.move(fighterm2,4,10)            
            else:
                canvas.move(fighterm2,0,15)           
        else:
            canvas.move(fighterm2,0,-900)
        canvas.after(100,movimientoFighterM2)

    # Fighter nivel 5 Player 2
    if(niveless.get() == 5)and(players.get()==2): 
        if(canvas.coords(fighterm2)[1]<700)and(i < 400):

            xf = canvas.coords(fighterm2)[0]
            yf = canvas.coords(fighterm2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xf and xc<=xf +30) and (yc>=yf and yc<=yf+60)) :
                canvas.move(fighterm2,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g5M -= 5
                vel5M -= 2
            if((xc <= xf and xc+30 >= xf) and (yc <= yf and yc+60 >= yf)) :
                canvas.move(fighterm2,0,300)
                print("K-BUM!"+"*Choque contra el Fighter*")
                g5M -= 4
                vel5M -= 2

            if(choqueCarretera1m2()):
                return 0

            elif(canvas.coords(carrom2)[0]<canvas.coords(fighterm2)[0]):
                canvas.move(fighterm2,-6,10)             
            elif(canvas.coords(carrom2)[0]>canvas.coords(fighterm2)[0]):
                canvas.move(fighterm2,6,10)            
            else:
                canvas.move(fighterm2,0,20)           
        else:
            canvas.move(fighterm2,0,-900)
        canvas.after(100,movimientoFighterM2)





#######################################################################################################################################################################





#FUNCION QUE MUEVE EL CARRO DEL PLAYER 1
def key2(event):
    """
    """
    global i,j,carrom,canvas

    tecla = repr(event.char)
    if(tecla == "'d'" or tecla == "'D'"):
        if(i < 95):
            canvas.delete(carrom)
            i = i + 15
            carrom = canvas.create_image(300+i,600+j,image=imagecarrom)

    if(tecla == "'a'"or tecla == "'A'"):
        if(i > -155):
            canvas.delete(carrom)
            i = i - 15
            carrom = canvas.create_image(300+i,600+j,image=imagecarrom)



    
p = 0
q = 0
#FUNCION QUE MUEVE EL CARRO DEL PLAYER 2
def keym2(event):
    """
    """
    global p,j,carrom2,canvas
    
    tecla = repr(event.char)
    if(tecla == "'ñ'" or tecla == "'Ñ'"):
        if(p < 170):
            canvas.delete(carrom2)
            p = p + 15
            carrom2 = canvas.create_image(1050+p,600+q,image=imagecarrom2)        
    if(tecla == "'k'"or tecla == "'K'"):
        if(p > -80):
            canvas.delete(carrom2)
            p = p - 15
            carrom2 = canvas.create_image(1050+p,600+q,image=imagecarrom2)




#######################################################################################################################################################################




###FUNCIONES DE LA GASOLINA EL CONTADOR DE GASOLINA Y LA VELOCIDAD DE TODOS LOS NIVELES###
g = 100
g2 = 100
g3 = 100
g4 = 100
g5 = 100

vel = 0
vel2 = 0
vel3 = 0
vel4 = 0
vel5 = 0
#Funciones de la gasolina y el contador de gasolina y de la velocidad para el player 1
def gasolina():
    global canvas,gasolinam,n1m,g,g2,g3,g4,g5,carrom,n2m,n3m,n4m,n5m
    #Nivel 1
    if(niveless.get() == 1)and(players.get()==2):
        if(canvas.coords(gasolinam)[1]<800):
            
            canvas.move(gasolinam,0,5)

            xg = canvas.coords(gasolinam)[0]
            yg = canvas.coords(gasolinam)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam,0,200)
                g = g+20
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam,0,200)
                g = g+20

            if(choqueCarretera1m()):
                g = 0
                return 0
            v.after(75,gasolina)
                    
            
        else:
            canvas.delete(gasolinam)
            gasolinam = canvas.create_image(random.randrange(140,400),random.randrange(-5000,-100),image=imagegasolinam)
            gasolina()

            
    #Nivel 2
    if(niveless.get() == 2)and(players.get()==2):
        if(canvas.coords(gasolinam)[1]<800):
            
            canvas.move(gasolinam,0,5)

            xg = canvas.coords(gasolinam)[0]
            yg = canvas.coords(gasolinam)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam,0,200)
                g2 = g2+15
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam,0,200)
                g2 = g2+15
                
            if(choqueCarretera1m()):
                g2 = 0
                return 0
            v.after(75,gasolina)
                    
            
        else:
            canvas.delete(gasolinam)
            gasolinam = canvas.create_image(random.randrange(140,400),random.randrange(-5000,-100),image=imagegasolinam)
            gasolina()

    #Nivel 3
    if(niveless.get() == 3)and(players.get()==2):
        if(canvas.coords(gasolinam)[1]< 800):
            
            canvas.move(gasolinam,0,5)

            xg = canvas.coords(gasolinam)[0]
            yg = canvas.coords(gasolinam)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam,0,200)
                g3 = g3+15
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam,0,200)
                g3 = g3+15
                
            if(choqueCarretera1m()):
                g3 = 0
                return 0 
            v.after(75,gasolina)
                    
            
        else:
            canvas.delete(gasolinam)
            gasolinam = canvas.create_image(random.randrange(140,400),random.randrange(-5000,-100),image=imagegasolinam)
            gasolina()

    #Nivel 4
    if(niveless.get() == 4)and(players.get()==2):
        if(canvas.coords(gasolinam)[1]<800):
            
            canvas.move(gasolinam,0,5)

            xg = canvas.coords(gasolinam)[0]
            yg = canvas.coords(gasolinam)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam,0,200)
                g4 = g4+10
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam,0,200)
                g4 = g4+10

            if(choqueCarretera1m()):
                g4 = 0
                return 0

            v.after(75,gasolina)
                    
            
        else:
            canvas.delete(gasolinam)
            gasolinam = canvas.create_image(random.randrange(140,400),random.randrange(-5000,-100),image=imagegasolinam)
            gasolina()

    #Nivel 5
    if(niveless.get() == 5)and(players.get()==2):
        if(canvas.coords(gasolinam)[1]<800):
            
            canvas.move(gasolinam,0,5)

            xg = canvas.coords(gasolinam)[0]
            yg = canvas.coords(gasolinam)[1]
            xc = canvas.coords(carrom)[0]
            yc = canvas.coords(carrom)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam,0,200)
                g5 = g5+10
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam,0,200)
                g5 = g5+10
            if(choqueCarretera1m()):
                g5 = 0
                return 0 
            v.after(75,gasolina)
                    
            
        else:
            canvas.delete(gasolinam)
            gasolinam = canvas.create_image(random.randrange(140,400),random.randrange(-5000,-100),image=imagegasolinam)
            gasolina()


def contgasm():
    global g,g2,g3,g4,g5,n1m,n2m,n3m,n4m,n5m
    #Nivel 1
    if(niveless.get() == 1)and(players.get()==2):
        gasm = tkinter.Label(n1m,text = "Fuel: "+str(g)).place(x=590,y=400)  
        if(g>0):
            g = g-1
            canvas.after(1800,contgasm)
        if(choqueCarretera1m()):
            g = 0
        
            
    #Nivel 2        
    if(niveless.get() == 2)and(players.get()==2):
        gasm = tkinter.Label(n2m,text = "Fuel: "+str(g2)).place(x=590,y=400)  
        if(g2>0):
            g2 = g2-1
            canvas.after(1600,contgasm)
        if(choqueCarretera1m()):
            g2 = 0
       

    #Nivel 3     
    if(niveless.get() == 3)and(players.get()==2):
        gasm = tkinter.Label(n3m,text = "Fuel: "+str(g3)).place(x=590,y=400)  
        if(g3>0):
            g3 = g3-1
            canvas.after(1400,contgasm)
        if(choqueCarretera1m()):
            g3 = 0
        

    #Nivel 4     
    if(niveless.get() == 4)and(players.get()==2):
        gasm = tkinter.Label(n4m,text = "Fuel: "+str(g4)).place(x=590,y=400)  
        if(g4>0):
            g4 = g4-1
            canvas.after(1200,contgasm)
        if(choqueCarretera1m()):
            g4 = 0
       

    #Nivel 5  
    if(niveless.get() == 5)and(players.get()==2):
        gasm = tkinter.Label(n5m,text = "Fuel: "+str(g5)).place(x=590,y=400)  
        if(g5>0):
            g5 = g5-1
            canvas.after(1000,contgasm)
        if(choqueCarretera1m()):
            g5 = 0
  



            


def velm():
    global vel,vel2,vel3,vel4,vel5,n1m,n2m,n3m,n4m,n5m
    #Nivel 1
    if(niveless.get() == 1)and(players.get()==2):
        velocidadm = tkinter.Label(n1m,text = "Speed: "+str(vel)).place(x=580,y=250)
        if(vel<240):
            vel = vel+1
            canvas.after(700,velm)
        if(choqueCarretera1m()):
            vel = 0

    #Nivel 2
    if(niveless.get() == 2)and(players.get()==2):
        velocidadm = tkinter.Label(n2m,text = "Speed: "+str(vel2)).place(x=580,y=250)
        if(vel2<240):
             vel2 = vel2+1
             canvas.after(680,velm)
        if(choqueCarretera1m()):
            vel2 = 0

    #Nivel 3
    if(niveless.get() == 3)and(players.get()==2):
        velocidadm = tkinter.Label(n3m,text = "Speed: "+str(vel3)).place(x=580,y=250)
        if(vel3<240):
             vel3 = vel3+1
             canvas.after(660,velm)
        if(choqueCarretera1m()):
            vel3 = 0

    #Nivel 4
    if(niveless.get() == 4)and(players.get()==2):
        velocidadm = tkinter.Label(n4m,text = "Speed: "+str(vel4)).place(x=580,y=250)
        if(vel4<240):
             vel4 = vel4+1
             canvas.after(640,velm)
        if(choqueCarretera1m()):
            vel4 = 0

    #Nivel 5
    if(niveless.get() == 5)and(players.get()==2):
        velocidadm = tkinter.Label(n5m,text = "Speed: "+str(vel5)).place(x=580,y=250)
        if(vel5<240):
             vel5 = vel5+1
             canvas.after(620,velm)
        if(choqueCarretera1m()):
            vel5 = 0






#Funciones de la gasolina, El contador de gasolina y  La velocidad para el player 2

gM = 100
g2M = 100
g3M = 100
g4M = 100
g5M = 100

velM = 1
vel2M = 1
vel3M = 1
vel4M = 1
vel5M = 1

def gasolina2():
    global canvas,gasolinam2,n1m,carrom2,n2m,n3m,n4m,n5m,gM,g2M,g3M,g4M,g5M
    #Nivel 1
    if(niveless.get() == 1)and(players.get()==2):
        if(canvas.coords(gasolinam2)[1]<900):
            
            canvas.move(gasolinam2,0,5)

            xg = canvas.coords(gasolinam2)[0]
            yg = canvas.coords(gasolinam2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc >= xg and xc <= xg+20) and (yc >= yg and yc <= yg+40)) :
                canvas.move(gasolinam2,0,200)
                gM = gM+20
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam2,0,200)
                gM = gM+20


            if(choqueCarretera1m2()):
                gM = 0
                return 0
            v.after(75,gasolina2)

        else:
            canvas.delete(gasolinam2)
            gasolinam2 = canvas.create_image(random.randrange(970,1230),random.randrange(-5000,-100),image=imagegasolinam2)
            gasolina2()
            

    #Nivel 2
    if(niveless.get() == 2)and(players.get()==2):
        if(canvas.coords(gasolinam2)[1]<900):
            
            canvas.move(gasolinam2,0,5)

            xg = canvas.coords(gasolinam2)[0]
            yg = canvas.coords(gasolinam2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam2,0,200)
                g2M = g2M+15
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam2,0,200)
                g2M = g2M+15

            if(choqueCarretera1m2()):
                g2M = 0
                return 0
            v.after(75,gasolina2)

        else:
            canvas.delete(gasolinam2)
            gasolinam2 = canvas.create_image(random.randrange(970,1230),random.randrange(-5000,-100),image=imagegasolinam2)
            gasolina2()

    #Nivel 3
    if(niveless.get() == 3)and(players.get()==2):
        if(canvas.coords(gasolinam2)[1]<900):
            
            canvas.move(gasolinam2,0,5)

            xg = canvas.coords(gasolinam2)[0]
            yg = canvas.coords(gasolinam2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam2,0,200)
                g3M = g3M+15
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam2,0,200)
                g3M = g3M+15
                
            if(choqueCarretera1m2()):
                g3M = 0
                return 0
            v.after(75,gasolina2)

        else:
            canvas.delete(gasolinam2)
            gasolinam2 = canvas.create_image(random.randrange(970,1230),random.randrange(-5000,-100),image=imagegasolinam2)
            gasolina2()


    #Nivel 4
    if(niveless.get() == 4)and(players.get()==2):
        if(canvas.coords(gasolinam2)[1]<900):
            
            canvas.move(gasolinam2,0,5)

            xg = canvas.coords(gasolinam2)[0]
            yg = canvas.coords(gasolinam2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam2,0,200)
                g4M = g4M+10
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam2,0,200)
                g4M = g4M+10
                
            if(choqueCarretera1m2()):
                g4M = 0
                return 0
            v.after(75,gasolina2)

        else:
            canvas.delete(gasolinam2)
            gasolinam2 = canvas.create_image(random.randrange(970,1230),random.randrange(-5000,-100),image=imagegasolinam2)
            gasolina2()



    #Nivel 5
    if(niveless.get() == 5)and(players.get()==2):
        if(canvas.coords(gasolinam2)[1]<900):
            
            canvas.move(gasolinam2,0,5)

            xg = canvas.coords(gasolinam2)[0]
            yg = canvas.coords(gasolinam2)[1]
            xc = canvas.coords(carrom2)[0]
            yc = canvas.coords(carrom2)[1]
            if((xc>=xg and xc<=xg +20) and (yc>=yg and yc<=yg+40)) :
                canvas.move(gasolinam2,0,200)
                g5M = g5M+10
            if((xc <= xg and xc+20 >= xg) and (yc <= yg and yc+40 >= yg)) :
                canvas.move(gasolinam2,0,200)
                g5M = g5M+10
                
            if(choqueCarretera1m2()):
                g5M = 0
                return 0
            v.after(75,gasolina2)

        else:
            canvas.delete(gasolinam2)
            gasolinam2 = canvas.create_image(random.randrange(970,1230),random.randrange(-5000,-100),image=imagegasolinam2)
            gasolina2()




def contgasm2():
    global gM,g2M,g3M,g4M,g5M,n1m,n2m,n3m,n4m,n5m
    #Nivel 1
    if(niveless.get() == 1)and(players.get()==2):
        gasm2 = tkinter.Label(n1m,text = "Fuel: "+str(gM)).place(x=710,y=400)
        if(gM>0):
            gM = gM-1
            canvas.after(1800,contgasm2)
        if(choqueCarretera1m2()):
            gM = 0

            
    #Nivel 2
    if(niveless.get() == 2)and(players.get()==2):
        gasm2 = tkinter.Label(n2m,text = "Fuel: "+str(g2M)).place(x=710,y=400)
        if(g2M>0):
            g2M = g2M-1
            canvas.after(1600,contgasm2)
        if(choqueCarretera1m2()):
            g2M = 0


    #Nivel 3
    if(niveless.get() == 3)and(players.get()==2):
        gasm2 = tkinter.Label(n3m,text = "Fuel: "+str(g3M)).place(x=710,y=400)
        if(g3M>0):
            g3M = g3M-1
            canvas.after(1400,contgasm2)
        if(choqueCarretera1m2()):
            g3M = 0
        

    #Nivel 4
    if(niveless.get() == 4)and(players.get()==2):
        gasm2 = tkinter.Label(n4m,text = "Fuel: "+str(g4M)).place(x=710,y=400)
        if(g4M>0):
            g4M = g4M-1
            canvas.after(1200,contgasm2)
        if(choqueCarretera1m2()):
            g4M = 0


    #Nivel 5
    if(niveless.get() == 5)and(players.get()==2):
        gasm2 = tkinter.Label(n5m,text = "Fuel: "+str(g5M)).place(x=710,y=400)
        if(g5M>0):
            g5M = g5M-1
            canvas.after(1000,contgasm2)
        if(choqueCarretera1m2()):
            g5M = 0




def velm2():
    global vel2M,vel3M,vel4M,vel5M,n1m,n2m,n3m,n4m,n5m,velM
    #Nivel 1
    if(niveless.get() == 1)and(players.get()==2):
        velocidadm2 = tkinter.Label(n1m,text = "Speed: "+str(velM)).place(x=710,y=250)
        if(velM<240):
            velM = velM+1
            canvas.after(700,velm2)
        if(choqueCarretera1m2()):
            velM = 0

    #Nivel 2
    if(niveless.get() == 2)and(players.get()==2):
        velocidadm2 = tkinter.Label(n2m,text = "Speed: "+str(vel2M)).place(x=710,y=250)
        if(vel2M<240):
            vel2M = vel2M+1
            canvas.after(680,velm2)
        if(choqueCarretera1m2()):
            vel2M = 0

    #Nivel 3
    if(niveless.get() == 3)and(players.get()==2):
        velocidadm2 = tkinter.Label(n3m,text = "Speed: "+str(vel3M)).place(x=710,y=250)
        if(vel3M<240):
            vel3M = vel3M+1
            canvas.after(660,velm2)
        if(choqueCarretera1m2()):
            vel3M = 0

    #Nivel 4
    if(niveless.get() == 4)and(players.get()==2):
        velocidadm2 = tkinter.Label(n4m,text = "Speed: "+str(vel4M)).place(x=710,y=250)
        if(vel4M<240):
            vel4M = vel4M+1
            canvas.after(640,velm2)
        if(choqueCarretera1m2()):
            vel4M = 0

    #Nivel 5
    if(niveless.get() == 5)and(players.get()==2):
        velocidadm2 = tkinter.Label(n5m,text = "Speed: "+str(vel5M)).place(x=710,y=250)
        if(vel5M<240):
            vel5M = vel5M+1
            canvas.after(620,velm2)
        if(choqueCarretera1m2()):
            vel5M = 0

#######################################################################################################################
def aceite():
    global canvas,n1m,carrom2,n2m,n3m,n4m,n5m,vel,vel2,vel3,vel4,vel5,velM,vel2M,vel3M,vel4M,vel5M,aceitem
    #Nivel 1
    if(canvas.coords(aceitem)[1]<800):
            
        canvas.move(aceitem,0,5)

        xa = canvas.coords(aceitem)[0]
        ya = canvas.coords(aceitem)[1]
        xc = canvas.coords(carrom)[0]
        yc = canvas.coords(carrom)[1]
        if((xc >= xa and xc <= xa+20) and (yc >= ya and yc <= ya+40)) :
            canvas.move(aceitem,0,200)
            vel = vel-5
            vel2 = vel2-5
            vel3 = vel3-5
            vel4 = vel4-5
            vel5 = vel5-5
        if((xc <= xa and xc+20 >= xa) and (yc <= ya and yc+40 >= ya)) :
            canvas.move(aceitem,0,200)
            vel = vel-5
            vel2 = vel2-5
            vel3 = vel3-5
            vel4 = vel4-5
            vel5 = vel5-5

        if(choqueCarretera1m()):
            return 0
        v.after(50,aceite)

    else:
        canvas.delete(aceitem)
        aceitem = canvas.create_image(random.randrange(140,400),random.randrange(-10000,-100),image=imageaceitem)
        aceite()
    
def aceite2():
    global canvas,n1m,carrom2,n2m,n3m,n4m,n5m,velM,vel2M,vel3M,vel4M,vel5M,aceitem2
    #Nivel 1
    if(canvas.coords(aceitem2)[1]<800):
            
        canvas.move(aceitem2,0,5)

        xa = canvas.coords(aceitem2)[0]
        ya = canvas.coords(aceitem2)[1]
        xc = canvas.coords(carrom2)[0]
        yc = canvas.coords(carrom2)[1]
        if((xc >= xa and xc <= xa+20) and (yc >= ya and yc <= ya+40)) :
            canvas.move(aceitem2,0,200)
            velM = velM-5
            vel2M = vel2M-5
            vel3M = vel3M-5
            vel4M = vel4M-5
            vel5M = vel5M-5
        if((xc <= xa and xc+20 >= xa) and (yc <= ya and yc+40 >= ya)) :
            canvas.move(aceitem2,0,200)
            velM = velM-5
            vel2M = vel2M-5
            vel3M = vel3M-5
            vel4M = vel4M-5
            vel5M = vel5M-5

        if(choqueCarretera1m2()):
            return 0
        v.after(50,aceite2)

    else:
        canvas.delete(aceitem2)
        aceitem2 = canvas.create_image(random.randrange(140,400),random.randrange(-10000,-100),image=imageaceitem2)
        aceite2()








#######################################################################################################################################################################


            

#############################################################################

#FUNCION DE COLISIONES CONTRA LOS BORDES
#Colision del player 1

def choqueCarretera1m():
    global carrom, canvas, imageexplosion2
    equis = canvas.coords(carrom)[0]
    ye = canvas.coords(carrom)[1]

    if(equis <= 145)or(equis >= 395):
        explosionM = canvas.create_image(equis,ye, image=imageexplosion2)
        return True


#Colision del player 2
def choqueCarretera1m2():
    global carrom2, canvas, imageexplosion2
    equis = canvas.coords(carrom2)[0]
    ye = canvas.coords(carrom2)[1]

    if(equis <= 960)or(equis >= 1220):        
        explosionM = canvas.create_image(equis,ye, image=imageexplosion2)
        return True
##############################################################################




#######################################################################################################################################################################

    


### FUNCIONES QUE MUEVEN EL MAPA DE TODOS LOS NIVELES ###

#Funcion que mueve la parte izquierda del NIVEL 1
fm1 = 0
def mov1m1():
    global canvas,fm1,fondon1m1,v,n1m
    if(canvas.coords(fondon1m1)[1] < 9800):
        
        if(fm1 < 4000):
            canvas.move(fondon1m1,0,10)
            fm1 = fm1 + 1
            if(choqueCarretera1m()):
                return 0
            
            canvas.after(60,mov1m1)
    else:
        return 0
        
    

#funcion que mueve la parte derecha del NIVEL 1
fm12 = 0
def mov1m2():
    global canvas,fm12,fondon1m2
    if(canvas.coords(fondon1m2)[1] < 9800):
        if(fm12 < 4000):
            canvas.move(fondon1m2,0,10)
            fm12 = fm12 + 1
            if(choqueCarretera1m2()):
                return 0
            canvas.after(60,mov1m2)
    
    else:
        return 0 




        
#Funcion que mueve la parte izquierda del NIVEL 2
fm2m = 0
def mov2m1():
    global canvas,fm2m,fondon2m1
    if(canvas.coords(fondon2m1)[1] < 12000):
        if(fm2m < 4000):
            canvas.move(fondon2m1,0,10)
            fm2m = fm2m + 1
            if(choqueCarretera1m()):
                return 0
            canvas.after(50,mov2m1)
    
    else:
        return 0
        
    

#funcion que mueve la parte derecha del NIVEL 2
fm12m = 0
def mov2m2():
    global canvas,fm12m,fondon2m2
    if(canvas.coords(fondon2m2)[1] < 12000):
        if(fm12m < 4000):
            canvas.move(fondon2m2,0,10)
            fm12m = fm12m + 1
            if(choqueCarretera1m2()):
                return 0
            canvas.after(50,mov2m2)
    
    else:
        return 0



#Funcion que mueve la parte izquierda del NIVEL 3
fm3m = 0
def mov3m1():
    global canvas,fm3m,fondon3m1
    if(canvas.coords(fondon3m1)[1] < 15000):
        if(fm3m < 4000):
            canvas.move(fondon3m1,0,10)
            fm3m = fm3m + 1
            if(choqueCarretera1m()):
                return 0
            canvas.after(40,mov3m1)
    
    else:
        return 0
        
    

#funcion que mueve la parte derecha del NIVEL 3
fm3m2 = 0
def mov3m2():
    global canvas,fm3m2,fondon3m2
    if(canvas.coords(fondon3m2)[1] < 15000):
        if(fm3m2 < 4000):
            canvas.move(fondon3m2,0,10)
            fm3m2= fm3m2 + 1
            if(choqueCarretera1m2()):
                return 0
            canvas.after(40,mov3m2)
    
    else:
        return 0



#Funcion que mueve la parte izquierda NIVEL 4
fm4m = 0
def mov4m1():
    global canvas,fm4m,fondon4m1
    if(canvas.coords(fondon4m1)[1] < 15000):
        if(fm4m < 4000):
            canvas.move(fondon4m1,0,10)
            fm4m = fm4m + 1
            if(choqueCarretera1m()):
                return 0
            canvas.after(30,mov4m1)
    
    else:
        return 0
        
    

#funcion que mueve la parte derecha del NIVEL 4
fm4m2 = 0
def mov4m2():
    global canvas,fm4m2,fondon4m2
    if(canvas.coords(fondon4m2)[1] < 15000):
        if(fm4m2 < 4000):
            canvas.move(fondon4m2,0,10)
            fm4m2= fm4m2 + 1
            if(choqueCarretera1m2()):
                return 0
            canvas.after(30,mov4m2)
    
    else:
        return 0





#Funcion que mueve la parte izquierda NIVEL 5
fm5m = 0
def mov5m1():
    global canvas,fm5m,fondon5m1,carrom
    if(canvas.coords(fondon5m1)[1] < 20000):
        if(fm5m < 4000):
            canvas.move(fondon5m1,0,10)
            fm5m = fm5m + 1
            if(choqueCarretera1m()):
                return 0
            canvas.after(20,mov5m1)
    
    else:
        return 0
    

#funcion que mueve la parte derecha del NIVEL 5
fm5m2 = 0
def mov5m2():
    global canvas,fm5m2,fondon5m2,carrom2
    if(canvas.coords(fondon5m2)[1] < 20000):
        if(fm5m2 < 4000):
            canvas.move(fondon5m2,0,10)
            fm5m2= fm5m2 + 1
            if(choqueCarretera1m2()):
                return 0
            canvas.after(20,mov5m2)
    
    else:
        return 0 


    

#######################################################################################################################################################################



### Funciones que ayudan a iniciar el juego con la letra "p" en los niveles del MULTIPLAYER ###

#Funcion del nivel 1M
def keypausam1(event):
    global  canvas,fondon1m1,fondon1m2
    tecla = repr(event.char)
    if(tecla == "'p'"):
        if(canvas.coords(fondon1m1)[1] < 9800)or(canvas.coords(fondon1m2)[1] < 9800):
            movimientoBanM1()
            movimientoBanM2()
            
            movimientoBanE()
            movimientoBanE2()
                
    ##        movimientoRunnerM1()
    ##        movimientoRunnerM2()

    ##        movimientoFighterM1()
    ##        movimientoFighterM2()
            gasolina()
            contgasm()
            gasolina2()
            contgasm2()
            velm()
            velm2()
            aceite()
            aceite2()
        
            canvas.bind("<KeyPress>", key2)
            canvas.bind("<KeyRelease>", keym2)
                
            mov1m1()
            mov1m2()
        else:
            return 0
        

        
        
#Funcion del nivel 2M
def keypausam2(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):

        movimientoBanM1()
        movimientoBanM2()
            
        movimientoRunnerM1()
        movimientoRunnerM2()

        gasolina()
        contgasm()
        gasolina2()
        contgasm2()
        velm()
        velm2()
        aceite()
        aceite2()

        canvas.bind("<KeyPress>", key2)
        canvas.bind("<KeyRelease>", keym2)

        mov2m1()
        mov2m2()



#Funcion del nivel 3M
def keypausam3(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):

        movimientoBanM1()
        movimientoBanM2()

        movimientoBanE()
        movimientoBanE2()
            
        movimientoRunnerM1()
        movimientoRunnerM2()

        movimientoFighterM1()
        movimientoFighterM2()

        gasolina()
        contgasm()
        gasolina2()
        contgasm2()
        velm()
        velm2()
        aceite()
        aceite2()

        canvas.bind("<KeyPress>", key2)
        canvas.bind("<KeyRelease>", keym2)

        mov3m1()
        mov3m2()




#Funcion del nivel 4M
def keypausam4(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):

        movimientoBanM1()
        movimientoBanM2()

        movimientoBanE()
        movimientoBanE2()
            
        movimientoRunnerM1()
        movimientoRunnerM2()

        movimientoFighterM1()
        movimientoFighterM2()

        gasolina()
        contgasm()
        gasolina2()
        contgasm2()
        velm()
        velm2()
        aceite()
        aceite2()

        canvas.bind("<KeyPress>", key2)
        canvas.bind("<KeyRelease>", keym2)

        mov4m1()
        mov4m2()



#Funcion del nivel 4M
def keypausam5(event):
    global  canvas
    tecla = repr(event.char)
    if(tecla == "'p'"):

        movimientoBanM1()
        movimientoBanM2()

        movimientoBanE()
        movimientoBanE2()
            
        movimientoRunnerM1()
        movimientoRunnerM2()

        movimientoFighterM1()
        movimientoFighterM2()

        gasolina()
        contgasm()
        gasolina2()
        contgasm2()
        velm()
        velm2()
        aceite()
        aceite2()

        canvas.bind("<KeyPress>", key2)
        canvas.bind("<KeyRelease>", keym2)

        mov5m1()
        mov5m2()
        





 
#####                                                                  #####
#######################################################################################################################################################################





    
#Imagenes niveles single player
imagen2 = tkinter.PhotoImage(file="carro.png")
imagen3 = tkinter.PhotoImage(file="ban.png")
imagen4 = tkinter.PhotoImage(file="runner.png")
imagen5 = tkinter.PhotoImage(file="fighter.png")
fondop = tkinter.PhotoImage(file="fondo1prueba.png")
esplosion = tkinter.PhotoImage(file="explosion.png")



###Imagenes de los niveles multiplayer###

#Imagenes de los carros y explosiones
imagecarrom = tkinter.PhotoImage(file="carroM.png")
imagecarrom2 = tkinter.PhotoImage(file="Carrom2.png")
imagebanm = tkinter.PhotoImage(file="banM.png")
imagebanm2 = tkinter.PhotoImage(file="banM2.png")

#Bans Extra
imagebanE = tkinter.PhotoImage(file="banE.png")
imagebanE2 = tkinter.PhotoImage(file="banE2.png")
#Carro estrellado
imagecarromE = tkinter.PhotoImage(file="carroE.png")
imagecarromE2 = tkinter.PhotoImage(file="carroE2.png")

imagerunnerm = tkinter.PhotoImage(file="runnerM.png")
imagerunnerm2 = tkinter.PhotoImage(file="runnerM2.png")
imagefighterm = tkinter.PhotoImage(file="fighterM.png")
imagefighterm2 = tkinter.PhotoImage(file="fighterM2.png")
imageexplosion2 = tkinter.PhotoImage(file="explosionM.png")
#Imagenes aceite y gasolina
imageaceitem = tkinter.PhotoImage(file="aceiteM.png")
imageaceitem2 = tkinter.PhotoImage(file="aceiteM2.png")
imagegasolinam = tkinter.PhotoImage(file="gasolinaM.png")
imagegasolinam2 = tkinter.PhotoImage(file="gasolinaM2.png")
#Imagenes del fondo 
fondo1m1 = tkinter.PhotoImage(file="fondo1m1.png")
fondo1m2 = tkinter.PhotoImage(file="fondo1m2.png")
fondo2m1 = tkinter.PhotoImage(file="fondo2m1.png")
fondo2m2 = tkinter.PhotoImage(file="fondo2m2.png")
fondo3m1 = tkinter.PhotoImage(file="fondo3m1.png")
fondo3m2 = tkinter.PhotoImage(file="fondo3m2.png")
fondo4m1 = tkinter.PhotoImage(file="fondo4m1.png")
fondo4m2 = tkinter.PhotoImage(file="fondo4m2.png")
fondo5m1 = tkinter.PhotoImage(file="fondo5m1.png")
fondo5m2 = tkinter.PhotoImage(file="fondo5m2.png")






#Funcion para el boton back (volver al menu)
def volverMenu():
    global v,n1,n2,n3,n4,n5,n1m,n2m,n3m,n4m,n5m
    if(niveless.get() == 1)and(players.get()==1):
        n1.destroy()
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
    global imagen1,fondonv3,imagen2,imagen3,imagen4,presiono,x,i,j,b,canvas,ban,runner,carro,banm,carrom,runnerm,fighterm,n1,n2,n3,n4,n5,fighter,n1m,n2m,n3m,n4m,n5m
    global fondon1,pruebaf,fondon1m1,fondon1m2,fondon2m1,fondon2m2,carrom2,banm2,runnerm2,fighterm2,gasolinam,gasolinam2,aceitem,aceitem2,banE,banE2
    global fondon3m2,fondon3m1,fondon4m2,fondon4m1,fondon5m2,fondon5m1,carromE,carromE2

##  #Abriendo Niveles single player
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

        #nombres de jugador
        p1 = tkinter.Label(n1,text="Player1:" + "\n" +nombre1.get()).place(x=1230,y=200)
        
        #cargando imagenes de fondo   

        pruebaf = canvas.create_image(675,-5000,image=fondop)

        carro = canvas.create_image(600,600,image=imagen2)    
        ban = canvas.create_image(random.randrange(450,800),-100,image=imagen3)
        runner = canvas.create_image(random.randrange(450,800),-100,image=imagen4)
        fighter = canvas.create_image(random.randrange(450,800),-100,image=imagen5)

        canvas.bind("<Key>", keypausa)

        
        n1.mainloop()




    if(niveless.get() == 2)and(players.get()==1):
        messagebox.showinfo("Mensaje",message="Lo sentimos pero el juego aun esta en una Pre-Alpha, no hay ningun nivel para el single player, sin embargo puedes echarle un ojo al nivel 1.")
    if(niveless.get() == 3)and(players.get()==1):
        messagebox.showinfo("Mensaje",message="Lo sentimos pero el juego aun esta en una Pre-Alpha, no hay ningun nivel para el single player, sin embargo puedes echarle un ojo al nivel 1.")
    if(niveless.get() == 4)and(players.get()==1):
        messagebox.showinfo("Mensaje",message="Lo sentimos pero el juego aun esta en una Pre-Alpha, no hay ningun nivel para el single player, sin embargo puedes echarle un ojo al nivel 1.")
    if(niveless.get() == 5)and(players.get()==1):
        messagebox.showinfo("Mensaje",message="Lo sentimos pero el juego aun esta en una Pre-Alpha, no hay ningun nivel para el single player, sin embargo puedes echarle un ojo al nivel 1.")





    ### ABRIENDO LOS NIVELES MULTIPLAYER ###

        
    # ABRIENDO NIVEL 1
    if(niveless.get() == 1)and(players.get()==2):

        

        n1m=tkinter.Toplevel()
        v.iconify()
        n1m.title("Nivel 2 Multiplayer - Road Fighter")
        canvas = tkinter.Canvas(n1m,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n1m,text="Back",fg="black",command = volverMenu).place(x=678,y=550)
        save = tkinter.Button(n1m,text="Save",fg="black").place(x=640,y=550)##falta la funcion para el command

        p1 = tkinter.Label(n1m,text="Player1:" + "\n" + "\n" +nombre1.get()).place(x=580,y=100)
        p2 = tkinter.Label(n1m,text="Player2:" + "\n" + "\n" +nombre2.get()).place(x=710,y=100)
        

        #fondos separados
        fondon1m1 = canvas.create_image(339,-8000,image=fondo1m1)
        fondon1m2 = canvas.create_image(1013,-8000,image=fondo1m2)

        #Carros, gasolina y aceite
        carrom = canvas.create_image(300,600,image=imagecarrom)
        carrom2 = canvas.create_image(1050,600,image=imagecarrom2)
        #Carro estrellado
##        carromE = canvas.create_image(300,600,image=imagecarromE)
##        carromE2 = canvas.create_image(1050,600,image=imagecarromE2)
        
        banm = canvas.create_image(random.randrange(140,400),-70,image=imagebanm)
        banm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanm2)
        #Ban Extra
        banE = canvas.create_image(random.randrange(140,400),-70,image=imagebanE)
        banE2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanE2)
        
        runnerm = canvas.create_image(random.randrange(140,400),-70,image=imagerunnerm)
        runnerm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagerunnerm2)

        fighterm = canvas.create_image(random.randrange(140,400),-70,image=imagefighterm)
        fighterm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagefighterm2)
        
        gasolinam = canvas.create_image(random.randrange(140,400),-200,image=imagegasolinam)
        gasolinam2 = canvas.create_image(random.randrange(970,1230),-200,image=imagegasolinam2)



###
        aceitem = canvas.create_image(random.randrange(140,400),-200,image=imageaceitem)
        aceitem2 = canvas.create_image(random.randrange(970,1230),-200,image=imageaceitem2)


        canvas.bind("<Key>", keypausam1)
        


         

        
        n1m.mainloop()




################################################################################################################






     #  ABRIENDO NIVEL 2
    if(niveless.get() == 2)and(players.get()==2):

        

              
        n2m=tkinter.Toplevel()
        v.iconify()
        n2m.title("Nivel 2 Multiplayer - Road Fighter")
        canvas = tkinter.Canvas(n2m,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n2m,text="Back",fg="black",command = volverMenu).place(x=678,y=550)
        save = tkinter.Button(n2m,text="Save",fg="black").place(x=640,y=550)##falta la funcion para el command

        p1 = tkinter.Label(n2m,text="Player1:" + "\n" + "\n" +nombre1.get()).place(x=580,y=100)
        p2 = tkinter.Label(n2m,text="Player2:" + "\n" + "\n" +nombre2.get()).place(x=710,y=100)
        

        #fondos separados
        fondon2m1 = canvas.create_image(339,-8000,image=fondo2m1)
        fondon2m2 = canvas.create_image(1013,-8000,image=fondo2m2)

        #Carros, gasolina y aceite
        carrom = canvas.create_image(300,600,image=imagecarrom)
        carrom2 = canvas.create_image(1050,600,image=imagecarrom2)
        
        banm = canvas.create_image(random.randrange(140,400),-70,image=imagebanm)
        banm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanm2)
        #Ban Extra
        banE = canvas.create_image(random.randrange(140,400),-70,image=imagebanE)
        banE2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanE2)
        
        runnerm = canvas.create_image(random.randrange(140,400),-70,image=imagerunnerm)
        runnerm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagerunnerm2)

        fighterm = canvas.create_image(random.randrange(140,400),-70,image=imagefighterm)
        fighterm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagefighterm2)
        
        gasolinam = canvas.create_image(random.randrange(140,400),-200,image=imagegasolinam)
        gasolinam2 = canvas.create_image(random.randrange(970,1230),-200,image=imagegasolinam2)

        aceitem = canvas.create_image(random.randrange(140,400),-200,image=imageaceitem)
        aceitem2 = canvas.create_image(random.randrange(970,1230),-200,image=imageaceitem2)



        canvas.bind("<Key>", keypausam2)
        
        
        n2m.mainloop()





################################################################################################################





    #  ABRIENDO NIVEL 3
    if(niveless.get() == 3)and(players.get()==2):

        

              
        n3m=tkinter.Toplevel()
        v.iconify()
        n3m.title("Nivel 3 Multiplayer - Road Fighter")
        canvas = tkinter.Canvas(n3m,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n3m,text="Back",fg="black",command = volverMenu).place(x=678,y=550)
        save = tkinter.Button(n3m,text="Save",fg="black").place(x=640,y=550)##falta la funcion para el command

        p1 = tkinter.Label(n3m,text="Player1:" + "\n" + "\n" +nombre1.get()).place(x=580,y=100)
        p2 = tkinter.Label(n3m,text="Player2:" + "\n" + "\n" +nombre2.get()).place(x=710,y=100)
        

        #fondos separados
        fondon3m1 = canvas.create_image(339,-8000,image=fondo3m1)
        fondon3m2 = canvas.create_image(1013,-8000,image=fondo3m2)

        #Carros, gasolina y aceite
        carrom = canvas.create_image(300,600,image=imagecarrom)
        carrom2 = canvas.create_image(1050,600,image=imagecarrom2)
        
        banm = canvas.create_image(random.randrange(140,400),-70,image=imagebanm)
        banm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanm2)
        #Ban Extra
        banE = canvas.create_image(random.randrange(140,400),-70,image=imagebanE)
        banE2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanE2)
        
        runnerm = canvas.create_image(random.randrange(140,400),-70,image=imagerunnerm)
        runnerm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagerunnerm2)

        fighterm = canvas.create_image(random.randrange(140,400),-70,image=imagefighterm)
        fighterm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagefighterm2)
        
        gasolinam = canvas.create_image(random.randrange(140,400),-200,image=imagegasolinam)
        gasolinam2 = canvas.create_image(random.randrange(970,1230),-200,image=imagegasolinam2)

        aceitem = canvas.create_image(random.randrange(140,400),-200,image=imageaceitem)
        aceitem2 = canvas.create_image(random.randrange(970,1230),-200,image=imageaceitem2)



        canvas.bind("<Key>", keypausam3)
        


         

        
        n3m.mainloop()



################################################################################################################




    #  ABRINDO NIVEL 4 
    if(niveless.get() == 4)and(players.get()==2):

        

              
        n4m=tkinter.Toplevel()
        v.iconify()
        n4m.title("Nivel 4 Multiplayer - Road Fighter")
        canvas = tkinter.Canvas(n4m,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n4m,text="Back",fg="black",command = volverMenu).place(x=678,y=550)
        save = tkinter.Button(n4m,text="Save",fg="black").place(x=640,y=550)##falta la funcion para el command

        p1 = tkinter.Label(n4m,text="Player1:" + "\n" + "\n" +nombre1.get()).place(x=580,y=100)
        p2 = tkinter.Label(n4m,text="Player2:" + "\n" + "\n" +nombre2.get()).place(x=710,y=100)
        

        #fondos separados
        fondon4m1 = canvas.create_image(339,-8000,image=fondo4m1)
        fondon4m2 = canvas.create_image(1013,-8000,image=fondo4m2)

        #Carros, gasolina y aceite
        carrom = canvas.create_image(300,600,image=imagecarrom)
        carrom2 = canvas.create_image(1050,600,image=imagecarrom2)
        
        banm = canvas.create_image(random.randrange(140,400),-70,image=imagebanm)
        banm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagebanm2)
        #Ban Extra
        banE = canvas.create_image(random.randrange(140,400),-150,image=imagebanE)
        banE2 = canvas.create_image(random.randrange(970,1230),-150,image=imagebanE2)
        
        runnerm = canvas.create_image(random.randrange(140,400),-70,image=imagerunnerm)
        runnerm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagerunnerm2)

        fighterm = canvas.create_image(random.randrange(140,400),-70,image=imagefighterm)
        fighterm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagefighterm2)
        
        gasolinam = canvas.create_image(random.randrange(140,400),-200,image=imagegasolinam)
        gasolinam2 = canvas.create_image(random.randrange(970,1230),-200,image=imagegasolinam2)

        aceitem = canvas.create_image(random.randrange(140,400),-200,image=imageaceitem)
        aceitem2 = canvas.create_image(random.randrange(970,1230),-200,image=imageaceitem2)



        canvas.bind("<Key>", keypausam4)
        


         

        
        n4m.mainloop()




################################################################################################################




    #  ABRIENDO NIVEL 5
    if(niveless.get() == 5)and(players.get()==2):

        

              
        n5m=tkinter.Toplevel()
        v.iconify()
        n5m.title("Nivel 5 Multiplayer - Road Fighter")
        canvas = tkinter.Canvas(n5m,width=1350,height=730)
        canvas.pack()
        canvas.focus_set()
        
        back = tkinter.Button(n5m,text="Back",fg="black",command = volverMenu).place(x=678,y=550)
        save = tkinter.Button(n5m,text="Save",fg="black").place(x=640,y=550)##falta la funcion para el command

        p1 = tkinter.Label(n5m,text="Player1:" + "\n" + "\n" +nombre1.get()).place(x=580,y=100)
        p2 = tkinter.Label(n5m,text="Player2:" + "\n" + "\n" +nombre2.get()).place(x=710,y=100)
        

        #fondos separados
        fondon5m1 = canvas.create_image(339,-8000,image=fondo5m1)
        fondon5m2 = canvas.create_image(1013,-8000,image=fondo5m2)

        #Carros, gasolina y aceite
        carrom = canvas.create_image(300,600,image=imagecarrom)
        carrom2 = canvas.create_image(1050,600,image=imagecarrom2)
        
        banm = canvas.create_image(random.randrange(140,400),-50,image=imagebanm)
        banm2 = canvas.create_image(random.randrange(970,1230),-50,image=imagebanm2)
        #Ban Extra
        banE = canvas.create_image(random.randrange(140,400),-50,image=imagebanE)
        banE2 = canvas.create_image(random.randrange(970,1230),-50,image=imagebanE2)
        
        runnerm = canvas.create_image(random.randrange(140,400),-70,image=imagerunnerm)
        runnerm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagerunnerm2)

        fighterm = canvas.create_image(random.randrange(140,400),-70,image=imagefighterm)
        fighterm2 = canvas.create_image(random.randrange(970,1230),-70,image=imagefighterm2)
        
        gasolinam = canvas.create_image(random.randrange(140,400),-200,image=imagegasolinam)
        gasolinam2 = canvas.create_image(random.randrange(970,1230),-200,image=imagegasolinam2)

        aceitem = canvas.create_image(random.randrange(140,400),-200,image=imageaceitem)
        aceitem2 = canvas.create_image(random.randrange(970,1230),-200,image=imageaceitem2)



        canvas.bind("<Key>", keypausam5)
        


         

        
        n5m.mainloop()



        






#######################################################################################################################################################################









############################ TODO LO DEL MENÚ #############################




#poniendo todas las varras donde se van a guardar los nombres y los values de los radio buttons
niveless = tkinter.IntVar()
players = tkinter.IntVar()
nombre1 = tkinter.StringVar()
nombre2 = tkinter.StringVar()



#definiendo funciones para los botones del menú

def onePlayer():
    p = tkinter.Label(v,text="Player:",bg="brown").place(x=725,y=360)
    player = tkinter.Entry(v,textvariable=nombre1 ).place(x=775,y=360)

def twoPlayers():
    p1 = tkinter.Label(v,text="Player1:\n",bg="brown").place(x=750,y=405)
    player1 = tkinter.Entry(v,textvariable = nombre1).place(x=800,y=405)
    p2 = tkinter.Label(v,text="Player2:",bg="brown").place(x=750,y=435)
    player2 = tkinter.Entry(v,textvariable = nombre2).place(x=800,y=435)

  
def select():
    global radioboton1, radioboton2
    radioboton1 = tkinter.Radiobutton(v,image=op,value=1,variable=players,command=onePlayer).place(x=590,y=355)
    radioboton2 = tkinter.Radiobutton(v,image=tp,value=2,variable=players,command=twoPlayers).place(x=590,y=413)


def Exit():
    exit()
        


#Creando los radio buttons
def radioButtons():
    rb1 = tkinter.Radiobutton(v,text="Lvl 1",value=1,variable = niveless).place(x=600,y=530)
    rb2 = tkinter.Radiobutton(v,text="Lvl 2",value=2,variable = niveless).place(x=660,y=530)
    rb3 = tkinter.Radiobutton(v,text="Lvl 3",value=3,variable = niveless).place(x=720,y=530)
    rb4 = tkinter.Radiobutton(v,text="Lvl 4",value=4,variable = niveless).place(x=600,y=560)
    rb5 = tkinter.Radiobutton(v,text="Lvl 5",value=5,variable = niveless).place(x=660,y=560)



#Cargando Imagenes de botones
selectp = tkinter.PhotoImage(file="players.png")
selectl = tkinter.PhotoImage(file="levels.png")
bexit = tkinter.PhotoImage(file="exit.png")
bplay = tkinter.PhotoImage(file="play.png")
tp = tkinter.PhotoImage(file="tp.png")
op = tkinter.PhotoImage(file="op.png")

#poniendo botones y cajas de texto
selectPlayer = tkinter.Button(v,image=selectp,command=select).place(x=590, y=288)
bExit = tkinter.Button(v,image=bexit,command = Exit).place(x=610,y=610)
bPlay = tkinter.Button(v,image=bplay,command = niveles).place(x=690,y=610)
selectLvl = tkinter.Button(v,image=selectl,command=radioButtons).place(x=590,y=480)



    
#Funcion que abre una ventana con las instrucciones
def instrucciones():
    vi = tkinter.Toplevel()    
    vi.geometry("1000x500")
    vi.title("Instructions")
    vi.config(bg="Brown")
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
                                                                                                                                                              
