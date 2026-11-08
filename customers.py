# Reflection
#
# 1. I would use .get() when a key might not be there, like an optional
#    field such as a customer's phone number, so the program keeps running
#    and uses a default instead. I would use brackets when the key has to
#    be there, like a customer's name, because if it's missing I want an
#    error so I know something is wrong. My rule of thumb is .get() for
#    optional data and brackets for required data.
#
# 2. Building a summary dictionary with a loop reminds me of a pivot table
#    or SUMIF in Excel, where you total up sales by region. The Python
#    version is more useful for large datasets because it can handle
#    millions of rows without slowing down or crashing, and I can rerun the
#    same code on new data without rebuilding anything by hand.


# Exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: Update and add
customer["phone"] = "813-555-0142"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)

# Exercise 4: Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping without .items() only gives you the keys, not the values.
# To get each value you would have to look it up with customer[key].
for key in customer:
    print(key)

# Exercise 5: Lookup table
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
discount = tier_discounts.get(customer["tier"], 0)
price = 200
final_price = price * (1 - discount)
print("Tier:", customer["tier"])
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: List of dicts
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Ben", "tier": "silver"},
    {"name": "Carla", "tier": "bronze"},
]
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = 300 * rate
    print(f"{c['name']} | {c['tier']} | Discount: ${discount_amount:.2f}")

# Exercise 7: Nested catalog
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} ({info['stock']} left)")

# Exercise 8: Sales by region
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]
for region in sorted(summary):
    print(f"{region}: {summary[region]}")
