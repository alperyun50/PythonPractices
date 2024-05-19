class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print("I can move") 

    def get_make_model(self):
        print(f"I am a {self.make} {self.model}.")

my_car = Vehicle("Tesla", "Model 3")

print(my_car.make)
my_car.moves()
my_car.get_make_model()

your_car = Vehicle("Cadillac", "Escalade")

your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("I can fly")


class Truck(Vehicle):
    def moves(self):
        print("I can drive")


class GolfCart(Vehicle):
    pass


cessa = Airplane("Cessna", "172", "N12345")
mack = Truck("Ford", "F150")
golfwagon = GolfCart("Golf", "Wagon")

cessa.get_make_model()
cessa.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("\n\n")

for v in (my_car, your_car, cessa, mack, golfwagon):
    v.get_make_model()
    v.moves()