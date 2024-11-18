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