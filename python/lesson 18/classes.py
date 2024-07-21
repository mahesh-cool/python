class Vehicle: # classes
    def __init__(self,make,model):
        # defining objects in the class
        self.make = make # objects defining
        self.model = model# objects defining

    def moves(self): 
        print('Moves along..')
    
    def get_make_model(self):
        print(f"'I' m a {self.make} {self.model}")

my_car = Vehicle('Tesla', 'alto 500') # object of Vehicle class
# tesla and alto 500 are object of my car class

print(my_car.make) # printing car make tesla seperate line
print(my_car.model)# printing car model tesla seperate line
my_car.get_make_model()# prints model and make in single line
my_car.moves() 
 
mahe_car = Vehicle('cadillac','elantra')
mahe_car.get_make_model()
mahe_car.moves()


class Airplane(Vehicle):
    # for Airplane class we are inheriting
    def moves(self):
        print('flies along..')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')

class Golfcart(Vehicle):
    pass

cessna = Airplane('Cessna','skyhawk')
tata = Truck('TATA','407')   
golfwagon = Golfcart('yamaha','GC100')

cessna.get_make_model()
cessna.moves()
tata.get_make_model()
tata.moves()
golfwagon.get_make_model()
golfwagon.moves()   


print('\n\n')

for v in(my_car,mahe_car, cessna, tata,golfwagon):
    v.get_make_model()
    v.moves()