import math
import argparse


def calculate_overpay(principal, total_payment):
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


def calculate_periods(interest, principal, payment):
    i = interest / ( 12 * 100)
    periods = math.ceil(
        math.log(payment / (payment - i * principal),1+i)
    )

    years = math.floor(periods / 12)
    months = periods % 12

    year_string = ""
    if years > 0:
        year_string = f"{years} {'year' if years == 1 else 'years'} and "

    print(f"It will take {year_string}{months} {'month' if months == 1 else 'months'} to repay this loan!")
    calculate_overpay(principal, payment * periods)


def calculate_principal(interest, payment, periods):
    i = interest / 12 / 100
    x = (1 + i) ** periods
    principal = payment / ((i * x) / (x - 1))
    print(f"Your loan principal = {principal}!")
    calculate_overpay(principal, payment * periods)


def calculate_payment(interest, principal, periods):
    i = interest / 12 / 100
    x = (1 + i) ** periods
    payment = math.ceil(principal * ((i * x) / (x - 1)))
    print(f"Your monthly payment = {payment}!")
    calculate_overpay(principal, payment * periods)


def calculate_diff_payment(interest, principal, periods):
    i = interest / 12 / 100
    total_payment = 0
    for x in range(periods):
        m = x + 1
        d = math.ceil(principal / periods + i * (principal - (principal * (m - 1 )) / periods))
        print(f"Month {m}: payment is {d}")
        total_payment += d
    calculate_overpay(principal, total_payment)


def is_arg_positive_or_None(arg):
    if arg is None:
        return True
    if float(arg) >= 0:
        return True
    return False


def are_inputs_valid(args):
    if args.type is None or (args.type != "annuity" and args.type != "diff"):
        return False
    if args.interest is None:
        return False
    if not is_arg_positive_or_None(args.payment):
        return False
    if not is_arg_positive_or_None(args.principal):
        return False
    if not is_arg_positive_or_None(args.periods):
        return False
    if not is_arg_positive_or_None(args.interest):
        return False
    return True


parser = argparse.ArgumentParser("Annuity payment calculator")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--type")
parser.add_argument("--interest")

args = parser.parse_args()

if are_inputs_valid(args):
    if args.type == "annuity":
        if args.payment is None:
            calculate_payment(float(args.interest), float(args.principal), int(args.periods))
        elif args.principal is None:
            calculate_principal(float(args.interest), float(args.payment), int(args.periods))
        else:
            calculate_periods(float(args.interest), float(args.principal), float(args.payment))
    else:
        calculate_diff_payment(float(args.interest), float(args.principal), int(args.periods))
else:
    print("Incorrect parameters.")

