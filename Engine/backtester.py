import pandas as pd


class Backtester:
    """
    A class to backtest trading strategies using historical data.
    """

    def __init__(self, historical_data, strategy, initial_cash=100000):
        """
        Initialize the Backtester.

        Parameters:
            historical_data (pd.DataFrame): Historical price data (e.g., stock prices).
            strategy (object): Strategy object that defines buy/sell rules.
            initial_cash (float): Starting cash for the portfolio.
        """
        self.historical_data = historical_data
        self.strategy = strategy
        self.initial_cash = initial_cash
        self.portfolio_value = initial_cash
        self.cash = initial_cash
        self.position = 0  # Number of shares currently held
        self.history = []  # To store transaction history and portfolio value

    def run(self):
        """
        Run the backtest over the historical data.
        """
        for date, row in self.historical_data.iterrows():
            signal = self.strategy.generate_signal(row)

            if signal == "buy" and self.cash >= row["close"]:
                self.buy(row["close"], date)
            elif signal == "sell" and self.position > 0:
                self.sell(row["close"], date)

            # Calculate the portfolio value at the end of the day
            self.portfolio_value = self.cash + self.position * row["close"]
            self.history.append(
                {"date": date, "cash": self.cash, "position": self.position, "portfolio_value": self.portfolio_value}
            )

    def buy(self, price, date):
        """
        Execute a buy order.

        Parameters:
            price (float): Price at which to buy.
            date (str): Date of the transaction.
        """
        self.position += 1
        self.cash -= price
        print(f"{date}: Bought 1 share at {price:.2f}")

    def sell(self, price, date):
        """
        Execute a sell order.

        Parameters:
            price (float): Price at which to sell.
            date (str): Date of the transaction.
        """
        self.position -= 1
        self.cash += price
        print(f"{date}: Sold 1 share at {price:.2f}")

    def results(self):
        """
        Return the results of the backtest.

        Returns:
            pd.DataFrame: A DataFrame containing the historical portfolio values.
        """
        return pd.DataFrame(self.history)


if __name__ == "__main__":
    # Example usage
    # Sample historical data
    data = pd.DataFrame({
        "date": pd.date_range(start="2022-01-01", periods=10),
        "close": [100, 102, 101, 105, 110, 108, 112, 115, 118, 120],
    }).set_index("date")

    # Example strategy
    class ExampleStrategy:
        def generate_signal(self, row):
            # Simple strategy: Buy if the price is below 105, sell if it's above 115
            if row["close"] < 105:
                return "buy"
            elif row["close"] > 115:
                return "sell"
            return None

    strategy = ExampleStrategy()
    backtester = Backtester(data, strategy)
    backtester.run()
    print(backtester.results())
