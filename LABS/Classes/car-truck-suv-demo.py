# This program creates a Car and SUV objects

import vehicles

def main ():
    # Create an object from Car class
    # The car is a 2007 Audi with 12,500 miles, price at $21,500.00, and has 4 doors
    new_car = vehicles.Car('Bugatti', 'Veyron', 0, 3000000.00, 2)

    # Display car's data
    print('Make: ', new_car.get_make())
    print('Model: ', new_car.get_model())
    print('Mileage: ', new_car.get_mileage())
    print('Price: ', new_car.get_price())
    print('Doors: ', new_car.get_doors())
    print()

    # Create an object from Truck class
    new_truck = vehicles.Trucks('Dodge', 'Power Wagon', 0, 57000.00, '4WD')

    # Display car's data
    print('Make: ', new_truck.get_make())
    print('Model: ', new_truck.get_model())
    print('Mileage: ', new_truck.get_mileage())
    print('Price: ', new_truck.get_price())
    print('Drive Type: ', new_truck.get_drive_type())
    print()

    # Create an object from SUV class
    new_suv = vehicles.SUV('Jeep', 'Grand Cherokee SRT8', 0, 57000.00, 7)

    # Display car's data
    print('Make: ', new_suv.get_make())
    print('Model: ', new_suv.get_model())
    print('Mileage: ', new_suv.get_mileage())
    print('Price: ', new_suv.get_price())
    print('Passenger Capacity: ', new_suv.get_pass_cap())
    print()
main()