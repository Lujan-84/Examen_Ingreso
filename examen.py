import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: marca (ford, volvo, fiat), tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Ford - Auto - 1000 km
         2 - Fiat - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo de marca 'Ford'.
    2- Kilometraje promedio de los autos por cada marca.
    3- Precio promedios de todos los servicios por marca.
    4- Informar los kilometrajes que superan el promedio (total) por tipo.
    5- Informar los kilometrajes que NO superan el promedio (total) por marca.
    6- Informar la cantidad de tipos por marca.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms de marca 'Volvo'.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de los servicios de marca 'Ford'.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
    
    *Si la marca es volvo tiene un recargo del 10%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []
        self.lista_marca_vehiculo = []
        self.lista_kms_vehiculos = []

    def btn_agregar_on_click(self):
        respuesta = True
        while respuesta:
            marca = prompt("Datos" , "Ingrese marca:")
            while marca != "ford" and marca != "volvo" and marca != "fiat":
                marca = prompt("Datos" , "Reingrese marca:")   
            
            
            tipo_vehiculo = prompt("Dato" , "Ingrese el tipo de vehículo:")
            while tipo_vehiculo != "auto" and tipo_vehiculo != "camioneta" and tipo_vehiculo != "moto": 
                tipo_vehiculo = prompt("Dato" , "Reingrese el tipo de vehículo:")  
            
            
            kilometros = prompt("Dato" , "Ingrese los kilómetros:")
            while kilometros == None or int(kilometros) < 1:
                kilometros = prompt("Dato" , "Reingrese los kilómetros:")
            kilometros = int(kilometros)

            self.lista_marca_vehiculo.append(marca)
            self.lista_tipo_vehiculo.append(tipo_vehiculo)
            self.lista_kms_vehiculos.append(kilometros)
            
            respuesta = question("", "Desea seguir?")
    
    def btn_mostrar_on_click(self):
        for i in range(len(self.lista_kms_vehiculos)):
            mensaje = str(i+1) + " - " + self.lista_marca_vehiculo[i] + " - " + self.lista_tipo_vehiculo[i] + " - " +  str(self.lista_kms_vehiculos[i]) + " Km"
            print(mensaje)


    def btn_informar_on_click(self):
        mensaje = ""
        contador_km_volvo = 0
        contador_km_fiat = 0
        contador_km_ford = 0
        acumulador_km_volvo = 0
        acumulador_km_fiat = 0
        acumuladro_km_ford = 0
        for i in range(len(self.lista_kms_vehiculos)):
            match self.lista_marca_vehiculo[i]:
                case "volvo":
                    contador_km_volvo += 1
                    acumulador_km_volvo += self.lista_kms_vehiculos[i]
                case "fiat":
                    contador_km_fiat += 1
                    acumulador_km_fiat += self.lista_kms_vehiculos[i]
                case "ford":
                    contador_km_ford +=1
                    acumuladro_km_ford += self.lista_kms_vehiculos[i]
        if contador_km_fiat != 0:
            promedio_km_fiat = acumulador_km_fiat / contador_km_fiat
            mensaje += "El promedio de kilometros de la marca Fiat es " + str(promedio_km_fiat) + " km\n"
        else:
            mensaje += "No hay vehículos de la marca Fiat \n"
        if contador_km_ford != 0:
            promedio_km_ford = acumuladro_km_ford / contador_km_ford
            mensaje += "El promedio de kilometros de la marca Ford es " + str(promedio_km_ford) + " Km\n"
        else:
            mensaje += "No hay vehículos de la marca Ford \n"
        if contador_km_volvo != 0:
            promedio_km_volvo = acumulador_km_volvo / contador_km_volvo
            mensaje += "El promedio de kilometros de la marca Volvo es " + str(promedio_km_volvo) + " Km\n"
        else:
            mensaje += "No hay vehículos de la marca Volvo\n"
            
        acumulador_precio = 0
        contador = 0
        for i in range(len(self.lista_kms_vehiculos)):
            if self.lista_kms_vehiculos[i] > 10000 and self.lista_marca_vehiculo[i] == "volvo":
                match self.lista_tipo_vehiculo[i]:
                    case "auto":
                        precio_servicio = 15000 * 1.1
                    case "camioneta":
                        precio_servicio = 25000 * 1.1
                    case "moto":
                        precio_servicio = 10000 * 1.1
                acumulador_precio += precio_servicio
                contador += 1
        
        if contador != 0:
            promedio_precio_servicio = round(acumulador_precio / contador,2)
            mensaje += "El precio promedio de los servicios cuyo kilometraje es mayor a 10000 Kms de marca Volvo es $" + str(promedio_precio_servicio) 
        print(mensaje)
                
       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()


