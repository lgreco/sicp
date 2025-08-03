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
    """_summary_

    Args:
        amount (_type_): _description_
        kinds_of_coins (_type_): _description_

    Returns:
        _type_: _description_
    """
    if amount == 0:
        ways = 1
    elif amount < 0 or kinds_of_coins == 0:
        ways = 0
    else:
        ways = cc(amount, kinds_of_coins - 1) + cc(
            amount - first_denomination(kinds_of_coins), kinds_of_coins
        )
    return ways
    # end method cc


def count_change(amount):
    """_summary_

    Args:
        amount (_type_): _description_

    Returns:
        _type_: _description_
    """
    return cc(amount, 5)
    # end method count_change


if __name__ == "__main__":
    print(count_change(100))
