from adress import Adress


class Mailing:
    to_address = Adress
    from_address = Adress
    cost = 1100
    track = 123456789

    def __init__(self, to_adress, from_adress, cost, track):
        self.to = to_adress
        self.fr = from_adress
        self.c = cost
        self.t = track
