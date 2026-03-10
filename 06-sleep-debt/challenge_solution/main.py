planned = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual = [5, 12, 6, 6, 9, 8, 6.5]

def calculate_sleep_debt(planned, actual):

    total_debt = 0
    current_streak = 0
    longest_streak = 0

    for p, a in zip(planned, actual):

        debt = max(0, p - a)
        total_debt += debt

        if debt > 0:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    total_debt += 1  # Daylight Savings hour

    return total_debt, longest_streak
