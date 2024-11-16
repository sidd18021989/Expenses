from datetime import date


def calculate_mobile_recharge_expense():
    """Calculates mobile recharge expenses."""
    mobile_recharge_amount = float(input("Enter the mobile recharge amount: "))
    mobile_recharge_date = date.today().strftime("%d/%m/%Y")
    return mobile_recharge_amount, mobile_recharge_date