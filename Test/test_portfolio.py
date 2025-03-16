import unittest
from engine.portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio(initial_cash=100000)

    def test_buy(self):
        self.portfolio.buy(asset="AAPL", price=150, quantity=10, date="2025-03-14")
        self.assertEqual(self.portfolio.positions["AAPL"], 10)
        self.assertEqual(self.portfolio.cash, 100000 - 150 * 10)

    def test_sell(self):
        self.portfolio.buy(asset="AAPL", price=150, quantity=10, date="2025-03-14")
        self.portfolio.sell(asset="AAPL", price=155, quantity=5, date="2025-03-15")
        self.assertEqual(self.portfolio.positions["AAPL"], 5)
        self.assertEqual(self.portfolio.cash, 100000 - 150 * 10 + 155 * 5)

    def test_portfolio_value(self):
        self.portfolio.buy(asset="AAPL", price=150, quantity=10, date="2025-03-14")
        market_prices = {"AAPL": 155}
        portfolio_value = self.portfolio.calculate_portfolio_value(market_prices)
        self.assertEqual(portfolio_value, self.portfolio.cash + 10 * 155)

if __name__ == "__main__":
    unittest.main()
