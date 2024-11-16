import motorcycle_expenses
import milk_expenses
import tv_recharge_expenses
import mobile_recharge_expenses
import csv
def main():
    """Calculates total expenses and prints the result."""
    motorcycle_fuel_expense,motorcycle_date = motorcycle_expenses.calculate_motorcycle_expenses()
    milk_expense,milk_date = milk_expenses.calculate_milk_expense()
    tv_recharge_expense,tv_recharge_date = tv_recharge_expenses.calculate_mtv_recharge_expense()
    mobile_recharge_expense,mobile_recharge_date = mobile_recharge_expenses.calculate_mobile_recharge_expense()

    total_expense = milk_expense + tv_recharge_expense + mobile_recharge_expense+motorcycle_fuel_expense

    print("Total expenses for the month: ", total_expense)

    with open('expenses.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Expense Type', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Date': motorcycle_date, 'Expense Type': 'Motorcycle', 'Amount': motorcycle_expenses})
        writer.writerow({'Date': milk_date, 'Expense Type': 'Milk', 'Amount': milk_expense})
        writer.writerow({'Date': tv_recharge_date, 'Expense Type': 'MTV Recharge', 'Amount': tv_recharge_expense})
        writer.writerow(
            {'Date': mobile_recharge_date, 'Expense Type': 'Mobile Recharge', 'Amount': mobile_recharge_expense})


if __name__ == "__main__":
    main()