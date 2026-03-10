from datetime import datetime, timedelta


def get_positive_int(prompt):
    """Prompt the user until a valid positive integer is entered."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive number.")


def select_frequency():
    """Ask the user to choose a medication frequency in hours."""
    print("\nSelect dosage frequency:")
    print("1. Every 6 hours")
    print("2. Every 8 hours")
    print("3. Every 12 hours")
    print("4. Custom interval")

    while True:
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            return 6
        elif choice == "2":
            return 8
        elif choice == "3":
            return 12
        elif choice == "4":
            return get_positive_int("Enter custom frequency in hours: ")
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


def get_start_datetime():
    """Prompt the user until a valid date and time is entered."""
    while True:
        user_input = input(
            "Enter first dose date and time (YYYY-MM-DD HH:MM): "
        ).strip()
        try:
            return datetime.strptime(user_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Please try again.")


def build_medication_schedule(start_datetime, frequency_hours, treatment_days):
    """Generate the medication schedule based on frequency and duration."""
    schedule = []
    interval = timedelta(hours=frequency_hours)
    end_datetime = start_datetime + timedelta(days=treatment_days)

    current_time = start_datetime
    while current_time < end_datetime:
        schedule.append(current_time)
        current_time += interval

    return schedule


def display_schedule(medication_name, pills_per_dose, frequency_hours, treatment_days, schedule):
    """Print the medication schedule and summary."""
    total_doses = len(schedule)
    total_pills = total_doses * pills_per_dose

    print("\n=== Medication Schedule ===")
    print(f"Medication: {medication_name}")
    print(f"Pills per dose: {pills_per_dose}")
    print(f"Frequency: Every {frequency_hours} hours")
    print(f"Treatment duration: {treatment_days} day(s)")
    print(f"Total doses: {total_doses}")
    print(f"Total pills needed: {total_pills}\n")

    for i, dose_time in enumerate(schedule, start=1):
        print(f"{i}. {dose_time.strftime('%Y-%m-%d %H:%M')}")


def main():
    print("=== Medication Schedule Generator ===")

    medication_name = input("Medication name: ").strip()
    pills_per_dose = get_positive_int("Pills per dose: ")
    frequency_hours = select_frequency()
    first_dose = get_start_datetime()
    treatment_days = get_positive_int("Treatment duration (days): ")

    schedule = build_medication_schedule(first_dose, frequency_hours, treatment_days)
    display_schedule(
        medication_name,
        pills_per_dose,
        frequency_hours,
        treatment_days,
        schedule
    )


if __name__ == "__main__":
    main()