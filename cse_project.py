grocery_items = {
    "Rice": 55,
    "Wheat Flour": 45,
    "Sugar": 42,
    "Milk": 30,
    "Eggs": 7,
    "Oil": 120,
    "Soap": 25,
    "Shampoo": 5,
    "Biscuits": 10
}

def show_items():
    print("\nItems Available:")
    print("Item                Price")
    for i,p in grocery_items.items():
        print(f"{i:<20}{p}")

def savebill(nm, items, total):
    fname = nm + "_bill.txt"
    f = open(fname, "w", encoding="utf-8")
    f.write("Grocery Billing System\n")
    f.write("Customer: " + nm + "\n\n")
    f.write("Item               Qty       Price\n")
    for x,(q,pr) in items.items():
        f.write(f"{x:<18}{q:<10}{pr}\n")
    f.write("\nTotal: ₹" + str(total))
    f.close()
    print("Bill saved as", fname)

def main():
    print("Grocery Billing System")
    name = input("Enter customer name: ")
    bought = {}
    total = 0

    while True:
        show_items()
        ch = input("\nEnter item (or done): ")

        if ch.lower() == "done":
            break

        if ch not in grocery_items:
            print("Item not found.")
            continue

        try:
            q = int(input("Enter quantity: "))
        except:
            print("Invalid qty")
            continue

        amt = grocery_items[ch] * q
        total += amt
        bought[ch] = (q, amt)
        print("Added", q, ch, "=", amt)

    print("\nFinal Bill:")
    for it,(q,pr) in bought.items():
        print(it, q, "=", pr)

    print("Total:", total)
    savebill(name, bought, total)

if __name__ == "__main__":
    main()