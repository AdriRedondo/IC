def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido a Python."
if __name__ == "__main__":
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    mensaje = saludar(nombre_usuario)
    print(mensaje)
    print(f"Python es genial para aprender a programar, {nombre_usuario}!")