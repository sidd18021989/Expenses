from datetime import date


def calculate_mtv_recharge_expense():
    """Calculates MTV recharge expenses."""
    tv_recharge_amount = float(input("Enter the MTV recharge amount: "))
    tv_recharge_date = date.today().strftime("%d/%m/%Y")
    return tv_recharge_amount,tv_recharge_date