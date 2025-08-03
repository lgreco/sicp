def first_denomination(kinds_of_coins):
    """Returns the denomination of the *currently* first kind of coins. The
    method is initially called with kinds_of_coins = 5, so the fist
    denomination is $0.50. Then we proceed with kinds_of_coins -= 1.
    """
    match kinds_of_coins:
        case 1:
            value = 1
        case 2:
            value = 5
        case 3:
            value = 10
        case 4:
            value = 25
        case 5:
            value = 50
    return value
    # end method first_denomination


def cc(amount, kinds_of_coins):
    """Computes the number of ways to make change for the given amount and
    the given coin denominations.

    Args:
        amount (int): amount to break into change of various coins denominations,
        expressed in pennies; for example $1 = 100 cents.

        kinds_of_coins (int): number of denominations available for change.
        Initially there are 5 kinds of coints (half dollars, quarters, dimes,
        nickels, and pennies).

    Returns:
        int: number of ways to change the given amount using standard US coins.
    """
    if amount == 0:
        # Base case: with the given kinds of coins, we have reached a zero
        # amount remaining to be changed; so we have just found one way to
        # change the given amount with the available coins.
        ways = 1
    elif amount < 0 or kinds_of_coins == 0:
        # Base case too: if we are out of amount to process or out of
        # coin denominations, this is not a way to make change.
        ways = 0
    else:
        # Recurse to the sum of ways to change the given amount with one
        # less denomination available, plus all the ways to make change
        # for the given amount minus the denomination of the first kind
        # of coins.
        ways = cc(amount, kinds_of_coins - 1) + cc(
            amount - first_denomination(kinds_of_coins), kinds_of_coins
        )
    return ways
    # end method cc


def count_change(amount):
    """Computes the number of ways to change an amount in USD with any
    combination of pennies, nickels, dimes, quarters, and half dollar coins.

    Args:
        amount (int): the amount, in USD to change

    Returns:
        int: how many different ways the given amount can be made to chage
        using $0.50, $0.25, $0.10, $0.05, and $0.01 coins.
    """
    # Convert USD into pennies because function cc uses pennies
    return cc(100 * amount, 5)
    # end method count_change


def brute_force():
    one_dollar = 100
    ways_count = 0
    half_dollars = 2
    quarters = 4
    dimes = 10
    nickels = 20
    pennies = 100
    for h in range(half_dollars + 1):
        for q in range(quarters + 1):
            for d in range(dimes + 1):
                for n in range(nickels + 1):
                    for p in range(pennies + 1):
                        amount = 50 * h + 25 * q + 10 * d + 5 * n + p
                        if amount == one_dollar:
                            ways_count += 1
    return ways_count, half_dollars * quarters * dimes * nickels * pennies


def brute_force_pruned():
    one_dollar = 100
    ways_count = 0
    steps = 0
    half_dollars = 2
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    for h in range(half_dollars + 1):
        hh = 50 * h
        for q in range(1 + ((one_dollar - hh) // quarter_value)):
            qq = quarter_value * q
            for d in range(1 + ((one_dollar - hh - qq) // dime_value)):
                dd = dime_value * d
                for n in range(1 + ((one_dollar - hh - qq - dd) // nickel_value)):
                    nn = nickel_value * n
                    for p in range(1 + ((one_dollar - hh - qq - dd - nn))):
                        amount = hh + qq + dd + nn + p
                        steps += 1
                        if amount == one_dollar:
                            ways_count += 1
    return ways_count, steps


if __name__ == "__main__":
    ways, steps = brute_force()
    print(
        f"\n\n  Full brute foces shows {ways} ways to change $1, after {steps:,d} steps."
    )
    ways, steps = brute_force_pruned()
    print(f"Pruned brute foces shows {ways} ways to change $1, after {steps:,d} steps.")
    print(f"          Recusion shows {count_change(1)} ways to change $1.\n")
