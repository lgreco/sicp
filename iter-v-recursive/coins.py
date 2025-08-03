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
        int: how many different was the given amount can be made to chage
        using $0.50, $0.25, $0.10, $0.05, and $0.01 coins.
    """
    # Convert USD into pennies because function cc uses pennies
    return cc(100 * amount, 5)
    # end method count_change


if __name__ == "__main__":
    print(count_change(9))
