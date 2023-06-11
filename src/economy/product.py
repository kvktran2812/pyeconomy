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

        self.mfg_date = datetime.date.today()
        self.exp_date = datetime.date.today()

    def __str__(self):
        return self._product_detail()

    def _product_detail(self):
        detail = f"{self.lifetime} {self.materials}"
        return detail

