import csv
STOCK_PRICES = {
    "AAPL": 317,
    "TSLA": 368,
    "GOOGL": 340,
    "AMZN": 260,
    "MSFT": 507,
    "NVDA": 220
}
def display_available_stocks():
    print("\n--- Available Stocks & Prices ---")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")
    print("==========================\n")
def get_user_portfolio():
    portfolio = {}
    while True:
        stock_name = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        if stock_name == 'DONE':
            break
        if stock_name not in STOCK_PRICES:
            print(f"[!] Error: '{stock_name}' is not in the price list. Please choose an available stock.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: ").strip())
            if quantity <= 0:
                print("  [!] Quantity must be greater than 0.")
                continue
        except ValueError:
            print("[!] Invalid input. Please enter a valid whole number for quantity.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
        print(f"[+] Added {quantity} share(s) of {stock_name} to portfolio.\n")
    return portfolio
def calculate_portfolio(portfolio):
    """Calculates individual stock totals and grand total."""
    results = []
    grand_total = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        total_val = price * qty
        grand_total += total_val
        results.append({
            "stock": stock,
            "price": price,
            "quantity": qty,
            "total_value": total_val
        })
    return results, grand_total

def display_summary(results, grand_total):
    print("\n" + "=" * 50)
    print("                 SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<10}{'Price ($)':<12}{'Quantity':<12}{'Total Value ($)':<16}")
    print("-" * 50)

    for item in results:
        print(f"{item['stock']:<10}${item['price']:<11}{item['quantity']:<12}${item['total_value']:<15.2f}")

    print("-" * 50)
    print(f"Total Investment Value: ${grand_total:,.2f}")
    print("=" * 50)

def save_to_file(results, grand_total):
    save_option = input("\nWould you like to save this summary to a file? (txt/csv/no): ").strip().lower()
    
    if save_option == 'txt':
        filename = "portfolio_summary.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write("                PORTFOLIO SUMMARY\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Stock':<10}{'Price ($)':<12}{'Quantity':<12}{'Total Value ($)':<16}\n")
            f.write("-" * 50 + "\n")
            for item in results:
                f.write(f"{item['stock']:<10}${item['price']:<11}{item['quantity']:<12}${item['total_value']:<15.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"Total Investment Value: ${grand_total:,.2f}\n")
            f.write("=" * 50 + "\n")
        print(f"  [+] Portfolio saved successfully to '{filename}'!")

    elif save_option == 'csv':
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock Symbol", "Price per Share ($)", "Quantity", "Total Value ($)"])
            for item in results:
                writer.writerow([item['stock'], item['price'], item['quantity'], f"{item['total_value']:.2f}"])
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", f"{grand_total:.2f}"])
        print(f"  [+] Portfolio saved successfully to '{filename}'!")

def main():
    print("=" * 50)
    print("         STOCK TRACKER")
    print("=" * 50)

    display_available_stocks()
    portfolio = get_user_portfolio()

    if not portfolio:
        print("\nNo stocks were entered. Exiting program.")
        return
    results, grand_total = calculate_portfolio(portfolio)
    display_summary(results, grand_total)
    save_to_file(results, grand_total)

if __name__ == "__main__":
    main()
