""" Implements functions to analyze cash flows, such as calculating net present value (NPV), internal rate of return (IRR), and modified duration.
"""


def __init__(self):
    pass

def duration_convexity(self):
    """Contains functions to calculate duration and convexity measures, including Macaulay duration, modified duration, and convexity.
    """
    
    pass

class Loan():
    def __init__(self, notional, redemption, interest_rate):
        """
        Initializes a Loan object with the given parameters.
        """
        self.notional = notional
        self.redemption = redemption
        self.interest_rate = interest_rate

    def Future_Value(self)-> float:
        """
        Returns the future value of the loan.
        """
        return self.redemption - self.notional * (1 + self.interest_rate)

    def Present_Value(self)-> float:
        """
        Returns the present value of the loan.
        """
        return self.redemption/(1 + self.interest_rate) - self.notional

    def Yield_to_Maturity(self)-> float:
        """
        Returns the yield to maturity of the loan.
        """
        return self.interest_rate

    def Duration(self)-> float:
        """
        Returns the duration of the loan.
        """
        return 1 / (1 + self.interest_rate)

    def Convexity(self)-> float:
        """
        Returns the convexity of the loan.
        """
        return 1 / (1 + self.interest_rate) ** 2
    
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

    return sum(periodic_coupon_rate * face_value * discount_factor for discount_factor in discount_factors) + face_value * discount_factors[-1]
    