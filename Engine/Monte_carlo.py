import numpy as np
import matplotlib.pyplot as plt

class MonteCarloSimulation:
    """
    A class to perform Monte Carlo simulations for financial strategies.
    """

    def __init__(self, initial_value, num_simulations, time_horizon, drift, volatility):
        """
        Initialize the Monte Carlo Simulation.

        Parameters:
            initial_value (float): The starting value of the simulation (e.g., portfolio value).
            num_simulations (int): Number of simulation runs.
            time_horizon (int): Total number of time steps in the simulation.
            drift (float): Expected return or mean growth rate.
            volatility (float): Standard deviation or variability of returns.
        """
        self.initial_value = initial_value
        self.num_simulations = num_simulations
        self.time_horizon = time_horizon
        self.drift = drift
        self.volatility = volatility

    def run_simulation(self):
        """
        Runs the Monte Carlo simulation.

        Returns:
            np.ndarray: Simulated paths (num_simulations x time_horizon).
        """
        # Time increments
        dt = 1 / self.time_horizon

        # Simulating percentage changes using geometric Brownian motion
        random_shocks = np.random.normal(
            loc=0, scale=np.sqrt(dt), size=(self.num_simulations, self.time_horizon)
        )
        price_changes = self.drift * dt + self.volatility * random_shocks

        # Simulating paths
        paths = np.exp(np.cumsum(price_changes, axis=1))
        paths = self.initial_value * paths

        # Insert initial value at the start of each path
        return np.insert(paths, 0, self.initial_value, axis=1)

    def summarize_simulation(self, paths):
        """
        Summarize the results of the simulation.

        Parameters:
            paths (np.ndarray): Simulated paths from the simulation.

        Returns:
            dict: Statistics such as mean, median, and standard deviation.
        """
        final_values = paths[:, -1]
        return {
            "mean": np.mean(final_values),
            "median": np.median(final_values),
            "std_dev": np.std(final_values),
            "min": np.min(final_values),
            "max": np.max(final_values),
        }

if __name__ == "__main__":
    # Set parameters for the simulation
    initial_value = 100000  # Starting portfolio value
    num_simulations = 1000  # Number of simulation runs
    time_horizon = 252      # 1 year of trading days
    drift = 0.07            # 7% expected annual return
    volatility = 0.2        # 20% annual volatility

    # Initialize and run the Monte Carlo simulation
    mc_simulator = MonteCarloSimulation(initial_value, num_simulations, time_horizon, drift, volatility)
    simulated_paths = mc_simulator.run_simulation()

    # Summarize and display results
    summary = mc_simulator.summarize_simulation(simulated_paths)
    print("Simulation Summary:", summary)

    # Plot the simulated paths
    plt.plot(simulated_paths)
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.title("Simulated Portfolio Paths")
    plt.show()