# This program demonstrates the Car class

import vehicles

def main ():
    # Create an object from Car class
    # The car is a 2007 Audi with 12,500 miles, price at $21,500.00, and has 4 doors
    used_car = vehicles.Car('Audi', 'A3', 12500, 21500.00, 4)

    # Display car's data
    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print('Doors: ', used_car.get_doors())

main()