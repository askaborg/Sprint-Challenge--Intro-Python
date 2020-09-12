# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle:
    pass

# Vehicle subclass
class GroundVehicle(Vehicle):
    pass

# GroundVehicle subclass
class Car(GroundVehicle):
    pass

# GroundVehicle subclass
class Motorcycle(GroundVehicle):
    pass

# Vehicle subclass
class FlightVehicle(Vehicle):
    pass

# FlightVehicle subclass
class Airplane(FlightVehicle):
    pass

# FlightVehicle subclass
class Starship(FlightVehicle):
    pass