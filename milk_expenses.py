from datetime import date


def calculate_milk_expense():
    """Calculates milk expenses."""
    liters_consumed = float(input("Enter the total liters of milk consumed: "))

    milk_cost_per_litre = float(input("Enter the cost of milk per litre: "))

    milk_expense = milk_cost_per_litre * liters_consumed
    milk_date = date.today().strftime("%d/%m/%Y")
    return milk_expense,milk_date
