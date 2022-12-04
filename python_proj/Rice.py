class Rice:
    def __init__(self, fields):
        self.fields = fields

    def grow_rice(self):
        self.fields[:, -1] += 1         # Adds one rice grain per day

    def rice_gets_eaten(self, plant: int):
        # if animal == "Sparrow":
        self.fields[plant, -1] -= 2  # Rice gets eaten
        if self.fields[plant, -1] < 0:
            self.fields[plant, -1] = 0
