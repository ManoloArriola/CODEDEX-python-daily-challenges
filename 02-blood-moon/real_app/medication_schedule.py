from datetime import datetime, timedelta

def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive number.")

def get_frequency():
    print("Select medication frequency:")
    print("1. Every 6 hours")
    print("2. Every 8 hours")
    print("3. Every 12 hours")
    print("4. Custom interval")

    while True:
        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            return 6
        elif choice == "2":
            return 8
        elif choice == "3":
            return 12
        elif choice == "4":
            return get_positive_int("Enter frequency in hours: ")
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

def generate_schedule(first_dose, frequency_hours, duration_days):
    schedule = []
    interval = timedelta(hours=frequency_hours)
    end_time = first_dose + timedelta(days=duration_days)

    current_time = first_dose
    while current_time <= end_time:
        schedule.append(current_time)
        current_time += interval

    return schedule

def main():
    print("=== Medication Schedule Generator ===")

    medication_name = input("Medication name: ").strip()
    pills_per_dose = get_positive_int("How many pills per dose?: ")
    frequency_hours = get_frequency()

    while True:
        first_dose_input = input("Enter first dose date and time (YYYY-MM-DD HH:MM): ").strip()
        try:
            first_dose = datetime.strptime(first_dose_input, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    duration_days = get_positive_int("How many days is the treatment?: ")

    schedule = generate_schedule(first_dose, frequency_hours, duration_days)

    total_doses = len(schedule)
    total_pills = total_doses * pills_per_dose

    print("\n=== Medication Schedule ===")
    print(f"Medication: {medication_name}")
    print(f"Pills per dose: {pills_per_dose}")
    print(f"Frequency: Every {frequency_hours} hours")
    print(f"Treatment length: {duration_days} day(s)\n")

    for i, dose_time in enumerate(schedule, start=1):
        print(f"{i}. {dose_time.strftime('%Y-%m-%d %H:%M')}")

    print("\n=== Summary ===")
    print(f"Total doses: {total_doses}")
    print(f"Total pills needed: {total_pills}")

if __name__ == "__main__":
    main()