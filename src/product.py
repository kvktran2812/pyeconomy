import datetime


class Product:
    def __init__(self, name: str, prize: float = 0.0, lifetime: str = "", materials=None):
        self.name = name
        self.prize = prize
        self.lifetime = lifetime

        if not materials:
            self.materials = {}
        else:
            self.materials = materials

        # mfg date and exp date
        # TODO fix exp date, calculate from mfg date and lifetime
        self.mfg_date = datetime.date.today()
        self.exp_date = datetime.date.today()

    def __str__(self):
        return f"{self.lifetime} {self.materials}"

    def product_detail(self):
        print(f"{self.lifetime} {self.materials}")

