def validate_purchase(requested, remaining):
    """Checks if the ticket request is valid based on rules and availability."""
    if requested < 1 or requested > 4:
        print("Error: You can only buy between 1 and 4 tickets.")
        return False
    if requested > remaining:
        print(f"Error: Only {remaining} tickets left. You cannot buy {requested}.")
        return False
    return True


def process_sales():
    """Main logic to handle the ticket pre-sale loop."""
    total_tickets = 20
    total_buyers = 0  # Accumulator

    print("--- Welcome to the Cinema Pre-Sale! ---")
    print(f"Total tickets available: {total_tickets}")

    # Loop until all tickets are sold
    while total_tickets > 0:
        try:
            # Input
            user_input = int(input(f"\nRemaining tickets: {total_tickets}. How many would you like to buy? "))

            # If statement (via function call) for validation
            if validate_purchase(user_input, total_tickets):
                total_tickets -= user_input  # Update remaining
                total_buyers += 1  # Increment accumulator
                print(f"Purchase successful! You bought {user_input} tickets.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Output final results
    print("\n" + "=" * 30)
    print("All tickets have been sold!")
    print(f"Total number of buyers: {total_buyers}")
    print("=" * 30)


# Execute the application
if __name__ == "__main__":
    process_sales()