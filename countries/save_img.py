import requests as req

# Escritura binaria de una imagen

# 1. Hacer request a la url que albergue la img

url_img = "https://images.unsplash.com/photo-1620215175664-cb9a6f5b6103?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80"
response = req.get(url_img).content # Debemos acceder al contenido de la imagen

# 2. Escribir el contendio dentro de response en binario
with open("foto_de_la_tia.jpg", "wb") as file:
    file.write(response)