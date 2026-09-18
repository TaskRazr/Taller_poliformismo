class Empleado:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def calcular_pago(self):
        pass


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, identificacion, salario_mensual):
        super().__init__(nombre, identificacion)
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.salario_mensual


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, identificacion, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, identificacion)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_pago(self):
        return self.horas_trabajadas * self.pago_por_hora


class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, identificacion, salario_base, ventas, porcentaje_comision):
        super().__init__(nombre, identificacion)
        self.salario_base = salario_base
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    def calcular_pago(self):
        return self.salario_base + (self.ventas * self.porcentaje_comision / 100)


empleados = [
    EmpleadoFijo("Ana Torres", "E001", 2500000),
    EmpleadoPorHoras("Luis Pérez", "E002", 160, 15000),
    EmpleadoPorComision("Marta Gómez", "E003", 1500000, 20000000, 3),
    EmpleadoFijo("Carlos Ruiz", "E004", 3000000),
    EmpleadoPorHoras("Sofía León", "E005", 140, 18000),
]

total_nomina = 0

for empleado in empleados:
    pago = empleado.calcular_pago()
    total_nomina = total_nomina + pago
    print(empleado.nombre, "-", type(empleado).__name__, "- Pago:", pago)

print("TOTAL NOMINA:", total_nomina)
