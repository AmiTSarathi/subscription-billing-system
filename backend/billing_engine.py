
from datetime import datetime

def is_due(sub, today):
    last = datetime.strptime(sub["last_billed"], "%Y-%m-%d")
    if sub["cycle"] == "monthly":
        return (today - last).days >= 30
    elif sub["cycle"] == "yearly":
        return (today - last).days >= 365
    return False

def apply_discount(sub):
    base = sub["amount"]
    discount = 0
    if "coupon" in sub and sub["coupon"]:
        coup = sub["coupon"]
        discount = coup["value"] if coup["type"] == "fixed" else (base * coup["value"] / 100)
    elif "discount" in sub and sub["discount"]:
        disc = sub["discount"]
        discount = disc["value"] if disc["type"] == "fixed" else (base * disc["value"] / 100)
    return round(discount, 2)

def calculate_tax(amount, rate):
    return round((amount * rate / 100), 2)

def generate_user_bill(user, today):
    items = []
    total = 0

    for sub in user["subscriptions"]:
        if is_due(sub, today):
            discount = apply_discount(sub)
            taxable_amount = sub["amount"] - discount
            tax = calculate_tax(taxable_amount, sub.get("tax_rate", 0))
            final_amount = round(taxable_amount + tax, 2)
            items.append({
                "subscription_id": sub["sub_id"],
                "description": sub["name"],
                "base_amount": sub["amount"],
                "discount_applied": discount,
                "tax_applied": tax,
                "final_amount": final_amount,
                "currency": sub["currency"]
            })
            sub["last_billed"] = today.strftime("%Y-%m-%d")
            total += final_amount

    return {
        "bill_id": f"bill-{user['user_id']}-{today.strftime('%Y%m%d')}",
        "user": {"user_id": user["user_id"], "name": user["name"]},
        "bill_date": today.strftime("%Y-%m-%d"),
        "items": items,
        "total_amount": round(total, 2),
        "currency": "USD"
    }
