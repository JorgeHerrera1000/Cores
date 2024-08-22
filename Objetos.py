class Gato:
    def __init__(self, nombre, edad, raza):
        #dentro del codigo vamos a definir el estado inicial de cualquier perro en este caso
        #que sea creado
        self.name = nombre
        self.age = edad
        self.race = raza

    def cumple(self):
        self.age += 1

    def getName(self):
        return self.name
    







# class Usuario:
#     def __init__(self):
#         self.name = "Jorge"
#         self.lastname = "Herrera"
#         self.email = "jghm1000@gmail.com"
#         self.credit_limit = 10000
#         self.pay = 0 
