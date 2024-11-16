from datetime import date


def calculate_motorcycle_expenses():
    petrol_cost = float(input("Enter the total petrol cost: "))
    service_cost = float(input("Enter the service cost: "))
    repair_cost = float(input("Enter the repair cost: "))

    motorcycle_expense = petrol_cost + service_cost + repair_cost
    motorcycle_date = date.today().strftime("%d/%m/%Y")
    return motorcycle_expense, motorcycle_date
