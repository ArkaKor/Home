from adress import Adress


class Mailing:
    to_address = Adress
    from_address = Adress
    cost = 1200
    track = 1234567890

    def __init__(self, to_adress, from_adress, cost: float, track: str):
        self.to = to_adress
        self.fr = from_adress
        self.c = cost
        self.t = track
