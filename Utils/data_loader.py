import pandas as pd

class DataLoader:
    """
    A class to load and preprocess historical market data.
    """

    @staticmethod
    def load_csv(file_path, date_column, price_column):
        """
        Load historical data from a CSV file.

        Parameters:
            file_path (str): Path to the CSV file.
            date_column (str): Name of the column containing dates.
            price_column (str): Name of the column containing prices.

        Returns:
            pd.DataFrame: A DataFrame with the historical data, indexed by date.
        """
        data = pd.read_csv(file_path)
        data[date_column] = pd.to_datetime(data[date_column])
        data = data[[date_column, price_column]].rename(
            columns={date_column: "date", price_column: "close"}
        )
        data.set_index("date", inplace=True)
        return data

    @staticmethod
    def add_moving_averages(data, short_window, long_window):
        """
        Add moving averages to the historical data.

        Parameters:
            data (pd.DataFrame): Historical data with a "close" column.
            short_window (int): Lookback period for the short-term moving average.
            long_window (int): Lookback period for the long-term moving average.

        Returns:
            pd.DataFrame: DataFrame with additional columns for moving averages.
        """
        data[f"short_ma_{short_window}"] = data["close"].rolling(window=short_window).mean()
        data[f"long_ma_{long_window}"] = data["close"].rolling(window=long_window).mean()
        return data
