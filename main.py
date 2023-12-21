from datetime import date


def calculate_date_delta(input_date: date) -> int:
    """Calculates the number of days since December 31, 2020"""
    end_of_2020 = date(2020, 12, 31)
    delta = input_date - end_of_2020
    return delta.days


def format_date(date_delta: int) -> str:
    day = 31 + date_delta  # 31 days in December
    return f"December {day}, 2020"


today = date.today()
print(format_date(calculate_date_delta(today)))
