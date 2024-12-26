class Cafe:
    def __init__(self, coffee_cost, sandwich_cost):
        self.coffee_cost = coffee_cost
        self.sandwich_cost = sandwich_cost
    def calculate_total_amount(self, wants_coffee, wants_sandwich):
        total_amount = 0
        if wants_coffee:
            total_amount += self.coffee_cost
        if wants_sandwich:
            total_amount += self.sandwich_cost
        return total_amount
    def handle_order(self, customer_name, wants_coffee, wants_sandwich):
        print(f"Processing order for {customer_name}...")
        total_amount = self.calculate_total_amount(wants_coffee, wants_sandwich)
        print(f"Total amount to pay: ${total_amount:.2f}")
        self.process_payment(total_amount)
    def process_payment(self, amount):
        print(f"Payment of ${amount:.2f} processed. Thank you for your order!")
    def update_prices(self, new_coffee_cost, new_sandwich_cost):
        self.coffee_cost = new_coffee_cost
        self.sandwich_cost = new_sandwich_cost
        print("Menu prices updated.")
def main():
    cafe = Cafe(5.0, 2.0)
    print("Welcome to the Cafe Application")
    cafe.handle_order("Alice", wants_coffee=True, wants_sandwich=False)
    cafe.update_prices(4.0, 1.0)
    cafe.handle_order("Bob", wants_coffee=True, wants_sandwich=True)
    print("Thank you for visiting our cafe!")
if __name__ == "__main__":
    main()
