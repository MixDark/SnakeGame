import turtle
import time
import random

class SnakeGame:
    
    def __init__(self, width=800, height=600, color="black"):
        #Inicializa los componentes del juego
        self._ancho = width
        self._alto = height
        # Inicializa el lienzo de la pantalla
        self.screen = turtle.Screen()
        self.screen.title("Juego de la culebrita")
        self.screen.bgcolor(color)
        self.screen.setup(width=width, height=height)
        self.screen.screensize(width, height)
        self.screen._root.resizable(False, False)
        self.screen.tracer(0)

        # Inicializa la serpiente
        self.snake = turtle.Turtle()
        self.snake.speed(0)
        self.snake.shape("circle")
        self.snake.color("green")
        self.snake.penup()
        self.snake.goto(0,0)
        # Inicializa el texto que se muestra en la pantalla
        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.shape("circle")
        self.texto.color("white")
        self.texto.penup()
        self.texto.hideturtle()
        self.texto.goto(0, (height / 2) - 40)
        # Inicialización de la comida de la serpiente
        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape('circle')
        self.comida.color("red")
        self.comida.penup()
        self.comida.goto(0, 100)
        # Atributos de la clase
        self._direccion = None
        self._delay = 0.1
        self._score = 0
        self._high_score = 0
        self.snake_cuerpo = []
        # Asociacion de los movimiento y las teclas
        self.screen.listen()
        self.screen.onkeypress(self.arriba, "Up")
        self.screen.onkeypress(self.abajo, "Down")
        self.screen.onkeypress(self.izquierda, "Left")
        self.screen.onkeypress(self.derecha, "Right")
        # Agregar reinicio con la tecla "r"
        self.screen.onkeypress(self.reiniciar, "r")  
        
        # Sacamos el texto por pantalla
        self._imprimir_puntaje()
        
    def arriba(self):
        if self._direccion != "abajo":
            self._direccion = "arriba"
            
    def abajo(self):
        if self._direccion != "arriba":
            self._direccion = "abajo"
            
    def izquierda(self):
        if self._direccion != "derecha":
            self._direccion = "izquierda"
            
    def derecha(self):
        if self._direccion != "izquierda":
            self._direccion = "derecha"

    def reiniciar(self):
        self._reset()
            
    def mover(self):
        
        # Obtener las coordenadas de la cabeza de la serpiente
        hx, hy = self.snake.xcor(), self.snake.ycor()
        
        # Movemos el cuerpo de la serpiente
        for i in range(len(self.snake_cuerpo)-1, 0, -1):
            x = self.snake_cuerpo[i-1].xcor()
            y = self.snake_cuerpo[i-1].ycor()
            self.snake_cuerpo[i].goto(x, y)
            
        # Mover el segmento mas cercano a la cabeza
        if len(self.snake_cuerpo) > 0:
            self.snake_cuerpo[0].goto(hx, hy)
            
        if self._direccion == "arriba":
            self.snake.sety(hy + 20)
        elif self._direccion == "abajo":
            self.snake.sety(hy - 20)
        elif self._direccion == "izquierda":
            self.snake.setx(hx - 20)
        elif self._direccion == "derecha":
            self.snake.setx(hx + 20)
            
    def jugar(self):
        while True:
            self.screen.update()
            self.colision_borde()
            self.colision_comida()
            self.colision_cuerpo()
            time.sleep(self._delay)
            self.mover()
        self.screen.mainloop()
        
    def colision_borde(self):
        bxcor = (self._ancho // 2) - 10
        bycor = (self._alto // 2) - 10
        
        if self.snake.xcor() > bxcor or self.snake.xcor() < -bxcor or self.snake.ycor() > bycor or self.snake.ycor() < -bycor:
            self._reset()
            self.texto.clear()
            self.texto.write("Presiona R para jugar de nuevo", align="center", font=("Courier", 24, "normal"))
            
            
    def colision_cuerpo(self):
        for s in self.snake_cuerpo:
            if s.distance(self.snake) < 20:
                self._reset()
                self.texto.clear()
                self.texto.write("Presiona R para jugar de nuevo", align="center", font=("Courier", 24, "normal"))

            
    def colision_comida(self):
        if self.snake.distance(self.comida) < 20:
            # Mover la comida a un lugar aleatorio
            bxcor = (self._ancho // 2) - 10
            bycor = (self._alto // 2) - 10
            x = random.randint(-bxcor, bxcor)
            y = random.randint(-bycor, bycor)
            self.comida.goto(x, y)
            # Incrementar el cuerpo de la serpiente
            self.incrementar_cuerpo()
            # Reducir el dalay
            self._delay -= 0.001
            # Aumentar el score
            self._score += 10
            self.texto.write
            self._imprimir_puntaje()
            
    def incrementar_cuerpo(self):
        segmento = turtle.Turtle()
        segmento.speed(0)
        segmento.shape('circle')
        segmento.color('MediumSeaGreen')
        segmento.penup()
        self.snake_cuerpo.append(segmento)
            
    def _imprimir_puntaje(self):
        self.texto.clear()
        self.texto.write(f"Puntos: {self._score} Record: {self._high_score}", align="center", font=("Courier", 24, "normal"))
        
    def _reset(self):
        time.sleep(1)
        self.snake.goto(0, 0)
        self._direccion = None
        # Reiniciamos el cuerpo de la serpiente
        for s in self.snake_cuerpo:
            s.ht() # Oculta el segmento
        # Limpiar la lista de segmentos
        self.snake_cuerpo.clear()
        # Reiniciar el delay
        
        self._delay = 0.1
        # Reiniciar el puntaje
        if self._score > self._high_score:
            self._high_score = self._score
        self._score = 0
        self._imprimir_puntaje()


snake_game = SnakeGame()
snake_game.jugar()