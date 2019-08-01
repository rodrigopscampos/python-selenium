import time
import os

def quadrado_preenchido():
    for l in range(0,10):
        print()
        for c in range(0,10):
            print("#", end="")
            time.sleep(0.05)
    print()

def escada():
    largura_degrau = 3
    qtd_degraus = 20

    largura_total = qtd_degraus * largura_degrau
    num_degrau = 0

    while num_degrau < qtd_degraus:
        for c in range(0, largura_total):
            if c == num_degrau * largura_degrau:
                for ld in range(0, largura_degrau):
                    print("#", end="")
                    time.sleep(0.05)
            else:
                print(" ", end="")
        
        print()
        num_degrau = num_degrau + 1

def X():
    largura = 21
    a = 1
    b = largura - 1
    print()
    while a < largura:
        for c in range (0, largura):
            if a == c or b == c:
                print("#", end="")
                time.sleep(0.2)
            else:
                print(" ", end = "")
        print()
        a = a + 1
        b = b - 1

def trapezio():
    base_maior = 30
    base_menor = 10
    margem = (base_maior - base_menor) / 2
    aux = 0
    print()
    while aux <= margem:
        for h in range (0, base_maior + 1):
            if h >= margem - aux and h <= margem + base_menor + aux:
                print ("*", end="")
                time.sleep(0.05)
            else:
                print(" ",end="")
        print()
        aux = aux + 1

def triangulo():
    largura = 31
    centro = largura / 2
    area = 0
    print()
    while area < centro:
        for c in range (0, largura):
            if c >= centro - area and c <= centro + area:
                print ("#", end ="")
                time.sleep(0.05)
            else:
                print (" ", end="")
        print()
        area = area + 1
        
def losango():
    margem = 5
    largura = 25
    centro = largura / 2
    area = 0
    print()
    for m in range (0, margem):
        print(" ",end="")
    
    while area < centro - 1:
        for c in range (0, largura):
            if c >= centro - area and c <= centro + area:
                print("#", end="")
                time.sleep(0.05)
            else:
                print(" ",end="")
        print()
        area = area + 1
        
        for m in range (0, margem):
            print(" ", end="")
    while area >= 0:
        for c in range (0, largura):
            if c >= centro - area and c <= centro + area:
                print("#", end="")
                time.sleep(0.05)
            else:
                print(" ",end="")
        print()
        area = area -1
        for m in range (0,margem):
            print (" ", end="")


def circulo():
    margem = 5
    diametro = 50
    raio = diametro / 2
    for v in range (0,diametro + 1):
        for m in range (0, margem):
            print(" ",end="") 
        
        x_1 = raio - ((raio**2) - ((raio - v)**2))**0.5
        x_2 = raio + ((raio**2) - ((raio - v)**2))**0.5
        
        for h in range (0, diametro):
            if h >= int(x_1) and h <= x_2:
                print("**", end="")
                time.sleep(0.0025)
            else:
                print("  ", end="")
        print()



if __name__ == "__main__":

    metodos = [
        quadrado_preenchido,
        escada,
        X,
        trapezio,
        triangulo,
        losango,
        circulo
    ]

    for n, metodo in zip(range(0, len(metodos)), metodos):
        print("{} - {}".format(n+1, metodo.__name__))

    opcao = int(input("Figura selecionada: "))

    while True:
        if opcao < 0 or opcao >= len(metodos):
            print("Opção inválida")
        else:
            print("Figura " + metodos[opcao - 1].__name__)
            break

    loop = input("Loop infinito ? (S/N) ").upper() == 'S'
    print("Vamos lá")
    print()


    while True:
        metodos[opcao - 1]()
        time.sleep(2)
        if not loop:
            break
        
        os.system('cls')





    '''
    quadrado_preenchido()
    time.sleep(2)
    os.system('cls')
    
    escada()
    time.sleep(2)
    os.system('cls')
    
    X()
    time.sleep(2)
    os.system('cls')
    
    trapezio()
    time.sleep(2)
    os.system('cls')

    triangulo()
    time.sleep(2)
    os.system('cls')
    
    losango()
    time.sleep(2)
    os.system('cls')
    
    circulo()
    time.sleep(2)
    os.system('cls')
    '''