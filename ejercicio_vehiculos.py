class VehiculoAutonomo:
    def __init__(self, codigo, nivel_bateria):
        self.codigo = codigo
        self.nivel_bateria = nivel_bateria

    def calcular_consumo(self, distancia):
        pass

    def mover(self, distancia):
        consumo = self.calcular_consumo(distancia)
        if consumo > self.nivel_bateria:
            print(self.codigo, "no puede moverse, batería insuficiente")
        else:
            self.nivel_bateria = self.nivel_bateria - consumo
            print(self.codigo, "-", type(self).__name__, "recorrió", distancia,
                  "| consumo:", consumo, "| batería restante:", self.nivel_bateria)


class AutomovilElectrico(VehiculoAutonomo):
    def __init__(self, codigo, nivel_bateria, consumo_por_km):
        super().__init__(codigo, nivel_bateria)
        self.consumo_por_km = consumo_por_km

    def calcular_consumo(self, distancia):
        return distancia * self.consumo_por_km


class Dron(VehiculoAutonomo):
    def __init__(self, codigo, nivel_bateria, altura_vuelo, consumo_por_km):
        super().__init__(codigo, nivel_bateria)
        self.altura_vuelo = altura_vuelo
        self.consumo_por_km = consumo_por_km

    def calcular_consumo(self, distancia):
        return (distancia * self.consumo_por_km) + (self.altura_vuelo * 0.1)


class RobotTerrestre(VehiculoAutonomo):
    def __init__(self, codigo, nivel_bateria, peso_carga, consumo_por_km):
        super().__init__(codigo, nivel_bateria)
        self.peso_carga = peso_carga
        self.consumo_por_km = consumo_por_km

    def calcular_consumo(self, distancia):
        return (distancia * self.consumo_por_km) + (self.peso_carga * 0.3)


vehiculos = [
    AutomovilElectrico("AUTO-01", 100, 2),
    Dron("DRON-01", 100, 50, 1.5),
    RobotTerrestre("ROBOT-01", 100, 20, 1),
]

distancia = 15

for vehiculo in vehiculos:
    vehiculo.mover(distancia)

dron_agotado = Dron("DRON-02", 5, 200, 1.5)
dron_agotado.mover(50)
