# ============================================
# Pharmacy Billing System (CLI)
# Author: Saloni Tiwari (refactored)
# Description: Multi-visit billing + loyalty points + redemption
# Rules:
#   - ₹100 bill => 1 point
#   - 1 point => ₹25 discount
#   - Minimum 10 points required to redeem
#   - Cannot exceed total bill
#   - Cannot redeem more than available points
# ============================================

POINTS_PER_100_RUPEES = 1
RUPEES_PER_POINT = 25
MIN_POINTS_TO_REDEEM = 10


def read_int(prompt: str, min_value: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Wrong Input: value must be >= {min_value}")
                continue
            return value
        except ValueError:
            print("Wrong Input: please enter an integer.")


def read_float(prompt: str, min_value: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Wrong Input: value must be >= {min_value}")
                continue
            return value
        except ValueError:
            print("Wrong Input: please enter a number.")


def get_visit_total() -> float:
    med_types = read_int("Enter how many types of medicines customer wants to purchase: ", min_value=0)

    if med_types == 0:
        print("No bill generated since user didn't purchase anything.")
        return 0.0

    total = 0.0
    valid_items = 0

    for j in range(1, med_types + 1):
        print(f"\nMedicine type {j}")
        qty = read_int(f"Enter medicine type {j} quantity: ", min_value=0)

        if qty == 0:
            print(f"Skipped: Quantity entered for type {j} medicine is zero.")
            continue

        cost = read_float(f"Enter medicine type {j} cost: ", min_value=0.0)
        if cost == 0.0:
            print(f"Skipped: Cost entered for type {j} medicine is zero.")
            continue

        total += qty * cost
        valid_items += 1

    if valid_items == 0:
        print("No bill generated since all quantities/costs were zero.")
        return 0.0

    return total


def earned_points_for_bill(total: float) -> int:
    return int(total // 100) * POINTS_PER_100_RUPEES


def redeem_points_flow(total: float, stored_points: int) -> tuple[float, int, int]:
    if stored_points < MIN_POINTS_TO_REDEEM:
        print(f"Redeeming not possible. Need at least {MIN_POINTS_TO_REDEEM} points.")
        return total, 0, stored_points

    ans = input("Do you want to redeem points? (y/n): ").strip().lower()
    if ans != "y":
        return total, 0, stored_points

    max_by_bill = int(total // RUPEES_PER_POINT)
    max_redeemable = min(stored_points, max_by_bill)

    if max_redeemable <= 0:
        print("This bill is too small to redeem any points.")
        return total, 0, stored_points

    print(f"Stored points: {stored_points} (value: ₹{stored_points * RUPEES_PER_POINT})")
    print(f"Max redeemable for this bill: {max_redeemable} points (value: ₹{max_redeemable * RUPEES_PER_POINT})")

    redeem_points = read_int("How many points you want to redeem: ", min_value=0)
    if redeem_points == 0:
        return total, 0, stored_points

    if redeem_points > max_redeemable:
        print("Wrong Input: redeem points are greater than allowed/available points.")
        return total, 0, stored_points

    discount = redeem_points * RUPEES_PER_POINT
    final_bill = total - discount
    updated_points = stored_points - redeem_points
    return final_bill, redeem_points, updated_points


def main():
    visits = read_int("No. of visits: ", min_value=1)
    points = 0

    for i in range(1, visits + 1):
        print(f"\n\n=== Visit {i} ===")
        total = get_visit_total()

        if total <= 0:
            print(f"Total points (carried): {points}")
            continue

        cur_points = earned_points_for_bill(total)

        print(f"\nBill amount: ₹{total}")
        print(f"Points earned this visit: {cur_points}")

        final_bill, redeemed, points = redeem_points_flow(total, points)

        points += cur_points

        if redeemed > 0:
            print(f"Final bill after redeeming {redeemed} points: ₹{final_bill}")
        else:
            print(f"Final bill: ₹{final_bill}")

        print(f"Total points after this visit: {points}")

    print("\nThank you for using Pharmacy Billing System!")


if __name__ == "__main__":
    main()