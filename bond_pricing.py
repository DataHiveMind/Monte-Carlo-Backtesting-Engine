"""
Contains functions for pricing bonds, including zero-coupon bonds, coupon bonds, and callable/putable bonds.
"""
import numpy as np

def price_bond(face_value, coupon_rate, yield_to_maturity, periods_to_maturity, frequency=2):
    """
    Calculates the price of a bond.

    Args:
        face_value: Face value of the bond.
        coupon_rate: Annual coupon rate.
        yield_to_maturity: Annual yield to maturity.
        periods_to_maturity: Number of periods to maturity.
        frequency: Number of coupon payments per year.

    Returns:
        Bond price.
    """

    periodic_coupon_rate = coupon_rate / frequency
    periodic_yield_to_maturity = yield_to_maturity / frequency
    discount_factors = [(1 + periodic_yield_to_maturity)**(-i) for i in range(1, periods_to_maturity + 1)]

    price = sum([periodic_coupon_rate * face_value * discount_factor for discount_factor in discount_factors]) + face_value * discount_factors[-1]
    return price