import fuel_rate as fr

try:
        print("Sai Petrol Pump")
        fuel_type = input("Enter fuel type :")
        amount = int(input("Enter Amount :"))
        quantity = 0.0
        if (fuel_type == "Petrol" or fuel_type == "petrol"):
                quantity = amount/fr.todays_petrol_rate
                print(f"Hi you got {quantity} liters {fuel_type} of Rs.{amount}")

        if (fuel_type == "Diesel" or fuel_type == "Diesel"):
                quantity = amount/fr.todays_diesel_rate
                print(f"Hi you get {quantity} liters {fuel_type} of Rs.{amount}")

        if (fuel_type == "CNG" or fuel_type == "cng"):
                quantity = amount/fr.todays_CNG_rate
                print(f"Hi you get {quantity} liters {fuel_type} of Rs.{amount}")

except BaseException as ex:
        print(f"Error occured = {ex}")

finally:
        print("Tata bye bye")
