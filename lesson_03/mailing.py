from address import Address


class Mailing:
    to_address = Address
    from_address = Address
    cost = float
    track = str

    def __init__(self, to_address, from_address, cost: float, track: str):
        self.to_adress_1 = to_address
        self.from_address_1 = from_address
        self.cost_1 = cost
        self.track_1 = track
