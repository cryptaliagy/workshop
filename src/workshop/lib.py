
def calculate_percent(
    subtotal: float,
    percentage: int = 15,
) -> float:
    '''
    A function that takes in a subtotal and the percentage associated with it, and returns the
    percentage value of that subtotal, for use in tax calculation and in tip calculation
    '''
    return round(subtotal * (percentage / 100), 2)


def calculate_subtotal(
    *item_costs: float
) -> float:
    '''
    A function to calculate the sum of a sequence of item costs
    '''

    subtotal: float = 0

    for cost in item_costs:
        subtotal += cost

    return subtotal
