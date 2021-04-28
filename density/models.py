class Municipality:
    contador = 0
    total_population = 0
    annual_growth_rate = 1.01

    def __init__(self, name, density, area):
        self.name = name
        self.density = density
        self.area = area
        Municipality.contador += 1
        Municipality.total_population += self.population

    @property
    def population(self):
        return self.density * self.area

    def __str__(self):
        return f"{self.name} con una densidad de: {round(self.density,3)} y con una superfice de: {round(self.area,3)}"

    def __repr__(self):
        return f"Municipality({self.name}, {self.density}, {self.area})"
