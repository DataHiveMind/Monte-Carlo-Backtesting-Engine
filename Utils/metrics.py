import numpy as np

class Metrics:
    """
    A class to calculate performance metrics for backtesting results.
    """

    @staticmethod
    def calculate_cumulative_returns(portfolio_values):
        """
        Calculate cumulative returns for the portfolio.

        Parameters:
            portfolio_values (list or np.ndarray): Daily portfolio values.

        Returns:
            np.ndarray: Cumulative returns over time.
        """
        returns = np.array(portfolio_values)
        return (returns / returns[0]) - 1


    @staticmethod
    def calculate_annualized_return(portfolio_values, num_days):
        """
        Calculate the annualized return of the portfolio.

        Parameters:
            portfolio_values (list or np.ndarray): Daily portfolio values.
            num_days (int): Total number of days in the backtest.

        Returns:
            float: Annualized return.
        """
        total_return = portfolio_values[-1] / portfolio_values[0] - 1
        return (1 + total_return) ** (252 / num_days) - 1

    @staticmethod
    def calculate_annualized_volatility(portfolio_values):
        """
        Calculate the annualized volatility of portfolio returns.

        Parameters:
            portfolio_values (list or np.ndarray): Daily portfolio values.

        Returns:
            float: Annualized volatility.
        """
        daily_returns = np.diff(portfolio_values) / portfolio_values[:-1]
        return np.std(daily_returns) * np.sqrt(252)

    @staticmethod
    def calculate_sharpe_ratio(portfolio_values, risk_free_rate=0.01):
        """
        Calculate the Sharpe ratio of the portfolio.

        Parameters:
            portfolio_values (list or np.ndarray): Daily portfolio values.
            risk_free_rate (float): Risk-free rate (default: 1%).

        Returns:
            float: Sharpe ratio.
        """
        annualized_return = Metrics.calculate_annualized_return(portfolio_values, len(portfolio_values))
        annualized_volatility = Metrics.calculate_annualized_volatility(portfolio_values)
        return (annualized_return - risk_free_rate) / annualized_volatility

    @staticmethod
    def calculate_max_drawdown(portfolio_values):
        """
        Calculate the maximum drawdown of the portfolio.

        Parameters:
            portfolio_values (list or np.ndarray): Daily portfolio values.

        Returns:
            float: Maximum drawdown.
        """
        cumulative_max = np.maximum.accumulate(portfolio_values)
        drawdowns = (portfolio_values - cumulative_max) / cumulative_max
        return np.min(drawdowns)
