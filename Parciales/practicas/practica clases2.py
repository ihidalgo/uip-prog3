class Perro(object):
   def __init__(self, nombre, raza, edad):
      self.nombre = nombre
      self.raza = raza
      self.edad = edad

   def ladra(self):
      print (self.nombre)

mascota = Perro("Lassie", "Collie", 18)
#mascota.ladra()
