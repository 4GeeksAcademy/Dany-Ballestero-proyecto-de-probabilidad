#Ejercicio 1 — Simulación con Dos Dados

#Dos dados se lanzan una vez y se observa el total obtenido.

#Queremos estimar, mediante simulación, la probabilidad de que la suma sea:

#- Mayor que 7  
#- O un número par  

#---

## 📌 ¿Qué es una simulación?

#Una simulación consiste en repetir el mismo experimento muchas veces para observar su comportamiento y aproximar probabilidades.

#En este caso:

#- Lanzamos 2 dados  
#- Sumamos sus resultados  
#- Repetimos esto 1000 veces  

#---

## 🧪 Pasos del Experimento

### 1️⃣ Ejecutar el experimento 1000 veces
#- Lanzar 2 dados.
#- Calcular la suma.
#- Repetir 1000 veces.

### 2️⃣ Llevar la cuenta

#Contar cuántas veces ocurre el evento:

#suma > 7  ó  suma es par

### 3️⃣ Calcular la probabilidad estimada

#Probabilidad estimada = (Número de veces que ocurrió el evento) / 1000

import random

# la semilla permite obtener los mismos resultados cuando hay aletoriedad (random) en nuestros jupyter.

N = 1000
favorables = 0

for _ in range(N):#usamos el guion bajo(_) como nombre de la variable cuando no nos interes el valor del contador, solo queremos repetir el bloque 1000 veces
    dado1 = random.randint(1, 6) # 5
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    
    # evento: total > 7 o total par
    if (total > 7) or (total % 2 == 0):#el simbolo de modulo o resto(%) indica que sie el resto de dividir por 2 es 0, significa que el numero es par 
        favorables += 1

prob_estimada = favorables / N #esta  es la formula de probabilidad clasica(Ley de Laplace)
print("Favorables:", favorables)#imprime el numero entero de veces que se cumplio la codicion
print("Probabilidad estimada:", prob_estimada) #muestra probabilidad en formato decimal

# 🎯 Ejercicio 2 — Simulación con Bolas (Con Reemplazo)

#Una caja contiene:

#- 10 bolas blancas  
#- 20 bolas rojas  
#- 30 bolas verdes  

#Total: **60 bolas**

#Tomamos **5 bolas con reemplazo**  
#(es decir, sacamos una bola, anotamos su color y la devolvemos a la caja).

#Queremos estimar la probabilidad de:

#1️⃣ Obtener **3 blancas y 2 rojas**  
#2️⃣ Obtener **todas del mismo color**

#---
import random

ball_box = {} #se crea diccionario

# Crear la caja con las bolas
for i in range(60): #inicia bucle que se repite 60 veces
    if i < 10: #las primeras 10 bolas se marcan como blancas
        ball_box[i] = "White" #agrega la bola al diccionario
    elif (i > 9) and (i < 30): #si la bola no es blanca, pero su numero esta entre 10 y 29, se marca como roja
        ball_box[i] = "Red"
    else:
        ball_box[i] = "Green" #se marcan como verdes
        
ball_box 

N = 1000      

casos_3W_2R = 0 #se crea variable para contar evento especifico
casos_mismo_color = 0 #esta variable es otro contador para un evento distinto

for _ in range(N): #indica que todo por debajo se repetira (N) veces

    # Sacar 5 bolas con reemplazo
    muestra = [] #crea lista vacia para guardar 5 bolas
    for _ in range(5):
        idx = random.randint(0, 59) #elige numero al azar entre 0 y 59
        muestra.append(ball_box[idx]) #busca en el diccionario el color de la bola

    # Contar colores
    w = muestra.count("White") #guardamos la cantidad de blancas, rojas y verdes que sacamos en ese grupo de 5
    r = muestra.count("Red")
    g = muestra.count("Green")

    # Evento 1: 3 blancas y 2 rojas
    if (w == 3) and (r == 2): #si sacamos 3 blancas y 2 rojas el contador sube
        casos_3W_2R += 1

    # Evento 2: todas del mismo color
    if (w == 5) or (r == 5) or (g == 5): #el or permite que el contador suba
        casos_mismo_color += 1

print("Probabilidad estimada (3 blancas y 2 rojas):", casos_3W_2R / N)
print("Probabilidad estimada (5 del mismo color):", casos_mismo_color / N)
