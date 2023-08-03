#Name: Jessy Vanderhoff 
#Date: July 21, 2023


#vehicle is the base class 
class vehicle:
  def setVehicle_make(self, strMake):
    self.vehicle_make = strMake

  def setVehicle_model(self, strModel):
    self.vehicle_model = strModel

  def getVehicle_make(self):
    return self.vehicle_make    

  def getVehicle_model(self):
    return self.vehicle_model

#set car class
class Car(vehicle):
  
  def setCar_Door(self, door):
    self.num_doors = door

  def getCar_Door(self):
    return self.num_doors

#set truck class
class Truck(vehicle):
  
  def setBed_length(self, length):
    self.bed_length = length

  def getBed_length(self):
    return self.bed_length

#Welcome message and choose options
print('\nWELCOME TO VIRTUAL GARAGE')

choose_vehicle = int(input("\nPlease enter 1 for car, 2 for truck, or 3 to quit:"))
if (choose_vehicle == 1):
  my_vehicle = Car()
  
  strMake = input("Please enter the Car make: ")
  my_vehicle.setVehicle_make(strMake)
  strModel = input("Please enter the Car model: ")
  my_vehicle.setVehicle_model(strModel)
  strDoors = input("Please enter the number of doors: ")
  my_vehicle.setCar_Door(strDoors)
  print("\nYour car has the following attributes:")
  current_make = my_vehicle.getVehicle_make()
  print(f"The make is {current_make}")
  current_model = my_vehicle.getVehicle_model()
  print(f"The model is {current_model}")
  current_doors = my_vehicle.getCar_Door()
  print(f"Amount of doors {current_doors}")
  print(f"Your Car has been added to the Garage!")      

elif (choose_vehicle == 2):
  my_truck = Truck()

  strMake = input("Please enter the Truck make: ")
  my_truck.setVehicle_make(strMake)
  strModel = input("Please enter the Truck model: ")
  my_truck.setVehicle_model(strModel)
  length = input("Please enter the bed length: ")
  my_truck.setBed_length(length)
  print("\nYour Truck has the following attributes:")
  current_make = my_truck.getVehicle_make()
  print(f"The make is {current_make}")
  current_model = my_truck.getVehicle_model()
  print(f"The model is {current_model}")
  current_length = my_truck.getBed_length()
  print(f"The Length of the bed is: {current_length}")
  print(f"Your Truck has been added to the Garage!")

elif (choose_vehicle == 3):
  print('\nThank you for using the Virtual Garage!')

else:
  print("Please only choose number 1 for Car, 2 for Truck, 3 for quit")

