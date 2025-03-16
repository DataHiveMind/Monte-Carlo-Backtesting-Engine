import unittest
import pandas as pd
from engine.backtester import Backtester

class TestBacktester(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "date": pd.date_range(start="2025-01-01", periods=5),
            "close": [100, 102, 101, 105, 110]
        }).set_index("date")

        class ExampleStrategy:
            def generate_signal(self, row):
                if row["close"] < 102:
                    return "buy"
                elif row["close"] > 105:
                    return "sell"
                return None
        
        self.strategy = ExampleStrategy()
        self.backtester = Backtester(self.data, self.strategy)

    def test_run(self):
        self.backtester.run()
        self.assertTrue(len(self.backtester.history) > 0)

    def test_results(self):
        self.backtester.run()
        results = self.backtester.results()
        self.assertIsInstance(results, pd.DataFrame)
        self.assertIn("portfolio_value", results.columns)

if __name__ == "__main__":
    unittest.main()
