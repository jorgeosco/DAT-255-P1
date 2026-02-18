import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon 
 
ancho = 10 
alto = 10 
 
num_figuras = 7 
num_vertices = 3 
colores = ['r', 'g', 'b', 'y', 'c', 'm'] 
 
fig, ax = plt.subplots() 
 
for i in range(num_figuras): 
 
    x = np.random.rand(num_vertices) * ancho 
    y = np.random.rand(num_vertices) * alto 
    vertices = list(zip(x, y)) 
 
 
    figura = Polygon( 
        vertices, 
        closed=True, 
        alpha=np.random.rand(), 
        facecolor=np.random.choice(colores), 
    ) 
    ax.add_patch(figura) 
 
 
ax.set_xlim(0, ancho) 
ax.set_ylim(0, alto) 
ax.set_aspect('equal', adjustable='box') 
ax.set_xticks([]) 
ax.set_yticks([]) 
 
 
ruta_salida = "output/G2-figuras_aleatorias.png" 
plt.savefig(ruta_salida) 
print(f"Imagen guardada en: {ruta_salida}") 