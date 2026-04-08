# profit_check.py
from decimal import Decimal

# soglia minima di profitto
MIN_PROFIT = Decimal(str(int(0.0002 * 10**18)))


def is_swap_profitable(
    amount_in: str,
    amount_out: str,
    gas_cost_eth: str,
) -> bool:
    """
    Valuta se lo swap è profittevole.

    profit = amount_out - amount_in - gas_cost
    """

    a_in = Decimal(amount_in)
    a_out = Decimal(amount_out)
    gas = Decimal(gas_cost_eth)

    profit = a_out - a_in - gas
    print(f"{a_out} - {a_in} - {int(gas)} = {(profit / Decimal(10**18)):.4f} ETH")

    return profit > MIN_PROFIT
