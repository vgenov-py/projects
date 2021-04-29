class Municipality:
    contador = 0
    total_population = 0
    annual_growth_rate = 1.01
    def __init__(self, name, density, area):
        self.dias= 0
        self.name = name
        self.density = density
        self.area = area
        Municipality.contador += 1
        Municipality.total_population += self.population

    @classmethod
    def from_str(cls, value):
        name, density, area = value.split("-")
        try:
            return cls(name,float(density),float(area))
        except ValueError:
            print("No has introducido valores númericos")

    @classmethod
    def set_annual_growth_rate(cls, value):
        cls.annual_growth_rate = value

    def apply_growth(self):
        self.density = self.density * Municipality.annual_growth_rate

    @property
    def population(self):
        return self.density * self.area

    def __str__(self):
        return f"{self.name} con una densidad de: {round(self.density,3)} y con una superfice de: {round(self.area,3)} con un población de {round(self.population,2)}"

    def __repr__(self):
        return f"Municipality({self.name}, {self.density}, {self.area})"

    @staticmethod
    def cualquiercosa():
        return 2



