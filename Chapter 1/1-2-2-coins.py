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
    """Counts the number of ways to make change for $1 using half dollar coins,
    quarters, dimes, nickels, and pennies, using naive brute force in nested
    for-loops."""
    one_dollar = 100
    ways_count = 0
    half_dollars = 2  # Max number of half dollars to use
    quarters = 4  # Max number of quarters to use
    dimes = 10  # Max number of dimes to use
    nickels = 20  # Max number of nickels to use
    pennies = 100  # Max number of pennies to use
    for h in range(half_dollars + 1):
        for q in range(quarters + 1):
            for d in range(dimes + 1):
                for n in range(nickels + 1):
                    for p in range(pennies + 1):
                        # Compute the sum of so many half dollars, quarters, etc
                        amount = 50 * h + 25 * q + 10 * d + 5 * n + p
                        # If it amounts to precisely $1, count this combination as
                        # one more way to break $1 in change.
                        if amount == one_dollar:
                            ways_count += 1
    # Done. Return the number of possible combinations, and the number of
    # steps it took to compute them.
    return ways_count, half_dollars * quarters * dimes * nickels * pennies
    # end method brute_force


def brute_force_pruned():
    """Counts the number of ways to make change for $1 using half dollar coins,
    quarters, dimes, nickels, and pennies, using some prunning to avoid
    unlikely scenarios, like 4 quarters and 3 dimes ($1.30)."""
    one_dollar = 100
    ways_count = 0
    steps = 0  # count of steps it takes to compute all combinations
    half_dollars = 2  # start with two half dollars
    quarter_value = 25  # demomination for quarter coins
    dime_value = 10  # denomination for dime coins
    nickel_value = 5  # denomination for nickel coins
    for h in range(half_dollars + 1):
        hh = 50 * h  # amount obtained with h half dollars
        # use this amount to limit how many quarters we can possibly use
        for q in range(1 + ((one_dollar - hh) // quarter_value)):
            qq = quarter_value * q  # amount obtained with q quarters
            # use this amount to limit how many dimes we can possibly use
            for d in range(1 + ((one_dollar - hh - qq) // dime_value)):
                dd = dime_value * d  # amount obtained with d dimes
                # use this amount to limit how many nickels we can possibly use
                for n in range(1 + ((one_dollar - hh - qq - dd) // nickel_value)):
                    nn = nickel_value * n  # amount obtained with n nickels
                    # use this amount to limit how many pennies we can possibly use
                    for p in range(1 + ((one_dollar - hh - qq - dd - nn))):
                        # Compute the amount we have here
                        amount = hh + qq + dd + nn + p
                        # Update the number of steps
                        steps += 1
                        # If amount is $1 we found one more way to change
                        if amount == one_dollar:
                            ways_count += 1
    # Done
    return ways_count, steps
    # end method brute_force_pruned


def coins_dynamic_programming():
    # List of available coin denominations in cents
    coins = [1, 5, 10, 25, 50]
    # Target amount in cents (e.g., $1.00 = 100 cents)
    target = 100
    steps = 0
    # Initialize a list to store the number of ways to make change for each amount
    # ways[i] will store the number of ways to make change for i cents
    ways = [0] * (target + 1)
    # There is one way to make 0 cents: using no coins
    ways[0] = 1
    # For each coin, update the ways array for all amounts >= coin value
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
            steps += 1
    return ways[target], steps


if __name__ == "__main__":
    ways, steps = brute_force()
    print(
        f"\n\n   Full brute foces shows {ways} ways to change $1, after {steps:,d} steps."
    )
    ways, steps = brute_force_pruned()
    print(
        f" Pruned brute foces shows {ways} ways to change $1, after {steps:,d} steps."
    )
    print(f"           Recusion shows {count_change(1)} ways to change $1.")
    ways, steps = coins_dynamic_programming()
    print(
        f"Dynanic programming shows {ways} ways to change $1, after {steps:,d} steps.\n"
    )
