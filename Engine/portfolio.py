class Portfolio:
    """
    A class to manage a portfolio of assets during backtesting.
    """

    def __init__(self, initial_cash=100000):
        """
        Initialize the Portfolio.

        Parameters:
            initial_cash (float): Starting cash amount for the portfolio.
        """
        self.cash = initial_cash
        self.positions = {}  # Dictionary to store positions: {asset: quantity}
        self.transaction_history = []  # List to log all transactions

    def buy(self, asset, price, quantity, date):
        """
        Buy an asset and update the portfolio.

        Parameters:
            asset (str): Name of the asset being bought.
            price (float): Price per unit of the asset.
            quantity (int): Number of units to buy.
            date (str): Date of the transaction.
        """
        total_cost = price * quantity
        if self.cash >= total_cost:
            self.cash -= total_cost
            self.positions[asset] = self.positions.get(asset, 0) + quantity
            self.transaction_history.append(
                {"date": date, "action": "buy", "asset": asset, "price": price, "quantity": quantity}
            )
            print(f"{date}: Bought {quantity} of {asset} at {price:.2f} each.")
        else:
            print(f"{date}: Insufficient cash to buy {quantity} of {asset} at {price:.2f} each.")

    def sell(self, asset, price, quantity, date):
        """
        Sell an asset and update the portfolio.

        Parameters:
            asset (str): Name of the asset being sold.
            price (float): Price per unit of the asset.
            quantity (int): Number of units to sell.
            date (str): Date of the transaction.
        """
        if self.positions.get(asset, 0) >= quantity:
            total_revenue = price * quantity
            self.cash += total_revenue
            self.positions[asset] -= quantity
            if self.positions[asset] == 0:
                del self.positions[asset]
            self.transaction_history.append(
                {"date": date, "action": "sell", "asset": asset, "price": price, "quantity": quantity}
            )
            print(f"{date}: Sold {quantity} of {asset} at {price:.2f} each.")
        else:
            print(f"{date}: Insufficient quantity of {asset} to sell {quantity}.")

    def calculate_portfolio_value(self, market_prices):
        """
        Calculate the total value of the portfolio, including cash and positions.

        Parameters:
            market_prices (dict): Current market prices of assets: {asset: price}.

        Returns:
            float: Total portfolio value.
        """
        total_value = self.cash
        for asset, quantity in self.positions.items():
            if asset in market_prices:
                total_value += market_prices[asset] * quantity
        return total_value

    def get_positions(self):
        """
        Get the current positions in the portfolio.

        Returns:
            dict: Current positions in the portfolio: {asset: quantity}.
        """
        return self.positions

    def get_transaction_history(self):
        """
        Get the transaction history of the portfolio.

        Returns:
            list: List of all transactions made during backtesting.
        """
        return self.transaction_history

if __name__ == "__main__":
    portfolio = Portfolio(initial_cash=100000)
    
    # Simulated market prices
    market_prices = {"AAPL": 150, "GOOGL": 2800}

    # Transactions
    portfolio.buy("AAPL", price=145, quantity=10, date="2025-03-14")
    portfolio.sell("AAPL", price=155, quantity=5, date="2025-03-15")
    portfolio.buy("GOOGL", price=2800, quantity=2, date="2025-03-16")

    # Portfolio value
    total_value = portfolio.calculate_portfolio_value(market_prices)
    print(f"Total Portfolio Value: {total_value:.2f}")

    # Current positions
    print("Current Positions:", portfolio.get_positions())

    # Transaction history
    print("Transaction History:", portfolio.get_transaction_history())
