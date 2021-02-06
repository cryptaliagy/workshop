import click

import workshop.lib as lib

from typing import Iterable


@click.command()
@click.argument(
    'cost',
    type=float,
    nargs=-1,
    metavar='[ITEM COST] [ITEM COST ...]'
)
def main(
    cost: Iterable[float]
):
    subtotal = lib.calculate_subtotal(*cost)
    tax = lib.calculate_percent(subtotal, 13)
    tip = lib.calculate_percent(subtotal + tax, 15)

    click.echo('The total cost of your items is ', nl=False)
    click.secho('$%.2f' % (subtotal + tax + tip), fg='green')


if __name__ == '__main__':  # pragma: no cover
    main()
