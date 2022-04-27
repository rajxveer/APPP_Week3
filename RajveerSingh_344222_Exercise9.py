# Neve use any classes or functions, they are REQUIRED

vehicles = {}

while True:
    
    print("===== Vehicle Inventory System =====\n")
    
    print("Vehicle Records")
    print("1) Add a vehicle")
    print("2) Edit a vehicle")
    print("3) Delete a vehicle")
    print("4) Display all vehicles")
    print("5) Exit the program")
    
    user_choice = input("\nPlease choose an option: ")
    
    if user_choice == "1":
        new_vehicle = input("\nEnter the vehicle unique ID: ")
        
        name = input("Vehicle name: ")
        kind = input("Vehicle kind: ")
        color = input("Vehicle color: ")
        value = input("Vehicle value: ")
        
        vehicles[new_vehicle] = name, kind, color, value
        print("\nVehicle was added successfully\n")
        
    elif user_choice == "2":
        if len(vehicles) == "1":
            print("\nThere are no vehicle records currently\n")
            continue
        print(vehicles)
        edit_vehicle = input("\nChoose the unique ID of the vehicle you would like to edit: ")
        
        new_name = input("Vehicle name: ")
        new_kind = input("Vehicle kind: ")
        new_color = input("Vehicle color: ")
        new_value = input("Vehicle value: ")
        
        vehicles[edit_vehicle] = new_name, new_kind, new_color, new_value
        print("\nVehicle was updated successfully\n")
        
    elif user_choice == "3":
        if len(vehicles) == "1":
            print("\nThere are no vehicle records currently\n")
            continue
        print(vehicles)
        delete_vehicle = input("\nChoose the unique ID of the vehicle you would like to delete: ")
        vehicles.pop(delete_vehicle)
        print("\nVehicle was deleted successfully\n")
    
    elif user_choice == "4":
        if len(vehicles) == "1":
            print("\nThere are no vehicle records currently\n")
            continue
        print(vehicles)
    
    elif user_choice == "5":
        print("\nEXIT\n")
        break
    
    else:
        print("\nPlease choose a valid option\n")