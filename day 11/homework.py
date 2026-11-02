total_income = 0
completed_rides = 0
cancelled_rides = 0
total_distance = 0
ride_history = []

while True:
    print(
    """
    ====== TAXI SYSTEM ======
    1. Order a Ride
    2. View Income
    3. Ride Statistics
    4. Exit
    =========================
    """
    )

    choice = int(input("Please enter choice: "))

    if choice == 1:
        distance = float(input("Enter distance (km): "))
        passengers = int(input("Enter passengers (1-4): "))
        night = input("Night ride? (yes/no): ").lower()

        if distance > 0 and 1 <= passengers <= 4 and night in ["yes", "no"]:

            fare = 2.50 + distance * 0.70

            if passengers >= 3:
                fare += 3

            night_extra = 0

            if night == "yes":
                night_extra = fare * 0.20
                fare += night_extra

            print("\n====== RIDE DETAILS ======")
            print("Distance:", distance, "km")
            print("Passengers:", passengers)
            print("Night ride:", night)
            print("Night extra:", round(night_extra, 2), "GEL")
            print("Final fare:", round(fare, 2), "GEL")

            confirm = input("Confirm ride? (yes/no): ").lower()

            while confirm not in ["yes", "no"]:
                confirm = input("Enter yes or no: ").lower()

            if confirm == "yes":
                total_income += fare
                completed_rides += 1
                total_distance += distance
                ride_history.append(round(fare, 2))
                print("Successfully completed ride!")

            else:
                cancelled_rides += 1
                print("Ride cancelled!")

        else:
            print("Invalid information! Try again!")

    elif choice == 2:
        print("Total income:", round(total_income, 2), "GEL")
        print("Completed rides:", completed_rides)

        if completed_rides > 0:
            print("Average fare:", round(total_income / completed_rides, 2), "GEL")
        else:
            print("No completed rides!")

    elif choice == 3:
        print(
        f"""
        ====== RIDE STATISTICS ======
        Completed rides: {completed_rides}
        Cancelled rides: {cancelled_rides}
        Total distance: {total_distance} km
        Total income: {round(total_income, 2)} GEL
        ============================
        """
        )

        if completed_rides > 0:
            print("Most expensive ride:", max(ride_history), "GEL")
            print("Cheapest ride:", min(ride_history), "GEL")
            print("Average fare:", round(total_income / completed_rides, 2), "GEL")

            expensive = 0

            print("\n====== RIDE HISTORY ======")

            for i in range(len(ride_history)):
                print("Ride", i + 1, ":", ride_history[i], "GEL")

                if ride_history[i] > 20:
                    expensive += 1

            print("Rides over 20 GEL:", expensive)

        else:
            print("No completed rides yet!")

    elif choice == 4:
        print("Thank you for using TAXI SYSTEM!")
        break

    else:
        print("Invalid option! Try again!")

