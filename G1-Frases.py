import random 
import os 
 
sujetos = [ 
    "El gato", 
    "La estudiante", 
    "Un programador", 
    "La luna", 
    "El robot", 
]  
verbos = [ 
    "observa", 
    "construye", 
    "descubre", 
    "imagina", 
    "escribe", 
] 
complementos = [ 
    "un misterio en el jardin.", 
    "una idea brillante.", 
    "la solucion del problema.", 
    "un mensaje secreto.", 
    "una historia curiosa.", 
] 
 
num_frases = 5 
 
frases = [] 
for i in range(num_frases): 
    sujeto = random.choice(sujetos) 
    verbo = random.choice(verbos) 
    complemento = random.choice(complementos) 
    frase = f"{sujeto} {verbo} {complemento}" 
    frases.append(frase) 
    print(f"Frase {i + 1}: {frase}") 
 
 
ruta_salida = os.path.join(os.path.dirname(__file__), 'output', 'G1-Frases_Generadas.txt')
os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

with open(ruta_salida, 'w', encoding='utf-8') as archivo:
    for frase in frases:
        archivo.write(frase + '\n')

print(f"Frases guardadas en: {ruta_salida}")
