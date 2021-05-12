import bcrypt

password = input("contraseña: ").encode()

print(type(password))
password_encriptada = bcrypt.hashpw(password, bcrypt.gensalt())
# print(password_encriptada)
# veredict = True if bcrypt.checkpw(password, password_encriptada) else False
# if veredict:
#     print("puedes acceder")
# else:
#     print("no puedes")


# password = b"hola"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
# print(hashed)
# if  bcrypt.checkpw(password, hashed):
#     print("Kuga")