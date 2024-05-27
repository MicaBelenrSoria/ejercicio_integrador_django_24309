class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Getters y setters para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía.")

    # Getters y setters para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._edad = valor
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    # Getters y setters para DNI
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._dni = valor
        else:
            raise ValueError("El DNI debe ser una cadena de caracteres no vacía.")

    def mostrar(self):
        
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"DNI: {self._dni}")

    def es_mayor_de_edad(self):
        
        return self._edad >= 18

# Ejemplo de uso
persona = Persona("Juan Pérez", 30, "12345678")
persona.mostrar()
print(f"¿Es mayor de edad? {'Sí' if persona.es_mayor_de_edad() else 'No'}")

# Probando setters y getters
try:
    persona.nombre = "Ana López"
    persona.edad = 25
    persona.dni = "87654321"
    persona.mostrar()
    print(f"¿Es mayor de edad? {'Sí' if persona.es_mayor_de_edad() else 'No'}")
except ValueError as e:
    print(e)
