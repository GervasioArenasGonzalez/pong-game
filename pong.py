import turtle
import winsound

#creo la pantalla
pantalla=turtle.Screen()
pantalla.title('Pong en python')
pantalla.bgcolor('green')
pantalla.setup(width=800, height=600)
pantalla.tracer(0)

#creo las paletas
paleta_izquierda=turtle.Turtle()
paleta_derecha=turtle.Turtle()
paleta_izquierda.shape('square')
paleta_izquierda.shapesize(5,1)
paleta_izquierda.color('white')
paleta_izquierda.penup()
paleta_izquierda.goto(-370,0)

paleta_derecha.shape('square')
paleta_derecha.shapesize(5,1)
paleta_derecha.color('white')
paleta_derecha.penup()
paleta_derecha.goto(370,0)

#creo la pelota
pelota=turtle.Turtle()
pelota.speed(0)
pelota.shape('circle')
pelota.color('white')
pelota.penup()
pelota.goto(0,0)

#velocidad de la pelota
pelota.dx=0.2
pelota.dy=0.2

#movimiento de las paletas
pantalla.listen()

def paleta_izq_arriba():
    y = paleta_izquierda.ycor()
    if y <250:
        paleta_izquierda.sety(y+20)

def paleta_izq_abajo():
    y = paleta_izquierda.ycor()
    if y >-250:
        paleta_izquierda.sety(y-20)

def paleta_der_arriba():
    y = paleta_derecha.ycor()
    if y <250:
        paleta_derecha.sety(y+20)

def paleta_der_abajo():
    y = paleta_derecha.ycor()
    if y >-250:
        paleta_derecha.sety(y-20)

pantalla.onkeypress(paleta_izq_arriba,'w')
pantalla.onkeypress(paleta_izq_abajo,'s')
pantalla.onkeypress(paleta_der_arriba,'Up')
pantalla.onkeypress(paleta_der_abajo,'Down')

puntos_izquierda=0
puntos_derecha=0

#lapiz izquierdo
lapiz_i=turtle.Turtle()
lapiz_i.hideturtle()

#lapiz derecho
lapiz_d=turtle.Turtle()
lapiz_d.hideturtle()


#Bucle principal solo para mover la pelota
while True:
    pantalla.update()
    

    #mover pelota
    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)

    #Rebote en bordes superior e inferior

    if pelota.ycor()>290:
        pelota.sety(290)
        pelota.dy*=-1
        winsound.Beep(500,50)
    
    if pelota.ycor()<-290:
        pelota.sety(-290)
        pelota.dy*=-1
        winsound.Beep(500,50)

    
    #Reiniciar la pelota si pasa por los bordes izquierdo o derecho

    if pelota.xcor()>390:
        pelota.goto(0,0)
        pelota.dx*=-1
        puntos_izquierda+=1
        lapiz_i.reset()
        lapiz_i.hideturtle()
        lapiz_i.penup()
        lapiz_i.goto(260,260)
        lapiz_i.write(str(puntos_izquierda),font=('Arial',24,'bold'))
        winsound.PlaySound('arcade_blip.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    
    if pelota.xcor()<-390:
        pelota.goto(0,0)
        pelota.dx*=-1
        puntos_derecha+=1
        turtle.reset()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-260,260)
        turtle.write(str(puntos_derecha), font=('Arial',24,'bold'))
        winsound.PlaySound('arcade_blip.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)

    
    #colision con paleta derecha
    if (340<pelota.xcor()<350)and(paleta_derecha.ycor()-50<pelota.ycor()<paleta_derecha.ycor()+50):
        pelota.setx(340)#evita que se clave dentro de la paleta
        pelota.dx*=-1#rebote
        winsound.Beep(1000,50)

    #colision con paleta izquierda
    if (-350<pelota.xcor()<-340)and(paleta_izquierda.ycor()-50<pelota.ycor()<paleta_izquierda.ycor()+50):
        pelota.setx(-340)#evita que se clave dentro de la paleta
        pelota.dx*=-1#rebote
        winsound.Beep(1000,50)
