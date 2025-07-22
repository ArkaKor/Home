class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.soname = last_name

    def get_name(self):
        return self.name

    def get_soname(self):
        return self.soname

    def get_full_name(self):
        return f"Полное имя: {self.name} {self.soname}"
