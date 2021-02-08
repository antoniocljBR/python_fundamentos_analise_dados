# Game Ping-Pong

# Comando import para importar os módulos 
from tkinter import *
import random
import time

# Criação da variável level que recebe uma string que é convertida
# para o tipo inteiro

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# Variável que armazena o tamanho da barra de acordo a dificuldade selecionada
length = 500/level

# Instanciando a janela 
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Instanciando o objeto canvas com tamanhos definidos
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
count = 0
lost = False

# Criando a classe Bola
class Bola:
    def __init__(self, canvas, Barra, color):
        # Criando as variáveis para serem utilizadas dentro da classe definida
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)
        
        # Criando uma lista dados inteiros
        starts_x = [-3, -2, -1, 1, 2, 3]
        
        # Rotacionando os valores da lista
        random.shuffle(starts_x)

        # Inicializando os valores das variáveis x e y
        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Criando método para desenhar a bola
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        # Variável com a posição da bola
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        # Variável para armazenamento da posição da barra criada
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Checa a posição da bola com a posição da barra, realizando 
        # incremento na pontuação caso estejam encostados
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()

        if pos[3] <= self.canvas_height:
            # Aguarda 10 ms para fazer um efeito de movimentação da bola
            self.canvas.after(10, self.draw)
        else:
            # Informativo ao usuário que ele perdeu o jogo
            game_over()
            global lost
            lost = True

class Barra:
    def __init__(self, canvas, color):
        # Criando as variáveis para serem utilizadas dentro da classe definida
        self.canvas = canvas
        
        # Cria o objeto retângulo
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        
        # Move o objeto retângulo para posiçõ inicial
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        # Verifica qual tecla foi pressionada e define uma ação desejada
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        # Movendo o objeto retângulo na tela
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        # Variável global para indicar o fim do jogo
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

def start_game(event):
    # Cria variáveis globais 
    global lost, count
    lost = False
    count = 0
    
    # Chama função para atualizar o placar 
    score()
    canvas.itemconfig(game, text=" ")

    # Aguarda um tempo inicial
    time.sleep(1)
    
    # Desenha a barra e a bola na tela
    Barra.draw()
    Bola.draw()

def score():
    # Atualiza a pontuação do jogador
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    # Informa ao jogador o fim do jogo
    canvas.itemconfig(game, text="Game over!")

# Cria o objeto barra
Barra = Barra(canvas, "orange")

# Cria o objeto bola 
Bola = Bola(canvas, Barra, "purple")

score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

# Checa botão pressionado para inciar o jogo
canvas.bind_all("<Button-1>", start_game)

root.mainloop()