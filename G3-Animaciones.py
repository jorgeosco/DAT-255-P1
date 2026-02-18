import os 
import random 
import numpy as np 
import imageio.v2 as imageio 
 
width, height = 640, 360 
fps = 30 
duration_seconds = 5 
num_frames = fps * duration_seconds 
 
num_rectangles = 8 
 
rect_w, rect_h = 60, 40 
 
rectangles = [] 
for _ in range(num_rectangles): 
    rect = { 
        "x": random.randint(0, width - rect_w),   # posición X inicial 
        "y": random.randint(0, height - rect_h),   # posición Y inicial 
        "vx": random.choice([-3, -2, -1, 1, 2, 3]),  # velocidad X 
        "vy": random.choice([-3, -2, -1, 1, 2, 3]),  # velocidad Y 
        "color": (                                     # color aleatorio 
            random.randint(80, 255), 
            random.randint(80, 255), 
            random.randint(80, 255), 
        ), 
    } 
    rectangles.append(rect) 
 
print(f"Rectángulos creados: {len(rectangles)}") 
 
 
frames = [] 
 
for i in range(num_frames): 
 
    frame = np.zeros((height, width, 3), dtype=np.uint8) 
 
    for rect in rectangles: 
        # Mover el rectángulo 
        rect["x"] += rect["vx"] 
        rect["y"] += rect["vy"] 
        # Dibujar el rectángulo en el frame 
        x0, y0 = rect["x"], rect["y"] 
        x1, y1 = x0 + rect_w, y0 + rect_h 
        frame[y0:y1, x0:x1] = rect["color"] 
 
    frames.append(frame) 
 
print(f"Frames generados: {len(frames)}") 
 
 
output_dir = "output" 
os.makedirs(output_dir, exist_ok=True) 
 
output_mp4 = os.path.join(output_dir, "G3-rectangulos-animacion.mp4") 
output_gif = os.path.join(output_dir, "G3-rectangulos-animacion.gif") 
 
try:
    with imageio.get_writer(output_mp4, fps=fps, codec="libx264") as writer:
        for frame in frames:
            writer.append_data(frame)
    print(f"Video MP4 guardado en: {output_mp4}")
except Exception as exc:
    print(f"MP4 falló ({exc}), guardando como GIF...")
    imageio.mimsave(output_gif, frames, fps=fps)
    print(f"Video GIF guardado en: {output_gif}")