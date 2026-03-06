from datetime import datetime, timedelta

""" This function gets the frecuency of the medicament to be taken"""
def get_frecuency():
    print("Select medication frecuency:")
    print("1. every 6 hours")
    print("2. every 8 hours")
    print("3. every 12 hours")
    print("4. Custom interval")

    while True:
        choice = input("Choose an option (1-4)")

        if choice == "1":
            return 6
        elif choice == "2":
            return 8
        elif choice == "3":
            return 12
        elif choice == "4":
            while True:
                custom = input("Enter frecuency in hours: ").strip()
                if custom.isdigit() and int(custom) > 0:
                    return int(custom)
                print("Please enter a valid positive number.")
        else:
            print("invalid option. Please choose 1, 2, 3, or 4")

def generate_schedule(first_dose,frequency_hours, duration_days):
    schedule = []
    interval = timedelta(hours=frequency_hours)
    end_date = first_dose + timedelta(days=duration_days)
