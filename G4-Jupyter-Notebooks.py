import nbformat 
 
py_path = "input/code-G4.py" 
ipynb_path = "output/G4-notebook.ipynb" 
 
with open(py_path, "r", encoding="utf-8") as f: 
    lines = f.readlines() 
 
print(f"Archivo leído: {py_path} ({len(lines)} líneas)") 
 
nb = nbformat.v4.new_notebook() 
 
buffer = [] 
current_type = None  # "code" o "markdown" 
 
for line in lines:
    # Línea vacía: termina la celda actual
    if line.strip() == "":
        if buffer:
            contenido = "".join(buffer)
            if current_type == "markdown":
                nb.cells.append(nbformat.v4.new_markdown_cell(contenido))
            else:
                nb.cells.append(nbformat.v4.new_code_cell(contenido))
            buffer = []
            current_type = None
        continue

    # Determinar si es comentario o código
    is_comment = line.lstrip().startswith("#") and not line.lstrip().startswith("#!")
    line_type = "markdown" if is_comment else "code"

 
    # Si cambia el tipo, guardar celda anterior 
    if current_type is not None and line_type != current_type: 
        contenido = "".join(buffer) 
        if current_type == "markdown": 
            nb.cells.append(nbformat.v4.new_markdown_cell(contenido)) 
        else: 
            nb.cells.append(nbformat.v4.new_code_cell(contenido)) 
        buffer = [] 
 
    current_type = line_type 
 
    # Procesar la línea según su tipo 
    if line_type == "markdown": 
        text = line.lstrip()[1:]  # Quitar el '#' 
        if text.startswith(" "): 
            text = text[1:]       # Quitar el espacio después del '#' 
        buffer.append(text) 
    else: 
        buffer.append(line) 
 
if buffer: 
    contenido = "".join(buffer) 
    if current_type == "markdown": 
        nb.cells.append(nbformat.v4.new_markdown_cell(contenido)) 
    else: 
        nb.cells.append(nbformat.v4.new_code_cell(contenido)) 
 
print(f"Celdas creadas: {len(nb.cells)}") 
 
 
with open(ipynb_path, "w", encoding="utf-8") as f: 
    nbformat.write(nb, f) 
 
print(f"Notebook creado: {ipynb_path}") 