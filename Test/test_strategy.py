import unittest
import pandas as pd
from engine.strategy import MovingAverageCrossoverStrategy, ThresholdStrategy

class TestMovingAverageCrossoverStrategy(unittest.TestCase):
    def setUp(self):
        self.data_row = {
            "short_ma_3": 105,
            "long_ma_5": 100
        }
        self.strategy = MovingAverageCrossoverStrategy(short_window=3, long_window=5)

    def test_buy_signal(self):
        signal = self.strategy.generate_signal(self.data_row)
        self.assertEqual(signal, "buy")

    def test_sell_signal(self):
        self.data_row["short_ma_3"] = 95
        signal = self.strategy.generate_signal(self.data_row)
        self.assertEqual(signal, "sell")

class TestThresholdStrategy(unittest.TestCase):
    def setUp(self):
        self.data_row = {"close": 100}
        self.strategy = ThresholdStrategy(lower_threshold=95, upper_threshold=105)

    def test_buy_signal(self):
        self.data_row["close"] = 90
        signal = self.strategy.generate_signal(self.data_row)
        self.assertEqual(signal, "buy")

    def test_sell_signal(self):
        self.data_row["close"] = 110
        signal = self.strategy.generate_signal(self.data_row)
        self.assertEqual(signal, "sell")

if __name__ == "__main__":
    unittest.main()
