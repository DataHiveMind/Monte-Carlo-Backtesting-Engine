import unittest
import numpy as np
from Engine.Monte_carlo import MonteCarloSimulation

class TestMonteCarloSimulation(unittest.TestCase):
    """
    Unit tests for the Monte Carlo Simulation class.
    """

    def setUp(self):
        """
        Set up test parameters and an instance of MonteCarloSimulation.
        """
        self.initial_value = 100000
        self.num_simulations = 100
        self.time_horizon = 252
        self.drift = 0.07
        self.volatility = 0.2

        self.mc_simulator = MonteCarloSimulation(
            self.initial_value,
            self.num_simulations,
            self.time_horizon,
            self.drift,
            self.volatility,
        )

    def test_run_simulation_output_shape(self):
        """
        Test that the output of run_simulation has the correct shape.
        """
        paths = self.mc_simulator.run_simulation()
        # Paths should have dimensions (num_simulations, time_horizon + 1)
        self.assertEqual(paths.shape, (self.num_simulations, self.time_horizon + 1))

    def test_run_simulation_positive_values(self):
        """
        Test that the simulated paths contain only positive values.
        """
        paths = self.mc_simulator.run_simulation()
        # All values in the paths array should be greater than zero
        self.assertTrue(np.all(paths > 0))

    def test_summarize_simulation(self):
        """
        Test the summarize_simulation method returns correct keys and non-empty values.
        """
        paths = self.mc_simulator.run_simulation()
        summary = self.mc_simulator.summarize_simulation(paths)

        # Check that all expected keys are in the summary
        expected_keys = {"mean", "median", "std_dev", "min", "max"}
        self.assertTrue(expected_keys.issubset(summary.keys()))

        # Check that summary values are non-empty
        for value in summary.values():
            self.assertIsNotNone(value)

    def test_deterministic_case(self):
        """
        Test a deterministic scenario with zero volatility (straight growth at drift rate).
        """
        deterministic_simulator = MonteCarloSimulation(
            self.initial_value,
            self.num_simulations,
            self.time_horizon,
            drift=0.05,
            volatility=0.0,  # No randomness
        )
        paths = deterministic_simulator.run_simulation()

        # Expected growth: initial_value * e^(drift * time)
        expected_final_value = self.initial_value * np.exp(0.05 * self.time_horizon)
        self.assertTrue(
            np.allclose(paths[:, -1], expected_final_value, atol=1e-2)
        )

if __name__ == "__main__":
    unittest.main()
