class Strategy:
    """
    Base class for trading strategies.
    """

    def generate_signal(self, data_row):
        """
        Generate a trading signal based on the provided market data.

        Parameters:
            data_row (pd.Series): A row of market data (e.g., close price, indicators).

        Returns:
            str: Signal ('buy', 'sell', or None).
        """
        raise NotImplementedError("Subclasses must implement the generate_signal method.")


class MovingAverageCrossoverStrategy(Strategy):
    """
    Example strategy based on moving average crossover.
    Buy signal: Short-term moving average crosses above long-term moving average.
    Sell signal: Short-term moving average crosses below long-term moving average.
    """

    def __init__(self, short_window, long_window):
        """
        Initialize the MovingAverageCrossoverStrategy.

        Parameters:
            short_window (int): Lookback period for the short-term moving average.
            long_window (int): Lookback period for the long-term moving average.
        """
        self.short_window = short_window
        self.long_window = long_window

    def generate_signal(self, data_row):
        """
        Generate a trading signal based on moving average crossover.

        Parameters:
            data_row (pd.Series): A row of market data with moving averages.

        Returns:
            str: Signal ('buy', 'sell', or None).
        """
        short_ma = data_row[f"short_ma_{self.short_window}"]
        long_ma = data_row[f"long_ma_{self.long_window}"]

        if short_ma > long_ma:
            return "buy"
        elif short_ma < long_ma:
            return "sell"
        else:
            return None


class ThresholdStrategy(Strategy):
    """
    Example strategy based on price thresholds.
    Buy signal: Price falls below a lower threshold.
    Sell signal: Price rises above an upper threshold.
    """

    def __init__(self, lower_threshold, upper_threshold):
        """
        Initialize the ThresholdStrategy.

        Parameters:
            lower_threshold (float): Price level to trigger a buy signal.
            upper_threshold (float): Price level to trigger a sell signal.
        """
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold

    def generate_signal(self, data_row):
        """
        Generate a trading signal based on price thresholds.

        Parameters:
            data_row (pd.Series): A row of market data (e.g., close price).

        Returns:
            str: Signal ('buy', 'sell', or None).
        """
        price = data_row["close"]

        if price < self.lower_threshold:
            return "buy"
        elif price > self.upper_threshold:
            return "sell"
        else:
            return None

import pandas as pd

# Sample historical data with moving averages
data = pd.DataFrame({
    "close": [100, 102, 101, 105, 110, 108, 112, 115, 118, 120],
    "short_ma_3": [None, None, 101, 102.67, 105.33, 107.67, 110.00, 111.67, 115.00, 117.67],
    "long_ma_5": [None, None, None, None, 103.6, 105.2, 106.8, 108.6, 111.4, 114.0],
})

# Moving Average Crossover Strategy
ma_strategy = MovingAverageCrossoverStrategy(short_window=3, long_window=5)
for index, row in data.iterrows():
    signal = ma_strategy.generate_signal(row)
    print(f"Date: {index}, Signal: {signal}")

# Threshold Strategy
threshold_strategy = ThresholdStrategy(lower_threshold=105, upper_threshold=115)
for index, row in data.iterrows():
    signal = threshold_strategy.generate_signal(row)
    print(f"Date: {index}, Signal: {signal}")
